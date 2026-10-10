"""Original signed-vector examples of Hölder and the triangle inequality."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
x = np.array([1., 2., -1.])
ys = [np.array([2., -1., 3.]), np.array([1., 4., -1.])]
p, q = 3., 1.5
fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), layout="constrained")
for ax, y, name in zip(axes, ys, ["Cancellation and a strict bound", "Matching powers gives equality"]):
    dot = float(x @ y); absolute = float(np.abs(x*y).sum())
    bound = float(np.sum(np.abs(x)**p)**(1/p)*np.sum(np.abs(y)**q)**(1/q))
    values = [abs(dot), absolute, bound]
    ax.bar([0, 1, 2], values, color=["#2563eb", "#059669", "#d97706"], width=.62)
    for j, v in enumerate(values): ax.text(j, v+.2, f"{v:.3f}", ha="center")
    ax.set(ylim=(0, 15.0), xticks=[0, 1, 2], xticklabels=[r"$|\sum x_i y_i|$", r"$\sum |x_i y_i|$", r"$\|x\|_3\|y\|_{3/2}$"], ylabel="Value", title=name)
    ax.text(.5, .95, "x = (1, 2, −1)\ny = ("+", ".join(f"{v:g}" for v in y)+")", transform=ax.transAxes, ha="center", va="top")
    ax.text(.5, .79, "Products: ("+", ".join(f"{v:g}" for v in x*y)+")", transform=ax.transAxes, ha="center", va="top", fontsize=10)
    ax.grid(axis="y", alpha=.2); ax.set_axisbelow(True); ax.spines[["top", "right"]].set_visible(False)
fig.suptitle(r"Two distinct gaps: cancellation, then Hölder's inequality ($p=3$, $q=3/2$)", fontsize=14)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
