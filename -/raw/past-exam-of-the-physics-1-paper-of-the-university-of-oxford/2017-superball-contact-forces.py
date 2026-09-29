"""Draw the signed contact-force model; save one PNG in the current directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(6, 4.4), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.add_patch(Circle((0, 1.1), 1.1, facecolor="#edf3fa", edgecolor="#315775", lw=2))
    ax.plot([-1.8, 1.8], [0, 0], color="0.25", lw=1.6)
    ax.plot(0, 1.1, "o", color="#315775", ms=4)

    def arrow(start, end, color):
        ax.annotate("", end, start,
                    arrowprops={"arrowstyle": "-|>", "lw": 2.4, "color": color})

    arrow((0, 0), (0, 0.65), "#247b57")
    ax.text(0.12, 0.3, r"$N$", color="#247b57")
    arrow((0, 1.1), (0, 0.75), "#9e3546")
    ax.text(0.13, 0.89, r"$Mg$", color="#9e3546")
    arrow((0, 0), (-1.25, 0), "#c05c12")
    ax.text(-0.9, -0.27, r"$f_t$", color="#c05c12")
    angles = np.linspace(np.deg2rad(-10), np.deg2rad(120), 80)
    sx, sy = 0.48 * np.cos(angles), 1.1 + 0.48 * np.sin(angles)
    ax.plot(sx, sy, color="#315775", lw=1.8)
    arrow((sx[-5], sy[-5]), (sx[-1], sy[-1]), "#315775")
    ax.text(-0.65, 1.8, r"$+\Omega$ anticlockwise", fontsize=11, color="#315775")
    arrow((1.4, 0.2), (1.95, 0.2), "0.45")
    arrow((1.4, 0.2), (1.4, 0.8), "0.45")
    ax.text(1.93, 0.25, r"$x$", color="0.4", fontsize=10)
    ax.text(1.45, 0.77, r"$y$", color="0.4", fontsize=10)
    ax.text(0, -0.56, r"Initial contact slip: $w_1=v_1+a\Omega_1>0$",
            ha="center", fontsize=11)
    ax.set(xlim=(-2.05, 2.2), ylim=(-0.7, 2.5), aspect="equal")
    ax.set_title("Forces at the start of rough contact", fontsize=13, pad=10)
    ax.axis("off")
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, dpi=120, facecolor="white", metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
