"""Original phase/coefficient sketches of three hydrogen SALCs, overlap neglected."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

angles = np.deg2rad([90, 210, 330])
xy = np.column_stack((np.cos(angles), np.sin(angles)))
coefficients = [np.ones(3)/np.sqrt(3), np.array([2, -1, -1])/np.sqrt(6),
                np.array([0, 1, -1])/np.sqrt(2)]
labels = [[r"$+1/\sqrt{3}$"]*3, [r"$+2/\sqrt{6}$", r"$-1/\sqrt{6}$", r"$-1/\sqrt{6}$"],
          ["0", r"$+1/\sqrt{2}$", r"$-1/\sqrt{2}$"]]
fig, axs = plt.subplots(1, 3, figsize=(10, 3.8), dpi=150)
for ax, values, texts, title in zip(axs, coefficients, labels, (r"$A_1$", r"$E$: first component", r"$E$: second component")):
    ax.plot(np.r_[xy[:, 0], xy[0, 0]], np.r_[xy[:, 1], xy[0, 1]], "--", color="#b0b5bc", lw=1)
    for p, coefficient, text, name in zip(xy, values, texts, "ABC"):
        color = "#2675a5" if coefficient>0 else "#c45a43" if coefficient<0 else "white"
        ax.scatter(*p, s=1250*abs(coefficient)+55, c=color, edgecolors="#3a434d", zorder=3)
        ax.text(*(p+np.array([0, .27])), f"H{name}: {text}", ha="center", fontsize=11)
    ax.set(title=title, xlim=(-1.45, 1.45), ylim=(-1.05, 1.65), aspect="equal")
    ax.axis("off")
fig.suptitle("Hydrogen symmetry orbitals in ammonia", fontsize=15)
fig.text(.5, .035, "Blue/red show opposite phases; areas indicate coefficient magnitude. Dashed triangle is a guide.", ha="center", fontsize=10)
fig.tight_layout(rect=(0, .07, 1, .93))
fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
