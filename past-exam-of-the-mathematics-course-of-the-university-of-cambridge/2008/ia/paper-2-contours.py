"""Original contour sketches. Tested with Python 3.14.4 and root pyproject deps.
Run from the desired media output directory; writes only the PNG basename.
Honors any caller-supplied MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    axis = np.linspace(-1.7, 1.7, 901)
    x, y = np.meshgrid(axis, axis)
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.3), layout='constrained')
    for ax, b in zip(axes, [0.5, 2.0]):
        f = x*x + y*y - 0.5*(x**4 + y**4) - b*x*x*y*y
        saddle = 0.5 if b < 1 else 1/(1+b)
        maximum = 1/(1+b) if b < 1 else 0.5
        levels = [-0.65, 0.0, 0.15, 0.7*saddle, saddle,
                  (saddle+maximum)/2, 0.97*maximum]
        contours = ax.contour(x, y, f, levels=levels, cmap='viridis', linewidths=1.15)
        ax.clabel(contours, inline=True, fontsize=8, fmt='%.2f')
        ax.contour(x, y, f, levels=[saddle], colors=['#b54a33'], linewidths=1.8)
        axis_points = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
        d = 1/np.sqrt(1+b)
        diagonal_points = np.array([[d, d], [-d, d], [d, -d], [-d, -d]])
        maxima, saddles = (diagonal_points, axis_points) if b < 1 else (axis_points, diagonal_points)
        ax.scatter(*maxima.T, c='black', s=27, marker='o', zorder=5)
        ax.scatter(*saddles.T, c='#b54a33', s=45, marker='x', linewidths=1.8, zorder=5)
        ax.scatter([0], [0], c='white', edgecolors='black', s=34, marker='s', zorder=5)
        ax.axhline(0, color='#999999', linewidth=0.45, zorder=0)
        ax.axvline(0, color='#999999', linewidth=0.45, zorder=0)
        ax.set(xlim=(-1.65, 1.65), ylim=(-1.65, 1.65), xlabel='$x$', ylabel='$y$', aspect='equal')
        ax.set_title(f'$b={b:g}$: '+('diagonal maxima' if b < 1 else 'axis maxima'), fontsize=12)
        ax.text(0.5, -0.17, f'Saddle level: {saddle:.3f}; maximum: {maximum:.3f}',
                transform=ax.transAxes, ha='center', fontsize=9)
    legend = [Line2D([0], [0], marker='o', color='none', markerfacecolor='black', label='Maximum'),
              Line2D([0], [0], marker='x', color='none', markeredgecolor='#b54a33', markersize=7, label='Saddle'),
              Line2D([0], [0], marker='s', color='none', markerfacecolor='white', markeredgecolor='black', label='Minimum')]
    fig.legend(handles=legend, loc='outside lower center', ncol=3, frameon=False)
    fig.savefig('paper-2-contours.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
