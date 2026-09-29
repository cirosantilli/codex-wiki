"""Original cone/cylinder sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes its PNG basename to cwd and respects an existing MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8.8, 4), dpi=100, facecolor='white')
ax = fig.add_subplot(121, projection='3d')
theta, radius = np.meshgrid(np.linspace(0, 2*np.pi, 49), np.linspace(0, 1, 20))
x, y = radius*np.cos(theta), radius*np.sin(theta)
for sign in [-1, 1]:
    ax.plot_surface(x, y, sign*radius, color='#6ca6ca', alpha=.65, linewidth=0)
angles, z = np.meshgrid(np.linspace(0, 2*np.pi, 49), np.linspace(-1, 1, 15))
ax.plot_wireframe(np.cos(angles), np.sin(angles), z, rstride=4, cstride=8, color='#ad7031', linewidth=.7)
ax.set(xlabel='x', ylabel='y', zlabel='z', xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), zlim=(-1.1, 1.1), title='Two cones closed by the cylinder')
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=19, azim=-50)
ax2 = fig.add_subplot(122)
r = np.linspace(0, 1, 100)
for sign in [-1, 1]:
    ax2.fill_between(sign*r, -r, r, color='#c7e0ef')
    ax2.plot(sign*r, r, color='#287aa5', lw=2)
    ax2.plot(sign*r, -r, color='#287aa5', lw=2)
    ax2.plot([sign, sign], [-1, 1], color='#ad7031', lw=2)
ax2.axhline(0, color='gray', lw=.6)
ax2.axvline(0, color='gray', lw=.6)
ax2.text(.46, 0, 'V', ha='center', fontsize=16)
ax2.set(xlabel='x (section y = 0)', ylabel='z', xlim=(-1.2,1.2), ylim=(-1.2,1.2), title=r'Meridional section: $|z|\leq |x|\leq1$')
ax2.set_aspect('equal')
fig.subplots_adjust(left=.01, right=.97, bottom=.13, top=.87, wspace=.2)
fig.savefig('paper-3-cone-cylinder.png', facecolor='white', transparent=False, dpi=100)
plt.close(fig)
