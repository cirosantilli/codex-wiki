"""Original triangular-wave plot, with its basic period highlighted."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3*np.pi, 3*np.pi, 1801)
phase = (x+np.pi) % (2*np.pi)-np.pi
f = 1-np.abs(phase)/np.pi
fig, ax = plt.subplots(figsize=(7, 3.8), layout="constrained")
ax.axvspan(-np.pi, np.pi, color="#e7f0f5", label="Basic interval")
ax.plot(x, f, color="#287ca3", lw=2)
ax.scatter([-np.pi, 0, np.pi], [0, 1, 0], color="#a45b2b", zorder=4, s=28)
ax.axhline(0, color="#777777", lw=.8)
ax.set(xlim=(-3*np.pi, 3*np.pi), ylim=(-.08, 1.2), xlabel="x", ylabel="f(x)",
       title=r"Periodic extension of $1-|x|/\pi$",
       xticks=np.arange(-3, 4)*np.pi,
       xticklabels=[r"$-3\pi$",r"$-2\pi$",r"$-\pi$","0",r"$\pi$",r"$2\pi$",r"$3\pi$"],
       yticks=[0, .5, 1])
ax.grid(alpha=.15)
ax.legend(frameon=False, loc="upper right")
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
