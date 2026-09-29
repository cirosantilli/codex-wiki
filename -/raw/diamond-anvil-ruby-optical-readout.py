"""Draw an original functional diamond-anvil/ruby readout, not historical dimensions.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the output is written into the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon, Rectangle
import numpy as np


BLUE = '#246c9a'
RED = '#b72e55'
INK = '#243648'


def main():
    plt.rcParams.update({'font.size': 11, 'text.color': INK, 'axes.labelcolor': INK})
    fig = plt.figure(figsize=(12, 7), facecolor='white')
    ax = fig.add_axes((0.015, 0.08, 0.97, 0.84))
    ax.set(xlim=(0, 12), ylim=(0, 8))
    ax.axis('off')
    fig.suptitle('Diamond-anvil cell: load, light and a local pressure signal', fontsize=17, y=0.98)

    def arrow(start, end, color=INK, width=1.7, style='-|>'):
        ax.annotate('', xy=end, xytext=start,
                    arrowprops={'arrowstyle': style, 'color': color, 'lw': width})

    def label(text, xy, at, color=INK, align='left'):
        ax.annotate(text, xy=xy, xytext=at, color=color, ha=align, va='center',
                    arrowprops={'arrowstyle': '-', 'color': color, 'lw': 1})

    def box(x, y, w, h, text, color='#eff3f6'):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.05',
                                   facecolor=color, edgecolor=INK, lw=1.1))
        ax.text(x+w/2, y+h/2, text, ha='center', va='center')

    upper = [(1.7, 5.8), (4.3, 5.8), (3.35, 4.15), (2.65, 4.15)]
    lower = [(2.65, 3.65), (3.35, 3.65), (4.3, 2), (1.7, 2)]
    for vertices in (upper, lower):
        ax.add_patch(Polygon(vertices, facecolor='#e8f5fa', edgecolor=BLUE, lw=2))
    for left, width in ((0.9, 1.75), (3.35, 1.75)):
        ax.add_patch(Rectangle((left, 3.65), width, 0.5, facecolor='#c6cbd0',
                               edgecolor=INK, lw=1.2, hatch='///'))
    ax.add_patch(Rectangle((2.65, 3.65), 0.7, 0.5, facecolor='#fff5d6', edgecolor=INK))
    ax.add_patch(Ellipse((3.16, 3.91), 0.18, 0.25, facecolor=BLUE))
    ax.add_patch(Ellipse((2.90, 3.88), 0.14, 0.17, facecolor=RED))
    label('Ruby sensor', (2.90, 3.9), (0.15, 4.9), RED)
    label('Gasket', (1.5, 3.85), (0.15, 3.08))
    label('Sample + medium\n(NaCl during calibration)', (3.2, 3.8), (4.0, 2.95))
    label('Flat culet', (3.34, 4.16), (4.5, 4.85))
    ax.text(3, 5.30, 'Diamond', ha='center', color=BLUE)
    ax.text(3, 2.43, 'Diamond', ha='center', color=BLUE)
    arrow((1.2, 6.8), (1.2, 5.88), width=3)
    arrow((1.2, 1.0), (1.2, 1.91), width=3)
    ax.text(0.70, 7.02, 'Load F', fontsize=12)
    ax.text(0.70, 0.65, 'Load F', fontsize=12)
    box(2.12, 6.74, 1.76, 0.64, 'Excitation light', '#eef6e9')
    arrow((3, 6.67), (3, 5.9), '#4d8b40', 2.3)
    arrow((3, 5.08), (2.9, 4.0), '#4d8b40', 2.3)
    arrow((2.9, 3.76), (3, 1.65), RED, 2.1)
    ax.add_patch(Ellipse((3, 1.48), 0.78, 0.16, facecolor='#e8f5fa', edgecolor=BLUE, lw=1.5))
    ax.plot([3, 3, 7.0], [1.35, 0.93, 0.93], color=RED, lw=2)
    arrow((5.5, 0.93), (7.02, 0.93), RED, 2.1)
    ax.text(3.5, 1.26, 'Collected fluorescence', color=RED)
    box(7.1, 0.5, 4.1, 0.85, 'Excitation rejection\n+ monochromator + photodetector')
    arrow((9.15, 1.43), (9.15, 2.21))
    ax.text(9.15, 1.82, 'Scan wavelength', ha='center', va='center')

    spec = fig.add_axes((0.635, 0.39, 0.31, 0.24), facecolor='white')
    x = np.linspace(0, 1, 500)
    for center, color, ls in ((0.28, '#6f7d87', '--'), (0.67, RED, '-')):
        spec.plot(x, np.exp(-0.5*((x-center)/0.048)**2), color=color, lw=2, ls=ls)
    spec.set(xlim=(0, 1), ylim=(0, 1.36), xticks=[0.28, 0.67],
             xticklabels=[r'$\lambda_0$', r'$\lambda$'], yticks=[],
             xlabel='Wavelength', ylabel='Signal')
    spec.annotate('', xy=(0.67, 1.18), xytext=(0.28, 1.18),
                  arrowprops={'arrowstyle': '<->', 'color': INK})
    spec.text(0.475, 1.25, r'$\Delta\lambda$', ha='center')
    spec.spines[['top', 'right']].set_visible(False)
    ax.text(9.1, 5.76, 'Fit the same R₁ line', ha='center', fontsize=13)
    box(7.1, 6.27, 4.1, 0.94, 'Shift + calibration + T + stress checks\n→ inferred local pressure', '#f6f0e3')
    arrow((9.15, 5.94), (9.15, 6.2))
    fig.text(0.5, 0.035, 'Functional arrangement and schematic spectra; no measured dimensions or calibration data.',
             ha='center', fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), dpi=100, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
