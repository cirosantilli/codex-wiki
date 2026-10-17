"""Original integration-region diagram; write PNG to the working directory."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6.5, 4.4), layout="constrained")
x1 = np.linspace(0, 1, 200)
x2 = np.linspace(1, 2, 200)
ax.fill_between(x1, 0, x1, color="#c5e0ef")
ax.fill_between(x2, 0, 1/x2, color="#c5e0ef")
ax.plot(x1, x1, lw=2, color="#247b9d", label=r"$y=x$")
ax.plot(x2, 1/x2, lw=2, color="#bd6c26", label=r"$y=1/x$")
ax.plot([0, 2, 2], [0, 0, .5], color="#444444", lw=1.6)
ax.plot([1, 1], [0, 1], color="#666666", ls="--", lw=1)
ax.scatter([0, 1, 2, 2], [0, 1, .5, 0], color="#444444", s=20, zorder=4)
ax.annotate("(1, 1)", (1, 1), xytext=(7, 6), textcoords="offset points")
ax.annotate("(2, 1/2)", (2, .5), xytext=(6, 6), textcoords="offset points")
ax.text(.62, .24, r"$0\leq y\leq x$", ha="center")
ax.text(1.52, .2, r"$0\leq y\leq 1/x$", ha="center")
ax.set(xlim=(-.08, 2.38), ylim=(-.06, 1.24), xlabel="x", ylabel="y",
       title="Vertical slices change at x = 1", xticks=[0, 1, 2], yticks=[0, .5, 1])
ax.legend(loc="upper left", frameon=False)
ax.grid(alpha=.15)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
