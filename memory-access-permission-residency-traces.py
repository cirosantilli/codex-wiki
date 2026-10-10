"""Four independent toy traces; Python 3.14, matplotlib 3.10.7.

Run from _media; output is this script's basename with a .png extension.
All starting states and outcomes are illustrative, not measured hardware data.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, ax = plt.subplots(figsize=(11, 6.7), dpi=100, facecolor='white')
    ax.set(xlim=(0, 11), ylim=(0, 6.7)); ax.axis('off')
    ax.text(5.5, 6.35, 'Residency and permission produce different access traces',
            ha='center', fontsize=16, weight='bold')
    ax.text(5.5, 5.98, 'Process A • 12-bit virtual addresses • 64-byte pages • offset 45 in every row',
            ha='center', fontsize=11, color='#43586d')
    for x, label in [(1.55, 'REQUEST AND INITIAL STATE'), (5.25, 'LOOKUP AND CONTROL'), (9.05, 'RESULT')]:
        ax.text(x, 5.45, label, ha='center', fontsize=10, weight='bold')

    rows = [
        ('Read 0x12D • page 4\nresident, frame 13\nread-only • TLB empty',
         'TLB miss → entry lookup\nresident and permitted\nrefill; continue read',
         'Read PA 0x36D\nno nonresident fault', '#e7f4ec'),
        ('Write 0x12D • page 4\nresident, frame 13\nread-only • TLB populated',
         'TLB hit → permission check\nwrite denied\nno target-byte write',
         'Protection failure\nresident byte unchanged', '#fbe9e8'),
        ('Read 0x16D • page 5\nread permitted\nnonresident • TLB empty',
         'TLB miss → nonresident fault\nOS loads into free frame 2\nupdate mapping; retry read',
         'Then read PA 0x0AD\ncontents supplied first', '#fff1d9'),
        ('Read 0x1AD • page 6\nno authorized mapping\nTLB empty',
         'TLB miss → invalid mapping\nOS rejects in this model\nno data read',
         'Access rejected\nfree space is insufficient', '#fbe9e8'),
    ]
    for i, (start, path, result, color) in enumerate(rows):
        y = 4.22 - i * 1.13
        for x, w, text, fill in [(.22, 2.7, start, '#f0f4fa'), (3.65, 3.2, path, color), (7.5, 3.15, result, color)]:
            ax.add_patch(FancyBboxPatch((x, y), w, .9, boxstyle='round,pad=0.025',
                                       facecolor=fill, edgecolor='#526579', linewidth=1.1))
            ax.text(x+w/2, y+.45, text, ha='center', va='center', linespacing=1.4)
        for a, b in [(2.95, 3.62), (6.88, 7.47)]:
            ax.annotate('', xy=(b, y+.45), xytext=(a, y+.45),
                        arrowprops={'arrowstyle': '-|>', 'color': '#34485b', 'lw': 1.5})
    ax.text(5.5, .37, 'Independent starting states • no copy-on-write • stale translations invalidated',
            ha='center', fontsize=11)
    ax.text(5.5, .10, 'Logical outcomes; fault names and check order depend on architecture.',
            ha='center', fontsize=10, color='#43586d')
    fig.subplots_adjust(left=.01, right=.99, bottom=.01, top=.99)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
