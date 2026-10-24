"""Draw the 2015 Q4 counter; output to the current working directory.

Dependencies: root pyproject.toml, Python 3.14, matplotlib 3.10.7.
Repeated net labels denote physical connections, including output feedback.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

OUT = Path('digital-main-2015-up-down-counter.png')
BLUE = '#155a83'
INK = '#182c3d'
fig, ax = plt.subplots(figsize=(12, 7.6), dpi=125, facecolor='white')
ax.set_facecolor('white')
ax.set(xlim=(0, 15), ylim=(0, 9.4))
ax.axis('off')

def wire(points, color=INK, lw=1.6):
    xs, ys = zip(*points)
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle='round')

def gate(x, y, label, inputs, output):
    width, height = 1.18, 0.92
    ax.add_patch(Rectangle((x, y-height/2), width, height, edgecolor=INK,
                           facecolor='#f0f6fa', lw=1.5, zorder=3))
    ax.text(x+width/2, y, label, ha='center', va='center', fontsize=12, color=INK)
    offsets = [0] if len(inputs) == 1 else [0.23, -0.23]
    for name, off in zip(inputs, offsets):
        wire([(x-0.62, y+off), (x, y+off)])
        ax.text(x-0.71, y+off, name, ha='right', va='center', fontsize=12, color=BLUE)
    wire([(x+width, y), (x+width+0.68, y)])
    ax.text(x+width+0.78, y, output, va='center', fontsize=12, color=BLUE)

ax.text(7.5, 9.03, 'Synchronous 3-bit up-down counter', ha='center', fontsize=19, color=INK)
ax.text(7.5, 8.58, 'A = 1: increment    |    A = 0: decrement    |    all arithmetic modulo 8',
        ha='center', fontsize=11.5, color=INK)
ax.text(3.0, 7.98, 'Shared combinational signals', ha='center', fontsize=12.5, weight='bold', color=INK)
ax.text(10.6, 7.98, 'Next-state logic and state storage', ha='center', fontsize=12.5, weight='bold', color=INK)
gate(2.15, 7.1, 'NOT', ['A'], 'N')
gate(2.15, 5.57, 'XOR', ['B0', 'N'], 'T0')
gate(2.15, 4.02, 'XOR', ['B1', 'N'], 'T1')
gate(2.15, 2.47, 'AND', ['T0', 'T1'], 'C')
ax.text(3.0, 1.40, 'T0 = B0 XOR N\nT1 = B1 XOR N\nC = T0 AND T1', ha='center', va='center',
        fontsize=11.5, color=INK, linespacing=1.5)

for i, y, label, inputs in [(0, 6.8, 'NOT', ['B0']),
                             (1, 4.6, 'XOR', ['B1', 'T0']),
                             (2, 2.4, 'XOR', ['B2', 'C'])]:
    gate(7.4, y, label, inputs, f'D{i}')
    wire([(9.65, y), (10.05, y)])
    ax.add_patch(Rectangle((10.05, y-.58), 1.6, 1.16, facecolor='white', edgecolor=INK, lw=1.6))
    ax.text(10.85, y+.12, 'D flip-flop', ha='center', va='center', fontsize=10.8, color=INK)
    ax.text(10.22, y-.05, 'D', ha='center', va='center', fontsize=10, color=INK)
    ax.text(11.47, y-.05, 'Q', ha='center', va='center', fontsize=10, color=INK)
    ax.add_patch(Polygon([(10.51, y-.58), (10.73, y-.37), (10.95, y-.58)],
                         closed=False, fill=False, edgecolor=INK, lw=1.4))
    wire([(11.65, y), (13.0, y)])
    ax.text(13.14, y, f'B{i}', va='center', fontsize=13, weight='bold', color=BLUE)
    wire([(9.82, y-.9), (10.73, y-.9), (10.73, y-.58)], color=BLUE)
    ax.plot(9.82, y-.9, 'o', color=BLUE, markersize=4)
wire([(9.82, 0.92), (9.82, 5.9)], color=BLUE)
ax.text(9.82, .62, 'CLK (shared rising edge)', ha='center', fontsize=11.5, color=BLUE)
ax.text(7.5, .05, 'Repeated blue net labels are connected wires; B0, B1 and B2 feed back to their named inputs.',
        ha='center', fontsize=10.8, color=INK)
fig.subplots_adjust(left=.025, right=.985, bottom=.04, top=.98)
fig.savefig(OUT, facecolor='white', metadata={'Software': 'codex-wiki matplotlib generator'})
plt.close(fig)
print(OUT)
