"""Functional tensile-test readouts; Python 3.14, matplotlib 3.10.7.

Original schematic, not a dimensional reconstruction of an instrument.
Run from the desired output directory; writes this script's basename.png.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def arrow(ax, start, end, color="#253746", style="->", lw=1.6):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": style, "color": color, "lw": lw})


def spring(ax, x, bottom, top, color):
    ys = np.linspace(bottom + 0.18, top - 0.18, 15)
    xs = x + 0.22 * np.array([0] + [(-1) ** i for i in range(13)] + [0])
    ax.plot([x, x], [bottom, ys[0]], color=color, lw=2)
    ax.plot(xs, ys, color=color, lw=2)
    ax.plot([x, x], [ys[-1], top], color=color, lw=2)


plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
fig, (ax, model) = plt.subplots(1, 2, figsize=(12, 7.6),
                               gridspec_kw={"width_ratios": [1.6, 1]})
fig.patch.set_facecolor("white")
blue, orange, teal = "#2266a2", "#d16a16", "#087e83"
ax.set(xlim=(0, 9), ylim=(0, 10))
ax.set_title("Apparatus and independent readouts", loc="left", weight="bold", pad=13)
ax.axis("off")

# Closed mechanical load path: fixed frame, force sensor, grips, bar, actuator.
for x in [0.7, 5.5]:
    ax.add_patch(Rectangle((x, 1.0), 0.17, 8.1, fc="#d6dce1", ec="#788792"))
ax.add_patch(Rectangle((0.45, 8.9), 5.55, 0.25, fc="#bdc7cf", ec="#788792"))
ax.add_patch(Rectangle((0.45, 0.75), 5.55, 0.3, fc="#bdc7cf", ec="#788792"))
ax.plot([3.1, 3.1], [7.9, 8.9], color="#253746", lw=3)
ax.add_patch(Rectangle((2.58, 7.35), 1.04, 0.55, fc="#dce9f6", ec=blue, lw=2))
ax.text(3.1, 7.62, "F", ha="center", va="center", color=blue, weight="bold")
ax.plot([3.1, 3.1], [6.8, 7.35], color="#253746", lw=3)
for y in [2.7, 6.15]:
    ax.add_patch(Rectangle((2.55, y), 1.1, 0.65, fc="#a8b7c3", ec="#253746"))
ax.add_patch(Rectangle((2.9, 3.35), 0.4, 2.8, fc="#e5b77a", ec="#8b5618", lw=2))
ax.add_patch(Rectangle((2.1, 2.38), 2, 0.3, fc="#b5c5d1", ec="#253746"))
ax.add_patch(Rectangle((2.55, 1.1), 1.1, 0.8, fc="#f6e0cf", ec=orange, lw=2))
ax.plot([3.1, 3.1], [1.9, 2.38], color=orange, lw=4)
arrow(ax, (2.0, 2.3), (2.0, 1.4), orange)
ax.text(1.8, 1.85, "pull", color=orange, ha="right", va="center")

# Extensometer's contacts lie inside the uniform exposed specimen.
for y in [4.0, 5.45]:
    ax.plot([3.3, 4.25], [y, y], color=teal, lw=2)
    ax.plot(3.3, y, "o", color=teal, ms=5)
ax.plot([4.25, 4.25], [4.0, 5.45], color=teal, lw=3)
arrow(ax, (3.85, 4.0), (3.85, 5.45), teal, "<->")
ax.text(3.66, 4.73, "$L_g$", color=teal, ha="right", va="center")
arrow(ax, (2.16, 3.35), (2.16, 6.15), blue, "<->")
ax.text(1.95, 4.75, "$L$", color=blue, ha="right", va="center")
ax.text(2.92, 5.9, "$A_0$", ha="right", color="#8b5618")

# Callout connectors distinguish all three measured channels.
for start, end, label, color in [
    ((3.62, 7.62), (6.05, 7.62), "Load cell\nforce $F$", blue),
    ((4.25, 4.73), (6.05, 4.73), "Extensometer\nlocal $\\Delta L_g$", teal),
    ((3.65, 1.5), (6.05, 1.5), "Actuator encoder\ntravel $x$", orange),
]:
    arrow(ax, start, end, color)
    ax.text(end[0] + 0.1, end[1], label, color=color, va="center")
ax.text(0.8, 8.55, "Fixed reaction frame", color="#53636e")
ax.text(0.05, 0.12, "Local gauge length $L_g$ may be shorter than exposed length $L$.",
        fontsize=10, color="#253746")

model.set(xlim=(0, 6), ylim=(0, 10))
model.axis("off")
model.set_title("Series compliance model", loc="left", weight="bold", pad=13)
model.plot([1.0, 2.0], [8.6, 8.6], color="#253746", lw=3)
for x in np.linspace(1, 2, 7):
    model.plot([x, x + 0.14], [8.6, 8.82], color="#253746", lw=1)
spring(model, 1.5, 6.5, 8.6, orange)
spring(model, 1.5, 3.8, 6.5, blue)
model.plot(1.5, 6.5, "o", color="#253746")
model.plot([1.5, 1.5], [3.8, 3.3], color="#253746", lw=2)
arrow(model, (1.5, 3.3), (1.5, 2.55), "#253746")
model.text(1.8, 2.9, "$F$", va="center")
model.text(2.12, 7.6, "Apparatus\n$\\Delta x_m=C_mF$", color=orange, va="center")
model.text(2.12, 5.2, "Uniform specimen\n$\\Delta L=FL/(EA_0)$", color=blue, va="center")
model.text(0.35, 1.7, "$x-x_0=\\Delta L+\\Delta x_m$", fontsize=14)
model.text(0.35, 0.88, "Same force; extensions add.\nFrame and grips also deform.",
           fontsize=11, linespacing=1.6)
fig.subplots_adjust(left=0.025, right=0.985, top=0.91, bottom=0.07, wspace=0.17)
fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
plt.close(fig)
