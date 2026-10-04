"""Ordered Grassmann bilinear contractions; Python 3.14, root Matplotlib/NumPy.

Write the matching PNG to the caller's working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(9, 3.2), layout='constrained', facecolor='white')
ink = '#243746'
def curve(ax, x, y, arrow_index):
    ax.plot(x, y, color=ink, lw=2.2)
    i = arrow_index
    ax.annotate('', (x[i+3], y[i+3]), (x[i-3], y[i-3]),
                arrowprops={'arrowstyle':'-|>', 'color':ink, 'lw':1.5, 'mutation_scale':14})
def vertex(ax, x, y, label):
    ax.scatter([x], [y], s=45, color=ink, zorder=3)
    ax.text(x, y-.19, label, ha='center', va='top', fontsize=14)

ax = axes[0]
for center, label in [(-.85, '$M$'), (.85, '$N$')]:
    t = np.linspace(-np.pi/2, 3*np.pi/2, 161)
    curve(ax, center+.5*np.cos(t), .18+.5*np.sin(t), 75)
    vertex(ax, center, -.32, label)
ax.set_title('Two disconnected fermion loops', fontsize=13)
ax.text(0, -1.0, r'$+\,\mathrm{tr}(MC)\,\mathrm{tr}(NC)$', ha='center', fontsize=15)

ax = axes[1]
t = np.linspace(np.pi, 0, 121)
curve(ax, .95*np.cos(t), .52*np.sin(t), 65)
t = np.linspace(0, -np.pi, 121)
curve(ax, .95*np.cos(t), .52*np.sin(t), 65)
vertex(ax, -.95, 0, '$M$')
vertex(ax, .95, 0, '$N$')
ax.text(0, .67, '$C$', ha='center', fontsize=13)
ax.text(0, -.67, '$C$', ha='center', fontsize=13)
ax.set_title('One connected fermion loop', fontsize=13)
ax.text(0, -1.0, r'$-\,\mathrm{tr}(MCNC)$', ha='center', fontsize=15)
for ax in axes:
    ax.set(xlim=(-1.65, 1.65), ylim=(-1.24, .94))
    ax.set_aspect('equal')
    ax.axis('off')
fig.suptitle(r'Bilinear contractions with $C=B^{-1}$', fontsize=15)
fig.savefig('paper-51-fermion-loops.png', dpi=120, facecolor='white')
plt.close(fig)
