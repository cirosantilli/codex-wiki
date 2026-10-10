"""Original solved rod example, with independent complex finite-difference checks.

Python 3.14, NumPy 2.3.5, matplotlib 3.10.7; no SciPy.
Run in _media; writes its basename PNG to the current working directory.
"""
from pathlib import Path
import json

import matplotlib.pyplot as plt
import numpy as np

ALPHA = 1e-4
PERIOD = 100.0
OMEGA = 2*np.pi/PERIOD
LOSS = 0.01
THETA0 = 4.0
SENSORS = np.array([0.02, 0.05])


def gamma(loss):
    return np.sqrt((loss + 1j*OMEGA)/ALPHA)


def finite_rod(x, length, loss=LOSS):
    """Exact phasor: prescribed left temperature, insulated right end."""
    g = gamma(loss)
    return THETA0*np.cosh(g*(length-x))/np.cosh(g*length)


def finite_difference(length, dx, loss, insulated=False):
    """Solve discretized αz'' − (loss+iω)z=0 by complex Thomas elimination.

    This assembles the differential equation, without using its analytic roots.
    The final node is eliminated via z_N = z_(N-1) for insulation at the
    half-grid point L-dx/2; otherwise the right temperature is zero at L.
    """
    n = round(length/dx)
    x = np.arange(n+1)*dx
    m = n-1
    diag = np.full(m, 2*ALPHA/dx**2 + loss + 1j*OMEGA, dtype=complex)
    off = -ALPHA/dx**2
    rhs = np.zeros(m, dtype=complex)
    rhs[0] = -off*THETA0
    if insulated:
        diag[-1] += off
    for j in range(1, m):
        factor = off/diag[j-1]
        diag[j] -= factor*off
        rhs[j] -= factor*rhs[j-1]
    z = np.zeros(n+1, dtype=complex)
    z[0] = THETA0
    z[n-1] = rhs[-1]/diag[-1]
    for j in range(m-2, -1, -1):
        z[j+1] = (rhs[j]-off*z[j+2])/diag[j]
    if insulated:
        z[-1] = z[-2]
    return x, z


def infer(z, spacing=0.03):
    attenuation = np.log(abs(z[0]/z[1]))
    lag = np.angle(z[0]/z[1])
    return OMEGA*spacing**2/(2*attenuation*lag)


def checks():
    out = {"parameters": {"alpha": ALPHA, "period_s": PERIOD, "loss_rate_s_inverse": LOSS}, "cases": []}
    for loss in [0.0, LOSS]:
        g = gamma(loss)
        exact = THETA0*np.exp(-g*SENSORS)
        errors = []
        for dx in [0.001, 0.0005, 0.00025]:
            x, z = finite_difference(0.8, dx, loss)
            obs = z[np.rint(SENSORS/dx).astype(int)]
            errors.append(float(np.max(abs(obs/exact-1))))
        assert errors[-1] < 3e-6
        assert errors[0]/errors[1] > 3.9 and errors[1]/errors[2] > 3.9
        # Recover phasors from real time traces by an independent least-squares fit.
        t = np.linspace(0, 3*PERIOD, 1500, endpoint=False)
        design = np.column_stack([np.ones_like(t), np.cos(OMEGA*t), np.sin(OMEGA*t)])
        trace = 0.7 + (exact[:, None]*np.exp(1j*OMEGA*t)).real
        fit = np.linalg.lstsq(design, trace.T, rcond=None)[0]
        recovered = fit[1]-1j*fit[2]
        assert np.max(abs(recovered-exact)) < 1e-13
        assert abs(infer(recovered)/ALPHA-1) < 1e-13
        assert abs(2*g.real*g.imag-OMEGA/ALPHA) < 1e-12
        out["cases"].append({"loss_rate": loss, "a": float(g.real), "b": float(g.imag), "amplitudes_K": abs(exact).tolist(), "lag_rad": float(g.imag*0.03), "time_lag_s": float(g.imag*0.03/OMEGA), "inferred_alpha": float(infer(recovered)), "finite_difference_relative_errors": errors, "refinement_ratios": [errors[0]/errors[1], errors[1]/errors[2]], "trace_fit_max_error_K": float(np.max(abs(recovered-exact)))})
    # Finite-end check uses a different boundary condition and exact cosh solution.
    finite_errors = []
    for dx in [0.0004, 0.0002, 0.0001]:
        x, z = finite_difference(0.08, dx, LOSS, insulated=True)
        exact = finite_rod(x[:-1], 0.08-dx/2)
        finite_errors.append(float(np.max(abs(z[:-1]-exact))/THETA0))
    assert finite_errors[-1] < 3e-7
    assert finite_errors[0]/finite_errors[1] > 3.8
    out["finite_insulated_end"] = {"finite_difference_max_relative_to_drive_errors": finite_errors, "alpha_apparent_L_0_08": float(infer(finite_rod(SENSORS, 0.08))), "alpha_apparent_L_0_3": float(infer(finite_rod(SENSORS, 0.3)))}
    return out


