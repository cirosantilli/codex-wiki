"""Original quantum-network sketches; Python 3.14, Matplotlib 3.10.7.

Write the opaque PNG to the caller's current directory. The caller controls
MPLBACKEND and MPLCONFIGDIR; no environment or repository configuration changes.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, axes = plt.subplots(2, 1, figsize=(11, 5.8), dpi=100)
fig.patch.set_facecolor('white')


def box(ax, x, y, text, width=0.55, height=0.46):
    ax.add_patch(Rectangle((x-width/2, y-height/2), width, height,
                           facecolor='white', edgecolor='#263238', linewidth=1.5, zorder=3))
    ax.text(x, y, text, ha='center', va='center', fontsize=13, zorder=4)


def wire(ax, y):
    ax.plot([1.3, 8.7], [y, y], color='#263238', linewidth=1.4, zorder=1)


for ax in axes:
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, 3.1)
    ax.set_facecolor('white')
    ax.axis('off')

ax=axes[0]
ax.set_title('Walsh–Hadamard transform: one Hadamard gate on each wire', fontsize=14, pad=10)
for y, lab in zip([2.4, 1.7, 0.5], ['1', '2', 'n']):
    wire(ax, y)
    ax.text(1.1, y, rf'$|x_{lab}\rangle$', ha='right', va='center', fontsize=13)
    box(ax, 4.8, y, r'$H$')
    ax.text(8.9, y, rf'$H|x_{lab}\rangle$', ha='left', va='center', fontsize=13)
ax.text(4.8, 1.08, r'$\vdots$', ha='center', va='center', fontsize=17)

ax=axes[1]
ax.set_title('Bernstein–Vazirani network: a single oracle call reveals the string a', fontsize=14, pad=10)
for y, lab in zip([2.4, 1.7, 0.5], ['1', '2', 'n']):
    wire(ax, y)
    ax.text(1.1, y, r'$|0\rangle$', ha='right', va='center', fontsize=13)
    box(ax, 2.2, y, r'$H$')
    box(ax, 6.8, y, r'$H$')
    box(ax, 8.2, y, 'M', width=0.5)
    ax.text(8.9, y, rf'$a_{lab}$', ha='left', va='center', fontsize=13)
wire(ax, -0.2)
ax.text(1.1, -0.2, r'$|-\rangle$', ha='right', va='center', fontsize=13)
ax.text(8.9, -0.2, r'$|-\rangle$', ha='left', va='center', fontsize=13)
ax.text(2.2, 1.08, r'$\vdots$', ha='center', va='center', fontsize=17)
ax.text(6.8, 1.08, r'$\vdots$', ha='center', va='center', fontsize=17)
ax.add_patch(Rectangle((4.1, -0.42), 1.4, 3.06, facecolor='#edf5fc', edgecolor='#263238', linewidth=1.5, zorder=3))
ax.text(4.8, 1.1, r'$U_f$', ha='center', va='center', fontsize=20, zorder=4)
fig.subplots_adjust(left=0.025, right=0.98, top=0.91, bottom=0.06, hspace=0.44)
fig.savefig(Path('paper-47-hadamard-networks.png'), facecolor='white', transparent=False)
plt.close(fig)
