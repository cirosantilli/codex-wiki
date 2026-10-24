"""Generate digital-main-sensor-multiplex.png in CWD; Python 3.14, matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 4.6), dpi=130)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 11), ylim=(0, 5))
ax.axis('off')
blue, orange = '#145b91', '#ae5000'

def box(x, y, w, h, label, color=blue):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08', facecolor='#f3f7fb', edgecolor=color, linewidth=1.5))
    ax.text(x+w/2, y+h/2, label, ha='center', va='center', fontsize=11)

def arrow(a, b, label=None, color=blue, text_offset=(0, 0.12)):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=13, linewidth=1.5, color=color))
    if label:
        ax.text((a[0]+b[0])/2+text_offset[0], (a[1]+b[1])/2+text_offset[1], label, ha='center', va='bottom', fontsize=10, color=color)

ax.text(5.5, 4.72, 'Eight sensors share one eight-bit data bus', ha='center', fontsize=15, weight='bold')
box(0.3, 1.4, 2.4, 2.3, 'Sensors 0–7\n\nEach supplies\neight bits')
box(4.3, 1.4, 2.2, 2.3, 'Eight parallel\n8:1 multiplexers\n\nOne per bit j')
arrow((2.8, 2.85), (4.15, 2.85), '64 wires')
ax.text(3.45, 2.2, r'$d_{i,j}$', fontsize=13, ha='center')
arrow((6.6, 2.85), (10.5, 2.85), '8 data lines')
ax.text(8.5, 2.2, r'Output bit $j=d_{q,j}$', ha='center', fontsize=12)
box(0.3, 0.25, 2.4, 0.62, '3-bit counter', orange)
arrow((2.8, 0.56), (10.5, 0.56), '3 address lines: q₂ q₁ q₀', orange, (2.25, 0.15))
ax.plot([5.4, 5.4], [0.56, 1.28], color=orange, lw=1.5)
ax.add_patch(FancyArrowPatch((5.4, 0.9), (5.4, 1.32), arrowstyle='-|>', mutation_scale=13, color=orange, linewidth=1.5))
ax.plot(5.4, 0.56, 'o', color=orange, ms=4)
ax.text(5.85, 0.99, 'select', color=orange, fontsize=10)
ax.text(10.65, 1.7, 'To\nreceiver', ha='center', va='center', fontsize=11)
fig.tight_layout(pad=0.5)
fig.savefig(Path(__file__).stem+'.png', facecolor='white')
plt.close(fig)
