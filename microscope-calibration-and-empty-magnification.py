"""Original microscope calibration and display-enlargement diagram.

Python 3.14, NumPy and Matplotlib only. All dimensions are toy values.
Run from _media to emit the generator basename with a .png suffix.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def blurred_pair(x):
    """Stipulated Gaussian pair; not an Airy model or measured data."""
    separation, sigma = 0.8, 0.6
    return (np.exp(-0.5 * ((x - separation / 2) / sigma) ** 2)
            + np.exp(-0.5 * ((x + separation / 2) / sigma) ** 2)) / 2


def main():
    plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
    fig = plt.figure(figsize=(11, 7.2), dpi=100, facecolor='white')
    grid = fig.add_gridspec(2, 2, height_ratios=[1, 1.15], hspace=0.7, wspace=0.27)
    scale = fig.add_subplot(grid[0, :])
    scale.set_xlim(-2, 42)
    scale.set_ylim(-1.25, 2.1)
    scale.axis('off')
    scale.set_title('Calibration: compare two scales in the same view', loc='left', pad=15,
                    fontsize=14, fontweight='bold')
    for i in range(41):
        scale.plot([i, i], [0.75, 0.75 + (0.3 if i % 10 == 0 else 0.15)],
                   color='#2868ac', linewidth=1.2)
        if i % 10 == 0:
            scale.text(i, 1.15, str(i), ha='center', color='#2868ac')
    scale.plot([0, 40], [0.75, 0.75], color='#2868ac')
    scale.text(0, 1.7, 'Eyepiece intervals (arbitrary units)', color='#2868ac')
    for i in range(11):
        x = 4 * i
        scale.plot([x, x], [0.1, -0.1 if i % 5 else -0.23],
                   color='#207a47', linewidth=1.5)
        if i % 5 == 0:
            scale.text(x, -0.5, f'{10*i} μm', ha='center', color='#207a47')
    scale.plot([0, 40], [0.1, 0.1], color='#207a47')
    for x in [0, 40]:
        scale.plot([x, x], [-0.25, 1.05], '--', color='#757575', linewidth=1)
    scale.annotate('', xy=(0, 0.42), xytext=(18, 0.42),
                   arrowprops={'arrowstyle': '<->', 'lw': 2, 'color': '#c34737'})
    scale.text(9, 0.47, '18 intervals → 45 μm', ha='center', va='bottom', color='#c34737')
    scale.text(20, -1.05, '100 μm / 40 intervals = 2.5 μm per interval  •  Toy values, not laboratory readings',
               ha='center', fontsize=11)
    x = np.linspace(-2, 2, 601)
    profile = blurred_pair(x)
    for col, q in enumerate([1, 2]):
        ax = fig.add_subplot(grid[1, col])
        ax.set_facecolor('white')
        ax.plot(q*x, profile, color='#734ba1', lw=2.5)
        ax.fill_between(q*x, profile, color='#734ba1', alpha=0.12)
        for source in [-0.4, 0.4]:
            ax.axvline(q*source, color='#777777', linestyle=':', lw=1)
        ax.set_xlim(-4, 4)
        ax.set_ylim(0, 1.12)
        ax.set_xticks([-4, -2, 0, 2, 4])
        ax.set_yticks([0, 0.5, 1])
        ax.set_xlabel('Display coordinate (arbitrary units)')
        ax.set_ylabel('Normalized signal' if col == 0 else '')
        ax.set_title('Original display' if q == 1 else 'Same image enlarged 2 times', fontsize=12)
        ax.spines[['top', 'right']].set_visible(False)
        ax.text(0.5, 0.93, 's = 0.8,  b = 0.6' if q == 1 else 's = 1.6,  b = 1.2',
                transform=ax.transAxes, ha='center')
    fig.suptitle('Measuring size and revealing detail are different tasks', fontsize=16, y=0.975)
    fig.text(0.5, 0.059, 'Both separation s and blur width b double: s/b stays 4/3. No extra detail appears.',
             ha='center', fontsize=11)
    fig.text(0.5, 0.022, 'Stipulated Gaussian blur (b = σ), not an exact diffraction profile or a resolution test.',
             ha='center', fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.16, top=0.86)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
