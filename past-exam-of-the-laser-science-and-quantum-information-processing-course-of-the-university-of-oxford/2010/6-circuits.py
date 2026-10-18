"""Draw the four linear oracles and their exact Hadamard conjugates.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write 6-circuits.png in the current working directory, independently of script path.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "mathtext.fontset": "dejavusans", "savefig.facecolor": "white"})
fig, axes = plt.subplots(4, 2, figsize=(9, 6.1), dpi=140, facecolor="white")
fig.subplots_adjust(left=.08, right=.98, top=.87, bottom=.09, hspace=.28, wspace=.34)
fig.suptitle("Four linear oracles: reversing the CNOT controls", fontsize=16, y=.975)
fig.text(.29, .91, r"Oracle $U_a$", ha="center", fontsize=13)
fig.text(.75, .91, r"Full circuit $WU_aW$,  $W=H^{\otimes 3}$", ha="center", fontsize=13)


def cnot(ax, xpos, control, target):
    ax.plot([xpos, xpos], [control, target], color="#172a3a", lw=1.5, zorder=2)
    ax.add_patch(Circle((xpos, control), .065, color="#172a3a", zorder=4))
    ax.add_patch(Circle((xpos, target), .15, facecolor="white",
                        edgecolor="#172a3a", lw=1.5, zorder=3))
    ax.plot([xpos-.15, xpos+.15], [target, target], color="#172a3a", lw=1.3, zorder=4)
    ax.plot([xpos, xpos], [target-.15, target+.15], color="#172a3a", lw=1.3, zorder=4)


for row, bits in enumerate(((0, 0), (0, 1), (1, 0), (1, 1))):
    for col in range(2):
        ax = axes[row, col]
        ax.set(xlim=(-.75, 3.6), ylim=(-.3, 2.35), aspect="equal")
        ax.axis("off")
        for y, label in ((2, r"$x_1$"), (1, r"$x_2$"), (0, r"$y$")):
            ax.plot([0, 3.5], [y, y], color="#657582", lw=1.1)
            ax.text(-.2, y, label, va="center", ha="right")
        ax.text(-.65, 2.4, f"a = {bits[0]}{bits[1]}", weight="bold", fontsize=10)
        for j, bit in enumerate(bits):
            if bit:
                data_y = 2-j
                cnot(ax, 1.15+1.2*j, data_y if col == 0 else 0,
                     0 if col == 0 else data_y)
        if not any(bits):
            ax.text(1.7, 1.52, r"$I$", color="#546674", fontsize=12, ha="center")
fig.text(.5, .025, "Wire order: x₁, x₂, y.  The diagrams are operator identities for arbitrary inputs.",
         ha="center", fontsize=10, color="#394e5c")
fig.savefig(Path.cwd() / "6-circuits.png", dpi=140, facecolor="white", transparent=False,
            metadata={"Software": "codex-wiki figure generator"})
plt.close(fig)
