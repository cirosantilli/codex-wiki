"""Plot the two Fourier-series limits in Oxford Prelims V resit 2021, Q4(b).

Run in the desired output directory; writes the PNG to the current directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (root pyproject.toml).
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True, layout="constrained")
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="0.55", linewidth=0.8)
        ax.axvline(0, color="0.55", linewidth=0.8)
        ax.axvspan(0, 1, color="#dae8f2", alpha=0.55)
        ax.grid(alpha=0.2)
        ax.set_xlim(-3.1, 3.1)
        ax.set_xticks(np.arange(-3, 4))
        ax.set_ylabel("Series limit")

    # Abscissae are x/pi; the ordinate is the actual (unscaled) function value.
    scaled_x = np.linspace(-3, 3, 1801)
    reduced_x = np.pi * ((scaled_x + 1) % 2 - 1)
    axes[0].plot(scaled_x, 1 + np.abs(reduced_x), color="#1565a5", linewidth=2)
    axes[0].set_title("Cosine series: continuous even extension, period 2π")
    axes[0].set_ylim(0, 4.7)
    axes[0].set_yticks([0, 1, 1 + np.pi], ["0", "1", "1 + π"])
    axes[0].text(0.5, 0.25, "Original interval", ha="center", fontsize=9)

    # Each open interval between consecutive multiples of pi is a line segment.
    # Separate segments and open endpoints avoid drawing vertical jump lines.
    for k in range(-3, 3):
        segment_x = np.array([k, k + 1], dtype=float) * np.pi
        midpoint = (k + 0.5) * np.pi
        shift = 2 * np.pi * np.floor((midpoint + np.pi) / (2 * np.pi))
        segment_y = segment_x - shift + np.sign(midpoint - shift)
        axes[1].plot(segment_x / np.pi, segment_y, color="#ad3b29", linewidth=2)
        axes[1].plot(
            segment_x / np.pi,
            segment_y,
            "o",
            markersize=5,
            markerfacecolor="white",
            markeredgecolor="#ad3b29",
            markeredgewidth=1.2,
        )
    axes[1].plot(np.arange(-3, 4), np.zeros(7), "o", color="black", markersize=4)
    axes[1].set_title(
        "Sine series: odd extension, value 0 at every jump\n"
        "Open circles: excluded endpoint values; black dots: series values",
        fontsize=11,
    )
    axes[1].set_ylim(-4.7, 4.7)
    axes[1].set_yticks(
        [-1 - np.pi, -1, 0, 1, 1 + np.pi], ["−(1 + π)", "−1", "0", "1", "1 + π"]
    )
    axes[1].set_xlabel("x / π")
    fig.savefig("mathematics-v-resit-fourier-extensions.png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
