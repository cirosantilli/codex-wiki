"""Original bus-role schematic; Python 3.14, matplotlib 3.10.7.

Run from _media; output is an opaque white PNG in the current directory.
The schematic specifies roles, not any particular hardware protocol.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(10, 6), dpi=140, facecolor='white')
ax.set(xlim=(0, 10), ylim=(0, 6))
ax.axis('off')
colors = ['#2364a0', '#24826b', '#975b18']

def box(x, y, w, h, text, color='#eaf0f6'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.04',
                              facecolor=color, edgecolor='#334155', linewidth=1.3))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=11)

def arrow(a, b, color='#334155', style='->', dashed=False):
    ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle=style,
                color=color, lw=1.6, linestyle='--' if dashed else '-'))

ax.text(5, 5.8, 'One shared path: several potential initiators',
        ha='center', fontsize=16, weight='bold')
box(.4, 4.45, 1.9, .7, 'CPU\ninitiator A')
box(3.05, 4.45, 1.9, .7, 'DMA engine\ninitiator B')
box(6.85, 4.45, 2.65, .7, 'Arbiter\nselects one initiator', '#fff2dd')
ax.plot([1.35, 1.35, 7.4, 7.4], [5.15, 5.45, 5.45, 5.15],
        color='#334155', lw=1.6, linestyle='--')
arrow((1.35, 5.4), (1.35, 5.15), dashed=True)
arrow((7.4, 5.4), (7.4, 5.15), dashed=True)
arrow((4.95, 4.8), (6.85, 4.8), style='<->', dashed=True)
ax.text(5.85, 5.3, 'request / grant', ha='center', fontsize=10)
ax.text(7.95, 4.05, 'Selection governs access;\nnot an extra payload path.',
        ha='center', fontsize=10)
ys = [3.65, 3.1, 2.55]
for y, color in zip(ys, colors):
    ax.plot([.75, 9.25], [y, y], color=color, lw=3)
for x in (1.35, 4):
    for dx, y, color in zip((-.13, 0, .13), ys, colors):
        ax.plot([x+dx, x+dx], [4.45, y], color=color, lw=1)
        ax.plot(x+dx, y, 'o', color=color, ms=4)
box(.4, .75, 2.9, .75, 'Memory interface\ntarget')
box(6.55, .75, 2.9, .75, 'Device registers\ntarget')
for x in (1.85, 8):
    for dx, y, color in zip((-.13, 0, .13), ys, colors):
        ax.plot([x+dx, x+dx], [1.5, y], color=color, lw=1)
        ax.plot(x+dx, y, 'o', color=color, ms=4)
# White labels keep long lines readable without ambiguous crossing text.
for y, label, color in zip(ys, ['ADDRESS: initiator selects location / target',
                               'DATA: write to target; read back to initiator',
                               'CONTROL: operation, readiness, completion'], colors):
    ax.text(5.35, y+.1, label, fontsize=10, color=color, ha='center',
            bbox=dict(facecolor='white', edgecolor='none', pad=2))
ax.text(5, 1.85, 'Only the selected target responds to a transaction.', ha='center', fontsize=11)
ax.text(5, .15, 'Logical roles shown separately; some designs reuse wires in different phases.',
        ha='center', fontsize=10)
fig.tight_layout(pad=.7)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
