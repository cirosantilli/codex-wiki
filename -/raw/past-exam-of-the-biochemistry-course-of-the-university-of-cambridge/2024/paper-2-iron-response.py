"""Original explanatory schematic; Python 3.14 and matplotlib; output goes to cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

fig, axes = plt.subplots(2, 1, figsize=(9.2, 5.2), facecolor='white')
for ax, pos, label, consequence in zip(axes, [1.4, 6.9], ['Ferritin mRNA: IRE near the 5′ end', 'Transferrin receptor 1 mRNA: IREs in the 3′ region'], ['Initiation inhibited → less iron storage', 'RNA protected from decay → more iron uptake']):
    ax.set_xlim(0, 9)
    ax.set_ylim(-0.5, 2.0)
    ax.axis('off')
    ax.text(0.15, 1.67, label, fontsize=13, weight='bold')
    ax.plot([.5, 8.4], [.6, .6], lw=2.5, color='#555555', zorder=0)
    ax.text(.23, .58, '5′', ha='right', va='center')
    ax.text(8.65, .58, '3′', va='center')
    ax.add_patch(FancyBboxPatch((2.4, .43), 3.0, .34, boxstyle='round,pad=.04', facecolor='#dce9f0', edgecolor='#20618b'))
    ax.text(3.9, .6, 'Coding region', ha='center', va='center', fontsize=11)
    for x in ([pos] if pos < 2 else [pos-.65, pos, pos+.65]):
        ax.plot([x-.08, x-.08, x+.08, x+.08], [.6, .94, .94, .6], color='#20618b', lw=2)
        ax.add_patch(Circle((x, 1.02), .15, facecolor='#e6aa4e', edgecolor='#785113', zorder=4))
    ax.text(pos if pos<2 else pos+.8, 1.22, 'Bound IRP', ha='center', fontsize=10, color='#785113')
    ax.text(3.9, -.13, consequence, ha='center', fontsize=12, color='#124a67')
fig.suptitle('Low available iron: active RNA-binding IRPs', fontsize=15, weight='bold')
fig.text(.5, .035, 'Higher iron reduces IRP occupancy and reverses these outputs. Conceptual drawing; not to scale.', ha='center', fontsize=10)
fig.tight_layout(rect=(0, .08, 1, .94), h_pad=1.2)
fig.savefig('paper-2-iron-response.png', dpi=150, facecolor='white')
plt.close(fig)
