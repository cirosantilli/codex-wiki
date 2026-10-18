"""Exact periodic entropy profiles; Python 3.14, dependencies in pyproject.toml."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def profile(x, t):
    if t == 0:
        return ((x + .5) % 1 < .5).astype(float)
    if t < 1:
        r = (x + .5) % 1 - .5
        return np.where(r < t - .5, (r + .5) / t,
                        np.where(r < t / 2, 1., 0.))
    return .5 + ((x - t / 2) % 1 - .5) / t


def main():
    fig, axes = plt.subplots(2, 2, figsize=(10, 5.5), dpi=110,
                             sharex=True, sharey=True, facecolor='white')
    x = np.linspace(-1.5, 1.5, 18001)
    for ax, t in zip(axes.flat, [0., .5, 1., 3.]):
        ax.set_facecolor('white')
        ax.plot(x, profile(x, t), color='#246894', lw=2)
        ax.axhline(.5, color='#888888', ls='--', lw=1,
                   label='Conserved mean')
        ax.set(xlim=(-1.5, 1.5), ylim=(-.07, 1.07), title=rf'$t={t:g}$')
        ax.set_xticks(np.arange(-1.5, 1.51, .5))
        ax.set_yticks([0, .5, 1])
        ax.grid(alpha=.16)
        ax.spines[['top', 'right']].set_visible(False)
    axes[0, 0].legend(loc='upper right', fontsize=9)
    for ax in axes[-1]:
        ax.set_xlabel('$x$')
    for ax in axes[:, 0]:
        ax.set_ylabel('$u(x,t)$')
    fig.suptitle('Periodic inviscid Burgers flow: pulse interaction and relaxation',
                 fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, .94))
    fig.savefig(Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
