"""Draw a quantum control loop; tested with Python 3.14 and root pinned deps.

Write the PNG basename into the caller's working directory. Matplotlib uses
any MPLCONFIGDIR supplied by the caller.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(8.0, 3.25), dpi=150, facecolor='white')
ax.set(xlim=(0, 10), ylim=(0, 4))
ax.axis('off')

def box(x, y, w, h, text, color='#edf3fa', fontsize=10):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08', facecolor=color, edgecolor='#254666', linewidth=1.2))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=fontsize, color='#16334c')

def arrow(a, b, label=None, offset=(0, 0), color='#254666', dashed=False):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=13, linewidth=1.4, color=color, linestyle='--' if dashed else '-'))
    if label:
        ax.text((a[0]+b[0])/2+offset[0], (a[1]+b[1])/2+offset[1], label, fontsize=9, ha='center', va='center', color=color)

box(0.3, 2.35, 1.2, .7, 'Target')
box(2.1, 2.35, 1.7, .7, 'Controller')
box(4.45, 2.35, 1.45, .7, 'Actuator\n(fields)')
box(6.6, 2.35, 1.75, .7, 'Quantum\nsystem')
box(6.6, .6, 1.75, .7, 'Sensor\n(measurement)')
box(8.7, 2.35, 1.05, .7, 'Environment', '#f6efe4', fontsize=8)
arrow((1.58, 2.7), (2.02, 2.7))
arrow((3.88, 2.7), (4.37, 2.7))
arrow((5.98, 2.7), (6.52, 2.7))
arrow((8.62, 2.7), (8.43, 2.7), color='#996426')
arrow((7.75, 2.27), (7.75, 1.38), 'signal', (.46, 0))
arrow((7.0, 1.38), (7.0, 2.27), 'backaction', (-.74, 0), color='#a23c4c', dashed=True)
arrow((6.52, .95), (2.95, .95), 'measurement record', (0, .26))
arrow((2.95, .95), (2.95, 2.27))
ax.text(.3, .05, 'Open loop: prescribe the input without the return record.\nClosed loop: use measured results to update the input.', fontsize=9, color='#16334c', va='bottom')
fig.savefig('paper-52-control-loop.png', facecolor='white', transparent=False, bbox_inches='tight', pad_inches=.12)
plt.close(fig)
