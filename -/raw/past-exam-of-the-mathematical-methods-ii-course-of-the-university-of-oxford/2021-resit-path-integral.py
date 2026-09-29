"""Draw an original integration path; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 13, "figure.facecolor": "white"})
fig, ax = plt.subplots(figsize=(6, 4), dpi=120, facecolor="white")
ax.plot([0, 2], [0, 0], color="#206895", linewidth=3)
ax.plot([2, 2], [0, 1], color="#c16921", linewidth=3)
ax.annotate("", (1.25, 0), (0.7, 0), arrowprops={"arrowstyle": "->", "lw": 2.4, "color": "#206895"})
ax.annotate("", (2, 0.72), (2, 0.3), arrowprops={"arrowstyle": "->", "lw": 2.4, "color": "#c16921"})
ax.scatter([0, 2, 2], [0, 0, 1], color="#222222", zorder=4)
for xy, label, offset in [((0, 0), "start (0, 0)", (5, 12)),
                          ((2, 0), "(2, 0)", (-55, -25)),
                          ((2, 1), "end (2, 1)", (-100, 10))]:
    ax.annotate(label, xy, xytext=offset, textcoords="offset points")
ax.text(0.8, 0.14, r"$y=0:\ I_1=64$", color="#206895")
ax.text(1.2, 0.55, r"$x=2:$" + "\n" + r"$I_2=-4$", color="#a45313")
ax.set(xlabel="$x$", ylabel="$y$", xlim=(-0.3, 2.5), ylim=(-0.35, 1.35),
       title="Oriented path for the line integral", xticks=[0, 1, 2], yticks=[0, 0.5, 1])
ax.grid(alpha=0.15)
ax.set_aspect("equal")
fig.tight_layout()
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            facecolor="white", transparent=False)
plt.close(fig)
