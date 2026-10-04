"""Zero-framed Hopf-link diagram; output basename in caller CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
MPLCONFIGDIR, when supplied by the caller, is left unchanged.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    separation = 0.65
    theta = np.arccos(separation)
    gap = 0.105
    fig, ax = plt.subplots(figsize=(5.5, 3.6), dpi=140, facecolor='white')
    ax.set_facecolor('white')
    # Blue is under at the lower crossing; orange is under at the upper.
    for center, color, under_angle in [(-separation, '#1967b3', 2*np.pi-theta),
                                       (separation, '#cc6619', np.pi-theta)]:
        start = under_angle + gap
        stop = under_angle + 2*np.pi - gap
        angles = np.linspace(start, stop, 900)
        ax.plot(center+np.cos(angles), np.sin(angles), color=color,
                linewidth=4.2, solid_capstyle='round')
    ax.text(-1.88, 0, '0', ha='center', va='center', fontsize=20, color='#1967b3')
    ax.text(1.88, 0, '0', ha='center', va='center', fontsize=20, color='#cc6619')
    ax.set_title(r'$0$-framed Hopf link for $S^2\times S^2$', fontsize=15, pad=18)
    ax.text(0, -1.28, 'Two two-handles; cap the remaining three-sphere with a four-handle',
            ha='center', va='center', fontsize=9.5)
    ax.set_xlim(-2.12, 2.12)
    ax.set_ylim(-1.44, 1.22)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.tight_layout(pad=1.2)
    fig.savefig(Path('paper-27-hopf.png'), facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
