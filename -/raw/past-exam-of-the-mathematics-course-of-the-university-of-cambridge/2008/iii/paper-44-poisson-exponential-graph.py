"""Draw the Poisson-exponential hierarchy; write its PNG in the caller's cwd."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

fig, ax = plt.subplots(figsize=(6.8, 3.0), dpi=100, facecolor='white')
ax.set(xlim=(0, 6.8), ylim=(0, 3.0), aspect='equal')
ax.axis('off')
ax.add_patch(FancyBboxPatch((2.55, 0.62), 3.65, 1.45, boxstyle='round,pad=0.1',
                          edgecolor='#657080', facecolor='none', linewidth=1.3))
for x, label, color in [(1.3, r'$\psi$', 'white'), (3.4, r'$\theta_i$', 'white'),
                         (5.35, r'$y_i$', '#dbe4ef')]:
    ax.add_patch(Circle((x, 1.4), 0.33, facecolor=color, edgecolor='#263c59', linewidth=1.5))
    ax.text(x, 1.4, label, ha='center', va='center', fontsize=18, color='#263c59')
for a, b in [(1.65, 3.05), (3.75, 5.0)]:
    ax.add_patch(FancyArrowPatch((a, 1.4), (b, 1.4), arrowstyle='-|>', mutation_scale=17,
                                linewidth=1.5, color='#263c59'))
ax.text(2.22, 1.8, r'Exp$(\psi)$', fontsize=11, ha='center', color='#263c59')
ax.text(4.35, 1.8, r'Poisson$(\theta_i)$', fontsize=11, ha='center', color='#263c59')
ax.text(6.0, 0.74, r'$i=1,\ldots,n$', ha='right', fontsize=12, color='#263c59')
ax.text(3.4, 2.53, 'Shared hyperparameter and hospital-specific rates', ha='center',
        fontsize=14, color='#263c59')
ax.text(3.4, 0.19, 'Shaded node: observed count   •   Unshaded nodes: latent rate and hyperparameter',
        ha='center', fontsize=10, color='#263c59')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
