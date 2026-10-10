"""Rigid neutral dipole and orientation energy; analytical model, not data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; the PNG is written to the current working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch
import numpy as np

plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'figure.facecolor': 'white'})
fig, (geometry, energy) = plt.subplots(1, 2, figsize=(10, 4.5), layout='constrained')
fig.suptitle('Rigid electric dipole in a uniform external field — analytical model', fontsize=15)
angle = np.deg2rad(50)
u = np.array([np.cos(angle), np.sin(angle)])
minus, plus = -0.8 * u, 0.8 * u
for y in [-1.15, -0.35, 0.45, 1.2]:
    geometry.annotate('', (1.8, y), (-1.8, y),
                      arrowprops={'arrowstyle': '->', 'color': '#d6dee4', 'lw': 1.3}, zorder=0)
geometry.plot([minus[0], plus[0]], [minus[1], plus[1]], color='#5b6570', lw=3)
geometry.scatter(*minus, s=520, color='#2879aa', zorder=4)
geometry.scatter(*plus, s=520, color='#c44335', zorder=4)
for pos, label in [(minus, r'$-q$'), (plus, r'$+q$')]:
    geometry.text(*pos, label, color='white', ha='center', va='center', fontsize=13, zorder=5)
geometry.annotate('', minus + [-0.8, 0], minus + [-0.12, 0],
                  arrowprops={'arrowstyle': '-|>', 'color': '#2879aa', 'lw': 2.7})
geometry.annotate('', plus + [0.8, 0], plus + [0.12, 0],
                  arrowprops={'arrowstyle': '-|>', 'color': '#c44335', 'lw': 2.7})
geometry.text(-1.55, -0.88, r'$\mathbf{F}_-=-q\mathbf{E}_{\rm ext}$', fontsize=11)
geometry.text(0.58, 0.84, r'$\mathbf{F}_+=q\mathbf{E}_{\rm ext}$', fontsize=11)
offset = np.array([-0.23, 0.19])
geometry.annotate('', plus + offset, minus + offset,
                  arrowprops={'arrowstyle': '-|>', 'color': '#168059', 'lw': 2.5})
geometry.text(-0.83, 0.14, r'$\mathbf{p}=q\mathbf{d}$', color='#168059')
geometry.plot([0, 0.8], [0, 0], ls=':', color='#69737b')
geometry.add_patch(Arc((0, 0), 0.95, 0.95, theta1=0, theta2=50, color='#69737b'))
geometry.text(0.48, 0.16, r'$\theta$')
geometry.add_patch(FancyArrowPatch((0.82, -0.95), (-0.25, -1.05),
                                  connectionstyle='arc3,rad=-0.5', arrowstyle='-|>',
                                  mutation_scale=14, color='#7b4b9b', lw=2))
geometry.text(-0.6, -1.46, 'Clockwise torque; net force = 0', color='#7b4b9b', fontsize=11)
geometry.text(0.9, 1.35, r'$\mathbf{E}_{\rm ext}$ →', color='#69737b')
geometry.set(xlim=(-1.95, 1.95), ylim=(-1.65, 1.75), aspect='equal')
geometry.set_title('Equal opposite forces form a couple')
geometry.axis('off')

theta = np.linspace(-180, 180, 721)
energy.plot(theta, -np.cos(np.deg2rad(theta)), color='#168059', lw=2.7)
energy.scatter([0, 180, -180], [-1, 1, 1], color=['#168059', '#7b4b9b', '#7b4b9b'], zorder=4)
energy.axhline(0, color='#aab2b8', lw=1)
energy.annotate('Parallel: minimum', (0, -1), (0, -0.65), ha='center',
                arrowprops={'arrowstyle': '->', 'color': '#168059'}, fontsize=11)
energy.text(0, 1.1, 'Antiparallel: maximum at ±180°', ha='center', fontsize=11)
energy.set(xlim=(-190, 190), ylim=(-1.18, 1.35), xlabel=r'Angle $\theta$ (degrees)',
           ylabel=r'$U/(pE_{\rm ext})$', title=r'$U=-pE_{\rm ext}\cos\theta$')
energy.set_xticks([-180, -90, 0, 90, 180])
energy.grid(alpha=0.2)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', transparent=False)
plt.close(fig)
