"""B2 weight diagrams. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Write exactly one PNG in the caller's working directory, independently of the
script's location. Point positions use Euclidean coordinates; labels use the
long-first Dynkin convention (a,b)=(x-y,2y).
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})
    spin = [(x, y, 1) for x in (-0.5, 0.5) for y in (-0.5, 0.5)]
    vector = [(1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1), (0, 0, 1)]
    adjoint = [(x, y, 1) for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1),
                                    (1, 1), (1, -1), (-1, 1), (-1, -1)]] + [(0, 0, 2)]
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.2), dpi=120, facecolor='white')
    panels = [('Spinor: 4', '(0, 1)', spin, '#24659c'),
              ('Vector: 5', '(1, 0)', vector, '#1b7a59'),
              ('Adjoint: 10', '(0, 2)', adjoint, '#a65523')]
    for ax, (name, highest, weights, color) in zip(axes, panels):
        ax.set_facecolor('white')
        ax.axhline(0, color='#b8c0c8', lw=0.8, zorder=0)
        ax.axvline(0, color='#b8c0c8', lw=0.8, zorder=0)
        coords = np.array([(x, y) for x, y, _ in weights])
        if len(weights) == 4:
            outline = np.array([[-.5, -.5], [.5, -.5], [.5, .5], [-.5, .5], [-.5, -.5]])
        elif len(weights) == 5:
            outline = np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [1, 0]])
        else:
            outline = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]])
        ax.plot(outline[:, 0], outline[:, 1], color=color, alpha=.35, lw=1.2)
        ax.scatter(coords[:, 0], coords[:, 1], c=color, s=48, zorder=3)
        for x, y, mult in weights:
            a, b = int(round(x-y)), int(round(2*y))
            label = f'({a}, {b})' + (' ×2' if mult == 2 else '')
            dx = -7 if x < 0 else (7 if x > 0 else 0)
            dy = -15 if y < 0 else 9
            ax.annotate(label, (x, y), xytext=(dx, dy), textcoords='offset points',
                        ha='right' if x < 0 else ('left' if x > 0 else 'center'),
                        va='top' if y < 0 else 'bottom', fontsize=9, color='#182b3b')
        ax.set(xlim=(-1.65, 1.65), ylim=(-1.6, 1.6), aspect='equal')
        ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
        ax.tick_params(length=0, labelsize=8, colors='#64717a')
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_title(name + '\nHighest Dynkin weight ' + highest, fontsize=11, pad=12)
        ax.set_xlabel('Euclidean x', fontsize=9, color='#64717a')
    axes[0].set_ylabel('Euclidean y', fontsize=9, color='#64717a')
    fig.suptitle('B₂ weights — long simple root first', fontsize=14, y=.98)
    fig.text(.5, .025, 'Point labels: Dynkin coordinates (x − y, 2y). Each point has multiplicity 1 unless marked ×2.',
             ha='center', fontsize=10, color='#263b4c')
    fig.subplots_adjust(left=.055, right=.985, top=.77, bottom=.16, wspace=.32)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False,
                metadata={'Software': 'codex-wiki B2 weight diagram generator'})
    plt.close(fig)


if __name__ == '__main__':
    main()
