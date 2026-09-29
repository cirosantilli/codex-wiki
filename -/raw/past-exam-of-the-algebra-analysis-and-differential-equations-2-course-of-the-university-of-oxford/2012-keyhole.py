"""Original keyhole schematic. Python 3.14; numpy 2.3.5, matplotlib 3.10.7.
Run from the desired PNG output directory; writes 2012-keyhole.png to CWD.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6.4, 5.2), facecolor='white')
R, rho, eps = 2.05, 0.32, 0.075
blue = '#1965a0'
theta = np.linspace(eps, 2*np.pi-eps, 600)
ax.plot(R*np.cos(theta), R*np.sin(theta), color=blue, lw=2)
ax.plot(rho*np.cos(theta), rho*np.sin(theta), color=blue, lw=2)
for sign in [1, -1]:
    ax.plot([rho*np.cos(eps), R*np.cos(eps)], [sign*rho*np.sin(eps), sign*R*np.sin(eps)], color=blue, lw=2)
for radius, angle, direction in [(R, 1.15, 1), (rho, 3.6, -1)]:
    start = angle-0.14*direction
    end = angle+0.14*direction
    ax.annotate('', (radius*np.cos(end), radius*np.sin(end)), (radius*np.cos(start), radius*np.sin(start)), arrowprops=dict(arrowstyle='->', color=blue, lw=2))
for sign, start, end in [(1, 0.9, 1.35), (-1, 1.35, 0.9)]:
    ax.annotate('', (end*np.cos(eps), sign*end*np.sin(eps)), (start*np.cos(eps), sign*start*np.sin(eps)), arrowprops=dict(arrowstyle='->', color=blue, lw=2))
ax.axhline(0, color='0.8', lw=0.8, zorder=0)
ax.axvline(0, color='0.8', lw=0.8, zorder=0)
ax.plot([0, 2.45], [0, 0], '--', color='#b23b38', lw=1.5)
ax.scatter([0, 0], [1, -1], marker='x', s=65, color='#b23b38', zorder=5)
ax.text(0.12, 1.03, r'$i$', fontsize=13)
ax.text(0.12, -1.15, r'$-i$', fontsize=13)
ax.text(0.9, 0.23, r'$\log x,\quad +\sqrt{x}$', fontsize=12)
ax.text(0.55, -0.48, r'$\log x+2\pi i,\quad -\sqrt{x}$', fontsize=12)
ax.text(-0.23, 0.02, r'$0$', fontsize=11)
ax.text(-0.62, 0.36, r'$\rho$', fontsize=12)
ax.text(-1.8, 1.2, r'$R$', fontsize=12)
ax.text(2.17, -0.15, r'$\mathrm{Re}\,z$', fontsize=11)
ax.text(0.12, 2.16, r'$\mathrm{Im}\,z$', fontsize=11)
ax.set_title(r'Keyhole contour: $0<\arg z<2\pi$', fontsize=14, pad=12)
ax.set_aspect('equal')
ax.set_xlim(-2.3, 2.7)
ax.set_ylim(-2.3, 2.45)
ax.axis('off')
fig.tight_layout()
fig.savefig('2012-keyhole.png', dpi=160, facecolor='white')