def main():
    checked = checks()
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.6), dpi=120, constrained_layout=True)
    x = np.linspace(0, 0.12, 400)
    colors = ["#146c94", "#b34f23"]
    for loss, col in zip([0, LOSS], colors):
        g = gamma(loss)
        label = "No side loss" if loss == 0 else "Linear loss λ = 0.010 s⁻¹"
        axes[0, 0].plot(x*100, THETA0*np.exp(-g.real*x), color=col, label=label)
        axes[0, 1].plot(x*100, g.imag*x, color=col, label=label)
        xn, zn = finite_difference(0.8, 0.0005, loss)
        idx = np.rint(SENSORS/0.0005).astype(int)
        axes[0, 0].plot(SENSORS*100, abs(zn[idx]), "o", color=col, ms=5)
        axes[0, 1].plot(SENSORS*100, -np.angle(zn[idx]), "o", color=col, ms=5)
    axes[0, 0].set(title="Spatial amplitude: loss makes decay steeper", xlabel="Distance x (cm)", ylabel="Amplitude A(x) (K)")
    axes[0, 0].legend(fontsize=9)
    axes[0, 1].set(title="Unwrapped lag: loss makes this slope shallower", xlabel="Distance x (cm)", ylabel="Lag from driven end (rad)")
    for ax in axes[0]:
        for sx in SENSORS*100:
            ax.axvline(sx, color="#999999", ls=":", lw=0.8)
    t = np.linspace(0, 2*PERIOD, 600)
    for sx, col in zip(SENSORS, ["#146c94", "#7c3f96"]):
        z = THETA0*np.exp(-gamma(LOSS)*sx)
        axes[1, 0].plot(t, (z*np.exp(1j*OMEGA*t)).real, color=col, label=f"x = {sx*100:.0f} cm, A = {abs(z):.3f} K")
    axes[1, 0].set(title="Steady periodic traces with linear loss", xlabel="Time t (s)", ylabel="Oscillating temperature θ (K)")
    axes[1, 0].legend(fontsize=9, loc="lower right")
    axes[1, 0].text(0.04, 0.95, "Δφ = 0.4912 rad; Δt = 7.818 s", transform=axes[1, 0].transAxes, va="top", fontsize=9)
    lengths = np.linspace(0.06, 0.32, 300)
    apparent = np.array([infer(finite_rod(SENSORS, length)) for length in lengths])
    axes[1, 1].plot(lengths*100, apparent/ALPHA, color="#35754c")
    axes[1, 1].axhline(1, ls="--", color="#444444", lw=1)
    axes[1, 1].plot([8, 30], [infer(finite_rod(SENSORS, length))/ALPHA for length in [0.08, 0.3]], "o", color="#35754c")
    axes[1, 1].set(title="Insulated far end: bias from using one exponential", xlabel="Total rod length L (cm)", ylabel="Apparent α / true α", ylim=(0.7, 1.7))
    for ax in axes.flat:
        ax.grid(alpha=0.2)
    fig.suptitle("Original model: α = 10⁻⁴ m²/s, period = 100 s, driven amplitude = 4 K", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)
    print(json.dumps(checked, indent=2))


if __name__ == "__main__":
    main()
