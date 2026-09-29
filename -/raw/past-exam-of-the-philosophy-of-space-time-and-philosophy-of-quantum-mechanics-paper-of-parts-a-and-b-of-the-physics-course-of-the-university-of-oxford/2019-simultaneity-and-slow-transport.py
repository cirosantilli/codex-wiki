"""Original diagram; Python 3.14, NumPy and Matplotlib. Save only in caller CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "axes.titlesize": 12, "figure.facecolor": "white", "savefig.facecolor": "white"})
fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.3), layout="constrained")
ax = axes[0]
x = np.linspace(-1.5, 1.5, 200)
for beta, color in [(-0.6, "#bc472b"), (0.0, "#333333"), (0.6, "#126782")]:
    ax.plot(x, beta*x, color=color, lw=2, label=rf"$t'=0$, $v/c={beta:g}$")
ax.plot(x, x, color="#777777", ls="--", lw=1)
ax.plot(x, -x, color="#777777", ls="--", lw=1)
ax.axvline(0, color="#cccccc", lw=1)
ax.scatter([0], [0], c="black", zorder=5)
ax.annotate("P", (0,0), xytext=(6, 7), textcoords="offset points")
ax.text(1.05, 1.35, "light cone", fontsize=10, color="#666666")
ax.set(xlim=(-1.6,1.6), ylim=(-1.6,1.6), xlabel=r"$x/L$", ylabel=r"$ct/L$", title="Simultaneity depends on the frame")
ax.set_aspect("equal")
ax.legend(loc="lower left", fontsize=9, framealpha=1)
ax = axes[1]
beta = np.linspace(0, .85, 301)
lag = beta/(1+np.sqrt(1-beta**2))
ax.plot(beta, lag, lw=2.2, color="#126782", label="exact ideal-clock result")
ax.plot(beta, beta/2, "--", color="#bc472b", lw=1.7, label=r"slow limit $u/(2c)$")
ax.scatter([0],[0], color="#126782", zorder=5)
ax.set(xlabel=r"Transport speed $u/c$", ylabel=r"Clock lag $\delta/(L/c)$", xlim=(0,.85), ylim=(0,.59), title="Slow transport approaches Einstein synchronization")
ax.grid(alpha=.2)
ax.legend(loc="upper left", fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=120, transparent=False)
plt.close(fig)
