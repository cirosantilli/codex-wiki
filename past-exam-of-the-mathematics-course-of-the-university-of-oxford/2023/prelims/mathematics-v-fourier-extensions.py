"""Plot the two Fourier extensions; write the PNG to the working directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the mirrored _media directory to put the image beside its page's media.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    pi = np.pi
    x = np.linspace(-3 * pi, 3 * pi, 18001)
    r = (x + pi) % (2 * pi) - pi
    even = np.minimum(np.abs(r), pi / 2)
    odd = np.sign(r) * even
    # Break the plotted limit at jumps instead of drawing vertical connectors.
    jump_indices = np.flatnonzero(np.abs(np.diff(r)) > pi)
    for j in jump_indices:
        odd[max(j - 1, 0) : j + 2] = np.nan
    odd[[0, -1]] = np.nan

    cosine_sum = np.full_like(x, 3 * pi / 8)
    sine_sum = np.zeros_like(x)
    for n in range(1, 61):
        an = 2 * (np.cos(n * pi / 2) - 1) / (pi * n**2)
        bn = 2 * np.sin(n * pi / 2) / (pi * n**2) - (-1) ** n / n
        cosine_sum += an * np.cos(n * x)
        sine_sum += bn * np.sin(n * x)

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 1, figsize=(10, 6.4), sharex=True,
                             layout="constrained", facecolor="white")
    for ax, limit, partial, title in zip(
        axes, (even, odd), (cosine_sum, sine_sum),
        ("Even periodic extension: cosine series",
         "Odd periodic extension: sine series"), strict=True
    ):
        ax.set_facecolor("white")
        ax.plot(x / pi, limit, color="#242424", linewidth=2.1,
                label="Limit of the series", zorder=2)
        ax.plot(x / pi, partial, color="#1577b8", linewidth=1.0,
                label=r"Partial sum through $n=60$", zorder=3)
        ax.set_title(title, loc="left")
        ax.set_ylabel("Value")
        ax.grid(alpha=0.18)
        ax.axhline(0, color="#888888", linewidth=0.6)
        ax.set_xlim(-3, 3)
        ax.legend(loc="lower right", fontsize=9)
    axes[0].set_ylim(-0.15, 1.9)
    axes[0].set_yticks([0, pi / 2], ["0", r"$\pi/2$"])
    axes[1].set_ylim(-2.1, 2.1)
    axes[1].set_yticks([-pi / 2, 0, pi / 2],
                      [r"$-\pi/2$", "0", r"$\pi/2$"])
    jumps = np.array([-3, -1, 1, 3])
    for side in [-1, 1]:
        axes[1].scatter(jumps, np.full(4, side * pi / 2), s=32,
                        facecolor="white", edgecolor="#242424", zorder=5,
                        clip_on=False)
    axes[1].scatter(jumps, np.zeros(4), s=24, color="#242424", zorder=6,
                    clip_on=False)
    axes[1].annotate("Gibbs oscillations", xy=(0.965, 1.82),
                     xytext=(1.45, 2.0), fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": "#1577b8"},
                     color="#1577b8")
    axes[1].set_xticks(np.arange(-3, 4),
                      [r"$-3\pi$", r"$-2\pi$", r"$-\pi$", "0",
                       r"$\pi$", r"$2\pi$", r"$3\pi$"])
    axes[1].set_xlabel("x")
    fig.savefig("mathematics-v-fourier-extensions.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
