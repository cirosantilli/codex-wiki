"""Synthetic light curve, not Kepler measurements.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
From _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../light-curve-aperture-calibration.py
Writes only light-curve-aperture-calibration.png to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DEPTH = 0.01
HALF_DURATION = 2.0  # hours
HALF_FLAT = 1.4  # hours
EXPOSURE = 0.5  # hours
REFERENCE_RATE = 100_000.0  # electrons/second
SKY_RATE = 4_000.0  # electrons/second
DRIFT = 0.0003  # per hour
SIGMA = 0.0006  # injected relative Gaussian scatter, not a detector noise model


def relative_flux(t):
    """A continuous trapezoid, deliberately not a physical transit profile."""
    t = np.asarray(t)
    fraction = np.clip((HALF_DURATION - np.abs(t)) / (HALF_DURATION - HALF_FLAT), 0, 1)
    return 1 - DEPTH * fraction


def exposure_mean(t, response_drift=0.0, duration=EXPOSURE):
    """Exact piecewise integral of linear response times piecewise-linear flux."""
    centres = np.asarray(t, dtype=float)
    result = np.empty_like(centres)
    for index in np.ndindex(centres.shape):
        left, right = centres[index] - duration / 2, centres[index] + duration / 2
        edges = [left] + [x for x in (-2.0, -1.4, 1.4, 2.0) if left < x < right] + [right]
        integral = 0.0
        for a, b in zip(edges[:-1], edges[1:]):
            # Simpson's rule is exact on each quadratic segment.
            points = np.array([a, (a + b) / 2, b])
            values = (1 + response_drift * points) * relative_flux(points)
            integral += (b - a) * (values[0] + 4 * values[1] + values[2]) / 6
        result[index] = integral / duration
    return result


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(17091)
    samples = np.arange(-5.75, 6.0, EXPOSURE)
    dense = np.linspace(-6, 6, 1201)
    response = 1 + DRIFT * samples
    source_mean = exposure_mean(samples, DRIFT)
    injected_noise = rng.normal(0, SIGMA, samples.size)
    recorded = SKY_RATE + REFERENCE_RATE * (source_mean + response * injected_noise)
    corrected = (recorded - SKY_RATE) / (REFERENCE_RATE * response)
    expected = source_mean / response

    fig, axes = plt.subplots(2, 1, figsize=(8.6, 6.4), sharex=True)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.12, right=0.97, top=0.86, bottom=0.10, hspace=0.33)
    fig.suptitle("From detector counts to a light curve", fontsize=16, y=0.97)
    fig.text(0.5, 0.91, "Synthetic toy example • no observed source • 30-minute exposures", ha="center", color="#555555")
    ax = axes[0]
    ax.set_title("1. Recorded aperture rate includes sky and response drift", loc="left", fontsize=12)
    ax.plot(dense, (SKY_RATE + REFERENCE_RATE * (1 + DRIFT * dense)) / 1000,
            "--", color="#b36a12", lw=1.6, label="baseline without transit")
    ax.plot(dense, (SKY_RATE + REFERENCE_RATE * (1 + DRIFT * dense) * relative_flux(dense)) / 1000,
            color="#156c97", lw=2, label="instantaneous toy model")
    ax.errorbar(samples, recorded / 1000, yerr=REFERENCE_RATE * response * SIGMA / 1000,
                fmt="o", ms=3.5, color="#293b48", elinewidth=0.8, capsize=2, label="synthetic exposure samples")
    ax.set_ylabel("Aperture rate\n(thousand electrons/s)")
    ax.set_ylim(102.7, 104.35)
    ax.legend(fontsize=9, loc="lower right", framealpha=1)

    ax = axes[1]
    ax.set_title("2. Subtract known sky; divide by known response and reference", loc="left", fontsize=12)
    ax.axhline(1, color="#b36a12", ls="--", lw=1.4)
    ax.plot(dense, relative_flux(dense), color="#156c97", lw=2, label="instantaneous relative flux")
    ax.plot(samples, expected, "s", mfc="white", mec="#ba4c40", ms=6, label="exposure-averaged expectation")
    ax.errorbar(samples, corrected, yerr=SIGMA, fmt="o", ms=3.5, color="#293b48",
                elinewidth=0.8, capsize=2, label="corrected synthetic samples")
    ax.set_ylabel("Relative brightness")
    ax.set_xlabel("Time from mid-transit (hours)")
    ax.set_ylim(0.9875, 1.003)
    ax.set_xlim(-6, 6)
    ax.annotate("1% depth", xy=(0, 0.99), xytext=(0, 0.995), ha="center", fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.legend(fontsize=9, loc="lower right", framealpha=1)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.16)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=135, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
