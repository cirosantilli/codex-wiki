"""Original schematic; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media to emit laser-cooling-opposed-beams-doppler-absorption.png.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np

fig = plt.figure(figsize=(9, 6.2), facecolor="white")
fig.suptitle("A moving atom absorbs more light from the beam ahead", fontsize=16, y=.97)
ax = fig.add_axes((.05, .50, .90, .39))
ax.set(xlim=(0, 10), ylim=(0, 3))
ax.axis("off")
blue, orange, green = "#2768a7", "#bb591b", "#168064"


def arrow(start, end, color, lw=3, style="-|>"):
    ax.annotate("", end, start, arrowprops=dict(arrowstyle=style, color=color, lw=lw, mutation_scale=18))


for x in (.25, 8.75):
    ax.add_patch(Rectangle((x, 1.35), 1, .5, facecolor="#f2e6e6", edgecolor="#804040"))
    ax.text(x+.5, 1.60, "Laser", ha="center", va="center", fontsize=12)
arrow((1.3, 1.60), (4.35, 1.60), blue, 2)
arrow((8.7, 1.60), (5.65, 1.60), orange, 5)
ax.add_patch(Circle((5, 1.60), .35, facecolor="#e4ebf0", edgecolor="#344657", linewidth=2))
ax.text(5, 1.60, "atom", ha="center", va="center", fontsize=11)
arrow((4.6, 2.43), (6.3, 2.43), green)
ax.text(5.45, 2.65, r"Velocity $v>0$", ha="center", color=green, fontsize=12)
ax.text(2.8, 2.08, r"$+k$: fewer absorptions", ha="center", color=blue, fontsize=12)
ax.text(7.3, 2.08, r"$-k$: more absorptions", ha="center", color=orange, fontsize=12)
ax.text(2.8, 1.08, r"Kick $+\hbar k$", ha="center", color=blue, fontsize=12)
ax.text(7.3, 1.08, r"Kick $-\hbar k$", ha="center", color=orange, fontsize=12)
for end in ((4.3, .62), (5.5, .56), (5.88, 2.04)):
    arrow((5, 1.60), end, "#8a8a8a", 1.2)
ax.text(5, .12, "Spontaneous emission: zero mean kick, nonzero kick variance", ha="center", fontsize=11)

ax2 = fig.add_axes((.12, .12, .77, .30))
delta = np.linspace(-1.8, 1.0, 800)
ax2.plot(delta, 1/(1+4*delta**2), color="#344657", lw=2)
ax2.axvline(0, color="#777777", ls=":", lw=1)
for q, color, label, offset in ((-.75, blue, r"$d-u=-0.75$", (-100, -8)), (-.25, orange, r"$d+u=-0.25$", (-155, 14))):
    y = 1/(1+4*q*q)
    ax2.plot(q, y, "o", color=color, ms=8)
    ax2.annotate(label, (q, y), xytext=offset, textcoords="offset points", color=color, fontsize=12,
                 arrowprops=dict(arrowstyle="->", color=color))
ax2.set(xlim=(-1.8, 1), ylim=(0, 1.13), xlabel=r"Atom-frame detuning / $\Gamma$", ylabel="Relative scattering rate")
ax2.set_title(r"Illustrative model: $d=-0.5$, $u=kv/\Gamma=0.25$", fontsize=12, pad=8)
ax2.text(.12, 1.04, "resonance", fontsize=10, color="#555555")
ax2.spines[["top", "right"]].set_visible(False)
fig.text(.5, .015, "Schematic and calculated line shape; arrow thickness indicates unequal scattering, not measured data.", ha="center", fontsize=9)
fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
plt.close(fig)
