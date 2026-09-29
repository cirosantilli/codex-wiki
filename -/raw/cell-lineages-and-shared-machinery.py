"""Cellular comparison, not a phylogenetic tree; output basename.png in cwd.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Entries concern representative cells, not universal per-cell requirements.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    headings = ["Component / function", "Bacteria", "Archaea", "Eukaryotes"]
    rows = [
        ["Cell membrane\nSelective boundary", "Present", "Present", "Present"],
        ["DNA genome\nInherited information", "Present", "Present", "Present"],
        ["Ribosomes\nProtein synthesis", "Present", "Present", "Present"],
        ["Metabolism\nMatter and energy conversions", "Present", "Present", "Present"],
        ["DNA compartment\nWhere chromosomes reside", "Nucleoid;\nno nuclear envelope", "Nucleoid;\nno nuclear envelope", "Nucleus with\nnuclear envelope¹"],
        ["Chromosome form\nTypical organization", "Often circular;\nexceptions occur", "Often circular;\nexceptions occur", "Nuclear chromosomes\ntypically linear"],
        ["Cell wall\nDistinct from cell membrane", "Peptidoglycan\nin most", "No peptidoglycan;\nwalls vary", "Typical plants / fungi: yes\nAnimals: no"],
        ["Energy-converting membranes\nRepresentative locations", "Cell membrane;\nother membranes in some", "Cell membrane", "Mitochondria;\nchloroplasts in some²"],
        ["Examples", "E. coli;\ncyanobacteria", "Methane-producing\narchaea; many others", "Yeasts; plants; animals"],
    ]
    assert all(len(row) == len(headings) for row in rows)
    shared = np.array([[entry == "Present" for entry in row[1:]] for row in rows[:4]])
    assert shared.shape == (4, 3) and shared.all()

    fig, ax = plt.subplots(figsize=(10.8, 7.0))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.axis("off")
    fig.subplots_adjust(left=.025, right=.975, top=.85, bottom=.17)
    table = ax.table(cellText=rows, colLabels=headings, cellLoc="center",
                     colWidths=[.28, .24, .23, .25], bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#d3dbe0")
        cell.set_linewidth(.8)
        cell.PAD = .065
        cell.get_text().set_color("#29333c")
        if row == 0:
            cell.set_facecolor("#205b78")
            cell.get_text().set_color("white")
            cell.get_text().set_weight("bold")
        elif row <= 4:
            cell.set_facecolor("#eef6f1")
        else:
            cell.set_facecolor("#f2f5f8" if row % 2 else "white")
        if col == 0:
            cell.get_text().set_ha("left")
            if row > 0:
                cell.get_text().set_weight("medium")

    fig.suptitle("Shared machinery, distinguishing organization", fontsize=16, y=.975)
    fig.text(.5, .915, "Green rows: shared functions, with lineage-specific molecular machinery",
             ha="center", fontsize=11, color="#367759")
    fig.text(.04, .125, "¹ Eukaryotic lineage characteristic; some specialized cells lose the nucleus.", fontsize=10)
    fig.text(.04, .091, "² Typical cells: mitochondrial reduction / loss occurs; chloroplasts are not in every eukaryote.", fontsize=10)
    fig.text(.5, .035, "Comparison only: column order implies neither ancestry nor evolutionary rank. Not a phylogenetic tree.",
             ha="center", fontsize=10, color="#4d5661")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1296 × 840 pixels")


if __name__ == "__main__":
    main()
