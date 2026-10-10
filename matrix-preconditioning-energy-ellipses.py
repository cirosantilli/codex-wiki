"""Original equal-energy contours before and after diagonal scaling.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; the output basename matches this script's basename.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

A = np.array([[1.0, 0.2], [0.2, 100.0]])
S = np.diag([1.0, 10.0])
B = np.linalg.solve(S, np.linalg.solve(S, A).T).T
levels = [0.25, 1.0, 2.04]
theta = np.linspace(0.0, 2.0 * np.pi, 1201)
circle = np.vstack([np.cos(theta), np.sin(theta)])
colors = ['#aec7e8', '#5b8fb9', '#245b85']
plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12, 'figure.facecolor': 'white'})
fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.8), layout='constrained')
fig.suptitle('Diagonal scaling preserves energy and changes its geometry', fontsize=14)
for ax, matrix, prefix, point, title in zip(
    axes, [A, B], ['e', r'\eta'], [np.array([1.0, 0.1]), np.array([1.0, 1.0])],
    ['Original coordinates', 'Scaled coordinates'], strict=True
):
    values, vectors = np.linalg.eigh(matrix)
    for t, color in zip(levels, colors, strict=True):
        points = vectors @ (np.sqrt(t / values)[:, None] * circle)
        assert np.max(np.abs(np.sum(points * (matrix @ points), axis=0) - t)) < 1e-12
        ax.plot(*points, color=color, linewidth=2, label=f'Energy = {t/2:g}')
    ax.axhline(0, color='#cccccc', linewidth=0.8)
    ax.axvline(0, color='#cccccc', linewidth=0.8)
    ax.plot(*point, 'o', color='#a23c72', markersize=6)
    label = '(1, 0.1)' if prefix == 'e' else '(1, 1)'
    ax.annotate(label, point, xytext=(-45, 16), textcoords='offset points', color='#a23c72')
    assert np.isclose(point @ matrix @ point / 2, 1.02)
    ax.set(xlim=(-1.6, 1.6), ylim=(-1.6, 1.6), aspect='equal',
           xlabel=f'${prefix}_1$', ylabel=f'${prefix}_2$',
           title=title + '\n' + rf'$\kappa_2={values[-1]/values[0]:.6f}$')
    ax.grid(alpha=0.15)
axes[0].legend(loc='upper left', fontsize=10, framealpha=1)
fig.supxlabel(r'$\eta=M^{1/2}e=(e_1,10e_2)^T$; both panels use equal coordinate scales', fontsize=11)
fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
plt.close(fig)
