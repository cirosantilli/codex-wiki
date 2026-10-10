"""Original schematic of published phenol IR comparisons; no spectral data.

Source: Saggu, Levinson, Boxer (2011), doi:10.1021/ja2069592,
Figure 1, Table 1, and the dilution-control discussion.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../hydrogen-bond-phenol-infrared-controls.py
Writes only hydrogen-bond-phenol-infrared-controls.png to the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 6.1), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.1))
    ax.axis("off")
    ax.text(0.2, 5.79, "Test association by changing the partner", fontsize=20, weight="bold", color="#202a35")
    ax.text(0.2, 5.42, "TOY EXPERIMENT LAYOUT • qualitative comparisons • no spectral curves or data", fontsize=10.5, color="#555555")
    cards = [
        (0.2, "Reference", "Phenol in CCl₄", "Free O–H peak"),
        (3.55, "Association", "Phenol in benzene", "O–H peak shifts lower"),
        (6.9, "Dilution control", "Add CCl₄", "Free + associated peaks"),
    ]
    for x, heading, contents, result in cards:
        ax.add_patch(FancyBboxPatch((x, 3.34), 2.85, 1.66, boxstyle="round,pad=0.06",
                                  facecolor="#f7f8fa", edgecolor="#b6c3ce"))
        ax.text(x+0.13, 4.72, heading, weight="bold", fontsize=13, color="#185d9b")
        ax.text(x+0.13, 4.3, contents, fontsize=12)
        ax.annotate("", xy=(x+1.42, 3.84), xytext=(x+1.42, 4.08),
                    arrowprops={"arrowstyle": "->", "color": "#555555"})
        ax.text(x+0.13, 3.59, result, fontsize=10.5)
    ax.annotate("", xy=(6.73, 4.17), xytext=(6.49, 4.17), arrowprops={"arrowstyle": "->", "lw": 1.6})
    ax.text(0.2, 2.85, "Dilution separates free and associated forms in the same sample.", fontsize=13, weight="bold")
    ax.text(0.2, 2.45, "Free peak nearly fixed; associated peak depends on the ring partner.", fontsize=12)
    ax.plot([0.2, 9.8], [2.12, 2.12], color="#dce1e7", lw=1)
    ax.text(0.25, 1.74, "Role assignment", fontsize=13, weight="bold")
    ax.text(2.6, 1.16, "phenol", fontsize=13, ha="right")
    ax.plot([2.77, 3.18], [1.23, 1.23], color="#202a35", lw=2)
    ax.text(3.37, 1.23, "O", color="#a94b13", fontsize=23, ha="center", va="center")
    ax.plot([3.56, 4.08], [1.23, 1.23], color="#202a35", lw=2)
    ax.text(4.28, 1.23, "H", color="#a94b13", fontsize=23, ha="center", va="center")
    ax.plot([4.5, 5.75], [1.23, 1.23], color="#555555", lw=2, linestyle=":")
    ax.add_patch(Ellipse((6.65, 1.23), 1.55, 0.59, edgecolor="#185d9b", facecolor="#edf4fa", lw=2))
    ax.text(6.65, 1.23, "ring π region", ha="center", va="center", fontsize=11, color="#185d9b")
    ax.text(3.8, 0.62, "O–H donor", color="#a94b13", ha="center", fontsize=12)
    ax.text(6.65, 0.62, "benzene acceptor", color="#185d9b", ha="center", fontsize=12)
    ax.text(0.2, 0.12, "Saggu, Levinson & Boxer (2011). The connector does not specify contact geometry.", fontsize=10.5, color="#555555")
    fig.subplots_adjust(left=0.025, right=0.99, top=0.99, bottom=0.02)
    fig.savefig(Path.cwd() / "hydrogen-bond-phenol-infrared-controls.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
