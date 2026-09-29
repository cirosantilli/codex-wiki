"""Exact midpoint subdivision of an original cubic; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes paper-66-bezier-halves.png only to the caller's working directory.
MPLCONFIGDIR is supplied by the caller and is never changed here.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def bezier(controls, parameter):
    t = np.asarray(parameter)[:, None]
    return ((1-t)**3 * controls[0] + 3*t*(1-t)**2 * controls[1]
            + 3*t*t*(1-t) * controls[2] + t**3 * controls[3])


def main():
    p = np.array([[0.0, 0.0], [0.8, 2.7], [3.2, -1.2], [4.0, 1.3]])
    a = (p[:-1] + p[1:]) / 2
    b = (a[:-1] + a[1:]) / 2
    h = (b[0] + b[1]) / 2
    left = np.array([p[0], a[0], b[0], h])
    right = np.array([h, b[1], a[2], p[3]])
    t = np.linspace(0, 1, 241)
    assert np.allclose(bezier(left, t), bezier(p, t/2))
    assert np.allclose(bezier(right, t), bezier(p, (1+t)/2))
    assert np.allclose(h-b[0], b[1]-h)

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.1), dpi=120, facecolor='white')
    blue, orange = '#1769aa', '#c65d0e'
    for ax in axes:
        ax.set_facecolor('white')
        ax.plot(p[:, 0], p[:, 1], '--', color='#a3a3a3', lw=1.1, label='Original polygon')
        ax.plot(*bezier(p, t).T, color='#515151', lw=2.0)
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim(-0.28, 4.28)
        ax.set_ylim(-1.55, 3.04)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(alpha=0.15)
    ax = axes[0]
    ax.plot(a[:, 0], a[:, 1], '-o', color='#58945b', markersize=4, lw=1.1)
    ax.plot(b[:, 0], b[:, 1], '-o', color='#8553a1', markersize=4, lw=1.6)
    ax.scatter(*h, s=35, color='#202020', zorder=5)
    for j, point in enumerate(p):
        ax.scatter(*point, s=20, color='#515151')
        ax.annotate(f'$P_{j}$', point, xytext=(5, 7), textcoords='offset points')
    for j, point in enumerate(a):
        ax.annotate(f'$A_{j}$', point, xytext=((10, 25) if j == 1 else (4, -15)), textcoords='offset points', color='#39753c')
    for j, point in enumerate(b):
        ax.annotate(f'$B_{j}$', point, xytext=(-12, 8), textcoords='offset points', color='#8553a1')
    ax.annotate('$H$', h, xytext=(6, -15), textcoords='offset points')
    ax.set_title('Successive midpoint construction', fontsize=11)

    ax = axes[1]
    ax.plot(left[:, 0], left[:, 1], '-o', color=blue, lw=1.0, markersize=3)
    ax.plot(right[:, 0], right[:, 1], '-o', color=orange, lw=1.0, markersize=3)
    ax.plot(*bezier(left, t).T, color=blue, lw=3, label=r'Left: $0\leq t\leq1/2$')
    ax.plot(*bezier(right, t).T, color=orange, lw=3, label=r'Right: $1/2\leq t\leq1$')
    ax.scatter(*h, s=35, color='#202020', zorder=5)
    ax.annotate('$H=L_3=R_0$', h, xytext=(-37, -21), textcoords='offset points', fontsize=9)
    ax.set_title('Two exact subcurves and their polygons', fontsize=11)
    ax.legend(loc='upper right', fontsize=8, framealpha=1)
    fig.suptitle('A cubic Bézier curve split at its parameter midpoint', fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(Path('paper-66-bezier-halves.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
