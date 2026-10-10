"""Original circle-coordinate and trace plots; output matching PNG to CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
fig = plt.figure(figsize=(10.6, 4.8), layout="constrained")
grid = fig.add_gridspec(2, 2, width_ratios=[.95, 1.25])
circle = fig.add_subplot(grid[:, 0])
cosine = fig.add_subplot(grid[0, 1])
sine = fig.add_subplot(grid[1, 1])
theta = np.linspace(0, 2*np.pi, 601)
alpha = np.pi/6
x, y = np.cos(alpha), np.sin(alpha)
circle.plot(np.cos(theta), np.sin(theta), color="#555555", lw=1.5)
circle.axhline(0, color="#aaaaaa", lw=.8)
circle.axvline(0, color="#aaaaaa", lw=.8)
circle.plot([0, x], [0, y], color="#333333", lw=2)
circle.plot([0, x], [0, 0], color="#2855a6", lw=4)
circle.plot([x, x], [0, y], color="#087e8b", lw=4)
circle.plot([0, x], [y, y], color="#087e8b", lw=1.2, ls=":")
circle.scatter([x], [y], color="#333333", s=42)
arc = np.linspace(0, alpha, 60)
circle.plot(.30*np.cos(arc), .30*np.sin(arc), color="#c45b12", lw=2)
circle.text(.34, .085, r"$\pi/6$", color="#c45b12", fontsize=13)
circle.text(x/2, -.14, r"$\cos(\pi/6)=\sqrt{3}/2$", color="#2855a6",
            ha="center", fontsize=12)
circle.text(x+.035, .27, r"$1/2$", color="#087e8b", fontsize=12)
circle.text(.05, y+.03, r"$\sin(\pi/6)=1/2$", color="#087e8b", fontsize=12)
beta=2*np.pi/3
circle.scatter([np.cos(beta)], [np.sin(beta)], color="#7d3c98", s=38)
circle.text(-.96, 1.04, r"At $2\pi/3$: $x=-1/2$, $y=\sqrt{3}/2$",
            color="#7d3c98", fontsize=11)
circle.set(xlim=(-1.12, 1.16), ylim=(-1.12, 1.18), aspect="equal",
           xticks=[-1,0,1], yticks=[-1,0,1],
           xlabel="Horizontal coordinate", ylabel="Vertical coordinate",
           title="Unit circle: signed coordinates")
for ax, values, value, colour, name in [(cosine,np.cos(theta),x,"#2855a6","cosine"),
                                        (sine,np.sin(theta),y,"#087e8b","sine")]:
    ax.plot(theta, values, color=colour, lw=2.4)
    ax.scatter([alpha], [value], color=colour, s=45, zorder=3)
    ax.axvline(alpha, color="#c45b12", ls=":", lw=1.3)
    ax.axhline(0, color="#aaaaaa", lw=.8)
    ax.set(xlim=(0,2*np.pi), ylim=(-1.18,1.18), ylabel=name,
           xticks=[0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],
           xticklabels=["0",r"$\pi/2$",r"$\pi$",r"$3\pi/2$",r"$2\pi$"])
    ax.grid(alpha=.15)
cosine.set_title("One turn gives two periodic traces")
sine.set_xlabel(r"Counterclockwise angle $\theta$ (radians)")
fig.suptitle("Sine and cosine read the same rotating point", fontsize=17)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
