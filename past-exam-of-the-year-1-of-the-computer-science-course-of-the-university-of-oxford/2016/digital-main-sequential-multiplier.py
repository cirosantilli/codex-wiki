"""Generate digital-main-sequential-multiplier.png in CWD; Python 3.14, matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 5.9), dpi=130)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 12), ylim=(0, 7))
ax.axis('off')
blue, orange = '#145b91', '#ae5000'

def box(x, y, w, h, label, color=blue):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.07', facecolor='#f3f7fb', edgecolor=color, linewidth=1.5))
    ax.text(x+w/2, y+h/2, label, ha='center', va='center', fontsize=11)

def arrow(a, b, label=None, color=blue, offset=(0, 0.13)):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=12, linewidth=1.5, color=color))
    if label:
        ax.text((a[0]+b[0])/2+offset[0], (a[1]+b[1])/2+offset[1], label, ha='center', va='bottom', fontsize=10, color=color)

ax.text(6, 6.62, 'Eight-cycle unsigned shift-and-add multiplier', ha='center', fontsize=15, weight='bold')
box(0.4, 4.6, 2.2, 0.85, 'M: 16-bit register\nload X; shift left')
box(0.4, 2.45, 2.2, 0.85, 'Q: 8-bit register\nload Y; shift right')
box(4.1, 4.6, 2.0, 0.85, 'Select M or 0\ncontrolled by Q₀')
box(7.25, 4.6, 1.55, 0.85, '16-bit\nadder')
box(9.7, 4.6, 1.9, 0.85, 'P: 16-bit register\nload 0; accumulate')
arrow((2.7, 5.025), (3.95, 5.025), 'M')
arrow((6.2, 5.025), (7.1, 5.025))
arrow((8.9, 5.025), (9.55, 5.025))
ax.plot([1.5, 5.1], [3.42, 3.42], color=orange, lw=1.5)
arrow((1.5, 3.32), (1.5, 3.42), color=orange)
arrow((5.1, 3.42), (5.1, 4.46), 'Q₀', orange, (0.38, 0))
# Accumulator feedback returns to the adder's second input.
ax.plot([10.65, 10.65, 8.0], [5.55, 5.99, 5.99], color=blue, lw=1.5)
arrow((8.0, 5.99), (8.0, 5.55))
ax.text(9.1, 6.12, 'P feedback', ha='center', fontsize=10, color=blue)
arrow((10.65, 4.5), (10.65, 3.6), 'Z = P', offset=(0.55, 0))
box(4.1, 2.45, 3.2, 0.85, 'Controller + 3-bit counter k\nIDLE → RUN → DONE', orange)
arrow((2.6, 1.65), (4.2, 2.38), 'start', orange, (-0.25, 0))
arrow((7.4, 2.87), (10.8, 2.87), 'done = (state is DONE)', orange)
ax.text(6, 1.15, 'Load inputs on acceptance; repeat conditional add and shifts eight times.', ha='center', fontsize=11)
ax.text(6, 0.64, 'Register load/hold multiplexers, clock and reset wiring are omitted for clarity.', ha='center', fontsize=10, color='#444444')
fig.tight_layout(pad=0.5)
fig.savefig(Path(__file__).stem+'.png', facecolor='white')
plt.close(fig)
