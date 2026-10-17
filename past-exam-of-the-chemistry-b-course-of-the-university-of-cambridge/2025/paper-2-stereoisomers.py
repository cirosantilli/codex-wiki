"""Original octahedral donor-position diagrams; Python 3.14, matplotlib.

Writes paper-2-stereoisomers.png into the current working directory.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig, axes = plt.subplots(1, 2, figsize=(9, 4.6), facecolor="white")
# Project orthogonal octahedral axes. Opposite vectors are trans.
v = [(0, 1.1), (0, -1.1), (-1.0, .35), (1., -.35),
     (1., .35), (-1., -.35)]
arrangements = [(["N", "Cl", "P", "Cl", "O", "Cl"], "Reflected facial arrangement"),
                (["N", "Cl", "O", "P", "Cl", "Cl"], "Meridional: O trans to P")]
for ax, (labels, title) in zip(axes, arrangements):
    ax.set(xlim=(-1.6, 1.6), ylim=(-1.7, 1.7), aspect="equal")
    ax.axis("off")
    ax.set_title(title, fontsize=13)
    for i, ((x, y), label) in enumerate(zip(v, labels)):
        if i in [2, 4]:
            ax.plot([0, .85*x], [0, .85*y], color="0.25", lw=2, ls="--")
        elif i in [3, 5]:
            ax.add_patch(Polygon([(0, 0), (.82*x-.06*y, .82*y+.06*x),
                                  (.82*x+.06*y, .82*y-.06*x)], color="0.25"))
        else:
            ax.plot([0, .85*x], [0, .85*y], color="0.25", lw=2)
        ax.text(x, y, label, ha="center", va="center", fontsize=16,
                color="#286b85" if label != "Cl" else "0.25")
    ax.text(0, 0, "Ti", ha="center", va="center", fontsize=16,
            bbox=dict(fc="white", ec="none", pad=2))
    # Connect only donor sites, suppressing the organic ligand backbone.
    for left, right in [("O", "N"), ("N", "P")]:
        a, b = v[labels.index(left)], v[labels.index(right)]
        ax.annotate("", xy=b, xytext=a,
                    arrowprops=dict(arrowstyle="-", color="#80a8b7", lw=2,
                                    connectionstyle="arc3,rad=.35"))
    ax.text(0, -1.5, "Pale lines: O–N–P ligand connectivity", ha="center", fontsize=9)
fig.tight_layout()
fig.savefig("paper-2-stereoisomers.png", dpi=180, facecolor="white")
