"""Original spring-triangle modes; Python 3.14, numpy 2.3, matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    a = np.sqrt(3)
    positions = np.array([[-a/2, -.5], [a/2, -.5], [0, 1]])
    modes = [
        ('Rigid rotation', r'$\omega^2=0$', [-1, -1, 2, a, -a, 0]),
        ('Breathing', r'$\omega^2=3k/m$', [-a, a, 0, -1, -1, 2]),
        ('First shear', r'$\omega^2=3k/(2m)$', [-a, a, 0, 1, 1, -2]),
        ('Second shear', r'$\omega^2=3k/(2m)$', [-1, -1, 2, -a, a, 0]),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(8.4, 7.4), dpi=120, layout='constrained')
    for ax, (name, freq, raw) in zip(axes.flat, modes):
        for i, j in [(0, 1), (0, 2), (1, 2)]:
            edge = positions[[i, j]]
            ax.plot(edge[:, 0], edge[:, 1], color='0.7', lw=1.5, zorder=1)
        displacement = np.array(raw).reshape(2, 3).T * .23
        ax.scatter(positions[:, 0], positions[:, 1], color='#176d9c', s=48, zorder=4)
        ax.quiver(positions[:, 0], positions[:, 1], displacement[:, 0], displacement[:, 1], angles='xy', scale_units='xy', scale=1, color='#ad562b', width=.009, headwidth=4, headlength=5, zorder=5)
        for i, (x, y) in enumerate(positions):
            ax.text(.78*x, .78*y, str(i+1), ha='center', va='center', color='0.3', fontsize=10, bbox={'facecolor':'white','edgecolor':'none','pad':.4})
        ax.set(xlim=(-1.55, 1.55), ylim=(-1.2, 1.65), xticks=[-1, 0, 1], yticks=[-1, 0, 1], xlabel='x', ylabel='y', title=name+'\n'+freq)
        ax.set_aspect('equal')
        ax.grid(alpha=.12)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
