"""Original binding-order diagram and analytical first-event probability toy."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


K_ON = 1.0  # micromolar**-1 second**-1, chosen, not measured
B = 1.0  # second**-1, chosen, not measured


def first_binding_probability(s):
    a = K_ON * np.asarray(s)
    return a / (a + B)


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig = plt.figure(figsize=(10, 7.2), facecolor='white')
    fig.suptitle('Binding and conformational change can occur in either order',
                 y=0.975, fontsize=15)
    scheme = fig.add_axes([0.08, 0.52, 0.84, 0.39])
    scheme.axis('off')
    scheme.set_xlim(0, 10)
    scheme.set_ylim(0, 4)
    nodes = {(2, 3): ('$E$', 'unbound, initial form'),
             (8, 3): ('$ES$', 'bound, initial form'),
             (2, 1): ('$E^*$', 'unbound, alternative form'),
             (8, 1): ('$E^*S$', 'bound, alternative form')}
    for (x, y), (symbol, label) in nodes.items():
        scheme.text(x, y, symbol, ha='center', va='center', fontsize=18,
                    bbox={'boxstyle': 'round,pad=0.35', 'fc': '#f0f4f7', 'ec': '#435363'})
        scheme.text(x, y-0.58, label, ha='center', fontsize=10)
    for start, end, color in [((2.7, 3), (7.2, 3), '#2479b0'),
                               ((2.7, 1), (7.2, 1), '#2479b0'),
                               ((2, 2.35), (2, 1.55), '#d86b18'),
                               ((8, 2.35), (8, 1.55), '#d86b18')]:
        scheme.annotate('', end, start,
                        arrowprops={'arrowstyle': '<->', 'color': color, 'lw': 2})
    scheme.text(5, 3.28, 'bind / release substrate', ha='center', color='#2479b0')
    scheme.text(5, 1.28, 'bind / release substrate', ha='center', color='#2479b0')
    scheme.text(0.6, 1.93, 'change\nstructure', ha='center', va='center', color='#d86b18')
    scheme.text(9.4, 1.93, 'change\nstructure', ha='center', va='center', color='#d86b18')
    scheme.text(5, 0.10, 'Induced fit: right, then down   |   Selection: down, then right',
                ha='center', fontsize=11)

    ax = fig.add_axes([0.10, 0.13, 0.51, 0.30])
    s = np.geomspace(0.01, 100, 401)
    ax.plot(s, first_binding_probability(s), lw=2.5, color='#2479b0')
    points = np.array([0.1, 1.0, 10.0])
    ax.scatter(points, first_binding_probability(points), color='#2479b0', zorder=3)
    for x, label, dy in zip(points, ['1/11', '1/2', '10/11'], [0.07, 0.07, -0.15]):
        ax.text(x, first_binding_probability(x)+dy, label, ha='center', fontsize=10)
    ax.set_xscale('log')
    ax.set_xlim(0.01, 100)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Free substrate concentration s (µM)')
    ax.set_ylabel('Probability of binding first')
    ax.set_title('Analytical toy: first event from E only', loc='left', fontsize=12)
    ax.grid(alpha=0.18)

    fig.text(0.66, 0.36, 'Chosen competing rates:\n'
             r'$a=k_{\mathrm{on}}s,\quad b=1\ \mathrm{s}^{-1}$' '\n'
             r'$k_{\mathrm{on}}=1\ \mathrm{\mu M}^{-1}\mathrm{s}^{-1}$', fontsize=11)
    fig.text(0.66, 0.21, r'$P(\mathrm{binding\ first})=\frac{a}{a+b}$', fontsize=14)
    fig.text(0.66, 0.13, 'Later events and reversals omitted.\nThis is not a full-route fraction.',
             fontsize=10, color='#53616d')
    fig.text(0.5, 0.035, 'Original schematic and analytical model • no experimental structures or measured curves',
             ha='center', fontsize=10, color='#53616d')
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
