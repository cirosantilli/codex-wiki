"""Original Neumann image-lattice illustration; Python 3.14, NumPy, Matplotlib.

Run with cwd equal to the mirrored _media paper directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10.2, 3.5), facecolor='white', gridspec_kw={'width_ratios': [1.35, 1]})
ax = axes[0]
ax.axvspan(-1, 1, color='#e9f3fc')
for wall in [-1, 1]:
    ax.axvline(wall, color='#334155', lw=1.8)
for n in range(-2, 3):
    color = '#be123c' if n == 0 else '#2563eb'
    ax.scatter([2*n], [0], color=color, s=70, zorder=3)
    ax.annotate('$q$', (2*n, 0), xytext=(0, 12), textcoords='offset points', ha='center', color=color, fontsize=12)
ax.text(0, -.52, 'physical strip', ha='center', fontsize=10, color='#334155')
ax.text(-4.7, 0, r'$\cdots$', ha='center', fontsize=15)
ax.text(4.7, 0, r'$\cdots$', ha='center', fontsize=15)
ax.set(xlim=(-5, 5), ylim=(-.9, .9), yticks=[], xticks=[-4,-2,-1,0,1,2,4], xticklabels=['$-4b$','$-2b$','$-b$','0','$b$','$2b$','$4b$'], title='Equal-sign image lattice')
ax.set_xlabel('$x$ (all sources lie at $y=0$)')
ax.spines[['top','left','right']].set_visible(False)
ax = axes[1]
x = np.linspace(-1, 1, 301)
y = np.linspace(-1.65, 1.65, 401)
xx, yy = np.meshgrid(x, y)
f = np.cosh(np.pi*yy)-np.cos(np.pi*xx)
v = np.log(np.maximum(f, 1e-12))/(4*np.pi)
v = np.ma.masked_where(xx**2+yy**2 < .035**2, v)
cs = ax.contour(xx, yy, v, levels=[-.3,-.18,-.08,0,.08,.16,.24,.32], colors='#2563eb', linewidths=1.1)
ax.axvline(-1, color='#334155', lw=1.8)
ax.axvline(1, color='#334155', lw=1.8)
ax.scatter([0],[0],s=30,color='#be123c',zorder=4)
ax.set(xlim=(-1.17,1.17), ylim=(-1.7,1.7), xlabel='$x/b$', ylabel='$y/b$', title='Potential contours inside the strip')
ax.set_aspect('equal')
ax.spines[['top','right']].set_visible(False)
fig.subplots_adjust(left=.04,right=.96,bottom=.22,top=.86,wspace=.3)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=155, facecolor='white')
plt.close(fig)
