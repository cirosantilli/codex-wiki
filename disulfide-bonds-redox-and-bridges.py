"""Original redox/connectivity schematic; no measured molecular coordinates.

Run from _media: MPLBACKEND=Agg python ../disulfide-bonds-redox-and-bridges.py
Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

BLUE, GREEN, AMBER, INK = '#27689c', '#278369', '#a96108', '#23313e'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(10, 6.7), dpi=120, facecolor='white')
ax.set(xlim=(0, 10), ylim=(0, 6.7))
ax.axis('off')
ax.text(5, 6.4, 'Disulfide bonds: electron counting and chemical bridges',
        ha='center', va='center', size=17, weight='bold', color=INK)
ax.add_patch(FancyBboxPatch((.25, 3.8), 9.5, 2.15, boxstyle='round,pad=0.03',
                         facecolor='#f4f7fa', edgecolor='#cbd5df'))
ax.text(.6, 5.57, 'Oxidation half-reaction', color=INK, weight='bold')
ax.text(.6, 4.94, r'$\mathrm{R{-}SH + R^{\prime}{-}SH}$', size=21, va='center')
ax.annotate('', xy=(5.05, 4.94), xytext=(4.0, 4.94),
            arrowprops={'arrowstyle': '->', 'lw': 2, 'color': AMBER})
ax.text(5.3, 4.94, r'$\mathrm{R{-}S{-}S{-}R^{\prime} + 2H^+ + 2e^-}$',
        size=20, va='center')
ax.text(.6, 4.35, 'Two thiols → one S–S bond + two transferred electrons', color=INK)
ax.text(.6, 4.0, 'Reverse reduction: add 2 H⁺ + 2 e⁻ to obtain two thiols.', color=INK)
ax.text(5, 3.43, 'Protein cartoons: the numbered backbone remains intact',
        ha='center', size=14, weight='bold', color=INK)


def chain(coords, color, first=1):
    xs, ys = zip(*coords)
    ax.plot(xs, ys, color=color, lw=4, solid_capstyle='round', zorder=1)
    for n, (x, y) in enumerate(coords, first):
        ax.add_patch(Circle((x, y), .15, facecolor='white', edgecolor=color,
                            lw=2, zorder=3))
        ax.text(x, y, str(n), ha='center', va='center', color=color, size=10, zorder=4)


def bridge(start, end, s1, s2):
    ax.plot([start[0], s1[0]], [start[1], s1[1]], color=AMBER, lw=2)
    ax.plot([s2[0], end[0]], [s2[1], end[1]], color=AMBER, lw=2)
    ax.plot([s1[0], s2[0]], [s1[1], s2[1]], color=AMBER, lw=3, zorder=2)
    for x, y in (s1, s2):
        ax.text(x, y, 'S', ha='center', va='center', weight='bold', color=AMBER,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1.5}, zorder=5)


intra = [(.6, 2.55), (1.5, 2.55), (2.4, 2.55), (3.3, 2.55),
         (3.3, 1.35), (2.4, 1.35), (1.5, 1.35), (.6, 1.35)]
chain(intra, BLUE)
bridge(intra[1], intra[6], (1.5, 2.13), (1.5, 1.77))
ax.text(2, 2.98, 'Intrachain: one chain', ha='center', weight='bold', color=BLUE)
ax.text(2, .88, '8 residues; 7 peptide bonds', ha='center', color=INK)
ax.text(2, .53, 'An extra bridge joins side chains 2 and 7.', ha='center', size=11, color=INK)

upper = [(6, 2.55), (7, 2.55), (8, 2.55), (9, 2.55)]
lower = [(6, 1.35), (7, 1.35), (8, 1.35), (9, 1.35)]
chain(upper, BLUE)
chain(lower, GREEN)
bridge(upper[1], lower[2], (7.35, 2.13), (7.65, 1.77))
ax.text(7.5, 2.98, 'Interchain: two chains', ha='center', weight='bold', color=BLUE)
ax.text(7.5, .88, '4 + 4 residues; 3 + 3 peptide bonds', ha='center', color=INK)
ax.text(7.5, .53, 'An extra bridge joins the two backbones.', ha='center', size=11, color=INK)
ax.text(5, .1, 'Original connectivity illustrations • invented chains • no molecular scale or measured structure',
        ha='center', size=10, color='#56616d')
assert len(intra) - 1 == 7
assert len(upper) - 1 + len(lower) - 1 == 6
fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
