"""Compare locations for (0, 1, 2, 3, 4, M), with fixed scale and threshold."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def huber_location(data, k=2.0, scale=1.0):
    """Solve the decreasing score by bisection, independently of the exact formula."""
    lo, hi = float(np.min(data)), float(np.max(data))
    for _ in range(70):
        midpoint = (lo + hi) / 2
        if np.clip((data - midpoint) / scale, -k, k).sum() > 0:
            lo = midpoint
        else:
            hi = midpoint
    return (lo + hi) / 2


def main():
    moving = np.linspace(0, 40, 801)
    data = np.column_stack([np.tile(np.arange(5.0), (len(moving), 1)), moving])
    means = data.mean(axis=1)
    medians = np.median(data, axis=1)
    huber = np.array([huber_location(row) for row in data])
    exact = np.minimum((8 + moving) / 5, 2.5)
    assert np.allclose(huber, exact, rtol=0, atol=2e-14)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9, 5), layout="constrained")
    inset = ax.inset_axes([0.42, 0.48, 0.53, 0.43])
    for panel in (ax, inset):
        panel.plot(moving, means, color="#c47a19", linewidth=2.2, label="Sample mean")
        panel.plot(moving, medians, color="#9863ac", linewidth=4.2, linestyle="--", label="Sample median")
        panel.plot(moving, huber, color="#176c9c", linewidth=1.9, label="Huber location (s=1, k=2)")
        panel.grid(alpha=0.2)
        panel.set_facecolor("white")
    ax.set(xlim=(0, 40), ylim=(1.15, 8.8), xlabel=r"Moving observation $M$", ylabel="Fitted location", title="Data (0, 1, 2, 3, 4, M): one observation moves")
    ax.legend(loc="upper left", fontsize=10)
    ax.scatter([40], [50 / 6], color="#c47a19", zorder=5)
    ax.annotate("Median = Huber = 2.5 for M ≥ 5", xy=(29, 2.5), xytext=(12, 3.15), arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    inset.set(xlim=(0, 6), ylim=(1.35, 2.82), title="Clipping transition", xlabel=r"$M$", ylabel="Location")
    inset.axvline(4.5, color="#777777", linestyle=":", linewidth=1)
    inset.text(4.5, 2.72, "M = 4.5", ha="center", fontsize=9)
    inset.tick_params(labelsize=9)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
