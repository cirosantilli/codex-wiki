"""Generate heat-engine-cyclic-energy-flows.png in the current directory.

Run from _media with MPLBACKEND=Agg and
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
All numbers are a constructed two-reservoir cyclic-engine budget, not data.
"""

from fractions import Fraction

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, FancyBboxPatch


def main():
    q_hot, q_cold = 1000, 600
    work = q_hot - q_cold
    t_hot, t_cold = 600, 300
    efficiency = Fraction(work, q_hot)
    entropy = Fraction(q_cold, t_cold) - Fraction(q_hot, t_hot)
    assert work == 400 and efficiency == Fraction(2, 5)
    assert entropy == Fraction(1, 3)
    assert efficiency < 1 - Fraction(t_cold, t_hot)

    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.6, 5.8), dpi=110, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 7))
    ax.axis("off")

    def box(x, y, width, height, color, label):
        ax.add_patch(FancyBboxPatch(
            (x, y), width, height, boxstyle="round,pad=0.06",
            linewidth=1.5, edgecolor=color, facecolor="white"))
        ax.text(x + width / 2, y + height / 2, label,
                ha="center", va="center", color=color, fontsize=12)

    def arrow(x, y, dx, dy, amount, color):
        # Shaft widths, rather than arrow lengths, encode transferred energy.
        width = 0.5 * amount / q_hot
        ax.add_patch(FancyArrow(
            x, y, dx, dy, width=width, head_width=width + 0.20,
            head_length=0.28, length_includes_head=True,
            facecolor=color, edgecolor=color))

    hot, cold, output = "#ac342b", "#2166ac", "#287749"
    box(1.0, 5.55, 4.2, 0.95, hot, "Hot reservoir\n600 K (fixed)")
    box(1.0, 2.85, 4.2, 1.2, "#333333", "Cyclic device\nSame state after every cycle")
    box(1.0, 0.8, 4.2, 0.95, cold, "Cold reservoir\n300 K (fixed)")
    box(7.15, 2.85, 2.6, 1.2, output, "Net work output\n400 J")
    arrow(3.1, 5.45, 0, -1.28, q_hot, hot)
    arrow(3.1, 2.75, 0, -0.9, q_cold, cold)
    arrow(5.33, 3.45, 1.7, 0, work, output)
    ax.text(4.0, 4.79, r"$Q_h=1000\ \mathrm{J}$", color=hot,
            ha="left", va="center")
    ax.text(4.0, 2.27, r"$Q_c=600\ \mathrm{J}$", color=cold,
            ha="left", va="center")
    ax.text(6.15, 4.12, r"$W=400\ \mathrm{J}$", color=output,
            ha="center", va="bottom")
    fig.suptitle("A complete cycle divides the incoming energy", fontsize=15, y=0.97)
    fig.text(0.5, 0.065,
             r"$\Delta U=0\qquad W=Q_h-Q_c\qquad \eta=W/Q_h=40\%$",
             ha="center", fontsize=14)
    fig.text(0.5, 0.022,
             "Constructed model • Transfers per cycle • Arrow widths show energy amounts",
             ha="center", fontsize=10, color="#444444")
    fig.subplots_adjust(left=0.025, right=0.98, bottom=0.15, top=0.90)
    fig.savefig("heat-engine-cyclic-energy-flows.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
