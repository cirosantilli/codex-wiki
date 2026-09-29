"""Interface-source schematic and exact modal growth rates.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes paper-76-interface-dynamo.png to the caller CWD; preserves MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.7), dpi=120, facecolor='white')
    ax = axes[0]
    ax.set_facecolor('white')
    ax.add_patch(Rectangle((0, 0), 1, 1, color='#e2eef8'))
    ax.add_patch(Rectangle((0, -1), 1, 1, color='#f8eadc'))
    ax.axhline(0, color='#404040', lw=1.4)
    ax.text(.5, .68, r'Alpha regeneration ($z>0$)', ha='center', fontsize=10)
    ax.text(.5, .44, r'Toroidal $B$ $\longrightarrow$ poloidal $A$', ha='center', fontsize=10)
    ax.text(.5, -.56, r'Shear induction ($z<0$)', ha='center', fontsize=10)
    ax.text(.5, -.8, r'Poloidal $a$ $\longrightarrow$ toroidal $b$', ha='center', fontsize=10)
    ax.annotate('', (.22, .24), (.22, -.28), arrowprops={'arrowstyle': '<->', 'color': '#555555', 'lw': 1.8})
    ax.annotate('', (.78, .24), (.78, -.28), arrowprops={'arrowstyle': '<->', 'color': '#555555', 'lw': 1.8})
    ax.text(.5, .06, r'Interface $z=0$', ha='center', fontsize=9)
    ax.text(.5, -.22, 'Diffusive coupling', ha='center', fontsize=9)
    ax.annotate('', (-.07, .8), (-.07, -.8), arrowprops={'arrowstyle': '->', 'lw': 1.1})
    ax.text(-.1, .91, '$z$', ha='center')
    ax.set_xlim(-.16, 1.06)
    ax.set_ylim(-1.06, 1.08)
    ax.set_title('Separated source regions', fontsize=11)
    ax.axis('off')

    ax = axes[1]
    ax.set_facecolor('white')
    D = np.linspace(0, 96, 385)
    plus = np.sqrt(D / 32) - 1
    minus = -np.sqrt(D / 32) - 1
    ax.plot(D, plus, color='#1769aa', lw=2.2, label=r'$s_+/(\eta k^2)$')
    ax.plot(D, minus, color='#c65d0e', ls='--', lw=1.6, label=r'$s_-/(\eta k^2)$')
    ax.axhline(0, color='#444444', lw=.8)
    ax.axvline(32, color='#888888', ls=':', lw=1.0)
    ax.scatter([32], [0], color='#202020', s=24, zorder=5)
    ax.annotate('$D=32$', (32, 0), xytext=(6, -22), textcoords='offset points')
    ax.fill_between(D, 0, plus, where=plus > 0, color='#cfe9d3', alpha=1)
    ax.text(70, .18, 'Growth', ha='center', fontsize=9)
    ax.set_xlim(0, 96)
    ax.set_ylim(-2.9, .95)
    ax.set_xticks([0, 16, 32, 48, 64, 80, 96])
    ax.set_xlabel(r'Dynamo number $D=V\alpha/(\eta^2 k^3)$')
    ax.set_ylabel(r'Dimensionless growth rate $s/(\eta k^2)$')
    ax.set_title('Equal-diffusivity surface-wave branches', fontsize=11)
    ax.grid(alpha=.17)
    ax.legend(loc='lower left', fontsize=9, framealpha=1)
    fig.tight_layout()
    fig.savefig(Path('paper-76-interface-dynamo.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
