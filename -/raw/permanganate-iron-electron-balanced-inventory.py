"""Draw the exact acidic permanganate/iron inventory; run from _media.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5. No measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white"})
    fig = plt.figure(figsize=(9.6, 6.4), dpi=120)
    ax = fig.add_axes([0.045, 0.46, 0.91, 0.43])
    ax.set(xlim=(0, 10), ylim=(0, 4))
    ax.axis("off")
    fig.suptitle("One permanganate needs five iron(II) ions", fontsize=19, y=0.965)
    ax.text(5, 3.55, r"$5\mathrm{Fe}^{2+}\;\longrightarrow\;5\mathrm{Fe}^{3+}+5e^-$",
            ha="center", fontsize=18, color="#a44a15")
    for i in range(5):
        x = 3.4 + i * 0.8
        ax.add_patch(Circle((x, 2.63), 0.24, facecolor="white", edgecolor="#a44a15", lw=1.6))
        ax.text(x, 2.63, "e⁻", ha="center", va="center", fontsize=14)
        ax.add_patch(FancyArrowPatch((x, 2.30), (x, 1.59), arrowstyle="-|>",
                                   mutation_scale=14, color="#095c80", lw=1.7))
        ax.add_patch(Circle((x, 1.22), 0.24, facecolor="white", edgecolor="#095c80", lw=1.6))
        ax.text(x, 1.22, "e⁻", ha="center", va="center", fontsize=14)
    ax.text(0.2, 2.63, "5 produced", va="center", fontsize=12, color="#a44a15")
    ax.text(0.2, 1.22, "5 consumed", va="center", fontsize=12, color="#095c80")
    ax.text(8.0, 1.93, "Match and cancel\nformal electron slots", va="center", fontsize=11)
    ax.text(5, 0.35,
            r"$\mathrm{MnO}_4^-+8\mathrm{H}^++5e^-\;\longrightarrow\;\mathrm{Mn}^{2+}+4\mathrm{H}_2\mathrm{O}$",
            ha="center", fontsize=18, color="#095c80")

    table_ax = fig.add_axes([0.09, 0.14, 0.82, 0.27])
    table_ax.axis("off")
    table_ax.set_title("Net reaction: atom counts and charge agree", fontsize=14, pad=9)
    inventory = [1, 4, 8, 5, "+17"]
    table = table_ax.table(cellText=[inventory, inventory], rowLabels=["Reactants", "Products"],
                          colLabels=["Mn", "O", "H", "Fe", "Charge / e"],
                          cellLoc="center", rowLoc="center", loc="center", bbox=[0.13, 0, 0.87, 0.9])
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#b7c3cc")
        cell.set_facecolor("white" if row else "#edf4f8")
    fig.text(0.5, 0.055, "Exact bookkeeping, not a free-electron path or an elementary reaction.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.025, "Counterions are omitted from the written net reaction; bulk solution remains neutral.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
