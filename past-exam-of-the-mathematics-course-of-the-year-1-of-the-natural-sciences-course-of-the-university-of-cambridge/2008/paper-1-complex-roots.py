"""Original Argand diagrams, independent of the statement's illustrations."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), layout="constrained",
                         gridspec_kw={"width_ratios": [1, 1.8]})
ax = axes[0]
t = np.linspace(0, 2 * np.pi, 500)
ax.plot(np.cos(t), np.sin(t), color="0.65", lw=1)
z = np.exp(1j * np.array([1, 2, 4, 5]) * np.pi / 3)
ax.scatter(z.real, z.imag, color="tab:blue", s=45, zorder=5)
ax.scatter([-1, 1], [0, 0], marker="x", color="tab:red", s=45,
           label="excluded roots of $z^6=1$")
ax.set(xlim=(-1.35, 1.35), ylim=(-1.35, 1.35), aspect="equal",
       title=r"$z^4+z^2+1=0$")
ax.legend(fontsize=8, loc="lower center")
ax = axes[1]
xs = np.pi / 2 + 2 * np.pi * np.arange(-2, 3)
for y in [-2, 2]:
    ax.axhline(y, color="0.7", ls="--", lw=1)
    ax.scatter(xs, np.full_like(xs, y), s=40, color="tab:blue", zorder=4)
ax.annotate("", (xs[2], 2.55), (xs[3], 2.55),
            arrowprops={"arrowstyle": "<->", "color": "0.3"})
ax.text((xs[2] + xs[3])/2, 2.72, r"$2\pi$", ha="center", fontsize=10)
ax.set(xticks=xs, xticklabels=[r"$\pi/2-4\pi$", r"$\pi/2-2\pi$", r"$\pi/2$",
                            r"$\pi/2+2\pi$", r"$\pi/2+4\pi$"],
       yticks=[-2, 0, 2], ylim=(-3.2, 3.3), xlim=(xs[0]-2, xs[-1]+2),
       title=r"$\sin z=\cosh 2$: both rows continue")
for ax in axes:
    ax.axhline(0, color="0.45", lw=0.7)
    ax.axvline(0, color="0.45", lw=0.7)
    ax.set(xlabel=r"$\operatorname{Re}z$", ylabel=r"$\operatorname{Im}z$")
    ax.grid(alpha=0.15)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
