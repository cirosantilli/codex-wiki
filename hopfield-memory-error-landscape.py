"""Exact single-pattern Hopfield recall; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
from itertools import product
from math import comb
import matplotlib.pyplot as plt
import numpy as np

xi = np.array([1, -1, 1, -1, 1])
w = np.outer(xi, xi) / 5
np.fill_diagonal(w, 0)
energy = lambda x: -float(x @ w @ x) / 2
states = np.array(list(product([-1, 1], repeat=5)))
for x in states:
    d = np.count_nonzero(x != xi)
    assert np.isclose(energy(x), -((5 - 2*d)**2 - 5)/10)
    for k in range(5):
        y = x.copy()
        y[k] *= -1
        assert np.isclose(energy(y)-energy(x), -(y[k]-x[k])*(w @ x)[k])
cue = np.array([-1, 1, 1, -1, 1])
trajectory = [cue.copy()]
for k in (0, 1):
    cue[k] = 1 if (w @ cue)[k] > 0 else -1
    trajectory.append(cue.copy())
assert np.array_equal(cue, xi)

plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 4.8), gridspec_kw={'width_ratios': [1.2, 1]})
fig.patch.set_facecolor('white')
d = np.arange(6)
e = -((5-2*d)**2-5)/10
ax.plot(d, e, color='#8795a1', lw=1.6, zorder=1)
ax.scatter(d, e, s=85, color='#355c87', zorder=3)
for k in (2, 1):
    ax.annotate('', xy=(k-1, e[k-1]), xytext=(k, e[k]), arrowprops={'arrowstyle': '-|>', 'color': '#dc6b20', 'lw': 2.8, 'shrinkA': 8, 'shrinkB': 8})
for k in range(6):
    ax.annotate(f'{comb(5,k)} state' + ('s' if comb(5,k)>1 else ''), (k, e[k]), xytext=(0, 15), textcoords='offset points', ha='center', fontsize=9)
ax.set(xlabel=r'Wrong bits relative to $\xi$: Hamming distance $d$', ylabel='Energy E', xticks=d, ylim=(-2.45, 1.05), title='All 32 states, grouped by error count')
ax.text(0, -2.33, r'$\xi$', ha='center', color='#355c87')
ax.text(5, -2.33, r'$-\xi$', ha='center', color='#355c87')
ax.grid(axis='y', alpha=.18)
a = np.array(trajectory)
bx.imshow(a, cmap=plt.matplotlib.colors.ListedColormap(['#dce7f0', '#355c87']), vmin=-1, vmax=1, aspect='auto')
for i in range(3):
    for j in range(5):
        bx.text(j,i,'+' if a[i,j]>0 else '−',ha='center',va='center',color='white' if a[i,j]>0 else '#233444',fontsize=21)
bx.set(xticks=range(5), xticklabels=range(1,6), yticks=range(3), yticklabels=['Cue: 2 wrong','Flip unit 1','Flip unit 2'], xlabel='Unit', title='One asynchronous retrieval')
bx.set_xticks(np.arange(-.5,5,1),minor=True)
bx.set_yticks(np.arange(-.5,3,1),minor=True)
bx.grid(which='minor',color='white',lw=2)
bx.tick_params(which='minor',bottom=False,left=False)
fig.suptitle('A stored pattern creates a basin of attraction',fontsize=15)
fig.text(.5,.025,'Orange arrows: E = 2/5 → −2/5 → −2.  The opposite pattern is a second stable memory.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.06,1,.93),w_pad=2)
fig.savefig(Path(__file__).stem+'.png',dpi=120,facecolor='white')
