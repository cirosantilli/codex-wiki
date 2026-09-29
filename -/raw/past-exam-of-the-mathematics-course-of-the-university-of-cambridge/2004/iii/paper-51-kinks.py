"""Four elementary phi-six profiles, output paper-51-kinks.png in caller CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Uses declared root dependencies and honors caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 4.8), sharex=True,
                             sharey=True, layout='constrained')
    fig.patch.set_facecolor('white')
    x = np.linspace(-4, 4, 501)
    cases = [(1, 1, '0 → +b'), (1, -1, '+b → 0'),
             (-1, 1, '0 → −b'), (-1, -1, '−b → 0')]
    for ax, (sigma, eta, title) in zip(axes.flat, cases):
        ax.set_facecolor('white')
        y = sigma / np.sqrt(1 + np.exp(-2 * eta * x))
        ax.plot(x, y, lw=2.5, color='#00699e' if sigma > 0 else '#a64421')
        for level in [-1, 0, 1]:
            ax.axhline(level, color='#999999', lw=.7, ls='--', zorder=0)
        ax.set(title=title, xlim=(-4, 4), ylim=(-1.15, 1.15))
        ax.set_yticks([-1, 0, 1])
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(alpha=.12)
    fig.supxlabel(r'Normalized position $b^2(x-x_0)$')
    fig.supylabel(r'Normalized field $\phi/b$')
    fig.suptitle(r'Elementary phi-six kinks: each has rest energy $b^4/4$')
    fig.savefig(Path.cwd() / 'paper-51-kinks.png', dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
