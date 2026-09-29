"""Original lumped energy-balance network; Python 3.14, Matplotlib 3.10."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(8.2, 3.4), layout="constrained")
    ax.set(xlim=(-0.3, 10.1), ylim=(-0.3, 3.4))
    ax.axis("off")
    positions = [0.8, 4.0, 7.2]
    labels = [
        ("Fuel reservoir", r"$C_F,\ \overline{T}_F$", "#e9b89d"),
        ("Moderator reservoir", r"$C_M,\ \overline{T}_M$", "#d5d8df"),
        ("Coolant reservoir", r"$C_C,\ \overline{T}_C$", "#a8cddd"),
    ]
    for x, (title, math_label, color) in zip(positions, labels):
        ax.add_patch(FancyBboxPatch((x, 1), 2.0, 1.0, boxstyle="round,pad=0.04",
                                   facecolor=color, edgecolor="#444444"))
        ax.text(x + 1, 1.68, title, ha="center", fontsize=10)
        ax.text(x + 1, 1.27, math_label, ha="center", fontsize=13)
    arrow = {"arrowstyle": "->", "linewidth": 1.6, "color": "#333333"}
    ax.annotate("", xy=(0.75, 1.5), xytext=(-0.2, 1.5), arrowprops=arrow)
    ax.text(0.22, 1.75, r"$P$", ha="center", fontsize=13)
    for x, y, text in [(2.85, 3.95, r"$Q_{FM}$"), (6.05, 7.15, r"$Q_{MC}$")]:
        ax.annotate("", xy=(y, 1.5), xytext=(x, 1.5), arrowprops=arrow)
        ax.text((x + y) / 2, 1.8, text, ha="center", fontsize=12)
    ax.annotate("", xy=(10, 1.5), xytext=(9.25, 1.5), arrowprops=arrow)
    ax.text(9.60, 1.8, r"$Q_{\rm out}$", ha="center", fontsize=12)
    ax.text(5.0, 2.8, "Stored energy changes = inputs minus outputs",
            ha="center", fontsize=13, weight="bold")
    ax.text(5.0, 0.35,
            r"$Q_{FM}=(\overline{T}_F-\overline{T}_M)/R_1$"
            r"       $Q_{MC}=(\overline{T}_M-\overline{T}_C)/R_2$",
            ha="center", fontsize=12)
    ax.text(5.0, -0.10, r"$Q_{\rm out}=2W_Cc_C(\overline{T}_C-T_i)$",
            ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
