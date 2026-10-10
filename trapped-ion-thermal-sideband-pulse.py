"""Chosen Lamb-Dicke model and independent checks; Python 3.14/numpy 2.3/mpl 3.10.

Run from _media. Numerical inputs are teaching choices, not experimental data.
"""

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


MEAN_N = .25
ETA = .08
OMEGA = 2 * math.pi * 100_000  # Carrier Rabi angular frequency, rad/s.
NU = 2 * math.pi * 2_000_000  # Motional angular frequency, rad/s.
HBAR = 1.054571817e-34
KB = 1.380649e-23


def populations(mean_n, size=80):
    n = np.arange(size)
    r = mean_n / (mean_n + 1)
    return (1-r) * r**n


def excitation(theta, p, blue=False):
    n = np.arange(len(p)) + int(blue)
    return np.sin(np.asarray(theta)[..., None] * np.sqrt(n) / 2)**2 @ p


def check_model():
    p = populations(MEAN_N)
    n = np.arange(len(p))
    theta = np.linspace(0, 4*math.pi, 501)
    red, blue = excitation(theta, p), excitation(theta, p, blue=True)
    assert abs(p.sum()-1) < 2e-15
    assert abs(n @ p - MEAN_N) < 2e-15
    assert np.all((red >= 0) & (blue >= 0) & (red <= 1) & (blue <= 1))
    ratio_error = np.max(abs(red - .2*blue))
    assert ratio_error < 1e-14
    # Independent 2x2 spectral exponentials check U†U and transition probabilities.
    unitary_error = probability_error = 0.
    for occupation in (0, 1, 2, 7):
        h = np.array([[0., math.sqrt(occupation)], [math.sqrt(occupation), 0.]])/2
        eigenvalues, vectors = np.linalg.eigh(h)
        u = (vectors * np.exp(-1j*math.pi*eigenvalues)) @ vectors.T
        unitary_error = max(unitary_error, float(np.max(abs(u.conj().T @ u-np.eye(2)))))
        probability_error = max(probability_error, abs(abs(u[1, 0])**2-
                                                       math.sin(math.pi*math.sqrt(occupation)/2)**2))
    assert unitary_error < 2e-15 and probability_error < 2e-15
    temperature = HBAR*NU / (KB*math.log1p(1/MEAN_N))
    recovered_mean = 1/math.expm1(HBAR*NU/(KB*temperature))
    assert abs(recovered_mean-MEAN_N) < 1e-15
    # Direct Poisson sums for the separate chosen fluorescence example, threshold 3.
    bright_false_dark = math.exp(-12)*sum(12**k/math.factorial(k) for k in range(3))
    dark_false_bright = sum(math.exp(-.2)*.2**k/math.factorial(k) for k in range(3, 40))
    assert abs(dark_false_bright-(1-math.exp(-.2)*sum(.2**k/math.factorial(k) for k in range(3)))) < 1e-15
    return {"population_sum": float(p.sum()), "mean_n": float(n@p),
            "tail_bound": .2**len(p), "thermal_ratio_max_error": float(ratio_error),
            "unitary_max_error": unitary_error, "spectral_probability_max_error": probability_error,
            "red_pi_excitation": float(excitation(math.pi, p)),
            "blue_pi_excitation": float(excitation(math.pi, p, blue=True)),
            "pi_pulse_seconds": math.pi/(ETA*OMEGA), "temperature_kelvin": temperature,
            "eta_rms": ETA*math.sqrt(2*MEAN_N+1),
            "bright_false_dark": bright_false_dark, "dark_false_bright": dark_false_bright,
            "equal_prior_readout_error": (bright_false_dark+dark_false_bright)/2}


def main():
    checks = check_model()
    p = populations(MEAN_N)
    theta = np.linspace(0, 4*math.pi, 601)
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [1, 1.65]},
                             layout="constrained", facecolor="white")
    ax = axes[0]
    ax.bar(np.arange(6), p[:6], color="#2563eb", width=.65)
    ax.set(xlabel=r"Motional quantum number $n$", ylabel=r"Probability $p_n$",
           title=r"Chosen thermal population: $\bar n=0.25$", ylim=(0, .9), xticks=np.arange(6))
    ax.text(1.5, .7, r"$p_0=0.8$"+"\n"+r"$T=59.6\;\mu$K"+"\n"+r"$\nu/(2\pi)=2$ MHz", fontsize=12)
    ax = axes[1]
    ax.plot(theta/math.pi, excitation(theta, p, blue=True), color="#2563eb", lw=2.5,
            label=r"Blue: $\sqrt{n+1}$ coupling")
    ax.plot(theta/math.pi, excitation(theta, p), color="#dc2626", lw=2.5,
            label=r"Red: $\sqrt{n}$ coupling")
    ax.axvline(1, color="#64748b", ls="--", lw=1.4)
    ax.scatter([1, 1], [checks["red_pi_excitation"], checks["blue_pi_excitation"]],
               color=["#dc2626", "#2563eb"], zorder=5)
    ax.text(1.08, .56, r"$n=1$ red $\pi$ pulse"+"\n"+r"$t=62.5\;\mu$s", fontsize=11)
    ax.set(xlabel=r"Pulse area $\theta/\pi=\eta\Omega t/\pi$", ylabel="Internal excitation probability",
           title="Same pulse duration for both sidebands", xlim=(0, 4), ylim=(0, 1.02))
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(alpha=.18)
    fig.suptitle(r"Ideal sideband model: $\eta=0.08$, $\Omega/(2\pi)=100$ kHz; no heating or decoherence",
                 fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    main()
