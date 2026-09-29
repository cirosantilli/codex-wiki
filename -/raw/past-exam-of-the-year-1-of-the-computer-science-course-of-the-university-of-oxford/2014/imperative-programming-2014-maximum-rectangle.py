"""Reproduce the Q2 solution figure; writes the PNG in the current directory.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

A = np.array([[c == 'T' for c in row] for row in [
    'FTTTTTTFTT', 'FTTTTTTFTT', 'TTFTTTFTTF', 'TTTTFTTTFT',
    'FTTTFFTTFF', 'FTTTFTTTTT', 'TTTTTFTTTF', 'TTFTFTTTTT',
    'TFTFTTTTTT', 'FFTTTFTTTT',
]], dtype=bool)
R = np.zeros((10, 10), dtype=int)
for i in range(10):
    for j in range(10):
        R[i, j] = (R[i, j-1] if j else 0) + 1 if A[i, j] else 0

fig, axes = plt.subplots(1, 2, figsize=(10, 5), facecolor='white')
for ax, data, title in zip(axes, [A.astype(int), R], ['Illuminated pixels: area 15', 'Consecutive true entries ending here']):
    ax.imshow(A, cmap=matplotlib.colors.ListedColormap(['#eeeeee', '#cce4f5']), vmin=0, vmax=1)
    for i in range(10):
        for j in range(10):
            ax.text(j, i, ('T' if A[i, j] else 'F') if ax is axes[0] else str(data[i, j]),
                    ha='center', va='center', fontsize=10, color='#182c3a')
    ax.add_patch(Rectangle((5.5, 4.5), 3, 5, fill=False, edgecolor='#b13b1b', linewidth=2.5))
    ax.set_xticks(range(10)); ax.set_yticks(range(10))
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='white', linewidth=1)
    ax.tick_params(which='minor', bottom=False, left=False)
    ax.xaxis.tick_top(); ax.xaxis.set_label_position('top')
    ax.set_xlabel('column', labelpad=9); ax.set_ylabel('row')
    ax.set_title(title, fontsize=12, pad=44)
axes[1].plot([8]*5, range(5,10), 'o', markersize=23, markerfacecolor='none', markeredgecolor='#b13b1b', linewidth=1)
fig.text(.5, .025, 'Rows 5–9, right edge 8: widths 4, 3, 4, 5, 3; minimum 3; height 5; area 15.',
         ha='center', fontsize=11)
fig.subplots_adjust(left=.06, right=.99, bottom=.10, top=.77, wspace=.20)
fig.savefig('imperative-programming-2014-maximum-rectangle.png', dpi=120, facecolor='white', metadata={'Software':'codex-wiki figure generator'})
plt.close(fig)
