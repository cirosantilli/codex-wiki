"""Original causal diagrams; write signaling-feedback-loops.png to CWD.

Tested with Python 3.14.4 and matplotlib 3.10.7 (Debian build).
Arrows denote activation and flat ends inhibition, not molecular transport.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

INK = '#263746'
BLUE = '#18769a'
RED = '#b54838'


def box(ax, center, label, width=1.55, height=0.85):
    x, y = center
    ax.add_patch(FancyBboxPatch((x - width / 2, y - height / 2), width, height,
                               boxstyle='round,pad=0.04', facecolor='#f1f6f8',
                               edgecolor=INK, linewidth=1.5, zorder=3))
    ax.text(x, y, label, ha='center', va='center', fontsize=12, zorder=4)


def arrow(ax, start, end, inhibit=False, color=BLUE):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-[' if inhibit else '-|>',
                                mutation_scale=13 if inhibit else 15, color=color,
                                linewidth=2, shrinkA=0, shrinkB=0, zorder=2))


def feedback_panel(ax, positive):
    ax.set(xlim=(0, 7), ylim=(0, 4.1))
    ax.axis('off')
    name = 'Positive feedback' if positive else 'Negative feedback'
    ax.set_title(name, fontsize=14, fontweight='bold', pad=12)
    box(ax, (2, 2.7), 'Earlier\nrelay A')
    box(ax, (5, 2.7), 'Later\nrelay B')
    ax.text(0.18, 2.9, 'Input', fontsize=11)
    arrow(ax, (0.4, 2.7), (1.17, 2.7))
    arrow(ax, (2.84, 2.7), (4.17, 2.7))
    ax.text(3.5, 3.03, 'activates', ha='center', color=BLUE, fontsize=11)
    color = BLUE if positive else RED
    # B returns along the lower route to A, closing the directed causal cycle.
    ax.plot([5, 5, 2], [2.23, 1.15, 1.15], color=color, lw=2)
    arrow(ax, (2, 1.15), (2, 2.22), inhibit=not positive, color=color)
    ax.text(3.5, 0.82, 'B activates A' if positive else 'B inhibits A',
            ha='center', fontsize=12, color=color)
    ax.text(3.5, 0.23, 'Reinforces activation' if positive else 'Opposes activation',
            ha='center', fontsize=11, color=INK)


def main():
    plt.rcParams.update({'font.size': 11, 'text.color': INK})
    fig = plt.figure(figsize=(9.5, 6.4), dpi=120, facecolor='white')
    grid = fig.add_gridspec(2, 2, height_ratios=[1, 1.1], hspace=0.43, wspace=0.18)
    feedback_panel(fig.add_subplot(grid[0, 0]), False)
    feedback_panel(fig.add_subplot(grid[0, 1]), True)
    ax = fig.add_subplot(grid[1, :])
    ax.set(xlim=(0, 12), ylim=(0, 4.4))
    ax.axis('off')
    ax.set_title('Incoherent feedforward: two opposing routes, no return path',
                 fontsize=14, fontweight='bold', pad=10)
    box(ax, (1.3, 2.25), 'Input s', width=1.6)
    box(ax, (5.0, 3.35), 'Fast branch x', width=2.4)
    box(ax, (5.0, 1.25), 'Slow branch a', width=2.4)
    box(ax, (9.8, 2.25), 'Readout\nr = x − a', width=2.5, height=1.1)
    arrow(ax, (2.17, 2.45), (3.72, 3.35))
    arrow(ax, (2.17, 2.05), (3.72, 1.25))
    arrow(ax, (6.28, 3.35), (8.48, 2.57))
    arrow(ax, (6.28, 1.25), (8.48, 1.94), inhibit=True, color=RED)
    ax.text(7.35, 3.37, '+ contribution', ha='center', color=BLUE, fontsize=11)
    ax.text(7.35, 0.86, '− contribution', ha='center', color=RED, fontsize=11)
    ax.text(1.3, 0.67, 'Both branches\nread the input', ha='center', fontsize=11)
    ax.text(5.0, 2.28, 'No x → a or a → x', ha='center', fontsize=10, color='#596673')
    ax.text(9.8, 0.62, 'No r → s, x or a', ha='center', fontsize=11)
    fig.text(0.5, 0.955, 'Where does the downstream effect go?', ha='center', fontsize=16)
    fig.text(0.5, 0.024, 'Arrow: activation   |   Flat end: inhibition   |   Original schematics, not measured pathways',
             ha='center', fontsize=10)
    fig.subplots_adjust(top=0.88, bottom=0.09, left=0.03, right=0.99)
    path = Path.cwd() / Path(__file__).with_suffix('.png').name
    fig.savefig(path, facecolor='white', transparent=False)
    plt.close(fig)
    print(f'Wrote {path.name}: 1140 × 768 pixels')


if __name__ == '__main__':
    main()
