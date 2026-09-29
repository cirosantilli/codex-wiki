"""Schematic spheroid rotation diagram. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes paper-72-rotation-support.png to the caller's CWD; honors MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def main():
    fig, ax = plt.subplots(figsize=(8.5, 5.2), dpi=150, facecolor='white')
    for beta, color in [(0, '#222222'), (0.2, '#9b3d19'), (0.4, '#6663ae')]:
        e = np.linspace(beta, 0.8, 450)
        ax.plot(e, np.sqrt((e-beta)/(1-e)), color=color, lw=2,
                label=rf'$\beta={beta:g}$ (approximate model)')
    for center, width, height, angle, color, label in [
        ((0.3, 0.2), 0.48, 0.32, 0, '#316c9f', 'Giant ellipticals'),
        ((0.4, 0.85), 0.47, 0.53, 35, '#9b4f9d', 'Lower-luminosity ellipticals'),
        ((0.32, 0.67), 0.44, 0.42, 30, '#27966b', 'Classical spiral bulges')]:
        ax.add_patch(Ellipse(center, width, height, angle=angle,
                             facecolor=color, edgecolor=color, alpha=0.19, label=label))
    ax.set(xlim=(0, 0.8), ylim=(0, 2.05), xlabel=r'Ellipticity $e=1-b/a$',
           ylabel=r'Rotation support $v/\sigma$',
           title='Rotation, random-motion anisotropy and spheroid flattening')
    ax.grid(alpha=0.2)
    ax.legend(loc='upper left', fontsize=8.8, framealpha=0.94)
    fig.text(0.5, 0.018, 'Shaded loci are schematic, not data. Observed projection and aperture conventions matter.',
             ha='center', fontsize=9)
    fig.tight_layout(rect=(0, 0.045, 1, 1))
    fig.savefig('paper-72-rotation-support.png', facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
