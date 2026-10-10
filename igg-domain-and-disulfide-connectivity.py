"""Draw an original IgG connectivity schematic; tested with Python 3.14.

Requires the repository's matplotlib 3.10.7. Run from _media; writes PNG to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse

HEAVY = '#2466a6'
LIGHT = '#c96520'
BOND = '#a57400'
INK = '#253446'


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, ax = plt.subplots(figsize=(10, 6.7), dpi=110, facecolor='white')
    fig.subplots_adjust(left=.035, right=.97, bottom=.07, top=.89)
    ax.set(xlim=(0, 10), ylim=(-.4, 6.4))
    ax.axis('off')
    fig.suptitle('IgG: four chains, two binding sites', fontsize=19, color=INK, y=.97)
    ax.text(5, 6.12, 'Unrolled connectivity schematic • positions are not atomic coordinates',
            ha='center', fontsize=11, color=INK)

    def domain(x, y, label, color):
        ax.add_patch(FancyBboxPatch((x-.4, y-.34), .8, .68,
                     boxstyle='round,pad=.04,rounding_size=.15',
                     facecolor='white', edgecolor=color, linewidth=2.4, zorder=3))
        ax.text(x, y, label, ha='center', va='center', color=color, fontsize=14, zorder=4)

    for x, name in [(3.5, 'H₁'), (6.5, 'H₂')]:
        ax.plot([x, x], [5.47, .45], color=HEAVY, linewidth=4, solid_capstyle='round')
        for y, label in [(5.05, r'$V_H$'), (3.9, r'$C_{H1}$'),
                         (1.8, r'$C_{H2}$'), (.8, r'$C_{H3}$')]:
            domain(x, y, label, HEAVY)
        ax.text(x, 5.62, 'N', ha='center', color=HEAVY, fontweight='bold')
        ax.text(x, .18, 'C', ha='center', color=HEAVY, fontweight='bold')
        ax.text(x, -.19, name+'  heavy chain', ha='center', color=HEAVY, fontsize=11)
    for x, name in [(2, 'L₁'), (8, 'L₂')]:
        ax.plot([x, x], [5.47, 3.45], color=LIGHT, linewidth=4, solid_capstyle='round')
        domain(x, 5.05, r'$V_L$', LIGHT)
        domain(x, 3.9, r'$C_L$', LIGHT)
        ax.text(x, 5.62, 'N', ha='center', color=LIGHT, fontweight='bold')
        ax.text(x, 3.13, 'C', ha='center', color=LIGHT, fontweight='bold')
        ax.text(x, 2.73, name+'  light chain', ha='center', color=LIGHT, fontsize=11)
    for a, b in [(2, 3.5), (6.5, 8)]:
        ax.plot([a, b], [3.5, 3.5], color=BOND, linewidth=3, zorder=5)
        ax.text((a+b)/2, 3.28, 'S—S', ha='center', color=BOND, fontsize=11)
    ax.plot([3.5, 6.5], [2.72, 2.72], color=BOND, linewidth=3, zorder=5)
    ax.text(5, 2.82, 'S—S', ha='center', color=BOND)
    ax.text(5, 2.28, 'hinge: heavy–heavy crosslinks', ha='center', fontsize=10, color=INK)
    for x in [2.75, 7.25]:
        ax.add_patch(Ellipse((x, 5.05), 2.6, 1.0, fill=False,
                            edgecolor=INK, linestyle='--', linewidth=1.2, zorder=2))
    ax.text(.15, 5.03, 'one\nsite', ha='center', va='center', color=INK, fontsize=11)
    ax.text(9.6, 5.03, 'one\nsite', ha='center', va='center', color=INK, fontsize=11)
    ax.text(5, 4.65, 'paired variable\ndomains', ha='center', va='center', color=INK, fontsize=11)
    ax.text(5, 1.29, 'Fc\nportions', ha='center', va='center', color=INK, fontsize=11)
    fig.text(.5, .025, 'Colored paths: peptide backbones   |   Gold: interchain disulfides (multiplicity schematic)\n'
             'N and C: chain termini   •   Intrachain disulfides omitted',
             ha='center', fontsize=10, color=INK)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
