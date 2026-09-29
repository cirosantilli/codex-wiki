"""Original Q3 sketch. Run in the mirrored _media directory; writes only to cwd.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (root pyproject.toml).
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
t = np.linspace(-np.pi, np.pi, 241)
v = np.linspace(0, 1, 45)
tt, vv = np.meshgrid(t, v)
zz = vv * np.cosh(tt)
fig = plt.figure(figsize=(10, 4.6), layout='constrained')
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(np.cos(tt), np.sin(tt), zz, color='#72b7ce', alpha=.23,
                linewidth=0, shade=False, rstride=3, cstride=5)
# Thin constant-height rings and generators show the cylindrical surface S.
for z in [0, 4, 8, 12]:
    ax.plot(np.cos(t), np.sin(t), np.full_like(t, z), color='#8a939b', lw=.7, alpha=.55)
for a in np.linspace(-np.pi, np.pi, 9)[:-1]:
    ax.plot([np.cos(a)]*2, [np.sin(a)]*2, [0, 12], color='#8a939b', lw=.5, alpha=.35)
ax.plot(np.cos(t), np.sin(t), np.cosh(t), color='#b33235', lw=2.6, label=r'$C: z=\cosh t$')
ax.scatter([-1, 1], [0, 0], [np.cosh(np.pi), 1], color='#b33235', s=25)
ax.text(-1, 0, np.cosh(np.pi)+.4, 'joined endpoints', fontsize=9)
ax.set(xlabel='$x$', ylabel='$y$', zlabel='$z$', zlim=(0, 12.8),
       title='One turn around the unit cylinder')
ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1]); ax.set_zticks([0, 4, 8, 12])
ax.set_box_aspect((1, 1, 1.65))
ax.view_init(elev=22, azim=42)
ax.legend(loc='upper left', frameon=False)
bx = fig.add_subplot(122)
bx.fill_between(t, 0, np.cosh(t), color='#72b7ce', alpha=.3)
bx.plot(t, np.cosh(t), color='#b33235', lw=2.5)
bx.plot([-np.pi, -np.pi], [0, np.cosh(np.pi)], '--', color='#59656d', lw=1)
bx.plot([np.pi, np.pi], [0, np.cosh(np.pi)], '--', color='#59656d', lw=1)
bx.scatter([0], [1], color='#b33235', s=25)
bx.text(0, 5.5, r'area $=\int_{-\pi}^{\pi}\cosh t\,dt$'+'\n'+r'$=2\sinh\pi$', ha='center')
bx.text(0, 11.7, 'Left and right edges are identified', ha='center', fontsize=9)
bx.set(xlabel='$t$', ylabel='$z$', xlim=(-3.4, 3.4), ylim=(0, 12.8), title='The shaded patch unrolled')
bx.set_xticks([-np.pi, 0, np.pi], [r'$-\pi$', '$0$', r'$\pi$'])
bx.spines[['top', 'right']].set_visible(False)
bx.grid(alpha=.2)
fig.savefig('mathematics-v-cylinder-curve.png', dpi=135, facecolor='white', transparent=False)
plt.close(fig)
