"""Original stipulated Newtonian chirps, with independent orbital checks.

Python 3.14, numpy 2.3.5, matplotlib 3.10.7; no measured strain or noise.
Run from _media: the matching PNG is emitted in the current directory.
SI constants below are stipulated rounded inputs, not fitted GW150914 values.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


G = 6.67430e-11
C = 299792458.0
MSUN = 1.98847e30
MPC = 3.085677581491367e22
F0 = 20.0
XCUT = 0.10


def parameters(component_solar):
    m = component_solar * MSUN
    total = 2 * m
    mu = m / 2
    mc = mu**0.6 * total**0.4
    k = 96 / 5 * np.pi**(8 / 3) * (G * mc / C**3)**(5 / 3)
    fcut = C**3 / (np.pi * G * total) * XCUT**1.5
    tau = lambda f: 3 / (8 * k) * f**(-8 / 3)
    return {"M": total, "mu": mu, "mc": mc, "K": k, "fcut": fcut,
            "duration": tau(F0) - tau(fcut), "taucut": tau(fcut)}


def waveform(t_before_cut, p):
    """Phase is zero at 20 Hz, and t=0 is the stipulated cutoff."""
    t = np.asarray(t_before_cut)
    f = (8 * p["K"] / 3 * (p["taucut"] - t))**(-3 / 8)
    phase = 6 * np.pi / (5 * p["K"]) * (F0**(-5 / 3) - f**(-5 / 3))
    amp = 4 * (G * p["mc"])**(5 / 3) * (np.pi * f)**(2 / 3) / (C**4 * 500 * MPC)
    cos_i = 0.5  # iota = 60 degrees
    return f, phase, amp, amp * (1 + cos_i**2) / 2 * np.cos(phase), amp * cos_i * np.sin(phase)


def orbital_integral(p, steps):
    """Integrate a, phase, and radiated energy independently of f(t).

    RK4 evolves the separation from Newtonian E(a) and quadrupole P(a).
    The energy state is scaled by |E_initial| to avoid numerical imbalance.
    """
    total, mu = p["M"], p["mu"]
    a0 = (G * total / (np.pi * F0)**2)**(1 / 3)
    e0 = G * mu * total / (2 * a0)
    dt = p["duration"] / steps

    def rhs(y):
        a = y[0]
        power = 32 * G**4 * mu**2 * total**3 / (5 * C**5 * a**5)
        dEda = G * mu * total / (2 * a**2)
        return np.array([-power / dEda, 2 * np.sqrt(G * total / a**3), power / e0])

    y = np.array([a0, 0.0, 0.0])
    trajectory = [y.copy()]
    for _ in range(steps):
        k1 = rhs(y)
        k2 = rhs(y + dt * k1 / 2)
        k3 = rhs(y + dt * k2 / 2)
        k4 = rhs(y + dt * k3)
        y += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        trajectory.append(y.copy())
    states = np.array(trajectory)
    times = np.linspace(-p["duration"], 0, steps + 1)
    analytic_f, analytic_phase, *_ = waveform(times, p)
    numeric_f = np.sqrt(G * total / states[:, 0]**3) / np.pi
    expected_radiated = a0 / states[:, 0] - 1
    return {"steps": steps,
            "frequency_max_relative_error": float(np.max(np.abs(numeric_f / analytic_f - 1))),
            "phase_max_absolute_error_rad": float(np.max(np.abs(states[:, 1] - analytic_phase))),
            "energy_balance_max_error_in_initial_binding_energy": float(np.max(np.abs(states[:, 2] - expected_radiated)))}


def validate_model():
    checks = []
    for mass in (10, 20):
        p = parameters(mass)
        coarse = orbital_integral(p, 1000)
        fine = orbital_integral(p, 2000)
        assert fine["frequency_max_relative_error"] < 1e-8
        assert fine["phase_max_absolute_error_rad"] < 1e-6
        assert fine["energy_balance_max_error_in_initial_binding_energy"] < 1e-8
        # Phase convergence can reach floating-point roundoff for the shorter case.
        assert fine["phase_max_absolute_error_rad"] < max(coarse["phase_max_absolute_error_rad"] / 5, 1e-10)
        fdot = p["K"] * 30**(11 / 3)
        recovered_mc = C**3 / G * (5 / 96 * np.pi**(-8 / 3) * 30**(-11 / 3) * fdot)**(3 / 5)
        assert np.isclose(recovered_mc, p["mc"], rtol=1e-13)
        # f^(-8/3) has constant slope; differentiate analytic phase separately.
        t = -0.1
        eps = 1e-6
        f, phase, *_ = waveform(t, p)
        num_phase_rate = (waveform(t + eps, p)[1] - waveform(t - eps, p)[1]) / (2 * eps)
        assert np.isclose(num_phase_rate, 2 * np.pi * f, rtol=1e-8)
        acut = (G * p["M"] / (np.pi * p["fcut"])**2)**(1 / 3)
        assert np.isclose(G * p["M"] / (acut * C**2), XCUT, rtol=1e-13)
        checks.append({"component_masses_Msun": [mass, mass], "chirp_mass_Msun": p["mc"] / MSUN,
                       "cutoff_Hz": p["fcut"], "duration_s": p["duration"],
                       "cycles": 3 / (5 * p["K"]) * (F0**(-5 / 3) - p["fcut"]**(-5 / 3)),
                       "coarse": coarse, "fine": fine})
    # Independent dimensional exponent arithmetic: (kg, m, s).
    gdim, mdim, cdim, fdim, ddim = map(np.array, [( -1, 3, -2), (1, 0, 0), (0, 1, -1), (0, 0, -1), (0, 1, 0)])
    assert np.allclose(5 / 3 * (gdim + mdim - 3 * cdim) + 11 / 3 * fdim, [0, 0, -2])
    assert np.allclose(5 / 3 * (gdim + mdim) + 2 / 3 * fdim - 4 * cdim - ddim, [0, 0, 0])
    # Two overhead interferometers rotated by 30 degrees: F=(cos 2psi,sin 2psi).
    assert np.isclose(0.5**2 + (np.sqrt(3) / 2)**2, 1)
    assert np.isclose(parameters(20)["K"] / parameters(10)["K"], 2**(5 / 3))
    return {"cases": checks, "dimensional_checks": "fdot in s^-2; strain dimensionless",
            "chirp_mass_inversion": "passed", "phase_derivative": "passed", "compactness_cutoff": "passed"}


def main():
    print(json.dumps(validate_model(), indent=2))
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10.5})
    fig, axes = plt.subplots(2, 2, figsize=(11.6, 7.6), facecolor="white")
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.09, top=0.86, wspace=0.30, hspace=0.52)
    fig.suptitle("Calculated Newtonian chirps and ideal detector projections", fontsize=17, y=0.975)
    fig.text(0.5, 0.925, "Stipulated examples — no measured strain, no added noise; stop at GM/(ac²) = 0.10",
             ha="center", fontsize=10.5)
    colors = ("#17649c", "#b33435")
    for mass, color in zip((10, 20), colors):
        p = parameters(mass)
        t = np.linspace(-p["duration"], 0, 6000)
        f, *_ = waveform(t, p)
        axes[0, 0].plot(t, f, color=color, label=f"{mass} + {mass} M☉")
        axes[0, 0].plot([0], [p["fcut"]], "o", color=color, ms=4)
        tlast = np.linspace(-0.15, 0, 1500)
        axes[0, 1].plot(tlast, waveform(tlast, p)[3] * 1e21, color=color, lw=1.1,
                        label=f"{mass} + {mass} M☉")
    axes[0, 0].set(title="A. Frequency evolution to the stated cutoff", xlabel="Time before each model cutoff (s)", ylabel="GW frequency (Hz)")
    axes[0, 0].legend(loc="upper left", frameon=False)
    axes[0, 1].set(title="B. Final 0.15 s of the same two models", xlabel="Time before each model cutoff (s)", ylabel=r"$h_+$  ($10^{-21}$)")
    axes[0, 1].text(0.03, 0.96, "D = 500 Mpc; inclination = 60°", transform=axes[0, 1].transAxes,
                    va="top", fontsize=9, bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})

    p = parameters(20)
    t = np.linspace(-0.25, 0, 2500)
    _, phase, amp, hp, hc = waveform(t, p)
    ha, hb = hp, 0.5 * hp + np.sqrt(3) / 2 * hc
    delay = 0.007
    axes[1, 0].plot(t, ha * 1e21, color=colors[0], lw=1.2, label="A: (1, 0)")
    axes[1, 0].plot(t + delay, hb * 1e21, color=colors[1], lw=1.2, label="B: (½, √3/2), +7 ms")
    axes[1, 0].set(title="C. Same 20 + 20 M☉ source, two records", xlabel="Detector time relative to A cutoff (s)", ylabel=r"Projected strain ($10^{-21}$)", ylim=(-0.28, 0.34))
    axes[1, 0].legend(loc="upper left", frameon=False, fontsize=9)
    cp, ci = 0.625, 0.5
    envelope_b = np.hypot(0.5 * cp, np.sqrt(3) / 2 * ci)
    axes[1, 1].plot(t, ha / (amp * cp), color=colors[0], lw=1.2, label="A / known envelope")
    axes[1, 1].plot(t, hb / (amp * envelope_b), color=colors[1], lw=1.2, label="B shifted −7 ms / envelope")
    axes[1, 1].set(title="D. Time alignment leaves a projection phase", xlabel="Aligned model time (s)", ylabel="Normalized projected strain", ylim=(-1.55, 1.55))
    axes[1, 1].legend(loc="upper left", frameon=False, fontsize=8.8)
    assert np.max(np.abs(hb / (amp * envelope_b) - np.cos(phase - np.arctan2(np.sqrt(3) / 2 * ci, 0.5 * cp)))) < 1e-12
    for ax in axes.flat:
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
        ax.margins(x=0.01)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
