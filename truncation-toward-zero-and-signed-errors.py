"""Truncation's sign-dependent steps and discarded fractional differences.

Output: matching opaque white PNG in CWD. See pyproject.toml for versions.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), dpi=120, facecolor='white')
for ax in axes:
    ax.set_facecolor('white')
    ax.grid(alpha=0.17)
    ax.axhline(0, color='#626c72', lw=0.8)
    ax.axvline(0, color='#626c72', lw=0.8)
    ax.set(xlim=(-3.5, 3.5), xticks=range(-3, 4), xlabel='Real input x')
for m in range(-3, 4):
    left, right = ((m-1, m) if m<0 else ((m, m+1) if m>0 else (-1, 1)))
    axes[0].plot([left, right], [m, m], color='#286f99', lw=2.3)
    axes[0].scatter([left, right], [m, m], s=37, facecolors='white', edgecolors='#286f99', zorder=4)
# Each integer maps to itself; zero is interior to the flat central segment.
axes[0].scatter(range(-3, 4), range(-3, 4), s=37, color='#286f99', zorder=6)
axes[0].set(ylim=(-3.7, 3.7), ylabel='Integer result trunc(x)', title='Discard magnitude, then restore the sign')
axes[0].annotate('Zero throughout (−1, 1)', (0.45, 0), xytext=(-1.9, 1.5), fontsize=10,
                 arrowprops={'arrowstyle': '->', 'color': '#286f99'})
# Plot intervals separately so no vertical segment implies intermediate outputs.
for k in range(-4, 4):
    x=np.linspace(k, k+1, 160)
    axes[1].plot(x, x-k, color='#bb7044', lw=1.5, alpha=0.8)
    axes[1].scatter([k], [0], s=25, color='#bb7044', zorder=4)
    axes[1].scatter([k+1], [1], s=25, facecolors='white', edgecolors='#bb7044', zorder=4)
for m in range(-3, 4):
    left,right=((m-1,m) if m<0 else ((m,m+1) if m>0 else (-1,1)))
    x=np.linspace(left,right,160)
    axes[1].plot(x,x-m,color='#286f99',lw=2.4)
    axes[1].scatter([left,right],[left-m,right-m],s=32,facecolors='white',edgecolors='#286f99',zorder=5)
axes[1].scatter(range(-3,4),np.zeros(7),s=32,color='#286f99',zorder=6)
axes[1].plot([],[],color='#286f99',lw=2.4,label='x − trunc(x): signed difference')
axes[1].plot([],[],color='#bb7044',lw=1.5,label='x − floor(x): fractional part')
axes[1].set(ylim=(-1.55,1.45),ylabel='Discarded difference',title='Negative inputs separate the two conventions')
axes[1].legend(loc='lower right',fontsize=8.6,framealpha=0.97)
fig.text(0.5,0.025,'Both differences have absolute value less than 1; only the floor-based fractional part is always nonnegative.',
         ha='center',fontsize=9.5)
fig.subplots_adjust(left=0.065,right=0.98,top=0.9,bottom=0.17,wspace=0.28)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white')
plt.close(fig)
