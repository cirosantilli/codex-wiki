"""Original circuit diagram. Tested with Python 3.14.4 and Matplotlib 3.10.7.

Dependencies are declared in the repository pyproject.toml. Run from the desired
output directory; the PNG is always written there, independently of script path.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    ink = "#253243"
    blue = "#176a8a"
    fig, ax = plt.subplots(figsize=(9, 3.1), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(-1, 8.4), ylim=(-1, 2.05))
    ax.axis("off")

    def gate(x, y, label, width=0.68, height=0.56, color="#e9f2f7"):
        ax.add_patch(FancyBboxPatch(
            (x-width/2, y-height/2), width, height,
            boxstyle="round,pad=0.025", facecolor=color, edgecolor=ink,
            linewidth=1.6, zorder=3,
        ))
        ax.text(x, y, label, ha="center", va="center", fontsize=17,
                color=ink, zorder=4)

    for y, input_label, output_label in [
        (1, r"$|a\rangle$", r"$|a\rangle$"),
        (0, r"$|b\rangle$", r"$|b\oplus a\rangle$"),
    ]:
        ax.plot([0, 7], [y, y], lw=1.7, color=ink, zorder=1)
        ax.text(-0.27, y, input_label, ha="right", va="center", fontsize=16)
        ax.text(7.25, y, output_label, ha="left", va="center", fontsize=16)

    for x in [1.3, 5.7]:
        gate(x, 1, "$X$")
        gate(x, 0, "$H$")
    gate(3.5, 0.5, r"$U_\pi$", width=1.05, height=1.62, color="#ede9f7")
    ax.annotate("Time", xy=(6.6, 1.68), xytext=(0.4, 1.68),
                ha="left", va="center", fontsize=11, color=blue,
                arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.4})
    ax.text(3.5, -0.7, r"$U_\pi=\mathrm{diag}(1,-1,1,1)$"
            + "     (basis 00, 01, 10, 11)",
            ha="center", va="center", fontsize=13, color=ink)
    fig.suptitle("Controlled-NOT from the collisional phase gate",
                 fontsize=16, color=ink, y=0.965)
    fig.subplots_adjust(left=0.035, right=0.98, bottom=0.04, top=0.86)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, facecolor="white", transparent=False,
                metadata={"Software": "codex-wiki original circuit diagram"})
    plt.close(fig)
    print(output)


if __name__ == "__main__":
    main()
