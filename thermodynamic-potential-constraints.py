"""Draw the vessel constraints selecting Helmholtz or Gibbs free energy.

Writes an opaque white PNG with this script's basename in the working directory.
Tested with Python 3.14.4, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 5.0), dpi=130)
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.17, top=0.74, wspace=0.10)
    fig.suptitle("The surroundings select the free-energy minimum", fontsize=15)
    fig.text(0.5, 0.875, "Closed system • fixed composition • only pressure–volume work",
             ha="center", fontsize=12)
    for ax, color in zip(axes, ["#236a9e", "#b6532b"]):
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
        ax.add_patch(Rectangle((0.03, 0.23), 0.94, 0.64, facecolor="#eef4f8",
                               edgecolor="#abbfce", lw=1.2))
        ax.text(0.5, 0.29, "Thermal reservoir at T", ha="center", fontsize=11)
        ax.annotate("", xy=(0.27, 0.51), xytext=(0.12, 0.51),
                    arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.8})
        ax.text(0.105, 0.59, "Heat", fontsize=10, ha="center", color=color)
        ax.add_patch(Rectangle((0.30, 0.40), 0.42, 0.27, facecolor="white",
                               edgecolor=color, lw=2))
        ax.text(0.51, 0.49, "System", ha="center", color=color)
    left, right = axes
    left.set_title("Rigid sealed vessel", fontsize=13, pad=10)
    left.plot([0.30, 0.72], [0.67, 0.67], color="#236a9e", lw=5)
    left.text(0.51, 0.75, "Fixed volume V", ha="center", color="#236a9e", fontsize=11)
    left.text(0.5, 0.15, r"Minimize $F=U-TS$", ha="center", fontsize=15, color="#236a9e")
    left.text(0.5, 0.02, "Pressure may change", ha="center", fontsize=11)

    right.set_title("Sealed cylinder with loaded piston", fontsize=13, pad=10)
    right.add_patch(Rectangle((0.30, 0.67), 0.42, 0.025,
                              facecolor="#b6532b", edgecolor="#b6532b"))
    right.plot([0.51, 0.51], [0.695, 0.75], color="#b6532b", lw=3)
    right.add_patch(Rectangle((0.42, 0.75), 0.18, 0.06,
                              facecolor="#dddddd", edgecolor="#555555"))
    right.text(0.51, 0.92, "Load fixes pressure p", ha="center", fontsize=11)
    right.annotate("", xy=(0.79, 0.76), xytext=(0.79, 0.58),
                   arrowprops={"arrowstyle": "<->", "color": "#b6532b", "lw": 1.8})
    right.text(0.5, 0.15, r"Minimize $G=U-TS+pV$", ha="center", fontsize=15, color="#b6532b")
    right.text(0.5, 0.02, "Volume may change", ha="center", fontsize=11)
    fig.text(0.5, 0.045, "Compare permitted states at the same imposed T and V, or T and p.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
