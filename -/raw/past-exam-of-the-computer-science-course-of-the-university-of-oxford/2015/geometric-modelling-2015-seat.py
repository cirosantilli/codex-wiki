"""Oxford 2015 geometric modelling Q1: primitives and the initial box.

Run from any directory; writes geometric-modelling-2015-seat.png there.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.mkdtemp(prefix='gmod-seat-mpl-'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
import numpy as np

s = np.sqrt(3.)
points = np.array([[2-s, 0], [2, 1], [1, 1], [1, 2], [0, 2], [0, 0]])
fig, axes = plt.subplots(1, 2, figsize=(9, 4.6), layout='constrained')
for ax in axes:
    ax.add_patch(Polygon(points, facecolor='#dbeaf6', edgecolor='#123e67', lw=2, zorder=3))
    ax.set(xlim=(-.5, 2.55), ylim=(-.5, 2.55), xlabel='x', ylabel='y')
    ax.set_aspect('equal')
    ax.grid(alpha=.18)
    for label, p, offset in zip('ABCDEO', points,
                              [(4, -17), (8, 0), (-15, -16), (8, 5), (-15, 5), (-15, -16)]):
        ax.plot(*p, 'o', color='#123e67', ms=3, zorder=5)
        ax.annotate(label, p, xytext=offset, textcoords='offset points', fontsize=11, zorder=6)

ax = axes[0]
x = np.linspace(-.5, 2.55, 100)
ax.plot(x, (x-(2-s))/s, '--', color='.55', lw=1, zorder=1)
for y in [0, 1, 2]:
    ax.axhline(y, ls='--', color='.65', lw=1, zorder=1)
for xx in [0, 1]:
    ax.axvline(xx, ls='--', color='.65', lw=1, zorder=1)
normals = np.array([[1, -s], [0, 1], [1, 0], [0, 1], [-1, 0], [0, -1]])
for i in range(6):
    mid = (points[i] + points[(i+1) % 6])/2
    v = .33*normals[i]/np.linalg.norm(normals[i])
    ax.annotate('', mid+v, mid, arrowprops=dict(arrowstyle='->', lw=1.6, color='#9b3514'), zorder=6)
    label_position = {1: (1.62, 1.4), 2: (1.43, 1.56), 4: (-.25, 1.13)}.get(i, mid+1.35*v)
    ax.text(*label_position, f'n{i+1}', fontsize=9, color='#9b3514', ha='center', va='center', zorder=6)
ax.set_title('Supporting lines and outward normals')

ax = axes[1]
ax.add_patch(Rectangle((1, 0), 1, 2, facecolor='#f4b942', alpha=.16, zorder=4))
ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, edgecolor='#a93535', lw=1.6, zorder=5))
ax.plot([1, 1], [0, 2], '--', color='#a93535', lw=1.7, zorder=5)
ax.text(1.6, 1.7, 'R: [1,2] × [0,2]', ha='center', fontsize=9)
ax.text(.5, 2.3, 'Q: [0,2] × [0,2]', ha='center', fontsize=10)
ax.plot(1.25, .75, 'o', color='#287845', zorder=7)
ax.annotate('inside', (1.25, .75), xytext=(6, -13), textcoords='offset points', fontsize=9)
ax.plot(1.5, 1.5, 'x', color='#a93535', ms=7, zorder=7)
ax.annotate('outside', (1.5, 1.5), xytext=(6, -13), textcoords='offset points', fontsize=9)
ax.set_title('First vertical subdivision')
fig.savefig('geometric-modelling-2015-seat.png', dpi=125, facecolor='white', transparent=False)
plt.close(fig)
