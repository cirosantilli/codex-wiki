"""Original Weyl cone, spin textures and shifted-node cuts; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(11, 7.7), layout='constrained')
gs = fig.add_gridspec(2, 3, height_ratios=[1, 1.35])
cut = fig.add_subplot(gs[0, 0])
k = np.linspace(-2.2, 2.2, 500)
for sign, color in [(1, '#2563eb'), (-1, '#d97706')]:
    cut.plot(k, sign*np.abs(k), color=color, lw=2)
cut.axhline(0, color='#94a3b8', lw=.8)
cut.axvline(0, color='#94a3b8', lw=.8)
cut.set(xlabel=r'$k_x$', ylabel=r'$E$ (units $\hbar v=1$)', title='Unperturbed, ky = kz = 0')
cut.grid(alpha=.15)
for col, sign, label, color in [(1, 1, 'Upper branch: spin outwards', '#2563eb'), (2, -1, 'Lower branch: spin inwards', '#d97706')]:
    ax = fig.add_subplot(gs[0, col])
    angles = np.linspace(0, 2*np.pi, 12, endpoint=False)
    for radius in [.65, 1.35]:
        x, y = radius*np.cos(angles), radius*np.sin(angles)
        ax.scatter(x, y, s=6, color='#334155')
        ax.quiver(x, y, sign*np.cos(angles), sign*np.sin(angles), color=color, angles='xy', scale_units='xy', scale=2.8, width=.009, pivot='mid')
    ax.set(xlim=(-1.8, 1.8), ylim=(-1.8, 1.8), xlabel=r'$k_x$', ylabel=r'$k_y$', aspect='equal', title=label)
    ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1]); ax.grid(alpha=.15)

# Illustrative perturbation b=(-0.7,0.4,0.8), d=0.3, hbar v=1.
# Plot the ky=-0.4 plane, which contains the shifted node.
x = np.linspace(-1.5, 2.9, 70)
z = np.linspace(-2.8, 1.2, 70)
X, Z = np.meshgrid(x, z)
D = np.sqrt((X-.7)**2+(Z+.8)**2)
cone = fig.add_subplot(gs[1, :2], projection='3d')
cone.plot_surface(X, Z, .3+D, color='#60a5fa', alpha=.55, linewidth=0)
cone.plot_surface(X, Z, .3-D, color='#fbbf24', alpha=.5, linewidth=0)
cone.scatter([.7], [-.8], [.3], color='#dc2626', s=40, depthshade=False)
cone.set(xlabel=r'$k_x$', ylabel=r'$k_z$', zlabel=r'$E$', title='Shifted cone in plane ky = −0.4: node at (0.7, −0.8)')
cone.view_init(elev=19, azim=-65)
cone.set_box_aspect((1.2,1,1))
nodecut = fig.add_subplot(gs[1, 2])
k = np.linspace(-1.3, 2.7, 600)
for sign, color in [(1, '#2563eb'), (-1, '#d97706')]:
    nodecut.plot(k, .3+sign*np.sqrt((k-.7)**2+.8**2), color=color, lw=2, label='kz = 0' if sign == 1 else None)
    nodecut.plot(k, .3+sign*np.abs(k-.7), color=color, lw=1.5, ls='--', label='kz = −0.8' if sign == 1 else None)
nodecut.annotate('', xy=(.7, 1.1), xytext=(.7,-.5), arrowprops={'arrowstyle':'<->', 'color':'#dc2626','lw':1.6})
nodecut.text(.83, .35, 'gap in\nthis cut', color='#b91c1c', fontsize=9)
nodecut.axhline(.3, color='#94a3b8', lw=.8)
nodecut.set(xlabel=r'$k_x$ at $k_y=-0.4$', ylabel=r'$E$', title='A fixed cut can miss the node')
nodecut.legend(fontsize=9, loc='upper right')
nodecut.grid(alpha=.15)
fig.suptitle('Spin follows the Pauli vector; a constant 2 × 2 perturbation translates the 3D crossing', fontsize=12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
