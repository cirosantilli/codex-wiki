"""Original figure; run from the mirrored _media directory. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(0, 14 * np.pi, 6000)
    radius = 1 / (1 + theta)
    x, y = radius * np.cos(theta), radius * np.sin(theta)
    fig, ax = plt.subplots(figsize=(6.8, 5.2), facecolor='white', layout='constrained')
    ax.set_facecolor('white')
    ax.plot(x, y, color='#176a9d', lw=1.8)
    for angle in (0.5, 3.8, 8.6):
        i = np.searchsorted(theta, angle)
        j = min(i + 32, len(theta) - 1)
        ax.annotate('', xy=(x[j], y[j]), xytext=(x[i], y[i]),
                    arrowprops={'arrowstyle': '-|>', 'color': '#176a9d', 'lw': 1.8})
    ax.scatter([1, 0], [0, 0], color=['#b5412e', '#222222'], s=[30, 20], zorder=4)
    ax.annotate(r'$t=0,\ \theta=0$', (1, 0), xytext=(0.55, -0.23),
                arrowprops={'arrowstyle': '->', 'color': '#555555'}, fontsize=11)
    ax.annotate(r'$r\to 0,\ \theta\to\infty$' + '\n' + r'$t\uparrow a^2/\sqrt{2k}$',
                (0, 0), xytext=(-0.45, -0.36),
                arrowprops={'arrowstyle': '->', 'color': '#555555'}, fontsize=10)
    ax.axhline(0, color='#aaaaaa', lw=0.7, zorder=0)
    ax.axvline(0, color='#aaaaaa', lw=0.7, zorder=0)
    ax.set(xlim=(-0.53, 1.12), ylim=(-0.47, 0.54), aspect='equal',
           xlabel=r'$x/a$', ylabel=r'$y/a$', title=r'$r/a=1/(1+\theta),\quad\theta\geq0$')
    ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(Path('mathematics-iv-q2-orbit.png'), dpi=150, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
