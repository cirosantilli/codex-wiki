"""Original edge-identification diagrams; output the matching PNG to the CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({"font.size": 13, "figure.facecolor": "white"})
fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), layout="constrained")
teal, orange, blue = "#087e8b", "#c45b12", "#2855a6"
for ax, twisted in zip(axes, [False, True]):
    ax.set(xlim=(-.24, 1.24), ylim=(-1.9, 2.2), aspect="auto")
    ax.axis("off")
    ax.add_patch(Rectangle((0, -1), 1, 2, facecolor="#f3f6fa", edgecolor="#667788"))
    ax.plot([0, 1], [1, 1], color=teal, linewidth=5)
    ax.plot([0, 1], [-1, -1], color=teal if twisted else orange, linewidth=5)
    ax.plot([0, 1], [0, 0], color="#555555", linestyle=":", linewidth=1.7)
    for x, direction in [(0, 1), (1, -1 if twisted else 1)]:
        ax.annotate("", xy=(x, direction * .62), xytext=(x, -direction * .62),
                    arrowprops={"arrowstyle": "-|>", "lw": 3, "color": blue})
    ax.annotate("", xy=(.66, -.25), xytext=(.36, -.25),
                arrowprops={"arrowstyle": "-|>", "lw": 2, "color": "#333333"})
    ax.annotate("", xy=(.36, .36), xytext=(.36, -.25),
                arrowprops={"arrowstyle": "-|>", "lw": 2, "color": "#333333"})
    ax.text(.68, -.28, r"$e_u$", va="center")
    ax.text(.35, .42, r"$e_v$", ha="center")
    ax.text(0, -1.17, r"$u=0$", ha="center")
    ax.text(1, -1.17, r"$u=1$", ha="center")
    ax.text(.5, 1.72, "Möbius band" if twisted else "Cylinder", ha="center",
            fontsize=18, weight="bold")
    ax.text(.5, 1.35, r"$(0,v)\sim(1,-v)$" if twisted else r"$(0,v)\sim(1,v)$",
            ha="center", fontsize=16)
    ax.text(.5, -1.53, r"Seam: $e_v\mapsto-e_v$, determinant $-1$" if twisted
            else r"Seam: $e_v\mapsto e_v$, determinant $+1$", ha="center", fontsize=12)
    ax.text(.5, -1.85, "One boundary circle; handedness reverses" if twisted
            else "Two boundary circles; handedness agrees", ha="center", fontsize=12)
fig.suptitle("The same local rectangle, two different global gluings", fontsize=17)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
