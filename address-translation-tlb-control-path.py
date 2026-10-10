"""Draw a logical translation path; Python 3.14, matplotlib 3.10.7.

Run from _media; output is this script's basename with a .png extension.
The 12-bit, 64-byte-page example is an original toy model, not hardware timing.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, ax = plt.subplots(figsize=(11, 7), dpi=100, facecolor='white')
    ax.set(xlim=(0, 11), ylim=(0, 7)); ax.axis('off')
    blue, green, amber, red = '#e9f2ff', '#e7f4ec', '#fff1d9', '#fbe9e8'

    def box(x, y, w, h, text, color=blue):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03',
                                   facecolor=color, edgecolor='#486076', linewidth=1.2))
        ax.text(x+w/2, y+h/2, text, ha='center', va='center', linespacing=1.4)

    def arrow(a, b, text=None, xy=None):
        ax.annotate('', xy=b, xytext=a,
                    arrowprops={'arrowstyle': '-|>', 'color': '#34485b', 'lw': 1.5})
        if text:
            ax.text(*(xy if xy else ((a[0]+b[0])/2, (a[1]+b[1])/2)), text,
                    ha='center', va='center', fontsize=10,
                    bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})

    ax.text(5.5, 6.72, 'Translate the address, check access, then read the data',
            ha='center', fontsize=16, weight='bold')
    ax.text(5.5, 6.37, 'Logical dependencies for an original single-byte read; no cycle timing implied',
            ha='center', fontsize=11, color='#43586d')
    box(.3, 5.25, 2.8, .8, 'Process A • read VA 0x12D\npage 4 + offset 45')
    box(4.0, 5.25, 2.8, .8, 'TLB lookup\ncurrent context + page 4')
    arrow((3.1, 5.65), (4, 5.65))
    box(7.8, 5.15, 2.85, 1.0, 'Resolve page-table entry\nhardware walk OR\nOS refill handler', amber)
    arrow((6.8, 5.65), (7.8, 5.65), 'miss')
    box(4, 3.55, 2.8, .9, 'Resident mapping\nframe 13 • read permitted', green)
    arrow((5.4, 5.25), (5.4, 4.45), 'hit', (5.75, 4.85))
    arrow((9.22, 5.15), (6.8, 4.1), 'resident + permitted:\nrefill and retry', (8.7, 4.58))
    box(8, 2.9, 2.65, 1.05, 'Unavailable or denied?\nOS policy decides:\nsupply contents or reject', red)
    arrow((9.3, 5.15), (9.3, 3.95))
    box(.3, 3.55, 2.8, .9, 'Permission failure\nrequested read blocked', red)
    arrow((4, 4), (3.1, 4), 'deny', (3.55, 4.3))
    box(4, 2.05, 2.8, .8, 'Physical address\n13 × 64 + 45 = 0x36D', green)
    arrow((5.4, 3.55), (5.4, 2.85), 'allow', (5.76, 3.2))
    box(4, .6, 2.8, .8, 'Read requested byte\ndata cache or main memory', green)
    arrow((5.4, 2.05), (5.4, 1.4))
    box(.3, .6, 2.8, 1.5, 'TLB caches:\nmapping + attributes\n\nData cache stores:\nrequested contents', '#f4f5f7')
    ax.text(8.98, 1.55, 'Same VA in process B:\npage 4 → frame 9\n9 × 64 + 45 = 0x26D',
            ha='center', va='center', fontsize=11, linespacing=1.5)
    ax.text(5.5, .12, 'A TLB hit does not guarantee permission or a data-cache hit.',
            ha='center', fontsize=11, weight='bold')
    fig.subplots_adjust(left=.01, right=.99, bottom=.01, top=.99)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
