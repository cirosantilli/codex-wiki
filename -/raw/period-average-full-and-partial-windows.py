"""Original full-period and half-period window averages; matching PNG to CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
fig, (left, right) = plt.subplots(1, 2, figsize=(10.6, 4.8), layout="constrained")
t = np.linspace(-.2, 3., 1601)
g = 2 + np.sin(2*np.pi*t) + .5*np.cos(4*np.pi*t)
left.plot(t, g, color="#2855a6", lw=2.2)
for start, colour in [(.2, "#087e8b"), (1.6, "#c45b12")]:
    mask = (t >= start) & (t <= start+1)
    left.fill_between(t, 0, g, where=mask, color=colour, alpha=.16)
    left.axvline(start, color=colour, ls=":", lw=1)
    left.axvline(start+1, color=colour, ls=":", lw=1)
    left.text(start+.5, .14, "Integral = 2\nLength = 1", ha="center", va="bottom", fontsize=11, color=colour,
              bbox={"facecolor": "white", "edgecolor": "none", "alpha": .85, "pad": 3})
left.axhline(2, color="#777777", lw=1, ls="--")
left.set(xlim=(-.2, 3.), ylim=(0, 3.4), xlabel=r"$t$", ylabel=r"$g(t)$",
         title="Same total over different full cycles")
a = np.linspace(-.1, 1.6, 801)
right.plot(a, np.full_like(a, 2.), color="#c45b12", lw=2.5, label="Window length 1: mean 2")
right.plot(a, 2 + 2/np.pi*np.cos(2*np.pi*a), color="#087e8b", lw=2.3,
           label="Window length 1/2: varying mean")
right.set(xlim=(-.1, 1.6), ylim=(1.1, 3.), xlabel=r"Window start $a$", ylabel="Window average",
          title="A partial cycle depends on the start")
right.legend(loc="upper right", fontsize=10, frameon=False)
for ax in (left, right):
    ax.grid(alpha=.15)
fig.suptitle(r"Analytical example: $g(t)=2+\sin(2\pi t)+\frac{1}{2}\cos(4\pi t)$", fontsize=16)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
