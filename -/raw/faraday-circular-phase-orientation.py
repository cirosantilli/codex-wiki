"""Illustrate circular-mode phase difference and linear-polarization orientation.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; writes an opaque PNG into the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white",
                     "axes.facecolor": "white", "savefig.facecolor": "white"})
blue, purple, orange = "#1764a0", "#8b4dab", "#c36513"
fig = plt.figure(figsize=(10, 6.7), layout="constrained")
grid = fig.add_gridspec(2, 3, height_ratios=[1.45, 1])
phase_time = np.pi / 4
fractions = [0, 0.5, 1]
for col, fraction in enumerate(fractions):
    ax = fig.add_subplot(grid[0, col])
    theta = fraction * np.pi / 6
    # u+ = (x - i y)/sqrt(2), u- = (x + i y)/sqrt(2).
    # Remove common phase, set phi+ = theta, phi- = -theta.
    ep = 0.5 * np.array([np.cos(theta - phase_time),
                         np.sin(theta - phase_time)])
    em = 0.5 * np.array([np.cos(theta + phase_time),
                         np.sin(theta + phase_time)])
    total = ep + em
    direction = np.array([np.cos(theta), np.sin(theta)])
    ax.axhline(0, color="#b9c0c7", lw=0.8)
    ax.axvline(0, color="#b9c0c7", lw=0.8)
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(0.5 * np.cos(t), 0.5 * np.sin(t), color="#e3e5e8", lw=1)
    ax.plot([-0.82 * direction[0], 0.82 * direction[0]],
            [-0.82 * direction[1], 0.82 * direction[1]],
            color=orange, lw=2, alpha=0.45)
    for vector, color in [(ep, blue), (em, purple), (total, orange)]:
        ax.annotate("", xy=vector, xytext=(0, 0),
                    arrowprops={"arrowstyle": "-|>", "lw": 2.7, "color": color})
    ax.plot([ep[0], total[0]], [ep[1], total[1]], color=purple, ls=":", lw=1.2)
    ax.plot([em[0], total[0]], [em[1], total[1]], color=blue, ls=":", lw=1.2)
    if theta:
        arc = np.linspace(0, theta, 70)
        ax.plot(0.29 * np.cos(arc), 0.29 * np.sin(arc), color=orange)
    ax.set(xlim=(-0.88, 0.88), ylim=(-0.65, 0.77), aspect="equal",
           xticks=[-0.5, 0, 0.5], yticks=[-0.5, 0, 0.5],
           xlabel=r"$E_x/E_0$", ylabel=r"$E_y/E_0$")
    ax.set_title(f"Path fraction {fraction:g}\n"
                 + rf"$\phi_+-\phi_-={fraction * 60:g}^\circ$, "
                 + rf"$\theta={fraction * 30:g}^\circ$", fontsize=11)

ax = fig.add_subplot(grid[1, :])
s = np.linspace(0, 1, 200)
ax.plot(s, 60 * s, color=blue, lw=2.4, label=r"Relative phase $\phi_+-\phi_-$")
ax.plot(s, 30 * s, color=orange, lw=2.4, label=r"Line orientation $\theta$")
ax.scatter(fractions, 60 * np.array(fractions), color=blue, s=25)
ax.scatter(fractions, 30 * np.array(fractions), color=orange, s=25)
ax.set(xlim=(0, 1.02), ylim=(0, 67), xlabel="Fraction of sample length",
       ylabel="Angle (degrees)", yticks=[0, 15, 30, 45, 60])
ax.grid(alpha=0.18)
ax.legend(loc="upper left", frameon=False)
fig.suptitle("Faraday rotation: the line turns by half the circular phase difference",
             fontsize=14)
handles = [Line2D([0], [0], color=blue, lw=3, label=r"Real $\mathbf{u}_+$ component"),
           Line2D([0], [0], color=purple, lw=3, label=r"Real $\mathbf{u}_-$ component"),
           Line2D([0], [0], color=orange, lw=3, label="Sum and oscillation line")]
fig.legend(handles=handles, loc="outside lower center", ncol=3, frameon=False,
           title=r"Top: one common instant, $\omega t=\pi/4$; normalized field components")
fig.savefig(Path(__file__).stem + ".png", dpi=120, transparent=False)
