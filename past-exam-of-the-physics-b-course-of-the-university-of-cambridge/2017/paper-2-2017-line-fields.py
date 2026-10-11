"""Original TEM cross-sections, Python 3.14; pyproject.toml dependencies.
Writes PNG basename in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10, 4.9), facecolor='white', layout='constrained')
blue, orange = '#176a98', '#bd6720'
ax = axes[0]
ax.add_patch(Circle((0, 0), 2.4, fill=False, color='0.35', lw=4))
ax.add_patch(Circle((0, 0), .75, color='0.85', ec='0.35', lw=2))
for angle in np.linspace(0, 2*np.pi, 12, endpoint=False):
    start = 1.0*np.array([np.cos(angle), np.sin(angle)])
    end = 2.15*np.array([np.cos(angle), np.sin(angle)])
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=10, color=blue, lw=1.3))
for angle in [0.3, 1.8, 3.3, 4.8]:
    start = 1.55*np.array([np.cos(angle), np.sin(angle)])
    end = 1.55*np.array([np.cos(angle+.7), np.sin(angle+.7)])
    ax.add_patch(FancyArrowPatch(start, end, connectionstyle='arc3,rad=.17', arrowstyle='-|>', mutation_scale=13, color=orange, lw=2))
ax.text(0, 0, r'$\odot\,I$', ha='center', va='center', fontsize=15)
ax.text(2.0, 2.05, 'Return $-I$', ha='center')
ax.set(title='Coaxial line', xlim=(-2.8, 2.8), ylim=(-2.8, 2.8), aspect='equal')
ax = axes[1]
for yy, label in [(1.4, '$+V/2$, current $\\odot$'), (-1.4, '$-V/2$, return $\\otimes$')]:
    ax.add_patch(Rectangle((-2.4, yy-.07), 4.8, .14, color='0.4'))
    ax.text(0, yy+(.26 if yy > 0 else -.46), label, ha='center')
for xx in np.linspace(-2, 2, 6):
    ax.annotate('', xy=(xx, -.95), xytext=(xx, .95), arrowprops=dict(arrowstyle='-|>', color=blue, lw=1.4))
for yy in [-.5, .5]:
    ax.annotate('', xy=(1.8, yy), xytext=(-1.8, yy), arrowprops=dict(arrowstyle='-|>', color=orange, lw=2))
ax.set(title='Wide parallel plates', xlim=(-2.8, 2.8), ylim=(-2.8, 2.8), aspect='equal')
for ax in axes:
    ax.axis('off')
fig.suptitle('Cross-sections: electric field E (blue), magnetic field H (orange)\nPropagation and energy flux are out of the page', fontsize=12)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=160, facecolor='white')
plt.close(fig)
