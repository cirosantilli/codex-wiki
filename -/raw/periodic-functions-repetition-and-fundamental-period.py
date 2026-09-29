"""Original analytical examples of repetition; write matching PNG to CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
t = np.linspace(-.5, 2.5, 1501)
fig, axes = plt.subplots(3, 1, figsize=(10.6, 7.4), sharex=True, layout="constrained")
examples = [
    (2 + np.sin(2*np.pi*t) + .5*np.cos(4*np.pi*t), 1.,
     r"$g(t)=2+\sin(2\pi t)+\frac{1}{2}\cos(4\pi t)$", (.2, 3.6), "#2855a6"),
    (np.sin(2*np.pi*t)**2, .5, r"$f(t)=\sin^2(2\pi t)$", (-.15, 1.45), "#087e8b"),
    (np.full_like(t, 2.), 1/3, r"$f(t)=2$: every shift preserves its value", (1.45, 2.75), "#7d3c98"),
]
for i, (ax, (values, period, title, limits, colour)) in enumerate(zip(axes, examples)):
    ax.axvspan(0, period, color=colour, alpha=.09)
    ax.axvspan(period, 2*period, color=colour, alpha=.18)
    ax.plot(t, values, color=colour, lw=2.3)
    ax.set(xlim=(-.5, 2.5), ylim=limits, ylabel=r"$f(t)$" if i else r"$g(t)$", title=title)
    level = limits[1] - .12*(limits[1]-limits[0])
    ax.annotate("", xy=(0, level), xytext=(period, level),
                arrowprops={"arrowstyle": "<->", "color": "#333333", "lw": 1.4})
    label = r"$T_0=1$" if i == 0 else r"$T_0=1/2$" if i == 1 else r"$T=1/3$ is one of infinitely many choices"
    ax.text(period + .08, level, label, va="center", fontsize=12,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": .85, "pad": 3})
    ax.axvline(0, color="#aaaaaa", lw=.8)
    ax.grid(alpha=.15)
axes[-1].set_xlabel(r"$t$ (dimensionless input)")
fig.suptitle("A period repeats the graph; a fundamental period is the shortest positive one", fontsize=16)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
