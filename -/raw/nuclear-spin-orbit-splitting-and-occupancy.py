"""Draw an isolated nuclear d doublet; Python 3.14, matplotlib 3.10.7.

Run from _media: MPLBACKEND=Agg python ../nuclear-spin-orbit-splitting-and-occupancy.py
The energy unit a is arbitrary; this is not a fit to a particular nucleus.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    fig = plt.figure(figsize=(11, 5.4), dpi=100, facecolor='white')
    ax = fig.add_axes([0.075, 0.21, 0.89, 0.62])
    ax.set(xlim=(0, 10), ylim=(-1.65, 2.25), ylabel=r'Energy shift / $a$')
    ax.set_xticks([])
    ax.set_yticks([-1, 0, 1.5], [r'$-1$', '0', r'$+3/2$'])
    ax.spines[['top', 'right', 'bottom']].set_visible(False)
    ax.axhline(0, color='#d9dde3', lw=1)
    ax.hlines(0, 0.4, 2.25, color='#5c6470', lw=4)
    ax.text(1.3, 0.2, r'$d$: $l=2$, ten states', ha='center')
    ax.plot([2.25, 4.0], [0, 1.5], '--', color='#8c94a0')
    ax.plot([2.25, 4.0], [0, -1], '--', color='#8c94a0')
    for j, energy, capacity, occupied, color in [
        ('3/2', 1.5, 4, 1, '#b85c18'), ('5/2', -1, 6, 6, '#156c9a')
    ]:
        ax.hlines(energy, 4.0, 8.0, color=color, lw=3)
        ax.text(4.0, energy + 0.28, rf'$d_{{{j}}}$: $2j+1={capacity}$ states', color=color)
        for k, x in enumerate(np.linspace(4.35, 7.65, capacity)):
            ax.plot(x, energy, 'o', ms=11, mec=color, mew=2,
                    mfc=color if k < occupied else 'white', zorder=3)
        ax.text(8.25, energy, f'{occupied} occupied', va='center', color=color)
    ax.annotate('', xy=(7.9, 1.5), xytext=(7.9, -1),
                arrowprops={'arrowstyle': '<->', 'color': '#343e4a', 'lw': 1.5})
    ax.text(8.15, 0.33, r'Gap $=5a/2$', va='center', fontsize=12)
    ax.text(1.3, -1.45, 'Before splitting', ha='center')
    ax.text(6.0, -1.45, 'Seven identical nucleons in the isolated doublet', ha='center')
    fig.suptitle('Negative spin–orbit coupling lowers the larger-j level', y=0.97, fontsize=17)
    fig.text(0.5, 0.88, r'$H_{\rm so}=-a\,\mathbf{L}\!\cdot\!\mathbf{S}/\hbar^2$,  $a>0$;  $j=l\pm1/2$', ha='center', fontsize=14)
    fig.text(0.5, 0.095, r'$\langle\mathbf{L}\!\cdot\!\mathbf{S}\rangle/\hbar^2=+1$ for $d_{5/2}$,  $-3/2$ for $d_{3/2}$', ha='center')
    fig.text(0.5, 0.035, 'Chosen model shifts; dots count states, not positions. Fill neutrons and protons separately.', ha='center', fontsize=11, color='#505967')
    fig.savefig(Path(__file__).stem + '.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
