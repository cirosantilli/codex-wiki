"""Compare free expansion with the reversible path used to compute entropy.

Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media; writes free-expansion-entropy-reference-path.png to CWD.
Stipulated ideal-gas example, not measurements: n=1 mol, T=300 K,
V1=0.025 m^3, V2=2V1, R=8.314 J/(mol K).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "text.color": "#243445"})
    n, temperature, gas_constant, v1 = 1.0, 300.0, 8.314, 0.025
    v2 = 2 * v1
    volumes = np.linspace(v1, v2, 2001)
    pressures = n * gas_constant * temperature / volumes / 1000  # kPa
    entropy = n * gas_constant * np.log(v2 / v1)
    work = temperature * entropy
    assert abs(np.trapezoid(pressures * 1000, volumes) - work) < 0.00004
    assert np.allclose(pressures[[0, -1]], [99.768, 49.884])
    fig = plt.figure(figsize=(9.4, 5.0), dpi=120)
    fig.suptitle("Same equilibrium endpoints; different heat and work",
                 fontsize=16, y=0.96)
    fig.text(0.5, 0.885, "Toy ideal gas: 1 mol at 300 K; accessible volume doubles",
             ha="center", fontsize=12)
    ax = fig.add_axes([0.09, 0.25, 0.40, 0.54])
    blue = "#216a99"
    ax.fill_between(volumes * 1000, 0, pressures, color="#d7eaf5")
    ax.plot(volumes * 1000, pressures, color=blue, lw=3)
    ax.scatter([v1 * 1000, v2 * 1000], pressures[[0, -1]], color="#243445", zorder=4)
    ax.annotate("Initial", (25, pressures[0]), xytext=(27, 106), fontsize=11)
    ax.annotate("Final", (50, pressures[-1]), xytext=(44, 58), fontsize=11)
    ax.text(37.5, 86, "Hypothetical reversible\nisothermal path", ha="center",
             color=blue, fontsize=12)
    ax.text(37.5, 27, r"$\int p\,dV=nRT\ln 2$" + f"\n= {work:.2f} J",
             ha="center", color=blue, fontsize=13)
    ax.annotate("", xy=(40, n * gas_constant * temperature / 0.04 / 1000),
                xytext=(37, n * gas_constant * temperature / 0.037 / 1000),
                arrowprops={"arrowstyle": "-|>", "color": blue, "lw": 2})
    ax.set(xlim=(23, 52), ylim=(0, 115), xlabel="Gas volume V (L)",
           ylabel="Equilibrium gas pressure p (kPa)")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xticks([25, 30, 35, 40, 45, 50])

    ledger = fig.add_axes([0.55, 0.20, 0.42, 0.59])
    ledger.axis("off")
    ledger.text(0.5, 0.98, "Gas accounting", ha="center", fontsize=14)
    rows = [["Heat in (J)", "0", f"{work:.2f}"],
            ["Work out (J)", "0", f"{work:.2f}"],
            ["ΔU (J)", "0", "0"],
            ["ΔS (J/K)", f"{entropy:.3f}", f"{entropy:.3f}"],
            ["Produced S (J/K)", f"{entropy:.3f}", "0"]]
    table = ledger.table(cellText=rows, colLabels=["", "Actual\nrelease", "Reversible\nreference"],
                         colWidths=[0.46, 0.25, 0.29], cellLoc="center",
                         bbox=[0, 0.23, 1, 0.65])
    table.auto_set_font_size(False)
    table.set_fontsize(10.5)
    for (row, column), cell in table.get_celld().items():
        cell.set_edgecolor("#c6d0d9")
        if row == 0:
            cell.set_facecolor("#eaf1f6")
            cell.set_text_props(weight="bold")
        elif column == 0:
            cell.set_text_props(ha="left")
    ledger.text(0.5, 0.09, "Reference bath loses 5.763 J/K;\nactual isolated gas produces 5.763 J/K.",
                 ha="center", fontsize=11)
    fig.text(0.5, 0.085, "Actual release: no equilibrium p(V) curve during the rush",
             ha="center", fontsize=12, color="#b35925")
    fig.text(0.5, 0.025, "Entropy uses a reversible comparison; the drawn curve is not measured data",
             ha="center", fontsize=10, color="#596673")
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
