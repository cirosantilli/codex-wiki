"""Draw original papain cleavage and constructed product counts.

Tested with Python 3.14 and matplotlib 3.10.7. Run from _media; PNG goes to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HEAVY = '#2466a6'
LIGHT = '#c96520'
BOND = '#a57400'
CUT = '#b5233d'
INK = '#253446'


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, ax = plt.subplots(figsize=(10, 6.3), dpi=110, facecolor='white')
    fig.subplots_adjust(left=.035, right=.98, bottom=.08, top=.89)
    ax.set(xlim=(0, 12), ylim=(0, 7))
    ax.axis('off')
    fig.suptitle('Papain cuts the backbones; crosslinks stay with their fragments',
                 fontsize=16, color=INK, y=.97)

    def line(xs, ys, color, width=5):
        ax.plot(xs, ys, color=color, linewidth=width, solid_capstyle='round')

    def arm(x, y):
        line([x, x], [y, y+1.6], HEAVY)
        line([x-.55, x-.55], [y+.18, y+1.6], LIGHT)
        line([x-.55, x], [y+.3, y+.3], BOND, 2.5)
        ax.text(x-.25, y+1.9, '1 binding site', ha='center', fontsize=10, color=INK)

    def stem(x, y):
        for dx in [-.28, .28]:
            line([x+dx, x+dx], [y, y+1.25], HEAVY)
        line([x-.28, x+.28], [y+1.1, y+1.1], BOND, 2.5)

    # Backbone layout is deliberately unrolled, to expose which bonds are cut.
    for x in [1.65, 2.55]:
        line([x, x], [3.6, 6.0], HEAVY)
        lightx = x-.43 if x < 2 else x+.43
        line([lightx, lightx], [4.85, 6.0], LIGHT)
        line([lightx, x], [4.97, 4.97], BOND, 2.5)
        line([x-.23, x+.23], [4.62-.13, 4.62+.13], CUT, 3)
    line([1.65, 2.55], [4.24, 4.24], BOND, 2.5)
    ax.text(2.1, 6.34, 'Intact IgG', ha='center', color=INK, fontsize=14)
    ax.text(2.1, 3.02, '2 continuous H backbones\n+ 2 complete L chains',
            ha='center', color=INK, fontsize=10)
    ax.annotate('two backbone cuts', xy=(2.55, 4.62), xytext=(3.3, 5.42),
                ha='left', fontsize=10, color=CUT,
                arrowprops={'arrowstyle': '->', 'color': CUT})
    ax.annotate('', xy=(6.1, 4.37), xytext=(4.55, 4.37),
                arrowprops={'arrowstyle': '->', 'lw': 2, 'color': INK})
    ax.text(5.2, 4.64, 'papain', ha='center', color=INK, fontsize=11)
    arm(7.05, 4.0)
    arm(9.0, 4.0)
    stem(10.85, 4.0)
    ax.text(6.8, 3.48, 'Fab', ha='center', color=INK, fontsize=14)
    ax.text(8.75, 3.48, 'Fab', ha='center', color=INK, fontsize=14)
    ax.text(10.85, 3.48, 'Fc', ha='center', color=INK, fontsize=14)
    ax.text(10.85, 5.65, '0 binding sites', ha='center', fontsize=10, color=INK)
    ax.text(9.0, 2.98, '6 backbone segments → 3 connected products',
            ha='center', color=INK, fontsize=11)
    ax.plot([.4, 11.6], [2.65, 2.65], color='#c8cdd3', linewidth=1)
    ax.text(6, 2.35, 'Constructed mixture: 5 pmol IgG, 60% completely digested',
            ha='center', color=INK, fontsize=13)
    boxes = [(1.85, 'Intact IgG', '2 pmol', '4 pmol sites', HEAVY),
             (5.85, 'Fab', '6 pmol', '6 pmol sites', LIGHT),
             (9.85, 'Fc', '3 pmol', '0 pmol sites', HEAVY)]
    for x, title, amount, sites, color in boxes:
        ax.add_patch(FancyBboxPatch((x-1.5, .85), 3, 1.12,
                     boxstyle='round,pad=.08,rounding_size=.12',
                     facecolor='white', edgecolor=color, linewidth=1.8))
        ax.text(x, 1.65, title+'  ·  '+amount, ha='center', va='center', color=color, fontsize=12)
        ax.text(x, 1.18, sites, ha='center', va='center', color=INK, fontsize=12)
    ax.text(6, .35, '11 pmol connected products   •   10 pmol binding sites retained in the ideal model',
            ha='center', color=INK, fontsize=11)
    fig.text(.5, .025, 'Schematic, not atomic structure. Gold: retained disulfides. Red: backbone cuts.\n'
             'Complete two-cut events only; small peptides and secondary cleavage excluded.',
             ha='center', fontsize=10, color=INK)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
