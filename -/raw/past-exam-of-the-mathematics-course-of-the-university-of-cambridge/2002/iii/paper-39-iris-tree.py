"""Draw the solved iris classification tree; tested with Python 3.14.

Dependencies: root pyproject.toml (NumPy 2.3.5, Matplotlib 3.10.7).
Output is the basename PNG in the caller's CWD; retain any caller MPLCONFIGDIR.
"""
from pathlib import Path
import os
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'codex-wiki-paper-39-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Positions and rules are our reconstructed decision tree, not a scan of the source.
nodes = {
    1: (0.32, 0.87, 'Petal length < 2.45?\nn = 150'),
    2: (0.075, 0.67, 'Predict s\nn = 50\n(c, s, v) = (0, 50, 0)'),
    3: (0.62, 0.67, 'Petal width < 1.75?\nn = 100'),
    6: (0.425, 0.47, 'Petal length < 4.95?\nn = 54'),
    7: (0.825, 0.47, 'Petal length < 4.95?\nn = 46'),
    12: (0.285, 0.27, 'Sepal length < 5.15?\nn = 48'),
    13: (0.57, 0.27, 'Predict v\nn = 6\n(c, s, v) = (2, 0, 4)'),
    14: (0.74, 0.27, 'Predict v\nn = 6\n(c, s, v) = (1, 0, 5)'),
    15: (0.915, 0.27, 'Predict v\nn = 40\n(c, s, v) = (0, 0, 40)'),
    24: (0.19, 0.07, 'Predict c\nn = 5\n(c, s, v) = (4, 0, 1)'),
    25: (0.38, 0.07, 'Predict c\nn = 43\n(c, s, v) = (43, 0, 0)'),
}
edges = [(1, 2), (1, 3), (3, 6), (3, 7), (6, 12), (6, 13), (7, 14), (7, 15), (12, 24), (12, 25)]
fig, ax = plt.subplots(figsize=(15.6, 8.6), dpi=110)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 1)
ax.set_ylim(-0.01, 1)
ax.axis('off')
ax.set_title('Iris classification: six terminal regions', fontsize=19, pad=15)
for source, target in edges:
    x0, y0, _ = nodes[source]
    x1, y1, _ = nodes[target]
    ax.annotate('', xy=(x1, y1 + 0.045), xytext=(x0, y0 - 0.035),
                arrowprops={'arrowstyle': '-|>', 'color': '#536477', 'lw': 1.5})
    yes = target == 2 * source
    ax.text((x0 + x1) / 2, (y0 + y1) / 2 + 0.012,
            'yes (<)' if yes else 'no (≥)', ha='center', fontsize=10,
            bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
for node, (x, y, label) in nodes.items():
    leaf = node in (2, 13, 14, 15, 24, 25)
    ax.text(x, y, label, ha='center', va='center', fontsize=10.5,
            bbox={'boxstyle': 'round,pad=0.5', 'facecolor': '#e7f2eb' if leaf else '#e8eff9',
                  'edgecolor': '#386044' if leaf else '#476587', 'linewidth': 1.1})
fig.subplots_adjust(left=0.018, right=0.985, bottom=0.05, top=0.91)
fig.savefig(Path.cwd() / 'paper-39-iris-tree.png', facecolor='white', transparent=False)
plt.close(fig)
