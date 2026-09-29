"""Draw the tensor-product Hadamard circuit. Tested with Python 3.14.
Uses the repository's numpy/matplotlib dependencies; honors MPLCONFIGDIR.
Writes paper-53-hadamard-network.png to the caller's working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(10, 3.4), dpi=120)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
for label, y in [('1', 2.5), ('2', 1.7), ('n', .35)]:
    ax.plot([1.15, 4.0], [y, y], color='black', lw=1.7, zorder=1)
    ax.add_patch(Rectangle((2.2, y-.24), .6, .48, facecolor='white', edgecolor='black', lw=1.5, zorder=2))
    ax.text(2.5, y, r'$H$', ha='center', va='center', fontsize=17)
    ax.text(1.0, y, rf'$|x_{label}\rangle$', ha='right', va='center', fontsize=16)
    ax.text(4.15, y, rf'$\frac{{|0\rangle+(-1)^{{x_{label}}}|1\rangle}}{{\sqrt{{2}}}}$', va='center', fontsize=18)
ax.text(2.5, 1.02, r'$\vdots$', ha='center', va='center', fontsize=21)
ax.set_title(r'Parallel Hadamard gates implement $H^{\otimes n}$', fontsize=16, pad=12)
ax.set_xlim(0, 8.2)
ax.set_ylim(-.2, 2.95)
ax.axis('off')
fig.tight_layout()
fig.savefig('paper-53-hadamard-network.png', dpi=120, facecolor='white', transparent=False)
plt.close(fig)
