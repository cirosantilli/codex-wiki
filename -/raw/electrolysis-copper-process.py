"""Original copper-transfer schematic; writes its PNG basename to CWD.

Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, ax = plt.subplots(figsize=(10, 6.4), dpi=120, facecolor="white")
ax.set(xlim=(0, 10), ylim=(0, 6.4))
ax.axis("off")
ink, blue, copper = "#243544", "#237b9b", "#bb7447"

def text(x, y, s, **kwargs):
    ax.text(x, y, s, ha="center", va="center", color=ink, **kwargs)

def arrow(start, end, color=blue):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=16, lw=2, color=color))

text(5, 6.12, "Copper electrolysis: reaction identities fix electrode names", fontsize=15, weight="bold")
text(5, 5.82, "MODEL SCHEMATIC • arrows show transport roles, not measured paths", fontsize=10)
ax.add_patch(Rectangle((3.6, 4.85), 2.8, .62, fc="#f1f4f7", ec=ink, lw=1.5))
text(5, 5.16, "Regulated DC source")
text(3.83, 4.98, "+", weight="bold")
text(6.16, 4.98, "−", weight="bold")
ax.plot([2.45, 2.45, 3.6], [3.7, 5.16, 5.16], color=ink, lw=1.8)
ax.plot([6.4, 7.55, 7.55], [5.16, 5.16, 3.7], color=ink, lw=1.8)
arrow((2.12, 4.06), (2.12, 4.93))
text(1.3, 4.56, "Electrons\nto source", fontsize=10)
arrow((7.9, 4.93), (7.9, 4.06))
text(8.76, 4.56, "Electrons\nfrom source", fontsize=10)
ax.add_patch(Rectangle((1.55, 1.88), 6.9, 1.77, fc="#e8f4fa", ec="none"))
ax.plot([1.55, 1.55, 8.45, 8.45], [3.85, 1.88, 1.88, 3.85], color=ink, lw=1.8)
for x in (2.22, 7.32):
    ax.add_patch(Rectangle((x, 2.1), .46, 1.65, fc=copper, ec=ink, lw=1.3))
text(3.55, 3.31, "Positive anode\nOXIDATION", fontsize=11, weight="bold")
text(6.4, 3.31, "Negative cathode\nREDUCTION", fontsize=11, weight="bold")
text(5, 2.76, r"Aqueous $\mathrm{CuSO_4}$ electrolyte", fontsize=12)
arrow((3.35, 2.35), (6.65, 2.35))
text(5, 2.11, "Net conventional current carried by ions", fontsize=10)
text(2.6, 1.51, r"$\mathrm{Cu}\ \longrightarrow\ \mathrm{Cu}^{2+}+2e^-$", fontsize=14)
text(7.38, 1.51, r"$\mathrm{Cu}^{2+}+2e^-\ \longrightarrow\ \mathrm{Cu}$", fontsize=14)
text(2.6, 1.13, "Dry mass decreases", weight="bold")
text(7.38, 1.13, "Dry mass increases", weight="bold")
ax.add_patch(Rectangle((1.05, .15), 7.9, .63, fc="#f5f7f9", ec="#c8d1da"))
text(5, .49, r"Readouts: $Q=\int I(t)\,dt$ and before/after dry masses", fontsize=12)
fig.subplots_adjust(left=.015, right=.985, bottom=.015, top=.985)
fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
plt.close(fig)
