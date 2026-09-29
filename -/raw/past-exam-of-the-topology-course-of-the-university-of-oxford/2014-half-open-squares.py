"""Original illustration; Python 3.14, NumPy 2.3, Matplotlib 3.10. Output in CWD."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

def b(s):
    s = s % 4
    if s <= 1: return np.array([s, 1.])
    if s <= 2: return np.array([1., 2-s])
    if s <= 3: return np.array([3-s, 0.])
    return np.array([0., s-3])

def phi(s): return 2*s if s <= 1 else 2+2*(s-1)/3

fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), facecolor='white')
c = np.array([.5, .5])
for j, ax in enumerate(axes):
    ax.fill([0,1,1,0],[0,0,1,1], color='#f3f8fc')
    ax.plot([0,1,1,0,0],[0,0,1,1,0], color='#333333', lw=2)
    omitted = np.array([b(s) for s in np.linspace(0, 1 if j == 0 else 2, 161)])
    ax.plot(omitted[:,0], omitted[:,1], color='#c73932', lw=4, ls='--')
    for s in [.2,.55,.9,1.4,2.3,3.2]:
        p = b(s if j == 0 else phi(s))
        ax.plot([c[0],p[0]],[c[1],p[1]], color='#267ca9', lw=1.2, alpha=.8)
        ax.plot(*(c+.6*(p-c)), 'o', color='#267ca9', ms=4)
    ax.plot(*c, 'o', color='#222222', ms=4)
    ax.text(.53,.48,'$c$', fontsize=12)
    ax.set(xlim=(-.12,1.12), ylim=(-.12,1.12), aspect='equal')
    ax.axis('off')
axes[0].set_title(r'$[0,1]\times[0,1)$: omit the top edge', fontsize=13)
axes[1].set_title(r'$[0,1)\times[0,1)$: omit top and right', fontsize=13)
fig.suptitle('Extend the boundary map along rays from the centre', fontsize=15)
fig.text(.5,.03,r'Boundary parameter: $s\mapsto 2s$ on $[0,1]$, then $s\mapsto2+\frac{2}{3}(s-1)$', ha='center', fontsize=12)
fig.tight_layout(rect=(0,.09,1,.94))
fig.savefig(Path.cwd() / '2014-half-open-squares.png', dpi=170, facecolor='white')
