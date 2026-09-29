"""Original potential plot; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0.001, 1.8, 540)
    y = np.linspace(0.001, 0.999, 300)
    xx, yy = np.meshgrid(x, y)
    potential = 1 - 4 / np.pi * np.arctan2(np.sin(np.pi * yy), np.sinh(np.pi * xx))
    fig, ax = plt.subplots(figsize=(8.2, 4.6), dpi=120, facecolor='white', layout='constrained')
    field = ax.pcolormesh(xx, yy, potential, cmap='coolwarm', vmin=-1, vmax=1, shading='nearest', rasterized=True)
    levels = [-0.75, -0.5, 0, 0.5, 0.75, 0.9]
    contours = ax.contour(xx, yy, potential, levels=levels, colors='#303030', linewidths=0.7)
    ax.clabel(contours, inline=True, fontsize=9, fmt='%g')
    ax.plot([0, 0], [0, 1], color='#315b9c', linewidth=4)
    ax.plot([0, 1.8], [0, 0], color='#b63335', linewidth=4)
    ax.plot([0, 1.8], [1, 1], color='#b63335', linewidth=4)
    ax.set(xlim=(0, 1.8), ylim=(0, 1), xlabel=r'$x/L$', ylabel=r'$y/L$', title='Bounded harmonic potential in a half-strip')
    ax.set_aspect('equal')
    colorbar = fig.colorbar(field, ax=ax, shrink=0.86, pad=0.035)
    colorbar.set_label(r'$V/V_0$')
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False, metadata={'Software': 'codex-wiki original mathematical plot'})
    plt.close(fig)


if __name__ == '__main__':
    main()
