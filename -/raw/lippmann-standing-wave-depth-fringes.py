"""Draw an illustrative Lippmann recording geometry and ideal electric fringes.

Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7. Run from _media.
The ideal phase-reversing reflector is not a fit to mercury or an emulsion.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(10, 7), layout='constrained')
    grid = fig.add_gridspec(3, 1, height_ratios=[1.25, .65, 1.6])
    ax = fig.add_subplot(grid[0])
    ax.set_xlim(-250, 1450)
    ax.set_ylim(-.15, 1.8)
    ax.axis('off')
    for x, width, face, label in [(-190, 190, '#b9c0c8', 'Mercury\nreflector'),
                                  (0, 1000, '#fff3cf', 'Sensitive layer'),
                                  (1000, 190, '#d8edf5', 'Glass')]:
        ax.add_patch(Rectangle((x, 0), width, 1.15, facecolor=face, edgecolor='#52606d'))
        ax.text(x + width/2, 1.28, label, ha='center', va='bottom')
    for y, start, end, color, label in [(.77, 1370, 40, '#b14b2d', 'Incident light'),
                                       (.30, 40, 1370, '#216c9e', 'Reflected light')]:
        ax.annotate('', (end, y), (start, y), arrowprops={'arrowstyle': '->', 'color': color, 'lw': 2.2})
        ax.text(550, y+.09, label, ha='center', color=color)
    ax.set_title('Recording: incident and returning light overlap inside the layer', loc='left', pad=20)
    ax = fig.add_subplot(grid[1])
    ax.axis('off')
    ax.text(.02, .68, 'Develop and dry', weight='bold', transform=ax.transAxes)
    ax.annotate('', (.36, .68), (.26, .68), xycoords='axes fraction', arrowprops={'arrowstyle': '->', 'lw': 1.8})
    ax.text(.39, .68, 'White-light readout: the recorded depth structure selects reflected colour',
            transform=ax.transAxes, va='center', fontsize=10)
    ax.text(.02, .10, 'The exposure reflector is distinct from the later recorded structure.',
            transform=ax.transAxes, color='#52606d', fontsize=10)
    ax = fig.add_subplot(grid[2])
    z = np.linspace(0, 1000, 2001)
    k = 2*np.pi*1.5/600
    exposure = 4*np.sin(k*z)**2
    ax.plot(z, exposure, color='#a5422b', lw=2)
    for maximum in np.arange(100, 1000, 200):
        ax.axvline(maximum, color='#d6a793', ls=':', lw=1)
    ax.annotate('', (100, 4.35), (300, 4.35), arrowprops={'arrowstyle': '<->', 'color': '#243746'})
    ax.text(200, 4.48, '200 nm', ha='center')
    ax.set(xlim=(0, 1000), ylim=(0, 5), xlabel='Depth z from reflector into layer (nm)',
           ylabel='Normalized electric\nexposure proxy')
    ax.set_yticks([0, 1, 2, 3, 4])
    ax.set_title(r'Chosen model: $\lambda_0=600$ nm, $n=1.5$, ideal $r=-1$', loc='left', fontsize=11)
    ax.grid(axis='y', alpha=.2)
    fig.savefig(Path(__file__).stem+'.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
