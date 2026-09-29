"""Draw the positively oriented integration region; Python 3.14 / root dependencies."""
import os
import tempfile

# Honor a caller-supplied Matplotlib cache location.
_cache = None
if 'MPLCONFIGDIR' not in os.environ:
    _cache = tempfile.TemporaryDirectory(prefix='paper-3-mpl-')
    os.environ['MPLCONFIGDIR'] = _cache.name

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

root2 = np.sqrt(2)
x_pq = np.linspace(1, root2, 160)
x_qr = np.linspace(root2, 2, 160)
x_rs = np.linspace(2, root2, 160)
x_sp = np.linspace(root2, 1, 160)
edges = [(x_pq, 1/x_pq), (x_qr, x_qr/2), (x_rs, 2/x_rs), (x_sp, x_sp)]
fig, ax = plt.subplots(figsize=(6.7, 4.8), dpi=120, facecolor='white')
ax.set_facecolor('white')
xs = np.concatenate([edge[0] for edge in edges])
ys = np.concatenate([edge[1] for edge in edges])
ax.fill(xs, ys, color='#deedf7')
for x, y in edges:
    ax.plot(x, y, color='#195980', lw=2)
    j = len(x)//2
    ax.annotate('', xy=(x[j+12], y[j+12]), xytext=(x[j-12], y[j-12]),
                arrowprops={'arrowstyle': '-|>', 'color': '#195980', 'lw': 1.8})
points = [('P', 1, 1, (-25, -5)), ('Q', root2, 1/root2, (0, -22)),
          ('R', 2, 1, (10, -3)), ('S', root2, root2, (-4, 13))]
for name, x, y, offset in points:
    ax.plot(x, y, 'o', color='#195980', ms=4)
    ax.annotate(name, (x, y), xytext=offset, textcoords='offset points', fontsize=12)
ax.text(1.14, .74, r'$xy=1$', fontsize=12, ha='center')
ax.text(1.75, .74, r'$x=2y$', fontsize=12, ha='center')
ax.text(1.81, 1.25, r'$xy=2$', fontsize=12, ha='center')
ax.text(1.07, 1.22, r'$x=y$', fontsize=12, ha='center')
ax.text(1.45, 1.05, r'$1\leq x/y\leq2$' '\n' r'$1\leq xy\leq2$', fontsize=12, ha='center')
ax.set(xlim=(.8, 2.2), ylim=(.55, 1.62), xlabel='$x$', ylabel='$y$',
       title='Counterclockwise boundary of the integration region')
ax.set_aspect('equal', adjustable='box')
ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig('paper-3-region.png', facecolor='white', transparent=False)
plt.close(fig)
if _cache is not None:
    _cache.cleanup()
