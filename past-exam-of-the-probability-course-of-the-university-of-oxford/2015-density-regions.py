"""Original illustrations of two probability supports; write PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.3), dpi=100)
grid = np.linspace(-2.6, 2.6, 251)
x, y = np.meshgrid(grid, grid)
left.contour(x, y, np.exp(-(x*x+y*y)/2)/(2*np.pi), levels=[.01, .03, .07, .12], colors=['#b9c2cd'], linewidths=1)
left.add_patch(Wedge((0, 0), 3.6, 45, 135, facecolor='#6baed6', alpha=.45, edgecolor='none'))
left.plot([0, 2.6], [0, 2.6], color='#2166ac')
left.plot([0, -2.6], [0, 2.6], color='#2166ac')
left.axhline(0, color='#444444', linewidth=.7)
left.axvline(0, color='#444444', linewidth=.7)
left.text(0, 1.8, r'$Y>|X|$', ha='center')
left.text(0, 1.3, r'angle $\pi/2$', ha='center')
left.text(0, .84, r'probability $1/4$', ha='center')
left.text(2.2, 2.5, r'$y=x$', ha='right')
left.text(-2.2, 2.5, r'$y=-x$', ha='left')
left.set(xlim=(-2.6, 2.6), ylim=(-2.6, 2.6), xlabel=r'$x$', ylabel=r'$y$', title='Independent standard normal coordinates')
left.set_aspect('equal')

u = np.linspace(0, 3.0, 101)
right.fill_between(u, u, 2*u, color='#9ecae1', alpha=.8)
right.plot(u, u, color='#2166ac')
right.plot(u, 2*u, color='#2166ac')
u0 = 1.7
right.plot([u0, u0], [u0, 2*u0], color='#cb181d', linewidth=3)
right.plot([u0, u0], [0, u0], ':', color='#999999')
right.scatter([u0, u0], [u0, 2*u0], facecolors='white', edgecolors='#cb181d', zorder=5)
right.text(2.8, 5.85, r'$v=2u$', ha='right')
right.text(2.8, 2.55, r'$v=u$', ha='right')
right.text(2.1, 3.6, r'$u<v<2u$')
right.text(.08, 5.2, r'given $U=u_0$:')
right.annotate('', xy=(u0, 2.55), xytext=(.75, 4.2),
               arrowprops={'arrowstyle':'->', 'color':'#444444'})
right.text(.08, 4.7, r'$V$ is uniform on $(u_0,2u_0)$')
right.set_xticks([0, 1, u0, 2, 3], ['0', '1', r'$u_0$', '2', '3'])
right.set(xlim=(0, 3.05), ylim=(0, 6.15), xlabel=r'$u$', ylabel=r'$v$', title=r'$U=X+Y,\quad V=X+2Y$; positive $X,Y$')
for ax in (left, right):
    ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout(pad=1.5)
fig.savefig(Path.cwd()/'2015-density-regions.png', facecolor='white', transparent=False)
