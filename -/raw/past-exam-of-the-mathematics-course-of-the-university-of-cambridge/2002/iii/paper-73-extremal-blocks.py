"""Extremal RN Penrose building blocks; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes only paper-73-extremal-blocks.png in the caller's working directory.
An explicitly supplied MPLCONFIGDIR is preserved.
"""
from pathlib import Path
import os
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'codex-wiki-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

RED = '#a42a35'
BLUE = '#266a9e'
fig, axes = plt.subplots(1, 2, figsize=(9.4, 5.1), dpi=120)
fig.patch.set_facecolor('white')

for ax in axes:
    ax.set_aspect('equal')
    ax.set_xlim(-1.65, 1.6)
    ax.set_ylim(-1.48, 1.46)
    ax.axis('off')
    ax.set_facecolor('white')

ax = axes[0]
poly = Polygon([(-1, 0), (0, 1), (1, 0), (0, -1)], closed=True,
               facecolor='#f4f7fa', edgecolor='none')
ax.add_patch(poly)
for offset in (-0.45, 0, 0.45):
    x = np.linspace(-1, 1, 201)
    for sign in (-1, 1):
        line, = ax.plot(x, sign * x + offset, color='#c2cbd0', lw=0.7)
        line.set_clip_path(poly)
ax.plot([-1, 0], [0, 1], color=RED, lw=2.6)
ax.plot([-1, 0], [0, -1], color=BLUE, lw=2.6)
ax.plot([0, 1, 0], [1, 0, -1], color='#263238', lw=1.7)
ax.plot(-1, 0, marker='o', markersize=6.5, markerfacecolor='white',
        markeredgecolor='#263238', zorder=5)
ax.text(0, 0.06, '$r>M$', ha='center', fontsize=13)
ax.text(0, 1.14, '$i^+$', ha='center', fontsize=12)
ax.text(0, -1.17, '$i^-$', ha='center', fontsize=12)
ax.text(1.10, 0, '$i^0$', va='center', fontsize=12)
ax.text(0.63, 0.61, '$\\mathscr{I}^+$', fontsize=13)
ax.text(0.63, -0.68, '$\\mathscr{I}^-$', fontsize=13)
ax.text(-0.90, 0.60, '$H^+$', color=RED, fontsize=12)
ax.text(-0.90, -0.66, '$H^-$', color=BLUE, fontsize=12)
ax.annotate('Excluded\nthroat end', xy=(-1, 0), xytext=(-1.58, 0.04),
            ha='center', va='center', fontsize=9,
            arrowprops={'arrowstyle': '-', 'color': '#52656e'}, color='#344950')
ax.set_title('Exterior block', fontsize=13, pad=9)

ax = axes[1]
poly = Polygon([(0, -1), (1, 0), (0, 1)], closed=True,
               facecolor='#fff8ed', edgecolor='none')
ax.add_patch(poly)
for offset in (-0.45, 0, 0.45):
    x = np.linspace(0, 1, 201)
    for sign in (-1, 1):
        line, = ax.plot(x, sign * x + offset, color='#d2c8b6', lw=0.7)
        line.set_clip_path(poly)
ax.plot([0, 1], [-1, 0], color=RED, lw=2.6)
ax.plot([1, 0], [0, 1], color=BLUE, lw=2.6)
# A jagged vertical line marks a timelike curvature singularity, not a null edge.
y = np.linspace(-0.985, 0.985, 95)
x = np.where(np.arange(len(y)) % 2 == 0, -0.025, 0.025)
ax.plot(x, y, color='#263238', lw=1.7)
ax.plot(1, 0, marker='o', markersize=6.5, markerfacecolor='white',
        markeredgecolor='#263238', zorder=5)
ax.text(0.37, 0.03, '$0<r<M$', ha='center', fontsize=12)
ax.text(-0.12, 0, '$r=0$\nTimelike\nsingularity', va='center', ha='right', fontsize=10)
ax.text(0.73, 0.68, 'Next horizon', rotation=-45, color=BLUE, fontsize=10)
ax.text(0.73, -0.76, 'Entry horizon', rotation=45, color=RED, fontsize=10)
ax.annotate('Excluded\nthroat end', xy=(1, 0), xytext=(1.47, 0.04),
            ha='center', va='center', fontsize=9,
            arrowprops={'arrowstyle': '-', 'color': '#52656e'}, color='#344950')
ax.set_title('Inner static block', fontsize=13, pad=9)

fig.text(0.5, 0.105, 'Glue the red edges at finite advanced time $v$ using the regular ingoing metric.',
         ha='center', fontsize=10.5, color=RED)
fig.text(0.5, 0.055, 'Repeat null-edge extensions to obtain the infinite diagram; open vertices are not bifurcation spheres.',
         ha='center', fontsize=9.4, color='#344950')
fig.subplots_adjust(left=0.025, right=0.975, top=0.89, bottom=0.16, wspace=0.15)
fig.savefig('paper-73-extremal-blocks.png', facecolor='white', transparent=False)
plt.close(fig)
