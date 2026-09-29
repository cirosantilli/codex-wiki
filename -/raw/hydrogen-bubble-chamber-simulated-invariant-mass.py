"""Invented two-daughter mass simulation, not historical data.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. No SciPy.
All numerical mass/momentum variables use GeV with c=1.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


DAUGHTER_MASS = .14
LOW, HIGH = .50, 1.10
CENTER, SCALE = .80, .020
N_SIGNAL, N_BACKGROUND = 700, 2400
MOMENTUM_NOISE = .012


def invariant_mass(momentum):
    """momentum has shape (events, daughters, three Cartesian components)."""
    energies = np.sqrt(DAUGHTER_MASS**2 + np.sum(momentum**2, axis=2))
    squared = np.sum(energies, axis=1)**2 - np.sum(np.sum(momentum, axis=1)**2, axis=1)
    assert np.all(squared > 0)
    return np.sqrt(squared)


def sample(seed=1968):
    rng = np.random.default_rng(seed)
    # Exact inverse-CDF sampling of the stipulated truncated Cauchy.
    a = np.arctan((LOW-CENTER)/SCALE)
    z = np.arctan((HIGH-CENTER)/SCALE)
    signal = CENTER + SCALE*np.tan(rng.uniform(a, z, N_SIGNAL))
    # t in [0,1] has density (4/3)(1-t/2), declining by a factor of two.
    # Inverting F(t)=(4/3)(t-t^2/4) gives t=2-sqrt(4-3u).
    t = 2 - np.sqrt(4 - 3*rng.random(N_BACKGROUND))
    background = LOW + (HIGH-LOW)*t
    truth = np.concatenate((background, signal))
    direction = rng.normal(size=(len(truth), 3))
    direction /= np.linalg.norm(direction, axis=1)[:, None]
    magnitude = np.sqrt((truth/2)**2-DAUGHTER_MASS**2)
    p = magnitude[:, None]*direction
    momenta = np.stack((p, -p), axis=1)
    exact = invariant_mass(momenta)
    np.testing.assert_allclose(exact, truth, rtol=2e-15, atol=2e-15)
    noisy = invariant_mass(momenta + rng.normal(0, MOMENTUM_NOISE, momenta.shape))
    return exact, noisy


def background_expectation(edges):
    t = (edges-LOW)/(HIGH-LOW)
    cdf = (4/3)*(t-t*t/4)
    return N_BACKGROUND*np.diff(cdf)


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    exact, noisy = sample()
    edges = np.linspace(LOW, HIGH, 41)
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 5.2), dpi=120, sharey=True, facecolor="white")
    fig.suptitle("Invented resonance + smooth background: same 3100 generated pairs", fontsize=15, y=.96)
    for ax, values, title in zip(axes, [exact, noisy], ["Exact stipulated momenta", "After chosen momentum noise"]):
        ax.hist(values, edges, histtype="step", color="#1e6091", lw=1.7, label="all simulated pairs")
        ax.hist(values[:N_BACKGROUND], edges, histtype="stepfilled", color="#e1b266", alpha=.48,
                label="known simulated background")
        ax.axvline(CENTER, color="#266f48", ls=":", lw=1.3)
        ax.set(xlabel=r"reconstructed invariant mass $M$ (GeV/$c^2$)", title=title,
               xlim=(LOW, HIGH), ylim=(0, 240))
        ax.grid(axis="y", alpha=.18)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].stairs(background_expectation(edges), edges, color="#a15d13", lw=1.5,
                   label="smooth input expectation")
    axes[0].set_ylabel(r"pairs per 0.015 GeV/$c^2$")
    axes[0].legend(loc="upper left", fontsize=8.5, frameon=False)
    axes[1].text(.515, 222, r"independent component noise:"+"\n"+r"$\sigma_p=0.012$ GeV/$c$", fontsize=10, va="top")
    axes[1].text(.515, 170, "The peak broadens;\nits width is not only a lifetime.", fontsize=10, va="top")
    fig.text(.5, .035, "All counts and distribution parameters stipulated; no historical measurements. Noise can move pairs outside the plotted range.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.07, right=.98, bottom=.17, top=.84, wspace=.12)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)
    print({"generated": len(exact), "background": N_BACKGROUND, "signal": N_SIGNAL,
           "noisy_in_display_range": int(np.sum((noisy>=LOW)&(noisy<=HIGH))),
           "signal_noise_mass_rms": float(np.sqrt(np.mean((noisy[N_BACKGROUND:]-exact[N_BACKGROUND:])**2)))})


if __name__ == "__main__":
    main()
