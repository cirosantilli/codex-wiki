"""Original schematic. Python 3.14, matplotlib; writes the PNG to the current directory."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, axes = plt.subplots(1, 2, figsize=(9, 4.0), facecolor='white')
blue = '#12659a'
for ax, label, patterns in zip(axes, ['Population I', 'Population II'], [[(0, 0), (1, 1)], [(1, 0), (0, 1)]]):
    ax.set(xlim=(0, 5), ylim=(-0.4, 3.5))
    ax.axis('off')
    ax.set_title(label, fontsize=15, fontweight='bold')
    for y, bits in zip([2.4, 1.5], patterns):
        ax.plot([1, 4], [y, y], color='#555555', lw=4, solid_capstyle='round')
        for x, bit in zip([1.7, 3.3], bits):
            ax.add_patch(Circle((x, y), 0.14, facecolor=blue if bit else 'white', edgecolor=blue, lw=2, zorder=3))
        ax.plot([2.5, 2.5], [y-0.25, y+0.25], color='#b25a2b', lw=1.5, linestyle='--')
        ax.text(0.7, y, '50%', ha='right', va='center', fontsize=11)
    for x, t in zip([1.7, 3.3], ['Site A', 'Site B']):
        ax.text(x, 2.85, t, ha='center', fontsize=11)
    ax.text(2.5, 0.9, 'Digest separates A from B', ha='center', fontsize=11, color='#844422')
    ax.annotate('', xy=(2.5, 0.22), xytext=(2.5, 0.72), arrowprops=dict(arrowstyle='->', lw=1.8))
    ax.text(2.5, -0.15, 'A modified: 50%     B modified: 50%', ha='center', fontsize=11, color=blue)
fig.text(0.5, 0.035, 'Filled circle = modification. Equal chain abundance; schematic populations, not experimental data.', ha='center', fontsize=10)
fig.tight_layout(rect=(0, 0.1, 1, 1), w_pad=2)
fig.savefig('paper-1-proteoform-linkage.png', dpi=150, facecolor='white')
plt.close(fig)
