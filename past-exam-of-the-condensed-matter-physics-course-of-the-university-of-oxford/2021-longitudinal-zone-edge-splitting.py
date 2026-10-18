"""Illustrate longitudinal boundary splitting with equal-spring chain models.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
The only output is the same-basename PNG in the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    q = np.linspace(0.0, 1.0, 501)
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6), layout='constrained')
    for ax, masses, title in zip(
        axes,
        ((1.0, 1.0), (27.0 / 29.0, 31.0 / 29.0)),
        ('Identical sites: contact at X', 'Different masses: split at X'),
        strict=True,
    ):
        m1, m2 = masses
        diagonal = 1.0 / m1 + 1.0 / m2
        discriminant = np.maximum(
            diagonal**2 - 4.0 / (m1 * m2) * np.sin(np.pi * q / 2.0)**2,
            0.0,
        )
        acoustic = np.sqrt(np.maximum(diagonal - np.sqrt(discriminant), 0.0))
        optical = np.sqrt(diagonal + np.sqrt(discriminant))
        ax.plot(q, acoustic, color='#1265a8', lw=2.3, label='Acoustic')
        ax.plot(q, optical, color='#b23c24', lw=2.3, label='Optical')
        ax.scatter([1, 1], [acoustic[-1], optical[-1]], s=28, c=['#1265a8', '#b23c24'], zorder=3)
        ax.set(xlim=(0, 1.05), ylim=(0, 2.17), xlabel=r'$k/(2\pi/a)$', title=title)
        ax.set_xticks([0, 0.5, 1], [r'$\Gamma$', '0.5', 'X'])
        ax.grid(alpha=0.2)
        ax.spines[['top', 'right']].set_visible(False)
    axes[0].set_ylabel(r'Angular frequency $\omega/\sqrt{K/\overline{M}}$')
    axes[0].legend(frameon=False, loc='lower right')
    axes[1].text(0.04, 0.5, 'Mass ratio 27:31\nEqual effective springs', transform=axes[1].transAxes, fontsize=10)
    fig.suptitle('Illustrative longitudinal chain models; not measured crystal spectra', fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
