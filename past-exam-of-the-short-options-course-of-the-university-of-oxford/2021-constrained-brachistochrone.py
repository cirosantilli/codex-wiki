"""Stationary fixed-length arches; Python 3.14, NumPy/Matplotlib per pyproject.toml."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def arch(b, size=16001):
    phi = np.linspace(0, 2 * np.pi, size)
    s = np.sin(phi / 2)
    density = s**2 / (1 - b*s)**3
    c = np.trapezoid(density, phi)
    dx = (density[1:] + density[:-1]) * np.diff(phi) / (2*c)
    x = np.r_[0., np.cumsum(dx)]
    y = s**2 / (c*(1-b*s)**2)
    length = np.trapezoid(s / (1-b*s)**3, phi) / c
    assert b < 1 and c > 0 and np.isclose(x[-1], 1)
    assert np.allclose(x + x[::-1], 1) and np.allclose(y, y[::-1])
    return x, y, length


def main():
    fig, ax = plt.subplots(figsize=(8, 4.8), layout='constrained')
    for b, color in [(-4, '#b44e19'), (0, '#176ca4'), (.75, '#23855b')]:
        x, y, length = arch(b)
        ax.plot(x, -y, lw=2, color=color, label=fr'$b={b:g}$, $L={length:.3f}$')
    ax.axhline(0, color='#5f666c', lw=.8)
    ax.axvline(.5, color='#9da6ad', ls=':', lw=1)
    ax.scatter([0, 1], [0, 0], color='#263238', zorder=4, s=24)
    ax.set(xlabel=r'Horizontal coordinate $x$', ylabel=r'Physical height $-y$',
           title='Fixed-length brachistochrone: symmetric stationary arches', xlim=(-.025, 1.025))
    ax.set_aspect('equal', adjustable='box')
    ax.legend(loc='upper center', bbox_to_anchor=(.5, -.16), frameon=False, ncols=3, fontsize=10)
    ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=150, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
