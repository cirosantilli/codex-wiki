"""Illustrate the local magnetic interface model; output PNG to caller CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 10, "axes.titlesize": 12})
fig, (ax, growth) = plt.subplots(1, 2, figsize=(10.4, 4.0))
fig.set_facecolor("white")
x = np.linspace(-1.0, 1.0, 500)
h = 0.09 * np.cos(2 * np.pi * x)
ax.fill_between(x, -0.9, h, color="#e3eff9")
ax.fill_between(x, h, 0.9, color="#fff1de")
ax.plot(x, h, color="#293846", lw=2)
ax.axhline(0, color="#7f8992", lw=0.8, ls=":")
ax.text(-0.88, 0.64, r"$\rho_+>\rho_-,\quad p_+>p_-$", fontsize=12)
ax.text(-0.88, 0.45, "Weaker field above", color="#975316")
ax.annotate("", (0.8, 0.31), (-0.75, 0.31),
            arrowprops={"arrowstyle": "->", "lw": 2.0, "color": "#c17628"})
ax.text(0, 0.37, r"$B_2\,\hat{\mathbf{x}}$", ha="center")
ax.text(-0.88, -0.67, "Stronger field below", color="#245983")
for xpos in (-0.65, 0, 0.65):
    ax.text(xpos, -0.40, r"$\otimes$", fontsize=22, ha="center", color="#245983")
ax.text(0, -0.58, r"$B_1\,\hat{\mathbf{y}}$ (into page)", ha="center")
ax.annotate("", (0.92, 0.50), (0.92, 0.83),
            arrowprops={"arrowstyle": "->", "color": "#263238"})
ax.text(0.85, 0.69, r"$g$", ha="right")
ax.text(-0.88, 0.12, r"$h(x)$", fontsize=11)
ax.set(xlim=(-1, 1), ylim=(-0.9, 0.9), xlabel=r"$x$", ylabel=r"$z$",
       title="Equal total pressure, unequal gas density", xticks=[], yticks=[0])

q = np.linspace(0, 2.05, 700)
field_ratio = 101.0
for angle, color in zip((0, 5, 15), ("#126c94", "#bc691a", "#6d54a3")):
    theta = np.deg2rad(angle)
    beta = np.cos(theta)**2 + field_ratio * np.sin(theta)**2
    curve = 2 * q - beta * q**2
    growth.plot(q, curve, lw=2.1, color=color, label=rf"$\theta={angle}^\circ$")
growth.scatter([1], [1], color="#126c94", s=35, zorder=4)
growth.axhline(0, color="#75808a", lw=0.8)
growth.axvline(1, color="#75808a", lw=0.8, ls=":")
growth.annotate("Fastest: along weaker field", xy=(1, 1), xytext=(0.58, 1.11),
                fontsize=10, arrowprops={"arrowstyle": "-", "color": "#43535e"})
growth.set(xlim=(0, 2.05), ylim=(-0.08, 1.20), xlabel=r"$K/K_*$",
           ylabel=r"$s^2/s_{\max}^2$",
           title="Turning the wavevector bends the stronger field")
growth.text(0.05, 0.96, r"$B_1^2/B_2^2=101$", transform=growth.transAxes,
            va="top", fontsize=10)
growth.legend(loc="upper right", bbox_to_anchor=(1, 0.87), frameon=False)
growth.grid(alpha=0.15)
fig.tight_layout(w_pad=2.4)
fig.savefig(Path.cwd() / "paper-74-magnetic-interface.png", dpi=130,
            facecolor="white", transparent=False)
plt.close(fig)
