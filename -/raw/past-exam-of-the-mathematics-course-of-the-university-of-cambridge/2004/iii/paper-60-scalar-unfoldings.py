"""Scalar unfolding sketches. Python 3.14/NumPy 2.3.5/Matplotlib 3.10.7.
Outputs paper-60-scalar-unfoldings.png to caller CWD; honors MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(1, 3, figsize=(9.2, 4.5), sharey=True,
                             layout='constrained')
    fig.patch.set_facecolor('white')
    x = np.linspace(-4.5, 1.7, 16001)
    for ax, eps in zip(axes, [0, .2, -.2]):
        ax.set_facecolor('white')
        h = x*x + x**3/3 - eps
        mu = np.sqrt(np.maximum(h, 0))
        for stable, color, style in [(True, '#00679c', '-'), (False, '#b24b15', '--')]:
            mask = (h >= 0) & (((x < -2) | (x > 0)) == stable)
            yy = np.where(mask, x, np.nan)
            for sign in [-1, 1]:
                ax.plot(sign*mu, yy, style, color=color, lw=2)
        for level in [0, 4/3]:
            if level-eps >= 0:
                xx = 0 if level == 0 else -2
                mm = np.sqrt(level-eps)
                ax.plot([-mm, mm], [xx, xx], 'o', color='#222222', ms=4)
        ax.axvline(0, color='#aaaaaa', lw=.7)
        ax.set(title=rf'$\varepsilon={eps:g}$', xlabel=r'$\mu$', xlim=(-1.7, 1.7), ylim=(-4.2, 1.6))
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(alpha=.12)
    axes[0].set_ylabel('Equilibrium x')
    axes[0].annotate('Transcritical', (0, 0), (.25, -.75),
                     arrowprops={'arrowstyle': '->', 'color': '#555555'}, fontsize=9)
    fig.suptitle('Stable branches solid; unstable branches dashed; folds marked')
    fig.savefig(Path.cwd()/'paper-60-scalar-unfoldings.png', dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
