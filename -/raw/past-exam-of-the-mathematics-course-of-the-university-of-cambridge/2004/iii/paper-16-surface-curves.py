"""Original genus-three double model. Python 3.14; NumPy/Matplotlib root deps.

Writes only paper-16-surface-curves.png in the caller's working directory.
Matplotlib's caller-provided MPLCONFIGDIR is honored without modification.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

fig, ax = plt.subplots(figsize=(10.4, 4.8), facecolor='white')
ax.set_facecolor('white')
outer = Ellipse((0, 0), 10, 4.4, facecolor='#edf2f6', edgecolor='#334155', linewidth=2)
ax.add_patch(outer)
for x in (-3, 0, 3):
    ax.add_patch(Ellipse((x, -0.05), 1.6, 1.05, facecolor='white', edgecolor='#334155', linewidth=1.8))
# One arc runs across the front and the matching return arc across the back.
x0 = -3
outer_y = 2.2 * np.sqrt(1 - (x0 / 5)**2)
hole_y = -0.05 + 1.05 / 2
s = np.linspace(0, 1, 120)
y = hole_y + (outer_y-hole_y)*s
ax.plot(x0 - 0.25*np.sin(np.pi*s), y, color='#c62828', linewidth=2.8)
ax.plot(x0 + 0.25*np.sin(np.pi*s), y, color='#c62828', linewidth=2.5, linestyle=(0,(4,3)))
ax.scatter([x0, x0], [hole_y, outer_y], color='#c62828', s=18, zorder=4)
ax.text(-4.5, 1.12, r'$C_1$', color='#c62828', fontsize=16)
ax.annotate('front', xy=(-3.25, 1.1), xytext=(-4.55, 0.95), color='#c62828', fontsize=10,
            arrowprops={'arrowstyle':'-', 'color':'#c62828'})
ax.text(-2.53, 1.1, 'back', color='#c62828', fontsize=10)
# This circle lies in a genuine disc patch of the front surface.
ax.add_patch(Ellipse((1.5, 1.05), 0.7, 0.62, fill=False, edgecolor='#1565c0', linewidth=2.8))
ax.text(1.93, 1.14, r'$C_2$', color='#1565c0', fontsize=16)
ax.text(1.48, 0.50, 'bounds a disc', color='#1565c0', fontsize=10, ha='center')
ax.text(0, -1.38, 'Front of a disc with three holes', ha='center', fontsize=12, color='#334155')
ax.text(0, -1.75, 'Glue an identical back along all four boundary circles', ha='center', fontsize=11, color='#334155')
ax.set_title('Genus-three surface as a double', fontsize=15, pad=10)
ax.set_xlim(-5.4, 5.4); ax.set_ylim(-2.5, 2.55)
ax.set_aspect('equal'); ax.axis('off')
fig.subplots_adjust(left=0.025, right=0.975, bottom=0.06, top=0.89)
fig.savefig('paper-16-surface-curves.png', dpi=125, facecolor='white', transparent=False)
plt.close(fig)
