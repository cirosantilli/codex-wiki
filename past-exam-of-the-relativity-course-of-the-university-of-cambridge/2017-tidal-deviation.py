"""Render a local tidal-acceleration schematic to the working directory."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def main():
    angle = np.linspace(0, 2*np.pi, 16, endpoint=False)
    x, y = np.cos(angle), np.sin(angle)
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.9), dpi=120, facecolor='white')
    for ax in axes:
        ax.set_facecolor('white')
        ax.set_aspect('equal')
        ax.set(xlim=(-1.7, 1.7), ylim=(-1.3, 1.3))
        ax.axhline(0, color='0.85', lw=0.8)
        ax.axvline(0, color='0.85', lw=0.8)
        ax.scatter([0], [0], s=45, marker='+', color='black', zorder=5)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel('Radial separation')
        ax.set_ylabel('Transverse separation')
    axes[0].scatter(x, y, color='#245f91', s=18)
    axes[0].quiver(x, y, 2*x, -y, angles='xy', scale_units='xy',
                   scale=6, color='#b65f21', width=0.009)
    axes[0].set_title('Relative tidal acceleration', fontsize=12)
    axes[1].add_patch(Ellipse((0, 0), 2, 2, fill=False, ls='--',
                              ec='0.55', lw=1.2, label='Initial cloud'))
    axes[1].add_patch(Ellipse((0, 0), 2.72, 1.64, fill=False,
                              ec='#245f91', lw=2.4, label='Later cloud (schematic)'))
    axes[1].scatter(1.36*x, 0.82*y, color='#245f91', s=18)
    axes[1].set_title('Radial stretch, transverse compression', fontsize=12)
    axes[1].legend(loc='upper right',
                   fontsize=8, framealpha=0.95)
    fig.suptitle('Small freely falling laboratory outside a spherical mass', fontsize=12)
    fig.tight_layout()
    fig.savefig(Path('2017-tidal-deviation.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
