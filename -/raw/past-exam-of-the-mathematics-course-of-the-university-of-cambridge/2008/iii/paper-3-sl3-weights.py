"""Tensor-square A2 weights; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Output is a white opaque PNG in caller CWD; caller MPLCONFIGDIR is respected.
"""
from collections import Counter
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

monomials = [(i, j, 2-i-j) for i in range(3) for j in range(3-i)]
weights = Counter(tuple(x+y for x, y in zip(a, b)) for a in monomials for b in monomials)
assert len(weights) == 15 and sum(weights.values()) == 36
L = np.array([[1., 0.], [-.5, np.sqrt(3)/2], [-.5, -np.sqrt(3)/2]])
fig, ax = plt.subplots(figsize=(6.7, 6.6), dpi=110, facecolor='white')
# Full triangular weight lattice, not a numerical interpolation of weights.
w1, w2 = L[0], -L[2]
for p in range(-8, 9):
    line=np.array([p*w1 + q*w2 for q in (-9, 9)])
    ax.plot(line[:, 0], line[:, 1], color='#e5e9ef', lw=.6, zorder=0)
for q in range(-8, 9):
    line=np.array([p*w1 + q*w2 for p in (-9, 9)])
    ax.plot(line[:, 0], line[:, 1], color='#e5e9ef', lw=.6, zorder=0)
for total in range(-9, 10):
    line=np.array([p*w1+(total-p)*w2 for p in (-9, 9)])
    ax.plot(line[:, 0], line[:, 1], color='#e5e9ef', lw=.6, zorder=0)
ax.fill([0, 6, 3], [0, 0, 3*np.sqrt(3)], color='#fff0cf', alpha=.8, zorder=1)
triangle=np.vstack([4*L, 4*L[0]])
ax.plot(triangle[:, 0], triangle[:, 1], color='#8794a5', lw=1.2, zorder=2)
for counts, multiplicity in sorted(weights.items()):
    x, y = np.array(counts) @ L
    p, q = counts[0]-counts[1], counts[1]-counts[2]
    color='#b86208' if p >= 0 and q >= 0 else '#1f618d'
    ax.scatter([x], [y], s=360, color=color, zorder=4)
    ax.text(x, y, str(multiplicity), ha='center', va='center', color='white', weight='bold', fontsize=11, zorder=5)
    ax.annotate(f'({p}, {q})', (x, y), xytext=(0, 17), textcoords='offset points', ha='center', fontsize=9, zorder=5)
ax.set_xlim(-3, 5)
ax.set_ylim(-4.3, 4.3)
ax.set_aspect('equal')
ax.set_title(r'$\mathrm{Sym}^2\mathbb{C}^3\otimes\mathrm{Sym}^2\mathbb{C}^3$', fontsize=16, pad=16)
ax.set_xlabel(r'Labels: Dynkin coordinates $(p,q)$; circle numbers: multiplicities', fontsize=10)
ax.text(.5, -.115, 'Orange weights lie in the closed dominant chamber', transform=ax.transAxes, ha='center', fontsize=10)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)
fig.subplots_adjust(left=.06, right=.96, top=.9, bottom=.16)
fig.savefig(Path('paper-3-sl3-weights.png'), facecolor='white', transparent=False)
plt.close(fig)
