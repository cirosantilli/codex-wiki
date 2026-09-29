"""Original spherical-micelle schematic. Python 3.14; NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

fig, ax = plt.subplots(figsize=(8.0, 4.7), facecolor='white')
ax.set_facecolor('white')
radius = .72
ax.add_patch(Circle((0, 0), .86, color='#e9f5fb', zorder=0))
ax.add_patch(Circle((0, 0), radius, color='#f6ead6', zorder=1))
for angle in np.linspace(0, 2*np.pi, 18, endpoint=False):
    radial = np.array([np.cos(angle), np.sin(angle)])
    tangent = np.array([-np.sin(angle), np.cos(angle)])
    r = np.linspace(.17, radius-.04, 12)
    wobble = .022*np.sin(np.arange(12)*np.pi/2)
    tail = r[:, None]*radial + wobble[:, None]*tangent
    ax.plot(*tail.T, color='#a86630', linewidth=1.8, zorder=2)
    ax.add_patch(Circle(radius*radial, .055, facecolor='#2a80b5', edgecolor='#185677', linewidth=.7, zorder=3))
ax.plot(0, 0, '.', color='#222222', markersize=5, zorder=4)
ax.annotate('', xy=(radius, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='<->', color='#222222'), zorder=5)
ax.text(.36, .06, r'$r_c=0.72\ \mathrm{nm}$', ha='center', fontsize=10,
        bbox=dict(facecolor='white', edgecolor='none', alpha=.9), zorder=6)
ax.annotate('hydrated heads\ncontact water', xy=(.51, .51), xytext=(1.05, .59), fontsize=11,
            arrowprops=dict(arrowstyle='->', color='#27678d'), color='#185677')
ax.annotate('hydrophobic\ntail-rich core', xy=(.37, -.32), xytext=(1.05, -.16), fontsize=11,
            arrowprops=dict(arrowstyle='->', color='#a86630'), color='#8a5026')
ax.text(1.05, -.62, r'$P=0.267<1/3$'+'\n'+r'$r_c<\ell=0.90\ \mathrm{nm}$', fontsize=12)
ax.text(-.9, -.94, 'Cross-section; molecule count is schematic', fontsize=9, color='#555555')
ax.set(xlim=(-1.05, 2.36), ylim=(-1.05, 1.03), aspect='equal')
ax.set_axis_off()
ax.set_title('Spherical micelle: compatible head and tail packing', fontsize=14, pad=15)
fig.subplots_adjust(left=.03, right=.98, bottom=.06, top=.86)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
plt.close(fig)
