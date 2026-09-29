"""Original fixed-pivot wheel and angular-momentum geometry. Python 3.14.

Run from _media with MPLBACKEND=Agg. Uses matplotlib 3.10.7/numpy 2.3.5.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Arc

BLUE = '#1266a4'
RED = '#b72a30'
GREEN = '#238249'
fig, (ax, top) = plt.subplots(1, 2, figsize=(10, 4.6), facecolor='white')
fig.suptitle('A spinning wheel: force, torque and precession', fontsize=16)
ax.set(xlim=(-.6, 3.6), ylim=(-1.1, 2.6), aspect='equal')
ax.axis('off')
# Side view is the xz plane; +y goes into the page.
pivot = np.array([0., .25])
e = np.array([np.sin(np.pi/3), np.cos(np.pi/3)])
centre = pivot + 2.1*e
ax.plot([-.45, .45], [-.4, -.4], color='gray', lw=6)
ax.plot([0, 0], [-.4, .25], color='gray', lw=5)
ax.plot(*zip(pivot, centre+.45*e), color='gray', lw=4)
ax.add_patch(Ellipse(centre, width=.58, height=1.42, angle=-30,
                     fc='#eef5fa', ec=BLUE, lw=3))
ax.plot(*pivot, 'ko', ms=7)
ax.plot(*centre, 'ko', ms=4)
ax.text(-.08, .07, r'$O$: fixed socket', ha='right', fontsize=11)
ax.text(centre[0]+.1, centre[1]-.2, 'centre of mass', fontsize=11)
def arrow(ax, start, end, color, lw=2.5):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='-|>', color=color, lw=lw))
arrow(ax, pivot, pivot+np.array([0, 2.1]), 'black', 1.5)
ax.text(-.08, 2.38, r'$+z$', fontsize=12)
arrow(ax, pivot, pivot+np.array([.7, 0]), 'black', 1.5)
ax.text(.72, .12, r'$+x$', fontsize=12)
arrow(ax, pivot+.07*np.array([-e[1], e[0]]), centre+.65*e, BLUE)
ax.text(2.35, 2.04, r'$L_s\hat{\mathbf{e}}$', color=BLUE, fontsize=13)
ax.text(.69, .92, r'$\mathbf{r}=d\hat{\mathbf{e}}$', color=BLUE, rotation=30, fontsize=12)
arrow(ax, centre, centre+np.array([0, -1.45]), RED)
ax.text(centre[0]+.12, -.31, r'$\mathbf{F}_g=-Mg\hat{\mathbf{z}}$', color=RED, fontsize=12)
ax.add_patch(Arc(pivot, .85, .85, theta1=30, theta2=90, color='black'))
ax.text(.22, .77, r'$\theta$', fontsize=13)
ax.plot(.52, 2.2, marker='x', color=GREEN, ms=9, mew=2)
ax.add_patch(plt.Circle((.52, 2.2), .14, fill=False, ec=GREEN, lw=1.5))
ax.text(.78, 2.17, r'$\tau$: into page ($+y$)', color=GREEN, fontsize=11)
ax.set_title('Side view: axle tilted 60° from vertical', fontsize=12)
# View from +z: the circle is the horizontal projection of the L-tip cone.
top.set(xlim=(-1.5, 1.6), ylim=(-1.5, 1.6), aspect='equal')
top.axis('off')
a = np.linspace(0, 2*np.pi, 200)
top.plot(np.cos(a), np.sin(a), '--', color='gray', lw=1.5)
top.plot(0, 0, 'ko', ms=5)
arrow(top, (0, 0), (1, 0), BLUE)
phi = .33
arrow(top, (0, 0), (np.cos(phi), np.sin(phi)), '#80b2d3', 2)
arrow(top, (1, 0), (1, .67), GREEN)
top.text(1.07, .64, r'$\tau\,dt$', color=GREEN, fontsize=13)
top.text(.38, -.17, r'$L_s\sin\theta$', color=BLUE, fontsize=13)
angles = np.linspace(.65, 1.62, 40)
top.plot(1.22*np.cos(angles), 1.22*np.sin(angles), color=GREEN, lw=2)
arrow(top, (1.22*np.cos(angles[-2]), 1.22*np.sin(angles[-2])),
      (1.22*np.cos(angles[-1]), 1.22*np.sin(angles[-1])), GREEN, 2)
top.text(-1.42, 1.23, r'$\Omega>0$: counterclockwise', color=GREEN, fontsize=11)
top.text(0, -1.42, 'Reverse spin → reverse slow precession', ha='center', fontsize=11)
top.set_title(r'Top view: horizontal projection of $\mathbf{L}$', fontsize=12)
fig.text(.5, .03, 'Original schematic • not to scale • spin-dominated angular momentum', ha='center', fontsize=11)
fig.subplots_adjust(left=.07, right=.97, bottom=.15, top=.8, wspace=.25)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=130, facecolor='white')
plt.close(fig)
