"""Illustrate shifted Ewald-sphere samples; original PNG diagram to cwd."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8.8, 6.4), dpi=100, facecolor='white')
ax = fig.add_subplot(111, projection='3d')
phi = np.linspace(0, 2 * np.pi, 80)
for theta, color in [(np.linspace(0, np.pi / 2, 40), '#499ac3'), (np.linspace(np.pi / 2, np.pi, 40), '#d99554')]:
    pp, tt = np.meshgrid(phi, theta)
    x = np.sin(tt) * np.cos(pp)
    y = np.sin(tt) * np.sin(pp)
    z = np.cos(tt) - 1
    ax.plot_surface(x, y, z, color=color, alpha=.28, edgecolor='none', shade=False)
    for angle in [0, np.pi / 2]:
        ax.plot(np.sin(theta) * np.cos(angle), np.sin(theta) * np.sin(angle), np.cos(theta) - 1, color=color, lw=1.5)
ax.plot(np.cos(phi), np.sin(phi), -np.ones_like(phi), color='#495f70', lw=1.2)
ax.scatter([0], [0], [0], s=30, color='#172d41', label='Zero Fourier transfer')
ax.scatter([0], [0], [-1], s=20, color='#444444')
ax.quiver(0, 0, -1, 0, 0, 1, color='#172d41', arrow_length_ratio=.12, linewidth=2)
ax.text(0, 0, -.47, r'$\mathbf{k}_i/k$', color='#172d41', fontsize=12)
ax.set(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), zlim=(-2.2, .2), xlabel=r'$\kappa_x/k$', ylabel=r'$\kappa_y/k$', zlabel=r'$\kappa_z/k$')
ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1]); ax.set_zticks([-2, -1, 0])
ax.set_box_aspect([1, 1, 1.05])
ax.view_init(elev=20, azim=-57)
ax.set_title('One incident direction samples a Fourier surface', fontsize=14, pad=17)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(facecolor='#499ac3', alpha=.6, label='Upper measurement plane'), Patch(facecolor='#d99554', alpha=.6, label='Lower measurement plane')], loc='upper left', fontsize=10)
fig.text(.5, .035, r'$|\boldsymbol{\kappa}+\mathbf{k}_i|=k$   —   unsampled volume remains on either side', ha='center', fontsize=12)
fig.subplots_adjust(left=.025, right=.95, bottom=.12, top=.87)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, facecolor='white', transparent=False)
plt.close(fig)
