"""Functional TEM aperture selection, not a ray trace or measured apparatus.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media; writes the script basename with a .png extension to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


CENTRAL = '#1769aa'
DIFFRACTED = '#c26413'
GREY = '#687380'


def arrow(ax, start, end, color, **kwargs):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', lw=2.0, color=color, **kwargs))


def panel(ax, dark):
    ax.set_xlim(-2.5, 3.0)
    ax.set_ylim(0.0, 10.5)
    ax.axis('off')
    ax.set_title('Dark field' if dark else 'Bright field', fontsize=15, weight='bold')
    arrow(ax, (0, 10.1), (0, 9.4), GREY)
    ax.text(0.25, 9.85, 'Incident beam', fontsize=10, va='center')
    ax.add_patch(Rectangle((-1.3, 9.0), 2.6, 0.25,
                           facecolor='#e1e7e9', edgecolor=GREY))
    ax.text(-2.4, 9.13, 'Specimen', fontsize=10, va='center')
    arrow(ax, (0, 9.0), (0, 8.35), GREY)
    ax.add_patch(FancyBboxPatch((-1.3, 7.3), 2.6, 0.9,
                                boxstyle='round,pad=0.1',
                                facecolor='#f1f4f7', edgecolor=GREY))
    ax.text(0, 7.75, 'Objective lens\nangles → positions',
            ha='center', va='center', fontsize=10)
    ax.plot([0, 0], [7.2, 5.05], color=CENTRAL, lw=2.2)
    ax.plot([0.35, 1.65], [7.2, 5.05], color=DIFFRACTED, lw=2.2)
    ax.text(-0.15, 6.25, '0', color=CENTRAL, ha='right', fontsize=12)
    ax.text(1.1, 6.25, 'g', color=DIFFRACTED, fontsize=12)
    # Schematic cross-section of the physical aperture at a diffraction plane.
    ax.axhline(4.9, color='#bcc3ca', lw=1, ls=':', zorder=0)
    ax.text(-2.4, 5.45, 'Back focal\nplane', fontsize=10, va='center')
    passed = 1.65 if dark else 0.0
    rejected = 0.0 if dark else 1.65
    opening = 0.28
    for lo, hi in [(-1.1, passed - opening), (passed + opening, 2.35)]:
        ax.add_patch(Rectangle((lo, 4.72), hi - lo, 0.35,
                               facecolor=GREY, edgecolor=GREY, zorder=5))
    ax.scatter([0, 1.65], [4.9, 4.9], s=38,
               color=[CENTRAL, DIFFRACTED], zorder=6)
    ax.text(2.55, 4.9, 'Aperture', fontsize=10, va='center', rotation=90)
    ax.scatter([rejected], [4.47], marker='x', s=65, color='#a02d2d', zorder=7)
    ax.text(rejected - 0.12, 4.0, 'Blocked', color='#a02d2d',
            fontsize=10, ha='right' if dark else 'center')
    color = DIFFRACTED if dark else CENTRAL
    arrow(ax, (passed, 4.68), (passed, 3.35), color)
    ax.add_patch(FancyBboxPatch((-0.8, 2.45), 3.0, 0.7,
                                boxstyle='round,pad=0.1',
                                facecolor='white', edgecolor=color))
    ax.text(0.7, 2.8, 'Image relay', fontsize=11, ha='center', va='center')
    arrow(ax, (0.7, 2.35), (0.7, 1.65), color)
    ax.add_patch(Rectangle((-0.8, 0.85), 3.0, 0.65,
                           facecolor='#fff8ee' if dark else '#edf5fc',
                           edgecolor=color))
    ax.text(0.7, 1.18, 'Specimen image from g' if dark else 'Specimen image from 0',
            fontsize=10, color=color, ha='center', va='center')


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, axes = plt.subplots(1, 2, figsize=(10, 6.3), dpi=120, facecolor='white')
    panel(axes[0], dark=False)
    panel(axes[1], dark=True)
    fig.suptitle('The aperture selects a beam direction', fontsize=17, y=0.98)
    fig.text(0.5, 0.025, 'Functional paths only • 0: central beam; g: chosen diffracted beam • not to scale',
             ha='center', fontsize=10, color=GREY)
    fig.subplots_adjust(top=0.86, bottom=0.065, left=0.025, right=0.98, wspace=0.12)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
