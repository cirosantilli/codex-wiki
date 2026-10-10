"""Original photon-momentum schematic. Tested with Python 3.14 / matplotlib 3.10.7.

Run from _media; writes radiation-pressure-beam-photon-transfer.png there.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

BLUE, ORANGE, GREEN = '#1768a8', '#bb5c13', '#16805c'
fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), facecolor='white')
fig.subplots_adjust(left=.025, right=.98, bottom=.06, top=.82, wspace=.11)
fig.suptitle('Light transfers momentum even without depositing its energy', fontsize=16, y=.96)


def arrow(ax, start, end, color):
    ax.annotate('', end, start, arrowprops=dict(arrowstyle='-|>', color=color, lw=3, mutation_scale=18))


for ax, reflecting in zip(axes, (False, True)):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis('off')
    ax.set_title('Perfect mirror' if reflecting else 'Perfect absorber', fontsize=14, pad=12)
    ax.add_patch(Rectangle((.64, .33), .055, .43, facecolor='#dbe5eb' if reflecting else '#404850', edgecolor='#263846', linewidth=1.5))
    arrow(ax, (.075, .67), (.62, .67), BLUE)
    ax.text(.31, .74, r'Incoming photon: $p_x=+E_\gamma/c$', color=BLUE, ha='center', fontsize=11)
    if reflecting:
        arrow(ax, (.61, .47), (.075, .47), ORANGE)
        ax.text(.31, .38, r'Reflected photon: $p_x=-E_\gamma/c$', color=ORANGE, ha='center', fontsize=11)
    else:
        ax.text(.32, .46, 'Photon absorbed\nNo outgoing photon', ha='center', fontsize=11, color='#404850')
    arrow(ax, (.70, .59), (.97, .59), GREEN)
    ax.text(.84, .71, 'Receiver gains', ha='center', color=GREEN, fontsize=11)
    ax.text(.83, .42, r'$2E_\gamma/c$' if reflecting else r'$E_\gamma/c$', ha='center', color=GREEN, fontsize=14)
    ax.text(.5, .13, r'$p_{\rm refl}=2I/c$' if reflecting else r'$p_{\rm abs}=I/c$', ha='center', fontsize=17)
    ax.text(.5, .015, 'Normal incidence · stationary surface · vacuum', ha='center', fontsize=10, color='#4b5560')

fig.savefig(Path(__file__).stem + '.png', dpi=110, facecolor='white')
plt.close(fig)
