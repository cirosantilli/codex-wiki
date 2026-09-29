"""Original motif intensity and phase simulation; run from _media (Python 3.14).

Real constant amplitudes f_A=1, f_B=0.6; single-scattering model, no measured data.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    h = np.arange(1, 9)
    def factor(u):
        return 1 + .6 * np.exp(2j * np.pi * h * u)
    half, quarter, inverted = factor(.5), factor(.25), factor(.75)
    assert np.allclose(abs(quarter)**2, abs(inverted)**2)
    assert np.allclose(abs(half[:4])**2, [.16, 2.56, .16, 2.56])
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(10, 7), dpi=120)
    grid = fig.add_gridspec(2, 2, height_ratios=[1, 1], hspace=.65, wspace=.35)
    ax = fig.add_subplot(grid[0, :])
    ax.bar(h - .17, abs(half)**2, width=.32, color='#176998', label=r'$u=1/2$')
    ax.bar(h + .17, abs(quarter)**2, width=.32, color='#b2590b', label=r'$u=1/4$')
    ax.set(xticks=h, xlabel=r'Reflection $(h00)$: integer $h$',
           ylabel=r'Squared motif amplitude $J=|F|^2$', ylim=(0, 3.2),
           title='Changing the motif changes strengths at the same reflection positions')
    ax.legend(loc='upper right', frameon=False, ncol=2)
    ax.grid(axis='y', alpha=.18)
    bx = fig.add_subplot(grid[1, 0])
    for y, u, color in [(1, .25, '#b2590b'), (0, .75, '#785ba2')]:
        bx.plot([0, 1], [y, y], color='#999999', lw=1)
        bx.scatter([0], [y], s=95, color='#333333', zorder=3)
        bx.scatter([u], [y], s=95, color=color, zorder=3)
        bx.text(.02, y+.15, 'A', color='#333333')
        bx.text(u, y+.15, 'B', ha='center', color=color)
    bx.set(xlim=(-.07, 1.08), ylim=(-.45, 1.6), xticks=[0, .25, .75, 1],
           yticks=[0, 1], yticklabels=[r'$u=3/4$', r'$u=1/4$'],
           xlabel=r'Fractional coordinate $x/a$', title='Invert the offset, keep A fixed')
    bx.text(.5, -.40, 'Other fractional coordinates are zero.', ha='center', fontsize=10)
    cx = fig.add_subplot(grid[1, 1])
    cx.axhline(0, color='#aaaaaa', lw=1)
    cx.axvline(0, color='#aaaaaa', lw=1)
    cx.add_patch(plt.Circle((0, 0), np.sqrt(1.36), fill=False, color='#bbbbbb', ls='--'))
    for imag, color in [(.6, '#b2590b'), (-.6, '#785ba2')]:
        cx.annotate('', (1, imag), (0, 0), arrowprops={'arrowstyle': '->', 'lw': 2, 'color': color})
        cx.scatter([1], [imag], color=color, s=35)
        cx.text(.90, imag + (.18 if imag > 0 else -.25),
                r'$1+0.6i$' if imag > 0 else r'$1-0.6i$', color=color, ha='center')
    cx.text(-1.15, 1.02, r'Both: $|F_{100}|^2=1.36$', fontsize=10)
    cx.set(aspect='equal', xlim=(-1.3, 1.6), ylim=(-1.25, 1.3),
           xticks=[0, 1], yticks=[-.6, 0, .6], xlabel=r'Real part of $F_{100}$',
           ylabel='Imaginary part', title='Same magnitude, opposite phase')
    fig.suptitle('Simulated basis strengths and an inversion ambiguity', fontsize=15, y=.97)
    fig.text(.5, .025, r'Chosen real amplitudes $f_A=1$, $f_B=0.6$. No instrument corrections or real-material data.', ha='center', fontsize=11)
    fig.subplots_adjust(left=.09, right=.97, top=.87, bottom=.12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
