"""Draw an illustrative molecular fluorescence process diagram.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the output directory; creates the matching PNG in the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(9.2, 5.7), dpi=130, facecolor='white')
    ax.set(xlim=(0, 10), ylim=(-0.7, 9.7))
    ax.axis('off')
    # Dimensionless energies chosen solely to separate the processes visually.
    for x0, x1, base, name in [(1, 5.8, 0, r'$S_0$'), (1, 5.8, 5, r'$S_1$'),
                                (1, 5.8, 8, r'$S_2$'), (7.5, 9.3, 3.6, r'$T_1$')]:
        for j in range(3):
            ax.plot([x0, x1], [base + 0.38*j]*2, color='#263238', lw=2 if j == 0 else 1)
        ax.text(x1 + 0.12, base, name, va='center', fontsize=14)
    ax.annotate('', (0.4, 9.2), (0.4, 0), arrowprops={'arrowstyle': '->', 'lw': 1.5})
    ax.text(0.16, 4.7, 'Energy', rotation=90, ha='center')

    def arrow(start, end, color, dashed=False):
        ax.annotate('', end, start, arrowprops={'arrowstyle': '-|>', 'lw': 2.4,
                                              'color': color, 'linestyle': '--' if dashed else '-'})

    arrow((1.65, 0), (1.65, 8.76), '#2460a7')
    ax.text(1.42, 4, 'Absorption', rotation=90, va='center', ha='right', color='#2460a7')
    # Nonradiative path: relax within S2, change electronic state, relax in S1.
    for a, b in [((2.8, 8.76), (2.8, 8)), ((2.8, 8), (2.8, 5.76)), ((2.8, 5.76), (2.8, 5))]:
        arrow(a, b, '#b65e0a', True)
    ax.text(3.05, 6.7, 'Relaxation without\na fluorescent photon', color='#974b08', va='center')
    arrow((4.7, 5), (4.7, 0.76), '#18845b')
    ax.text(4.94, 2.7, 'Fluorescence', rotation=90, va='center', color='#18845b')
    arrow((4.7, 0.76), (4.7, 0), '#b65e0a', True)
    arrow((5.65, 5), (7.5, 3.6), '#7753a6', True)
    ax.text(6.65, 5.9, 'Spin-changing\nroute', color='#7753a6', ha='center')
    arrow((8.4, 3.6), (8.4, 0), '#7753a6', True)
    ax.text(8.15, 1.65, 'Other loss\nchannels', color='#7753a6', ha='right')
    ax.text(3.3, -0.55, 'Thin lines: levels of molecular vibration', ha='center', fontsize=10)
    ax.text(8.3, 8.2, 'Singlet\nstates', ha='center', color='#263238')
    ax.text(8.4, 4.55, 'Triplet state', ha='center', color='#263238')
    fig.suptitle('Excitation → relaxation → fluorescence', y=0.97, fontsize=16)
    fig.text(0.5, 0.02, 'Illustrative level spacings and pathways; not measured energies or transition rates',
             ha='center', fontsize=10)
    fig.subplots_adjust(left=0.035, right=0.965, bottom=0.12, top=0.91)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
