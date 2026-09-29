"""Original normalized Euler dynamics; run in _media to write the PNG.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Only classical fourth-order Runge--Kutta is used; no invariant projection.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

INERTIA = np.array([1.0, 2.0, 3.0])


def rhs(w):
    x, y, z = w
    return np.array([-y * z, z * x, -x * y / 3])


def integrate(w0, stop=14.0, step=0.005):
    t = np.linspace(0, stop, round(stop / step) + 1)
    w = np.empty((len(t), 3))
    w[0] = w0
    for i, h in enumerate(np.diff(t)):
        a = rhs(w[i])
        b = rhs(w[i] + h * a / 2)
        c = rhs(w[i] + h * b / 2)
        d = rhs(w[i] + h * c)
        w[i + 1] = w[i] + h * (a + 2 * b + 2 * c + d) / 6
    return t, w


def invariant_errors(w):
    e = (w**2 * INERTIA).sum(axis=1) / 2
    l2 = (w**2 * INERTIA**2).sum(axis=1)
    return {"energy_relative_drift": float(np.max(abs(e / e[0] - 1))),
            "angular_momentum_squared_relative_drift": float(np.max(abs(l2 / l2[0] - 1)))}


def make_figure():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, (ax, early) = plt.subplots(1, 2, figsize=(10, 4.3), layout="constrained")
    checks = {}
    colors = ["#2171b5", "#c52f24", "#238b45"]
    for axis in range(3):
        transverse = [i for i in range(3) if i != axis]
        w0 = np.zeros(3)
        w0[axis] = 1
        w0[transverse[0]] = 0.01
        t, w = integrate(w0)
        norm = np.linalg.norm(w[:, transverse], axis=1)
        ax.semilogy(t, norm, color=colors[axis], label=f"Axis {axis + 1}, ε = 0.01")
        checks[f"axis_{axis+1}"] = invariant_errors(w)
        _, fine = integrate(w0, step=0.0025)
        checks[f"axis_{axis+1}"]["step_halving_max_difference"] = float(np.max(abs(w - fine[::2])))
    for eps, color in [(0.01, "#c52f24"), (0.001, "#8c6bb1")]:
        t, w = integrate([eps, 1, 0], stop=8)
        norm = np.hypot(w[:, 0], w[:, 2])
        early.semilogy(t, norm, color=color, label=f"Nonlinear, ε = {eps:g}")
        exact_linear = eps * np.sqrt(np.cosh(t / np.sqrt(3))**2 + np.sinh(t / np.sqrt(3))**2 / 3)
        early.semilogy(t, exact_linear, "--", color=color, label=f"Linear, ε = {eps:g}")
        mask = t <= 4
        checks[f"intermediate_eps_{eps}"] = {
            **invariant_errors(w),
            "early_linear_relative_error_through_t4": float(np.max(abs(norm[mask] / exact_linear[mask] - 1)))}
    ax.set(title="Two bounded wobbles; one growing disturbance", xlabel="Normalized time t", ylabel="Transverse angular-velocity norm")
    early.set(title="Linear prediction before the first tumble", xlabel="Normalized time t", ylabel=r"$\sqrt{\omega_1^2+\omega_3^2}$")
    for a in (ax, early):
        a.grid(alpha=0.2, which="both")
        a.legend(fontsize=9, loc="upper left")
    fig.suptitle(r"Torque-free rotation: $(I_1,I_2,I_3)=(1,2,3)$, initial main component = 1", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)
    assert max(v.get("energy_relative_drift", 0) for v in checks.values()) < 1e-9
    assert max(v.get("angular_momentum_squared_relative_drift", 0) for v in checks.values()) < 1e-9
    assert max(v.get("step_halving_max_difference", 0) for v in checks.values()) < 1e-7
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    make_figure()
