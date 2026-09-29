"""Original qualitative nucleoplasmin assay comparison; no measured counts."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


fig, ax = plt.subplots(figsize=(10, 6.2), dpi=110, facecolor="white")
ax.set(xlim=(0, 10), ylim=(0, 6.2))
ax.axis("off")
blue, purple, orange = "#3975a5", "#70569b", "#cb6a22"
ax.text(5, 5.95, "Separate entry from retention", ha="center", fontsize=18, weight="bold")
panels = [(1.7, "Tail-bearing cargo", False, False),
          (5, "Tailless core", True, False),
          (8.3, "Tailless core", True, True)]
for x, label, core, direct in panels:
    ax.text(x, 5.35, label, ha="center", fontsize=13, weight="bold")
    ax.text(x, 4.98, "Nuclear injection" if direct else "Cytoplasmic injection", ha="center", fontsize=11)
    ax.add_patch(Circle((x, 3.67), 1.02, facecolor="#edf5fa", edgecolor=blue, lw=1.8))
    ax.add_patch(Circle((x+.25, 3.67), .42, facecolor="#f1ecf8", edgecolor=purple, lw=2))
    target = (x+.25, 3.67) if direct else (x-.55, 3.67)
    ax.add_patch(FancyArrowPatch((x-.97, 4.57), target, arrowstyle="->", mutation_scale=15, lw=1.8, color="#343434"))
    ax.add_patch(Circle(target, .13, facecolor=orange, edgecolor="#974516", lw=1.2))
    if not core:
        ax.plot([target[0]-.09, target[0]-.25], [target[1]+.09, target[1]+.25], color=orange, lw=2)
    ax.text(x, 2.32, "Nuclear accumulation" if not core else ("Nuclear retention" if direct else "No nuclear entry"),
            ha="center", fontsize=12, color=purple if not core or direct else blue)
    ax.text(x, 1.94, "Entry + retention" if not core else ("Entry bypassed" if direct else "Entry fails"),
            ha="center", fontsize=11)
ax.text(5, 1.22, "Readout: separated nucleus / cytoplasm → gel → autoradiography", ha="center", fontsize=12)
ax.text(5, .77, "Section autoradiography checks internal localization", ha="center", fontsize=11)
ax.text(5, .28, "Qualitative comparison; shapes and single cargo symbols are schematic", ha="center", fontsize=10, color="#555555")
fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
