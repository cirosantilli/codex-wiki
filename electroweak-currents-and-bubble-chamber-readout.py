"""Original process/readout schematic. Python 3.14, matplotlib 3.10.7.

Run from _media; writes the matching PNG into the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


BLUE, RED, GREEN, GRAY = "#17679c", "#b24137", "#247c54", "#5e6971"
fig = plt.figure(figsize=(12, 7.5), facecolor="white", layout="constrained")
gs = fig.add_gridspec(3, 2, height_ratios=[1.0, 0.65, 1.12])


def process(ax, neutral):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.set_title("Z exchange: neutral current" if neutral else "W exchange: charged current", fontsize=15, fontweight="bold", pad=9)
    for x0, y0, x1, y1, label, color, dashed in [
        (.08, .85, .42, .62, r"$\nu_\mu$", BLUE, True),
        (.42, .62, .90, .85, r"$\nu_\mu$" if neutral else r"$\mu^-$", BLUE if neutral else RED, neutral),
        (.08, .10, .42, .33, r"$q$", GREEN, False),
        (.42, .33, .90, .10, r"$q$" if neutral else r"$q'$", GREEN, False),
    ]:
        ax.annotate("", (x1, y1), (x0, y0), arrowprops=dict(arrowstyle="->", lw=2, color=color, linestyle="--" if dashed else "-"))
        ax.text((x0+x1)/2, (y0+y1)/2 + (.07 if y0>.4 else -.10), label, ha="center", fontsize=16, color=color)
    y = np.linspace(.33, .62, 120)
    ax.plot(.42+.013*np.sin(np.linspace(0, 9*np.pi, len(y))), y, color=GRAY, lw=1.8)
    ax.text(.48, .45, r"$Z^0$" if neutral else r"$W^+$", fontsize=16)
    ax.text(.51, -.03, "Quark-level illustration; exchange boson is virtual", ha="center", fontsize=10, color=GRAY)


process(fig.add_subplot(gs[0, 0]), False)
process(fig.add_subplot(gs[0, 1]), True)
ax = fig.add_subplot(gs[1, :])
ax.axis("off")
ax.set(xlim=(0, 1), ylim=(0, 1))
stages = [(0.005, .20, "Protons on target\ncharged mesons"), (.255, .20, "Horn + decay region\nmesons → μ + ν"), (.505, .20, "Shielding\nabsorbs most other particles"), (.755, .20, "Heavy-liquid chamber\nphotograph charged tracks")]
for x, y, label in stages:
    ax.add_patch(FancyBboxPatch((x, y), .225, .60, boxstyle="round,pad=0.005", facecolor="#f0f5f8", edgecolor="#8c9ca8"))
    ax.text(x+.1125, y+.30, label, ha="center", va="center", fontsize=10)
    if x < .75:
        ax.annotate("", (x+.248, .50), (x+.228, .50), arrowprops=dict(arrowstyle="->", color=GRAY))


def readout(ax, neutral):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((.03, .15), .94, .73, boxstyle="round,pad=0.01", facecolor="white", edgecolor=GRAY))
    ax.text(.5, .96, "Hadronic neutral-current candidate" if neutral else "Charged-current comparison", ha="center", fontsize=13, fontweight="bold")
    v = (.34, .53)
    ax.annotate("", v, (.06, .53), arrowprops=dict(arrowstyle="->", lw=1.6, linestyle="--", color=BLUE))
    ax.text(.16, .58, r"$\nu_\mu$", color=BLUE, fontsize=13)
    ax.plot(*v, "o", color="black", ms=4)
    for end in [(.58, .76), (.67, .42), (.52, .24)]:
        t=np.linspace(0, 1, 16)
        ax.plot(v[0]+t*(end[0]-v[0]), v[1]+t*(end[1]-v[1]), ".", color=GREEN, ms=3)
    ax.text(.76, .24, "hadrons", color=GREEN, fontsize=11)
    if neutral:
        ax.annotate("", (.90, .69), v, arrowprops=dict(arrowstyle="->", lw=1.6, linestyle="--", color=BLUE))
        ax.text(.80, .75, r"$\nu_\mu$", color=BLUE, fontsize=13)
        message = "No outgoing μ identified; neutron background must be tested"
    else:
        t=np.linspace(0, 1, 34)
        ax.plot(v[0]+.55*t, v[1]+.08*t-.025*t*t, ".", color=RED, ms=3)
        ax.text(.86, .67, r"$\mu^-$", color=RED, fontsize=14)
        message = "Long track is a μ candidate; escaping hadrons can imitate it"
    ax.text(.50, .055, message, ha="center", fontsize=9.6)


readout(fig.add_subplot(gs[2, 0]), False)
readout(fig.add_subplot(gs[2, 1]), True)
fig.suptitle("From electroweak exchange to a photographed event", fontsize=19, fontweight="bold")
fig.supxlabel("Dots = visible charged-particle bubbles     Dashed = inferred neutrino path, never a visible track\nFunctional schematic; no detector scale or historical event is reproduced", fontsize=11)
fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
