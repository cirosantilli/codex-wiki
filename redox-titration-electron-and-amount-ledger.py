"""Original amount ledger; run from _media to write the PNG to CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The numerical example is constructed, not measured.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10, 7.2), dpi=120)
    ax = fig.add_axes([0.04, 0.04, 0.92, 0.86])
    ax.set(xlim=(0, 10), ylim=(0, 7))
    ax.axis("off")
    fig.suptitle("Redox titration: from delivery to iron inventory", fontsize=20, y=0.96)
    ax.text(5, 6.8, "Constructed example • acidic five-to-one balance • no measured data",
            ha="center", fontsize=12, color="#465563")

    def box(x, y, w, h, title, detail, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                                   facecolor="#f7f9fb", edgecolor=color, lw=1.6))
        ax.text(x + w / 2, y + h * 0.70, title, ha="center", va="center",
                fontsize=14, weight="bold", color=color)
        ax.text(x + w / 2, y + h * 0.30, detail, ha="center", va="center", fontsize=12)

    box(0.15, 5.30, 4.55, 1.05, "12.60 − 0.10 = 12.50 mL",
        "sample titre − blank = corrected delivery", "#713e91")
    box(5.30, 5.30, 4.55, 1.05, "0.2500 mmol permanganate",
        "0.02000 mol/L × 0.01250 L", "#713e91")
    ax.annotate("", xy=(5.20, 5.83), xytext=(4.80, 5.83),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#713e91"})
    ax.text(5, 4.85, "Equal electron amounts; unequal amounts of reacting species",
            ha="center", fontsize=15, weight="bold")

    table = ax.table(
        cellText=[
            [r"$\mathrm{MnO}_4^-\to\mathrm{Mn}^{2+}$", "0.2500 mmol", "accepts 5", "1.250 mmol"],
            [r"$\mathrm{Fe}^{2+}\to\mathrm{Fe}^{3+}$", "1.250 mmol", "supplies 1", "1.250 mmol"],
        ],
        colLabels=["Conversion", "Reacting amount", "Electrons / entity", "Electron amount"],
        colWidths=[0.27, 0.23, 0.25, 0.25], cellLoc="center",
        bbox=[0.015, 0.42, 0.97, 0.22],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#b7c3cc")
        cell.set_facecolor("#eaf0f4" if row == 0 else "white")
        if row == 1:
            cell.set_text_props(color="#713e91")
        elif row == 2:
            cell.set_text_props(color="#a14e18")

    ax.text(5, 2.52, r"$5\times0.2500 = 1\times1.250\quad$ (mmol of formal electrons)",
            ha="center", fontsize=17)
    ax.text(5, 2.12, "The electron ledger cancels; free electrons do not accumulate in the flask.",
            ha="center", fontsize=12, color="#465563")
    box(0.15, 0.75, 9.70, 1.02, "1.250 mmol Fe²⁺ ÷ 25.00 mL = 0.05000 mol/L",
        "Divide by the original aliquot volume, before adding acid, water or titrant.", "#a14e18")
    ax.text(5, 0.27, "Assumes correct titrant concentration, matched blank, complete selective reaction.",
            ha="center", fontsize=12)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
