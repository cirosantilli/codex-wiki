"""Original exact additive-volume bias comparison; no experimental data.

Run from _media using Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Writes basename.png in the current directory. All parameters are selected.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    ink, blue, orange = "#20364b", "#155e9b", "#b75520"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    fig = plt.figure(figsize=(10, 5.5), dpi=120, facecolor="white")
    fig.suptitle("Extra titre volume lowers the standardized concentration",
                 y=0.975, fontsize=16, weight="bold", color=ink)
    fig.text(0.5, 0.90, "Original additive-error model • selected inputs • not measured data",
             ha="center", fontsize=10.5, color=ink)

    ax = fig.add_axes([0.075, 0.23, 0.36, 0.56])
    delta = np.linspace(0, 0.2, 401)
    for reference, color in [(24.8, blue), (5.0, orange)]:
        bias = -100 * delta / (reference + delta)
        ax.plot(delta, bias, color=color, lw=2.4,
                label=f"Reference titre {reference:.2f} mL")
        point = -100 * 0.05 / (reference + 0.05)
        ax.plot(0.05, point, "o", color=color)
        ax.annotate(f"{point:.4f}%", xy=(0.05, point),
                    xytext=(0.077, point + (0.28 if reference > 5 else -0.48)),
                    color=color, fontsize=10,
                    arrowprops={"arrowstyle": "-", "color": color})
    ax.axhline(0, color="#8393a2", lw=0.8)
    ax.axvline(0.05, color="#8393a2", ls="--", lw=0.9)
    ax.set(xlim=(0, 0.2), ylim=(-4.1, 0.25),
           xlabel=r"Extra denominator volume $\delta V$ (mL)",
           ylabel="Relative concentration error (%)")
    ax.set_xticks(np.arange(0, 0.201, 0.05))
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="lower left", fontsize=9, frameon=False)
    ax.set_title("A small titre magnifies a fixed volume error", fontsize=11, pad=14)

    table_ax = fig.add_axes([0.48, 0.23, 0.50, 0.56])
    table_ax.axis("off")
    table_ax.set_title("Same 0.002500 mol inventory in every row", fontsize=11, pad=14)
    amount_mol, reference_ml = 0.0025, 24.8
    labels = ["Corrected reference", "+0.05 mL overshoot",
              "0.05 mL blank left in", "Both errors"]
    extras = [0.0, 0.05, 0.05, 0.10]
    rows = []
    for label, extra in zip(labels, extras):
        denominator = reference_ml + extra
        concentration = amount_mol / (denominator / 1000)
        error = -100 * extra / denominator
        rows.append([label, f"{denominator:.2f}", f"{concentration:.8f}",
                     "0" if extra == 0 else f"{error:.4f}"])
    table = table_ax.table(cellText=rows,
                          colLabels=["Case", "V (mL)", "c (mol/L)", "Error (%)"],
                          colWidths=[0.40, 0.16, 0.25, 0.19],
                          cellLoc="center", bbox=[0, 0.16, 1, 0.80])
    table.auto_set_font_size(False)
    table.set_fontsize(8.7)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#d4dfe8")
        cell.set_linewidth(0.6)
        cell.set_text_props(color=ink)
        if row == 0:
            cell.set_facecolor("#e6f0f7")
            cell.set_text_props(weight="bold")
        elif row in (2, 3):
            cell.set_facecolor("#fff4e9")
        else:
            cell.set_facecolor("white")
    table_ax.text(0.5, 0.02, "Equal extra denominators give equal bias.",
                  ha="center", fontsize=10, color=orange, weight="bold")
    fig.text(0.5, 0.115,
             r"$\widehat{c}=n_s/(V+\delta V)$"
             r"     $\Longrightarrow$     $(\widehat{c}-c)/c=-\delta V/(V+\delta V)$",
             ha="center", fontsize=15, color=blue)
    fig.text(0.5, 0.04,
             "Overshoot and unremoved blank are separate causes; their volume offsets add in this model.",
             ha="center", fontsize=9.5, color=ink)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
