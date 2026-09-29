"""Original ideal first-turn carbon-13 ledger; Python 3.14, matplotlib 3.10.7.

Run from _media. No experimental values: choose 10 micromol acetyl groups,
six micromol doubly labelled, plus 10 micromol unlabelled oxaloacetate.
The first-turn atom mapping retains both entering acetyl carbons.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np


def main():
    total = np.array([20, 60, 20, 40])
    labelled = np.array([12, 12, 0, 12])
    ordinary = total - labelled
    assert total[1] == total[2] + total[3]
    assert labelled[1] == labelled[2] + labelled[3]
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10, 6.6), facecolor="white")
    fig.subplots_adjust(left=0.12, right=0.97, bottom=0.22, top=0.78)
    x = np.array([0, 1.6, 3.8, 5.4])
    ax.bar(x, ordinary, width=0.8, color="#d9e2e8", edgecolor="#71808c")
    ax.bar(x, labelled, bottom=ordinary, width=0.8, color="#d78b28", edgecolor="#98621c")
    for xi, n, lab in zip(x, total, labelled):
        ax.text(xi, n + 1.5, f"{lab}/{n} labelled\n{100*lab/n:.0f}% of C atoms", ha="center", fontsize=12)
        if lab:
            ax.text(xi, n - lab / 2, str(lab), ha="center", va="center", weight="bold")
        ax.text(xi, (n - lab) / 2, str(n - lab), ha="center", va="center")
    ax.set_xticks(x, ["Acetyl input\n10 μmol groups", "Citrate stage\n10 μmol molecules",
                     "Released CO₂\n20 μmol molecules", "Regenerated\noxaloacetate\n10 μmol molecules"])
    ax.set(ylabel="Carbon atoms (μmol)", ylim=(0, 76), xlim=(-0.7, 6.1))
    ax.axvline(2.7, color="#7f8a92", ls="--", lw=1)
    ax.text(4.6, 73, "Together: first-turn outputs", ha="center", fontsize=12)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=0.18)
    fig.suptitle("First-turn label ledger: the acceptor changes its atoms", fontsize=18, y=0.97)
    fig.legend(handles=[Patch(facecolor="#d9e2e8", label="Unlabelled carbon"),
                        Patch(facecolor="#d78b28", label="Carbon-13 label")],
               loc="upper center", bbox_to_anchor=(0.5, 0.91), ncol=2, frameon=False)
    fig.text(0.5, 0.075, "Chosen ideal inputs: 6 μmol doubly labelled + 4 μmol unlabelled acetyl groups; 10 μmol unlabelled oxaloacetate.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.033, "One traversal each • no exchange or side pathways • natural isotope abundance omitted • not measured data",
             ha="center", fontsize=10, color="#4d5960")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
