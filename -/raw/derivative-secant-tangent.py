"""Visualize a derivative through secants and their limiting slope."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.1), dpi=130, constrained_layout=True)
fig.patch.set_facecolor("white")
x = np.linspace(0, 2.12, 500)
axes[0].plot(x, x*x, color="#204e8a", linewidth=2.6, label=r"$f(x)=x^2$")
axes[0].plot(x, 2*x-1, color="#b02b43", linewidth=2.3, label=r"tangent: slope $2$")
colors = ["#db9419", "#409173", "#9470ae"]
for h, color in zip((1., .5, .1), colors):
    line_x = np.linspace(.65, 1+h+.12, 100)
    axes[0].plot(line_x, 1+(2+h)*(line_x-1), color=color, linestyle="--",
                 label="secant: h = %g, slope = %g" % (h, 2+h))
    axes[0].scatter([1+h], [(1+h)**2], color=color, s=30, zorder=5)
axes[0].scatter([1], [1], color="#b02b43", s=42, zorder=6)
axes[0].set(xlim=(0, 2.15), ylim=(-.15, 4.6), xlabel=r"$x$", ylabel=r"$f(x)$",
            title="Nearby chords approach a tangent")
axes[0].legend(fontsize=9, loc="upper left", framealpha=1)
h = np.geomspace(.001, 1, 300)
axes[1].semilogx(h, 2+h, color="#409173", linewidth=2.8, label=r"quotient $2+h$")
axes[1].axhline(2, color="#b02b43", linestyle="--", linewidth=2.2, label=r"limit $f'(1)=2$")
axes[1].set(xlabel=r"increment $h>0$", ylabel="secant slope", ylim=(1.95, 3.08),
            title="The slopes converge as h approaches 0")
axes[1].annotate("smaller increments", xy=(.0018, 2.25), xytext=(.018, 2.25),
                 arrowprops={"arrowstyle": "->", "color": "#555555"}, ha="center", fontsize=10)
axes[1].legend(loc="upper left", fontsize=10)
for ax in axes:
    ax.set_facecolor("white")
    ax.grid(alpha=.16)
fig.savefig(Path.cwd() / "derivative-secant-tangent.png", facecolor="white", transparent=False)
plt.close(fig)
