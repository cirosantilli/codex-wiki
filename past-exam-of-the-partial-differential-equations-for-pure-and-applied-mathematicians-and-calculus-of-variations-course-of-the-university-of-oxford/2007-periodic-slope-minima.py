"""Original periodic-slope energy illustration; output PNG in the current directory.

Tested with Python 3.14, NumPy 2.3 and Matplotlib 3.10; root pyproject.toml records dependencies.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

delta = .6
x = np.linspace(0, 1, 1201)
u = np.where(x <= 1-delta/4, delta*x, (4-delta)*(1-x))
global_u = 4*np.minimum(x, 1-x)
v = np.linspace(-4.9, 1.8, 1400)
g = lambda v: -np.cos(np.pi*v/2)
gp = lambda v: np.pi/2*np.sin(np.pi*v/2)
fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 3.9), facecolor='white')
ax.plot(x, global_u, color='#2d8161', lw=2, label='global minimum')
ax.plot(x, u, color='#2465a5', lw=2.5, label='strict weak minimum')
ax.set(xlabel='x', ylabel='u(x)', xlim=(0, 1), ylim=(-.08, 2.15))
ax.set_title('Different slopes, different minimum notions')
ax.legend(frameon=False, loc='upper left', fontsize=9)
ax.text(.59, .68, r'$\delta=0.6$', color='#2465a5')
bx.plot(v, g(v), color='#3f4650', lw=2)
for s0 in [delta-4, delta]:
    near = np.linspace(s0-.58, s0+.58, 90)
    bx.axvspan(s0-.18, s0+.18, color='#dcecf8', alpha=.8)
    bx.plot(near, g(s0)+gp(s0)*(near-s0), '--', color='#b8782f', lw=1.5)
    bx.scatter([s0], [g(s0)], color='#2465a5', zorder=4, s=38)
bx.scatter([-4, 0], [-1, -1], color='#2d8161', zorder=4, s=38)
bx.axhline(0, color='#d5d8dc', lw=.7)
bx.set(xlabel='slope v', ylabel='g(v)', xlim=(-4.9, 1.8), ylim=(-1.25, 1.18))
bx.set_xticks([-4, delta-4, 0, delta], ['-4', r'$\delta-4$', '0', r'$\delta$'])
bx.set_title(r'$g(v)=-\cos(\pi v/2)$')
bx.text(-2.9, -1.17, 'local convexity at both blue slopes', color='#2465a5', fontsize=9)
for panel in [ax, bx]:
    panel.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig('2007-periodic-slope-minima.png', dpi=145, facecolor='white', bbox_inches='tight')
plt.close(fig)
