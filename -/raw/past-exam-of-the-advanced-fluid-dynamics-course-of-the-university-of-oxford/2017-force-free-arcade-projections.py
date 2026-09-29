"""Original linear force-free arcade projections; Python 3.14, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False})
k = np.pi
lam = .6*k
q = .8*k
fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.4), constrained_layout=True, facecolor='white')
colors = ['#1864ab', '#d9480f', '#2b8a3e', '#862e9c']
for j, (s, color) in enumerate(zip([.18, .34, .52, .72], colors)):
    xm = np.arcsin(s)/k
    xp = 1-xm
    x = np.linspace(xm, xp, 501)
    z = np.log(np.sin(k*x)/s)/q
    y = .15*j + (lam/q)*(x-xm)
    for ax, ordinate in zip(axes, [z, y]):
        ax.plot(x, ordinate, color=color, lw=2.1, label=f's = {s:.2f}')
        ix = 155
        ax.annotate('', xy=(x[ix+15], ordinate[ix+15]), xytext=(x[ix], ordinate[ix]), arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 1.8})
        ax.plot([xm, xp], [ordinate[0], ordinate[-1]], 'o', color=color, ms=4)
for ax in axes:
    ax.axvline(0, color='.6', lw=1, ls=':')
    ax.axvline(1, color='.6', lw=1, ls=':')
    ax.set_xlim(-.03, 1.03)
    ax.set_xlabel(r'$x/a$')
    ax.grid(alpha=.18)
axes[0].axhline(0, color='.3', lw=1)
axes[0].set_ylim(-.035, .76)
axes[0].set_ylabel(r'$z/a$')
axes[0].set_title('Vertical projection: flux-function contours')
axes[0].text(.02, .72, r'$\lambda/k=0.6,\quad q/k=0.8$', fontsize=11)
axes[0].text(.13, .035, r'$B_z>0$', fontsize=11)
axes[0].text(.69, .035, r'$B_z<0$', fontsize=11)
axes[0].legend(loc='upper right', frameon=False, fontsize=10)
axes[1].set_ylim(-.04, 1.05)
axes[1].set_ylabel(r'$y/a$')
axes[1].set_title('Horizontal projection: sheared connections')
axes[1].text(.07, .95, r'$dy/dx=\lambda/q=0.75$', fontsize=11)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=130, facecolor='white', transparent=False)
plt.close(fig)
