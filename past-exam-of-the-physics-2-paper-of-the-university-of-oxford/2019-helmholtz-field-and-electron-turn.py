"""Original field and orbit diagrams; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False})
fig, (ax, orbit) = plt.subplots(1, 2, figsize=(10, 4.3), layout='constrained', facecolor='white')
z = np.linspace(-0.5, 0.5, 601)
b1 = 0.5 / (1 + (z + 0.5)**2)**1.5
b2 = 0.5 / (1 + (z - 0.5)**2)**1.5
ax.plot(z, b1, '--', label='Left coil', color='#2879b9')
ax.plot(z, b2, ':', label='Right coil', color='#d26b21', linewidth=2)
ax.plot(z, b1 + b2, color='#222222', linewidth=2, label='Total')
ax.set(xlabel=r'Axial position $z/a$', ylabel=r'$B\,/\,(\mu_0 NI/a)$', title=r'Coil centres at $z/a=\pm 0.5$', ylim=(0, 0.8))
ax.legend(loc='lower center')
ax.grid(alpha=0.2)
t = np.linspace(0, np.pi, 401)
orbit.plot(np.sin(t), np.cos(t), color='#215fba', linewidth=2.5)
orbit.plot([-0.8, 0], [1, 1], color='#215fba', linewidth=2.5)
orbit.plot([-0.8, 0], [-1, -1], color='#215fba', linewidth=2.5)
for xy, xytext in [((-0.05, 1), (-0.6, 1)), ((-0.65, -1), (-0.1, -1)), ((0.99, -0.12), (0.99, 0.18))]:
    orbit.annotate('', xy=xy, xytext=xytext, arrowprops={'arrowstyle': '->', 'color': '#215fba', 'lw': 2})
orbit.annotate('', xy=(-0.95, 1), xytext=(-0.95, -1), arrowprops={'arrowstyle': '<->', 'color': '#333333'})
orbit.text(-1.02, 0, '2 cm', rotation=90, ha='right', va='center')
orbit.text(0.35, 0, r'$\otimes\ B$', ha='center', fontsize=20)
orbit.text(0.35, -0.35, 'Into the page', ha='center')
orbit.text(-0.5, 1.13, 'Electron in', ha='center')
orbit.text(-0.5, -1.25, 'Electron out', ha='center')
orbit.set(xlim=(-1.45, 1.35), ylim=(-1.5, 1.5), aspect='equal', title='A 180° electron turn')
orbit.axis('off')
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', transparent=False)
