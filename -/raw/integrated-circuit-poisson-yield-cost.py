"""Illustrative independent-defect yield and wafer output, not measured data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5. Run from _media;
output uses this script's basename. The edge correction is approximate.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                         'axes.spines.top': False, 'axes.spines.right': False})
    density = .005  # fatal defects per square millimetre, chosen assumption
    diameter = 200.  # mm
    cost = 1000.  # arbitrary cost units per processed wafer
    area = np.linspace(10, 250, 600)
    yield_fraction = np.exp(-density * area)
    area_only = np.pi * diameter**2 / (4 * area)
    edge_approx = area_only - np.pi * diameter / np.sqrt(2 * area)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 5.2), dpi=120)
    fig.patch.set_facecolor('white')
    fig.suptitle('Larger dies: fewer fit, and fewer survive',
                 fontsize=17, weight='bold', y=.97)
    left.plot(area, yield_fraction, color='#235789', lw=2.5)
    marks = np.array([25., 100., 200.])
    left.scatter(marks, np.exp(-density * marks), color='#235789', zorder=3)
    for a, offset in zip(marks, [(8, -2), (8, 10), (-14, 16)]):
        left.annotate(f'{a:g} mm²: {np.exp(-density*a):.3f}',
                      (a, np.exp(-density*a)), xytext=offset,
                      textcoords='offset points', fontsize=10,
                      ha='right' if a == 200 else 'left')
    left.set(xlim=(0, 260), ylim=(0, 1.03), xlabel='Die area A (mm²)',
             ylabel='Probability of no fatal defect Y', title=r'$Y=\exp(-DA)$')
    left.text(.06, .12, 'Chosen D = 0.005 mm⁻²\nUniform independent fatal defects',
              transform=left.transAxes, fontsize=10,
              bbox={'facecolor': 'white', 'edgecolor': '#d3dce4', 'pad': 7})
    right.plot(area, area_only * yield_fraction, color='#bd631c', lw=2,
               linestyle='--', label='Area-only gross count × Y')
    right.plot(area, edge_approx * yield_fraction, color='#235789', lw=2.5,
               label='Edge approximation × Y')
    a = 100.
    y = np.exp(-density * a)
    n = np.pi * diameter**2 / (4 * a) - np.pi * diameter / np.sqrt(2 * a)
    good = n * y
    right.scatter([a], [good], color='#235789', zorder=3)
    right.annotate(f'A = 100 mm²\nGross ≈ {n:.2f}\nGood ≈ {good:.2f}\nCost/good ≈ {cost/good:.3f} units',
                   (a, good), xytext=(120, 390), fontsize=10,
                   arrowprops={'arrowstyle': '->', 'color': '#235789'},
                   bbox={'facecolor': 'white', 'edgecolor': '#d3dce4', 'pad': 6})
    right.set(xlim=(0, 260), ylim=(0, 1250), xlabel='Die area A (mm²)',
              ylabel='Expected good dies per wafer', title='200 mm diameter wafer')
    right.legend(loc='upper right', frameon=False, fontsize=9)
    for ax in (left, right):
        ax.grid(alpha=.18)
    fig.text(.5, .035, 'Illustrative model · wafer cost = 1000 units · edge count approximate · no separation lanes or packaging losses',
             ha='center', fontsize=9, color='#344353')
    fig.subplots_adjust(left=.075, right=.98, bottom=.18, top=.81, wspace=.32)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
