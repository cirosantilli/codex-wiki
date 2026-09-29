"""Original nylon interface / chemical-unit schematic; no measured geometry.

Tested with Python 3.14.4 and matplotlib 3.10.7 (repository environment).
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
The matching PNG basename is written to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

NAVY, TEAL, ORANGE = "#18364b", "#007f82", "#c75f18"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "text.color": NAVY, "figure.facecolor": "white"})
fig = plt.figure(figsize=(11.2, 7.4), dpi=100, facecolor="white")
fig.suptitle("Nylon 6,10: feed molecules, chemical repeats, model segments",
             x=.5, y=.97, fontsize=17, weight="bold")
a = fig.add_axes([.04, .41, .39, .48])
b = fig.add_axes([.48, .41, .48, .48])
c = fig.add_axes([.055, .055, .89, .28])
for ax in (a, b, c):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
a.text(0, .97, "1  A film forms where the layers meet", weight="bold", fontsize=12)
# Immiscible liquid layers; opaque pastel fills on a white canvas.
a.add_patch(Rectangle((.12, .13), .51, .26, facecolor="#e1f1f3", edgecolor="none"))
a.add_patch(Rectangle((.12, .39), .51, .25, facecolor="#fff0df", edgecolor="none"))
a.plot([.12, .12, .63, .63], [.73, .13, .13, .73], color=NAVY, lw=2)
a.plot([.12, .63], [.39, .39], color=TEAL, lw=4)
a.text(.37, .55, "Organic layer\nacid-chloride monomer", ha="center", fontsize=10)
a.text(.37, .23, "Water layer\ndiamine monomer", ha="center", fontsize=10)
a.plot([.41, .44, .49, .56, .63, .72], [.39, .45, .54, .65, .75, .83], color=TEAL, lw=3)
a.plot([.65, .84], [.84, .84], color=NAVY, lw=7, solid_capstyle="round")
a.annotate("Draw and wind\nonto a glass rod", xy=(.71, .83), xytext=(.69, .61),
           fontsize=10, ha="left", arrowprops={"arrowstyle": "->", "color": NAVY})
a.annotate("Nylon film", xy=(.60, .39), xytext=(.70, .40),
           fontsize=10, arrowprops={"arrowstyle": "->", "color": TEAL})
a.text(.12, .025, "Continued withdrawal supplies a visible thread.", fontsize=10)

b.text(0, .97, "2  Two feed species supply one interior repeat", weight="bold", fontsize=12)
b.text(.02, .78, "A: Diamine", color=TEAL, weight="bold")
b.text(.02, .68, r"$\mathrm{H_2N{-}(CH_2)_6{-}NH_2}$", fontsize=15, color=TEAL)
b.text(.02, .53, "B: Diacid chloride", color=ORANGE, weight="bold")
b.text(.02, .43, r"$\mathrm{Cl{-}C(=O){-}(CH_2)_8{-}C(=O){-}Cl}$", fontsize=14, color=ORANGE)
b.annotate("", xy=(.48, .25), xytext=(.48, .38),
           arrowprops={"arrowstyle": "->", "lw": 1.8, "color": NAVY})
b.text(.55, .29, "formal loss of 2 HCl\nper interior-repeat budget", fontsize=10)
b.text(.02, .16, r"$\mathrm{{-}NH{-}(CH_2)_6{-}NH{-}C(=O){-}(CH_2)_8{-}C(=O){-}}$", fontsize=13)
b.text(.02, .035, "Repeat: C₁₆H₃₀N₂O₂. Finite chain ends need a correction.", fontsize=10)

c.text(0, .98, "3  Chemical repetition and statistical coarse-graining count different objects",
       fontsize=12, weight="bold")
left, width = .045, .91 / 18
for j in range(18):
    x = left + j * width
    color = TEAL if j % 2 == 0 else ORANGE
    c.add_patch(Rectangle((x, .62), width*.94, .17, facecolor=color, edgecolor="white"))
    c.text(x+width*.47, .705, "A" if j % 2 == 0 else "B", color="white", ha="center", va="center", fontsize=10)
# AB denotes one diamine-derived and one diacid-derived monomeric unit.
c.annotate("One AB chemical repeat", xy=(left+width, .60), xytext=(.035, .43),
           fontsize=10, arrowprops={"arrowstyle": "->", "color": NAVY})
for group in range(3):
    x0, x1 = left+group*6*width, left+(group+1)*6*width
    c.plot([x0, x0, x1, x1], [.59, .55, .55, .59], color=NAVY, lw=1)
    c.annotate("", xy=((x0+x1)/2, .29), xytext=((x0+x1)/2, .53),
               arrowprops={"arrowstyle": "->", "color": NAVY})
nodes = [left+i*6*width for i in range(4)]
for i in range(3):
    c.plot(nodes[i:i+2], [.20, .20], color=NAVY, lw=3)
for x in nodes:
    c.add_patch(Circle((x, .20), .011, color=NAVY))
c.text(.50, .025, "18 monomeric units = 9 chemical repeats → 3 arbitrarily chosen model segments",
       ha="center", fontsize=11)
fig.text(.5, .365, "Original explanatory schematic • not measured dimensions, chain conformations, or segment lengths",
         ha="center", fontsize=10, color="#526773")
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
plt.close(fig)
