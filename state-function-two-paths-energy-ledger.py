"""Original calculated transfer ledger; Python 3.14, matplotlib 3.10.7.

Run from _media; emits the matching opaque PNG into the current directory.
"""
from pathlib import Path
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    e0 = 8.314 * 300 / 1000  # kJ for the stipulated one-mole model
    du = 1.5 * e0
    work = [2 * e0 * math.log(3), e0 * math.log(3)]
    heat = [w + du for w in work]
    blue, orange, green = "#1768a5", "#bf5b17", "#278165"
    fig = plt.figure(figsize=(9, 5.5), dpi=120, facecolor="white")
    ax = fig.add_axes((0.18, 0.30, 0.76, 0.49), facecolor="white")
    for y, w, q, color in zip([1, 0], work, heat, [blue, orange]):
        ax.barh(y, w, height=0.46, color=color, edgecolor="white")
        ax.barh(y, du, left=w, height=0.46, color=green, edgecolor="white")
        ax.text(w / 2, y, rf"$W_{{\rm by}}$ out\n{w:.3f} kJ".replace("\\n", "\n"), ha="center", va="center", color="white", fontsize=12, fontweight="bold")
        ax.text(w + du / 2, y, rf"$\Delta U$ stored\n{du:.3f} kJ".replace("\\n", "\n"), ha="center", va="center", color="white", fontsize=12, fontweight="bold")
        ax.text(q, y + 0.34, rf"$Q$ in = {q:.3f} kJ", ha="right", fontsize=13, color=color)
    ax.set(xlim=(0, 10), ylim=(-0.48, 1.58), xlabel="Energy (kJ)")
    ax.set_yticks([1, 0], ["Upper route\nheat first", "Lower route\nexpand first"])
    ax.set_xticks(range(0, 11, 2))
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=14)
    ax.grid(axis="x", alpha=0.16)
    ax.set_axisbelow(True)
    fig.suptitle("Different transfers, identical stored increment", y=0.96, fontsize=17, fontweight="bold")
    fig.text(0.5, 0.855, r"$\Delta U=Q-W_{\rm by}$    or    $Q=W_{\rm by}+\Delta U$", ha="center", fontsize=15)
    fig.legend(handles=[Patch(facecolor=blue, label="upper-route work"), Patch(facecolor=orange, label="lower-route work"), Patch(facecolor=green, label="common storage")], loc="lower center", bbox_to_anchor=(0.5, 0.125), ncol=3, frameon=False, fontsize=11)
    fig.text(0.5, 0.080, r"One mole, $300\to600$ K, $0.010\to0.030\;\mathrm{m^3}$; $R=8.314\;\mathrm{J\,mol^{-1}\,K^{-1}}$", ha="center", fontsize=11)
    fig.text(0.5, 0.035, "Calculated ideal-gas example; lengths use unrounded values. Heat and work are transfers.", ha="center", fontsize=10, color="#45515c")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
