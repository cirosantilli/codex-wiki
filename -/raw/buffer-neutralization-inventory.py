"""Show dominant neutralization inventories; write basename.png in cwd.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Toy pKa = 5, initial volume 1 L, negligible added volume. Stoichiometric
inventories neglect tiny free-ion amounts and equilibration corrections;
pH also neglects activity coefficients. This is not exact speciation.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    before = np.array([0.10, 0.10])
    hydroxide = 0.01
    after = before + hydroxide * np.array([-1, 1])
    ph = 5.0 + np.log10(after[1] / after[0])
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.8), sharey=True)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.085, right=0.97, bottom=0.24, top=0.72, wspace=0.18)
    for ax, amounts, title in zip(axes, (before, after),
                                 ("Before addition: pH ≈ 5.00000", f"After neutralization: pH ≈ {ph:.5f}")):
        bars = ax.bar([0, 1], amounts, width=0.58, color=["#b6531f", "#236d99"])
        ax.bar_label(bars, labels=[f"{v:.2f} mol" for v in amounts], padding=6, fontsize=12,
                     bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
        ax.set_xticks([0, 1], labels=[r"Weak acid $HA$", r"Conjugate base $A^-$"], fontsize=11)
        ax.set_ylim(0, 0.14)
        ax.set_yticks([0, 0.05, 0.10])
        ax.set_title(title, fontsize=12, pad=13)
        ax.axhline(0.10, color="#777777", ls="--", lw=1, zorder=0)
        ax.grid(axis="y", alpha=0.2)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Approximate partner inventory (mol)", fontsize=11)
    fig.suptitle(r"Toy buffer: $HA+OH^-\longrightarrow A^-+H_2O$", fontsize=15, y=0.97)
    fig.text(0.5, 0.85, "Add 0.010 mol OH⁻ to 1 L; stipulated pKa = 5; negligible added volume", ha="center", fontsize=11)
    fig.text(0.5, 0.12, "0.010 mol transfers from acid to base; total partner inventory stays 0.20 mol.", ha="center", fontsize=11)
    fig.text(0.5, 0.065, "Dominant stoichiometry + ideal concentration approximation; not exact speciation.", ha="center", fontsize=10, color="#444444")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}; final inventories {after.tolist()}; calculated pH {ph:.12f}")


if __name__ == "__main__":
    main()
