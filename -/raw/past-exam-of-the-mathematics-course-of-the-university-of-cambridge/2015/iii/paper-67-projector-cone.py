"""Projector cone; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The only figure output is its PNG basename in the current working directory.
The caller controls MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

n, x, layers = 19, 9, 6
fig, ax = plt.subplots(figsize=(11, 4.6), dpi=100, facecolor="white")
for j in range(n):
    ax.plot([j, j], [-.45, layers+.4], color="#dddddd", linewidth=.8, zorder=0)
support = {x}
ax.scatter([x], [0], s=100, color="#b2182b", zorder=3)
ax.text(x+.25, -.12, r"$A_x$", color="#b2182b", fontsize=11)
for step in range(1, layers+1):
    # Rightmost P_even goes first: pairs (2,3), (4,5), ... in one-based labels.
    first = 1 if step % 2 else 0
    bonds = [(i, i+1) for i in range(first, n-1, 2)]
    retained = [(a,b) for a,b in bonds if a in support or b in support]
    for a,b in bonds:
        keep = (a,b) in retained
        ax.add_patch(Rectangle((a-.10, step-.12), 1.20, .24,
                     facecolor="#b2182b" if keep else "#ededed",
                     edgecolor="#b2182b" if keep else "#bbbbbb", linewidth=1))
    support |= {j for pair in retained for j in pair}
    ax.plot([min(support), max(support)], [step+.23]*2, color="#b2182b", alpha=.6, linewidth=2)
    label = r"$P_{\mathrm{even}}$" if step % 2 else r"$P_{\mathrm{odd}}$"
    ax.text(n-.15, step-.04, label, va="center", fontsize=10)
ax.axvline(x-6, color="#2166ac", linestyle=":", linewidth=1)
ax.axvline(x+6, color="#2166ac", linestyle=":", linewidth=1)
ax.text(x, layers+.62, r"$K^3$: six layers, support within distance six", ha="center", fontsize=12)
ax.set_xticks(range(n))
ax.set_xticklabels([str(j-x) for j in range(n)])
ax.set(xlabel=r"Site relative to $x$", xlim=(-.5,n+1.0), ylim=(-.5,layers+.9))
ax.set_yticks(range(layers+1))
ax.set_yticklabels(["Insertion"]+[str(i) for i in range(1,layers+1)])
ax.set_ylabel("Layer applied, from right to left")
ax.text(.01,.02,"Red: retained projectors    Gray: removed against the ground state", transform=ax.transAxes, fontsize=9, bbox=dict(facecolor="white", edgecolor="none"))
for spine in ["top","right"]:ax.spines[spine].set_visible(False)
fig.tight_layout(pad=1.1)
fig.savefig(Path.cwd() / "paper-67-projector-cone.png", dpi=100, facecolor="white", transparent=False)
plt.close(fig)
