"""Original spherical-collapse illustration; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes exactly one PNG in the caller's current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    angle = np.linspace(0.04, 2 * np.pi - 0.04, 1800)
    time = (angle - np.sin(angle)) / (2 * np.pi)
    radius = (1 - np.cos(angle)) / 2
    contrast = 4.5 * (angle - np.sin(angle))**2 / (1 - np.cos(angle))**3 - 1
    linear = 0.6 * (0.75 * (angle - np.sin(angle)))**(2 / 3)
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 3.7), dpi=110, facecolor='white')
    left.plot(time, radius, color='#176c9c', linewidth=2.4)
    left.scatter([0.5, 1], [1, 0], color='#176c9c', zorder=4, clip_on=False)
    left.annotate('Turnaround', xy=(0.5, 1), xytext=(0.36, 0.76), arrowprops={'arrowstyle': '->'})
    left.annotate('Formal collapse', xy=(1, 0), xytext=(0.57, 0.17), arrowprops={'arrowstyle': '->'})
    left.set(xlabel=r'Time $t/t_c$', ylabel=r'Radius $r/r_m$', xlim=(0, 1), ylim=(0, 1.08), title='Expansion and recollapse')
    right.semilogy(time, contrast, label=r'Nonlinear $\delta$', color='#176c9c', linewidth=2.4)
    right.semilogy(time, linear, '--', label=r'Linear extrapolation $\delta_L$', color='#b54727', linewidth=2.2)
    right.axvline(0.5, color='0.65', linewidth=1, linestyle=':')
    right.scatter([1], [0.6 * (1.5 * np.pi)**(2/3)], color='#b54727', clip_on=False, zorder=4)
    right.annotate(r'$\delta_c=1.686$', xy=(1, 1.686), xytext=(0.60, 0.17), arrowprops={'arrowstyle': '->'})
    right.set(xlabel=r'Time $t/t_c$', ylabel='Density contrast', xlim=(0, 1), ylim=(0.001, 1000), title='Linear theory misses the divergence')
    right.legend(loc='upper left', fontsize=9)
    for ax in (left, right):
        ax.set_facecolor('white')
        ax.grid(alpha=0.2)
        ax.spines[['top', 'right']].set_visible(False)
    fig.tight_layout(pad=1.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
