"""Original open-mitosis cartoon; Python 3.14 / matplotlib 3.10.7.

Run from _media. Hypothetical diploid 2n=4; no measured geometry or timing.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, FancyArrowPatch

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig = plt.figure(figsize=(12, 7.4), dpi=100, facecolor='white')
fig.text(.5, .956, 'Mitosis: allocate the copies made earlier in S phase',
         ha='center', weight='bold', fontsize=19, color='#18354b')
fig.text(.5, .914, 'Hypothetical animal cell: two homologous pairs, A / a and B / b (2n = 4)',
         ha='center', fontsize=12)
colors = ['#2456a6', '#cc512d', '#2456a6', '#cc512d']
names = ['A', 'a', 'B', 'b']
sizes = [.23, .23, .16, .16]

def panel(rect, heading):
    ax = fig.add_axes(rect)
    ax.set(xlim=(-1.15, 1.15), ylim=(-1.03, 1.12), aspect='equal')
    ax.axis('off')
    ax.text(0, 1.07, heading, ha='center', va='center', weight='bold', fontsize=14)
    return ax

def cell(ax):
    ax.add_patch(Ellipse((0, 0), 2.12, 1.62, facecolor='#f8fafc',
                         edgecolor='#5c6f80', lw=1.6))

def replicated(ax, x, y, height, color, label):
    # Each of the two continuous strokes represents one sister chromatid.
    for sign in [-1, 1]:
        ax.plot([x+sign*.09, x+sign*.025, x+sign*.09],
                [y+height, y, y-height], color=color, lw=4, solid_capstyle='round', zorder=4)
        ax.plot(x+sign*.025, y, 'o', ms=4, color='#253447', zorder=5)
    ax.plot([x-.025, x+.025], [y, y], color='#253447', lw=2.4, zorder=5)
    ax.text(x+.14, y, label, va='center', color=color, weight='bold', fontsize=10, zorder=6)

def single(ax, x, y, height, color, label, direction):
    ax.plot([x-direction*.095, x, x-direction*.095],
            [y+height, y, y-height], color=color, lw=4, solid_capstyle='round', zorder=4)
    ax.plot(x, y, 'o', color='#253447', ms=4, zorder=5)
    ax.text(x-direction*.16, y, label, ha='center', va='center',
            color=color, weight='bold', fontsize=10)

def spindle(ax, targets):
    for pole in [-.9, .9]:
        ax.plot(pole, 0, 'o', ms=8, color='#318f75', zorder=5)
        for x, y in targets(pole):
            ax.plot([pole, x], [0, y], color='#71b49c', lw=1.3, zorder=2)

def note(ax, text):
    ax.text(0, -.94, text, ha='center', va='center', fontsize=11, linespacing=1.45)

ax = panel([.035, .49, .285, .36], '1  Prophase')
cell(ax)
ax.add_patch(Ellipse((0, 0), 1.45, 1.23, facecolor='none', edgecolor='#8595b7', lw=1.5, ls='--'))
for x, y, h, color, name in zip([-.36, .28, -.3, .3], [.28, .28, -.28, -.28], sizes, colors, names):
    replicated(ax, x, y, h, color, name)
ax.plot([-.92, .92], [0, 0], 'o', color='#318f75', ms=7)
note(ax, '4 replicated chromosomes\n8 sister chromatids')

ax = panel([.3575, .49, .285, .36], '2  Metaphase')
cell(ax)
ys = [.48, .16, -.17, -.48]
spindle(ax, lambda pole: [( -.025 if pole < 0 else .025, y) for y in ys])
ax.plot([0, 0], [-.74, .74], color='#aab3c0', ls=':', lw=1)
for y, h, color, name in zip(ys, [.13, .13, .095, .095], colors, names):
    replicated(ax, 0, y, h, color, name)
note(ax, 'Sisters face opposite poles\nStill 4 chromosomes, 8 chromatids')

ax = panel([.68, .49, .285, .36], '3  Anaphase')
cell(ax)
spindle(ax, lambda pole: [( -.52 if pole < 0 else .52, y) for y in ys])
for direction in [-1, 1]:
    for y, h, color, name in zip(ys, [.13, .13, .095, .095], colors, names):
        single(ax, direction*.52, y, h, color, name, direction)
note(ax, '8 daughter chromosomes in one cell\n4 allocated toward each pole')

ax = panel([.25, .075, .285, .34], '4  Telophase')
cell(ax)
for direction in [-1, 1]:
    ax.add_patch(Ellipse((direction*.52, 0), .75, 1.22, facecolor='#eef2fa',
                         edgecolor='#8595b7', lw=1.5))
    for y, h, color, name in zip([.35, .12, -.12, -.35], [.08]*4, colors, names):
        single(ax, direction*.52, y, h, color, name, direction)
note(ax, 'Two daughter nuclei\nOne cell before cytokinesis finishes')

ax = panel([.665, .075, .30, .34], '5  After cytokinesis')
for direction in [-1, 1]:
    ax.add_patch(Ellipse((direction*.56, 0), .96, 1.6, facecolor='#f8fafc',
                         edgecolor='#5c6f80', lw=1.6))
    ax.add_patch(Ellipse((direction*.56, 0), .7, 1.2, facecolor='#eef2fa',
                         edgecolor='#8595b7', lw=1.5))
    for y, color, name in zip([.35, .12, -.12, -.35], colors, names):
        single(ax, direction*.56, y, .08, color, name, direction)
note(ax, 'Each daughter: 4 chromosomes\n4 double-stranded DNA molecules')

fig.text(.055, .354, 'Reading the cartoon', weight='bold', fontsize=12, color='#18354b')
fig.text(.055, .312, 'Blue / orange: homologues\nLong / short: pair identity\nDark dot: centromere region\nGreen: selected spindle fibers',
         fontsize=11, va='top', linespacing=1.6)
for start, end in [((.32, .68), (.355, .68)), ((.644, .68), (.678, .68)),
                   ((.83, .475), (.43, .425)), ((.55, .255), (.645, .255))]:
    fig.add_artist(FancyArrowPatch(start, end, transform=fig.transFigure,
                                  arrowstyle='-|>', mutation_scale=15, lw=1.5, color='#526879'))
fig.text(.5, .026, 'Original schematic, not a time-lapse recording. Simplified strokes persist so chromosome identities remain visible.',
         ha='center', fontsize=10, color='#526879')
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
