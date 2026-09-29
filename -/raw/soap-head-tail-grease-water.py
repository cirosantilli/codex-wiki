"""Draw an original soap orientation schematic; Python 3.14, matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


HEAD = '#2377a5'
TAIL = '#bf6b20'


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, ax = plt.subplots(figsize=(10, 5.4), dpi=100, facecolor='white')
    fig.subplots_adjust(left=0.02, right=0.98, top=0.97, bottom=0.04)
    ax.set(xlim=(0, 10), ylim=(0, 5))
    ax.set_aspect('equal')
    ax.axis('off')
    ax.text(5, 4.80, 'Soap: two regions, two different surroundings',
            ha='center', fontsize=19, weight='bold')
    ax.text(2.30, 4.17, 'A long-chain fatty carboxylate', ha='center', weight='bold')
    xs = np.linspace(0.55, 2.90, 13)
    ys = 2.90 + 0.09 * (-1.0) ** np.arange(13)
    ax.plot(xs, ys, color=TAIL, linewidth=5, solid_capstyle='round')
    ax.add_patch(Circle((3.22, 2.9), 0.31, facecolor=HEAD, edgecolor='white', linewidth=2))
    ax.text(3.22, 2.9, '−', color='white', ha='center', va='center', fontsize=20)
    ax.annotate('Hydrocarbon tail\nhydrophobic', xy=(1.50, 2.85), xytext=(1.50, 1.83),
                ha='center', color=TAIL, arrowprops={'arrowstyle': '->', 'color': TAIL})
    ax.annotate('Carboxylate head\nhydrophilic', xy=(3.22, 3.18), xytext=(3.00, 3.65),
                ha='center', color=HEAD, arrowprops={'arrowstyle': '->', 'color': HEAD})
    ax.text(2.25, 0.95, 'Both regions belong to the same ion:\nan amphiphile and a surfactant.',
            ha='center', linespacing=1.6)
    ax.add_patch(FancyBboxPatch((4.72, 0.66), 4.90, 3.65,
                 boxstyle='round,pad=0.10', facecolor='#f3f9fd', edgecolor='#c3dce9'))
    ax.text(7.16, 4.02, 'Water surrounds a coated grease droplet', ha='center', weight='bold', fontsize=12)
    center = np.array([7.16, 2.34])
    ax.add_patch(Circle(center, 0.88, facecolor='#f6dba6', edgecolor='#d4a04a', linewidth=1.5))
    for theta in np.linspace(0, 2 * np.pi, 18, endpoint=False):
        radial = np.array([np.cos(theta), np.sin(theta)])
        tangent = np.array([-np.sin(theta), np.cos(theta)])
        steps = np.linspace(0.47, 1.13, 8)
        wiggle = 0.033 * (-1.0) ** np.arange(8)
        xy = center + steps[:, None] * radial + wiggle[:, None] * tangent
        ax.plot(xy[:, 0], xy[:, 1], color=TAIL, linewidth=2.6, solid_capstyle='round')
        ax.add_patch(Circle(center + 1.20 * radial, 0.095, facecolor=HEAD, edgecolor='white', linewidth=0.6))
    ax.text(*center, 'Grease', ha='center', va='center', fontsize=14, weight='bold',
            bbox={'facecolor': '#f6dba6', 'edgecolor': 'none', 'pad': 3})
    ax.text(7.16, 0.84, 'Heads face water; tails enter grease.', ha='center', fontsize=12)
    ax.text(5, 0.18, 'Schematic cross-section: orientation only, not molecular sizes or measured structure.',
            ha='center', fontsize=11, color='#53616a')
    fig.savefig(Path(__file__).stem + '.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
