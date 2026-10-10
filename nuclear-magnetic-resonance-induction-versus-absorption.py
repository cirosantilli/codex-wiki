"""Original functional comparison of the two 1946 NMR instruments.

Python 3.14; matplotlib 3.10.7. Run from _media; output goes to CWD.
Sources: Physical Review 69, 127 and 37; 70, 474–480 (1946).
Geometry and connections are schematic, not engineering reconstructions.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch


plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
fig, axes = plt.subplots(1, 2, figsize=(12, 7), facecolor="white")
blue, orange = "#16679a", "#bd571b"


def box(ax, x, y, w, h, label, color=blue):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012",
                              facecolor="#f6f8fa", edgecolor=color, linewidth=1.5))
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=10)


def arrow(ax, start, end, color=blue):
    ax.annotate("", end, start, arrowprops={"arrowstyle": "->", "color": color,
                                         "linewidth": 1.6})


for ax in axes:
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")

ax = axes[0]
ax.set_title("Bloch–Hansen–Packard: induction", fontsize=15, weight="bold", pad=18)
ax.text(.5, .96, "Detailed October apparatus", ha="center", color="#555555")
ax.add_patch(Circle((.48, .72), .065, fc="#dceff8", ec=blue, lw=1.5))
ax.add_patch(Ellipse((.48, .72), .37, .17, fill=False, ec=orange, lw=2))
ax.add_patch(Ellipse((.48, .72), .18, .34, fill=False, ec=blue, lw=2))
ax.text(.48, .72, "water", ha="center", va="center", fontsize=9)
arrow(ax, (.58, .72), (.88, .72), orange)
ax.text(.89, .72, "$B_x$\nRF", va="center", color=orange)
arrow(ax, (.48, .80), (.48, .91))
ax.text(.52, .89, "pickup $y$", color=blue)
ax.text(.06, .87, "$\\odot\\ B_z$\nstatic", ha="left")
ax.text(.48, .51, "coil axes perpendicular", ha="center", fontsize=10)
box(ax, .04, .37, .25, .08, "RF source", orange)
box(ax, .44, .37, .48, .08, "tuned transmitter", orange)
arrow(ax, (.30, .41), (.43, .41), orange)
box(ax, .04, .22, .25, .08, "tuned pickup")
box(ax, .44, .22, .48, .08, "diode → audio amplifier")
arrow(ax, (.30, .26), (.43, .26))
box(ax, .44, .06, .48, .08, "oscillograph: vertical")
arrow(ax, (.68, .21), (.68, .15))
ax.text(.04, .10, "60 Hz field\nmodulation → horizontal", fontsize=9, va="center")

ax = axes[1]
ax.set_title("Purcell–Torrey–Pound: absorption", fontsize=15, weight="bold", pad=18)
ax.text(.5, .96, "January letter apparatus", ha="center", color="#555555")
box(ax, .24, .60, .53, .22, "loaded coaxial cavity\nparaffin", orange)
ax.add_patch(Ellipse((.22, .70), .075, .11, fill=False, ec=blue, lw=1.7))
ax.add_patch(Ellipse((.79, .70), .075, .11, fill=False, ec=blue, lw=1.7))
ax.text(.08, .79, "input\nloop", ha="center", fontsize=9)
ax.text(.92, .79, "output\nloop", ha="center", fontsize=9)
arrow(ax, (.37, .86), (.65, .86), orange)
ax.text(.5, .89, "$B_{\\rm RF}$", ha="center", color=orange)
ax.text(.06, .89, "$\\odot\\ B_0$", ha="center")
box(ax, .04, .37, .24, .08, "RF source")
box(ax, .42, .37, .20, .08, "cavity", orange)
box(ax, .76, .37, .18, .08, "balance")
arrow(ax, (.29, .41), (.41, .41))
arrow(ax, (.63, .41), (.75, .41))
ax.plot([.16, .16, .85, .85], [.36, .29, .29, .36], color=blue, lw=1.5)
arrow(ax, (.85, .30), (.85, .36))
ax.text(.5, .30, "reference", ha="center", va="bottom", fontsize=9)
box(ax, .32, .15, .62, .08, "amplify / detect → microammeter")
ax.plot([.95, .98, .98], [.41, .41, .19], color=blue, lw=1.5)
arrow(ax, (.98, .19), (.95, .19))
ax.text(.5, .055, "slow static-field sweep", ha="center", fontsize=10)

fig.suptitle("Bulk nuclei, two different electrical readouts", fontsize=18, y=.98)
fig.text(.5, .014, "Original functional schematics • continuous RF • field directions shown, winding geometry omitted",
         ha="center", fontsize=10, color="#555555")
fig.subplots_adjust(top=.86, bottom=.08, left=.03, right=.97, wspace=.15)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
