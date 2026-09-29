"""Generate the signed-intersection model. Python 3.14; NumPy and Matplotlib."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 800)
fig, ax = plt.subplots(figsize=(10, 3.6), dpi=100, facecolor="white")
ax.set_facecolor("white")
ax.plot(x, 2*x**3-x, color="#225e96", lw=2.5, label=r"$\Gamma:\ y=2x^3-x$")
ax.axhline(0, color="#555555", lw=1.4, label=r"$N:\ y=0$")
roots = [-1/np.sqrt(2), 0, 1/np.sqrt(2)]
for r, sign, color in zip(roots, ["+1", "-1", "+1"], ["#21744b", "#a32828", "#21744b"]):
    ax.scatter([r], [0], s=55, color=color, zorder=4)
    ax.annotate(sign, (r, 0), xytext=(0, 18 if sign == "+1" else -30),
                textcoords="offset points", ha="center", color=color, fontsize=13, weight="bold")
ax.set(xlim=(-1.04, 1.04), ylim=(-1.1, 1.1), xlabel=r"$x$", ylabel=r"$y$")
ax.set_title("Signed graph intersections: +1 -1 +1 = 1", fontsize=14)
ax.legend(loc="upper left", framealpha=1)
ax.grid(alpha=.18)
fig.subplots_adjust(left=.08, right=.98, top=.86, bottom=.18)
fig.savefig(Path.cwd() / "paper-15-signed-intersections.png", facecolor="white", transparent=False)
plt.close(fig)
