"""Show convergence and persistent square-wave Fourier overshoot; output to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def odd_sum(x, count):
    harmonics = np.arange(1, 2*count, 2)
    return (4/np.pi) * (np.sin(np.outer(x, harmonics)) / harmonics).sum(axis=1)


def main():
    counts = [3, 10, 50]
    x = np.linspace(-np.pi, np.pi, 5001)
    zoom = np.linspace(-.55, .55, 2401)
    assert np.allclose(odd_sum(np.array([0.0]), 50), 0)
    assert np.allclose(odd_sum(-zoom, 10), -odd_sum(zoom, 10), atol=1e-12)
    peaks = [(count, np.pi/(2*count), float(odd_sum(np.array([np.pi/(2*count)]), count)[0]))
             for count in counts]
    dense_count = 10000
    limiting_peak = float(odd_sum(np.array([np.pi/(2*dense_count)]), dense_count)[0])
    assert np.isclose(limiting_peak, 1.1789797444721675, atol=2e-8)
    # Midpoint quadrature gives an independent limiting-height calculation.
    u = (np.arange(20000) + .5) / 20000
    midpoint_limit = 2 * np.mean(np.sinc(u))
    assert np.isclose(midpoint_limit, limiting_peak, atol=2e-8)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.8), dpi=120, facecolor="white")
    colors = ["#be7723", "#377baa", "#298366"]
    for ax, domain in zip(axes, [x, zoom]):
        # Plot the one-sided levels separately: vertical lines are not function values.
        left = domain[domain < 0]
        right = domain[domain > 0]
        ax.plot(left, -np.ones_like(left), color="#303943", lw=1.7, linestyle="--", label="Square-wave levels")
        ax.plot(right, np.ones_like(right), color="#303943", lw=1.7, linestyle="--")
        ax.scatter([0], [0], color="#303943", s=35, zorder=6)
        for count, color in zip(counts, colors):
            ax.plot(domain, odd_sum(domain, count), color=color, lw=1.8, label=f"M = {count} odd modes")
        ax.set(ylim=(-1.35, 1.35), xlabel="Angular coordinate x (radians)", ylabel="Value")
        ax.grid(color="#e6eaed")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set(xlim=(-np.pi, np.pi), title="One complete period")
    axes[0].set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], ["−π", "−π/2", "0", "π/2", "π"])
    axes[1].set(xlim=(-.55, .55), title="The first peaks approach the jump")
    axes[1].axhline(limiting_peak, color="#9b566a", lw=1.4, linestyle=":")
    for (_, location, height), color in zip(peaks, colors):
        axes[1].scatter([location], [height], color=color, s=50, zorder=5)
    axes[1].text(-.53, 1.21, "Limiting first peak ≈ 1.17898", color="#87495b", fontsize=11,
                 bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    axes[1].text(-.53, -.52, "At the jump:\nevery sum equals 0", fontsize=11,
                 bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    fig.suptitle("Fourier sums sharpen a square wave while retaining overshoot", fontsize=16, y=.98)
    fig.text(.5, .105, "M nonzero odd modes retain frequencies 1, 3, …, 2M−1", ha="center", fontsize=12)
    fig.legend(*axes[0].get_legend_handles_labels(), loc="lower center", ncol=4,
               frameon=False, bbox_to_anchor=(.5, .024), fontsize=11)
    fig.subplots_adjust(left=.07, right=.98, top=.83, bottom=.23, wspace=.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print({"first_peaks": peaks, "limiting_peak": limiting_peak,
           "overshoot_fraction_of_jump": (limiting_peak-1)/2})


if __name__ == "__main__":
    main()
