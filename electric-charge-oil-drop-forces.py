"""Original apparatus and terminal-force schematic, not measured data.

Tested with Python 3.14.4 and matplotlib; run from _media to save there.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, axes = plt.subplots(1, 3, figsize=(11.2, 5.6), facecolor="white",
                         gridspec_kw={"width_ratios": [1.35, 1, 1]})
blue, red, green, gray = "#2266a0", "#b83c3c", "#26805a", "#384452"
for ax in axes:
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")

ax = axes[0]
ax.set_title("Apparatus: follow the same drop", fontsize=12, fontweight="bold", pad=16)
ax.plot([.1, .41], [.8, .8], lw=5, color=gray)
ax.plot([.47, .79], [.8, .8], lw=5, color=gray)
ax.plot([.1, .79], [.2, .2], lw=5, color=gray)
ax.text(.17, .85, "+   +   +", color=red)
ax.text(.2, .13, "−   −   −", color=blue)
ax.text(.44, .97, "oil spray", ha="center")
ax.annotate("", (.44, .83), (.44, .93), arrowprops={"arrowstyle": "->", "color": gray})
ax.add_patch(Circle((.44, .49), .035, facecolor="#d5a02d", edgecolor=gray))
ax.text(.34, .46, r"$q<0$", ha="right")
ax.annotate("", (.67, .36), (.67, .66), arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
ax.text(.71, .52, r"$\mathbf{E}$", color=blue)
ax.annotate("", (.06, .8), (.06, .2), arrowprops={"arrowstyle": "<->", "color": gray})
ax.text(.015, .5, r"$d$", ha="center")
ax.plot([.12, .75], [.43, .43], ls=":", color="#aab3bc")
ax.plot([.12, .75], [.57, .57], ls=":", color="#aab3bc")
ax.add_patch(Rectangle((.8, .44), .17, .12, facecolor="white", edgecolor=gray))
ax.text(.88, .5, "scope", ha="center", fontsize=9)
ax.text(.44, .04, r"$E \simeq |V|/d$; timed reticle crossings", ha="center", fontsize=10)

def arrow(ax, x, y0, y1, color, label, label_x, align):
    ax.annotate("", (x, y1), (x, y0), arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2})
    ax.text(label_x, (y0+y1)/2, label, color=color, ha=align, va="center", fontsize=11)

for ax in axes[1:]:
    ax.add_patch(Circle((.5, .5), .045, facecolor="#d5a02d", edgecolor=gray))
axes[1].set_title("Field off: terminal fall", fontsize=12, fontweight="bold", pad=16)
arrow(axes[1], .38, .54, .86, blue, r"$kv_f$ drag", .33, "right")
arrow(axes[1], .64, .54, .72, green, r"$F_b$", .69, "left")
arrow(axes[1], .5, .45, .13, gray, r"$mg$", .55, "left")
axes[1].text(.5, .04, r"$mg = F_b + kv_f$", ha="center", fontsize=12)
axes[2].set_title("Field on: terminal rise", fontsize=12, fontweight="bold", pad=16)
arrow(axes[2], .38, .54, .86, red, r"$|q|E$", .33, "right")
arrow(axes[2], .64, .54, .72, green, r"$F_b$", .69, "left")
arrow(axes[2], .38, .45, .13, gray, r"$mg$", .33, "right")
arrow(axes[2], .64, .45, .23, blue, r"$kv_r$ drag", .69, "left")
axes[2].text(.5, .04, r"$|q|E + F_b = mg + kv_r$", ha="center", fontsize=12)
fig.suptitle("Oil-drop inference: drag reverses with motion; buoyancy stays upward", fontsize=15, y=.98)
fig.text(.5, .025, r"Original idealized schematic • $k=6\pi\eta a$ before slip correction • geometry and arrow lengths not to scale", ha="center", fontsize=10, color=gray)
fig.subplots_adjust(left=.055, right=.965, top=.82, bottom=.13, wspace=.42)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white", transparent=False)
plt.close(fig)
