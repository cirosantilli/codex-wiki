"""Scalar sextic coexistence diagram. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.

Write the PNG basename to cwd; honor the caller's MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5.2), dpi=120, facecolor='white')
ax = fig.add_subplot(121, projection='3d')
U, k = np.meshgrid(np.linspace(-1.2, -0.002, 65), np.linspace(0, 0.25, 36))
s2 = -U / (4 / 3 - 2 * k)
s = np.sqrt(s2)
q = k * s2
R = (s2**2 - s2*q + 3*q*q) / 3
H = s**3 * q / 3
for sign, color in [(1, '#56b4e9'), (-1, '#e69f00')]:
    ax.plot_surface(U, R, sign*H, color=color, alpha=0.62, linewidth=0,
                    antialiased=True, shade=False)
uc = np.linspace(-1.2, 0.5, 90)
rc = np.where(uc < 0, 3*uc**2/16, 0)
ugrid, frac = np.meshgrid(uc, np.linspace(0, 1, 25))
rgrid = -0.18 + frac * (rc[None, :] + 0.18)
ax.plot_surface(ugrid, rgrid, np.zeros_like(rgrid), color='#999999', alpha=0.28,
                linewidth=0, shade=False)
u = np.linspace(-1.2, 0, 100)
ax.plot(u, 3*u*u/16, np.zeros_like(u), color='black', lw=2.3, label='Three-phase line')
for sign in [1, -1]:
    mc = sign*np.sqrt(-3*u/10)
    ax.plot(u, 9*u*u/20, 6*u*u*mc/25, color='#b2182b', lw=2, linestyle='--')
ax.plot([], [], [], color='#b2182b', linestyle='--', label='Wing critical edges')
upos = np.linspace(0, 0.5, 50)
ax.plot(upos, np.zeros_like(upos), np.zeros_like(upos), color='#542788', lw=2.5,
        label='Ordinary critical line')
ax.scatter([0], [0], [0], color='black', marker='*', s=65, depthshade=False)
ax.text(0.03, 0.045, 0.01, 'TCP', fontsize=9)
ax.set(xlabel='Quartic control u', ylabel='Thermal control r', zlabel='Conjugate field h',
       title='Coexistence surfaces (v = 1)', xlim=(-1.2, 0.5), ylim=(-0.18, 0.7),
       zlim=(-0.23, 0.23))
ax.view_init(elev=23, azim=-55)
ax.legend(loc='upper left', fontsize=7.5, framealpha=1)
ax2 = fig.add_subplot(122)
u = np.linspace(-1.2, 0.6, 250)
trans = np.where(u < 0, 3*u*u/16, 0)
ax2.fill_between(u, -0.25, trans, color='#d8e7f3')
ax2.fill_between(u, trans, 0.42, color='#fff0d3')
neg = u <= 0
ax2.plot(u[neg], trans[neg], color='black', lw=2.4, label='First-order transition')
ax2.plot(u[~neg], trans[~neg], color='#542788', lw=2.4, label='Continuous transition')
ax2.scatter([0], [0], s=85, color='black', marker='*', zorder=5)
ax2.annotate('Tricritical point', xy=(0, 0), xytext=(-0.43, 0.11),
             arrowprops={'arrowstyle': '->'}, fontsize=9)
ax2.text(-0.72, -0.14, 'Ordered phases ±m', fontsize=10)
ax2.text(-0.4, 0.31, 'Disordered phase m = 0', fontsize=10)
ax2.set(xlabel='Quartic control u', ylabel='Thermal control r', title='Zero-field section h = 0',
        xlim=(-1.2, 0.6), ylim=(-0.25, 0.42))
ax2.grid(alpha=0.18)
ax2.legend(loc='lower left', fontsize=8.5, framealpha=1)
fig.suptitle('Scalar tricritical phase diagram', fontsize=13)
fig.text(0.5, 0.025, 'The axes are three control parameters, not spatial coordinates.',
         ha='center', fontsize=9)
fig.subplots_adjust(left=0.02, right=0.98, top=0.88, bottom=0.14, wspace=0.3)
fig.savefig('paper-42-tricritical.png', dpi=120, facecolor='white', transparent=False)
plt.close(fig)
