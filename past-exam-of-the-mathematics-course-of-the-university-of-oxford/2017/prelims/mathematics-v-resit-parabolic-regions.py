"""Question 1: parabolic coordinate curves and regions.

Run from the mirrored _media/.../2017/prelims directory. Writes one PNG to
Path.cwd(). Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7,
using the dependencies declared in the repository's top-level pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


def xy(u, v):
    return (u * u - v * v) / 2, u * v


def setup(ax, title, xlim, ylim):
    ax.set_title(title, fontsize=11, pad=12)
    ax.axhline(0, color='0.55', linewidth=0.7)
    ax.axvline(0, color='0.55', linewidth=0.7)
    ax.set(xlim=xlim, ylim=ylim, xlabel='$x$', ylabel='$y$')
    ax.set_aspect('equal', adjustable='box')
    ax.grid(alpha=0.18)
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(labelsize=8)


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4), layout='constrained')
    fig.set_facecolor('white')
    blue, orange, green = '#1765a1', '#c35c10', '#287c5d'
    s = np.linspace(0, 1.9, 500)
    ax = axes[0]
    setup(ax, '(b) Coordinate curves', (-1.25, 1.25), (-0.08, 1.95))
    ax.plot(*xy(np.ones_like(s), s), color=blue, label='$u=1$')
    ax.plot(*xy(s, np.ones_like(s)), color=orange, label='$v=1$')
    ax.scatter([-.5, .5, 0], [0, 0, 1], s=14, color='black', zorder=5)
    ax.annotate('$(0,1)$', (0, 1), (6, 6), textcoords='offset points', fontsize=9)
    ax.legend(fontsize=9, loc='upper left', framealpha=.95)

    ax = axes[1]
    setup(ax, r'(c) $\frac{1}{2}\leq u,v\leq1$: area $7/24$', (-.47, .47), (.12, 1.14))
    t = np.linspace(.5, 1, 180)
    segments = [(t, np.full_like(t, .5)), (np.ones_like(t), t),
                (t[::-1], np.ones_like(t)), (np.full_like(t, .5), t[::-1])]
    points = np.concatenate([np.column_stack(xy(u, v)) for u, v in segments])
    ax.add_patch(Polygon(points, facecolor='#dceef8', edgecolor='none'))
    for (u, v), color in zip(segments, [green, blue, orange, green]):
        ax.plot(*xy(u, v), color=color, linewidth=1.8)
    ax.text(.19, .72, '$u=1$', color=blue, fontsize=9)
    ax.text(-.42, .72, '$v=1$', color=orange, fontsize=9)
    ax.text(-.11, .51, '$S$', fontsize=14)

    ax = axes[2]
    setup(ax, r'(d) $0\leq v\leq u^2$, $u\leq1$: area $26/105$', (-.055, .59), (-.045, 1.08))
    t = np.linspace(0, 1, 400)
    curve_x, curve_y = xy(t, t*t)
    parabola_x, parabola_y = xy(np.ones_like(t), t)
    points = np.column_stack((np.r_[0, .5, parabola_x, curve_x[::-1]],
                              np.r_[0, 0, parabola_y, curve_y[::-1]]))
    ax.add_patch(Polygon(points, facecolor='#e2f1e9', edgecolor='none'))
    ax.plot(parabola_x, parabola_y, color=blue, linewidth=1.8)
    ax.plot(curve_x, curve_y, color=orange, linewidth=1.8)
    ax.plot([0, .5], [0, 0], color=green, linewidth=2)
    ax.text(.38, .56, '$u=1$', color=blue, fontsize=9, rotation=34)
    ax.annotate('$v=u^2$', xy=(.116, .35), xytext=(.02, .59),
                arrowprops={'arrowstyle': '-', 'color': orange}, color=orange, fontsize=9)
    ax.scatter([0, .5, 0], [0, 0, 1], s=12, color='black', zorder=5)
    fig.savefig(Path.cwd() / 'mathematics-v-resit-parabolic-regions.png',
                dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
