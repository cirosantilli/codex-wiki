"""Original interfacial-chain schematics; Python 3.14, numpy, matplotlib."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


fig, axes = plt.subplots(1, 2, figsize=(11, 3.9), constrained_layout=True,
                         facecolor="white")
blue, orange, green = "#1764a0", "#c55412", "#197c54"
for ax in axes:
    ax.set(xlim=(0, 9), ylim=(-0.45, 3.1))
    ax.axhspan(-0.35, 0, color="0.86")
    ax.plot([0, 9], [0, 0], color="0.3", lw=1.3)
    ax.axis("off")
    ax.text(0.15, -0.25, "Solid substrate", fontsize=10, color="0.3")

ax = axes[0]
ax.set_title("Adsorbed chain: multiple contact types", fontsize=13)
t = np.linspace(0, 1, 180)
ax.plot(0.3+1.1*t+0.12*np.sin(6*np.pi*t), 1.55*(1-t)+0.08,
        color=green, lw=2.4)
for start, end in [(1.4, 3.1), (5.6, 6.7)]:
    ax.plot(start+(end-start)*t, 0.08+0.035*np.sin(14*np.pi*t),
            color=orange, lw=2.7)
ax.plot(3.1+2.5*t, 0.08+1.55*np.sin(np.pi*t), color=blue, lw=2.4)
ax.plot(6.7+1.8*t, 0.08+1.7*t+0.15*np.sin(5*np.pi*t), color=green, lw=2.4)
for text, pos, target, color in [
        ("Train", (2.0, 0.65), (2.3, 0.11), orange),
        ("Loop", (4.25, 2.22), (4.35, 1.6), blue),
        ("Tail", (7.8, 2.55), (7.65, 1.18), green)]:
    ax.annotate(text, xy=target, xytext=pos, ha="center", fontsize=12,
                color=color, arrowprops={"arrowstyle": "->", "color": color})
ax.text(0.4, 2.55, "Solvent", fontsize=11, color="0.35")

ax = axes[1]
ax.set_title("End grafting: coverage changes conformation", fontsize=13)
for pos in [0.8, 2.6]:
    x = pos+0.5*np.sin(4*np.pi*t)+0.12*np.sin(13*np.pi*t)
    y = 0.04+1.35*t+0.20*np.sin(4*np.pi*t)
    ax.plot(x, y, color=blue, lw=1.8)
    ax.plot(pos, 0.04, "o", color=orange, ms=5)
for j, pos in enumerate(np.linspace(4.6, 8.65, 14)):
    ax.plot(pos+0.075*np.sin(8*np.pi*t+j), 0.04+2.15*t,
            color=green, lw=1.5)
    ax.plot(pos, 0.04, "o", color=orange, ms=3.2)
ax.text(1.7, 1.9, "Isolated mushrooms", ha="center", fontsize=11, color=blue)
ax.text(6.6, 2.55, "Overlapping brush", ha="center", fontsize=11, color=green)
ax.text(4.3, -0.25, "Tethers", color=orange, fontsize=10)
fig.suptitle("Schematic conformations, not molecular simulations or measured layer profiles",
             fontsize=11)
fig.savefig("paper-1-polymer-interfaces.png", dpi=160, facecolor="white")
plt.close(fig)
