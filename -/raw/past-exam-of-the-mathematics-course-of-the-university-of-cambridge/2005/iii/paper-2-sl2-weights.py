"""Plot the sl2 exterior-square weights; output PNG to caller CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 11})
fig, axes = plt.subplots(3, 1, figsize=(9.5, 4.6), sharex=True)
fig.set_facecolor("white")
weights = [6, 4, 2, 0, -2, -4, -6]
data = [
    ("U (dimension 10)", weights, [1, 1, 2, 2, 2, 1, 1],
     [r"$w_{01}$", r"$w_{02}$", r"$w_{03},w_{12}$",
      r"$w_{04},w_{13}$", r"$w_{14},w_{23}$", r"$w_{24}$", r"$w_{34}$"]),
    ("L(6) (dimension 7)", weights, [1]*7, [rf"$v_{j}$" for j in range(7)]),
    ("L(2) (dimension 3)", [2, 0, -2], [1]*3, [rf"$t_{j}$" for j in range(3)]),
]
for ax, (title, ww, mm, labels) in zip(axes, data):
    ax.axhline(0, color="#bdc5cc", lw=1)
    colors = ["#ae3f35" if w == max(ww) else "#286e98" for w in ww]
    ax.scatter(ww, np.zeros(len(ww)), s=[55*m for m in mm], color=colors, zorder=3)
    for w, m, label in zip(ww, mm, labels):
        ax.text(w, 0.27, str(m), ha="center", fontsize=11)
        ax.text(w, -0.36, label, ha="center", fontsize=11)
    ax.text(-7.1, 0.43, title, fontsize=11)
    ax.set(ylim=(-0.65, 0.8), xlim=(-7.2, 7.2), yticks=[])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="x", length=0)
axes[-1].set_xticks(range(-6, 7, 2))
axes[-1].set_xlabel("Weight (number above a point is its multiplicity)")
fig.tight_layout(h_pad=0.65)
fig.savefig(Path.cwd()/"paper-2-sl2-weights.png", dpi=130,
            facecolor="white", transparent=False)
plt.close(fig)
