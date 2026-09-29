"""Draw a binary-channel cascade and information bounds; save PNG to cwd.

Uses only matplotlib and numpy from the root pyproject.toml.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def binary_entropy(probability):
    p = np.asarray(probability, dtype=float)
    result = np.zeros_like(p)
    interior = (p > 0) & (p < 1)
    values = p[interior]
    result[interior] = -values * np.log2(values) - (1 - values) * np.log2(1 - values)
    return result


def draw_channel(ax, left, right, error, color):
    """Draw all four conditional transition probabilities of one BSC."""
    for value in (0, 1):
        y = 0.66 if value == 0 else 0.16
        ax.add_patch(FancyArrowPatch((left + 0.14, y), (right - 0.14, y),
                                    arrowstyle='-|>', mutation_scale=13,
                                    linewidth=1.7, color=color))
        ax.text((left + right) / 2, y + 0.045, f'{1-error:.2f}',
                ha='center', va='bottom', color=color, fontsize=11,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
        other_y = 0.16 if value == 0 else 0.66
        bend = 0.14 if value == 0 else -0.14
        ax.add_patch(FancyArrowPatch((left + 0.14, y), (right - 0.14, other_y),
                                    connectionstyle=f'arc3,rad={bend}',
                                    arrowstyle='-|>', mutation_scale=12,
                                    linewidth=1.2, color=color, alpha=0.65))
        ax.text(left + 0.30, y + (-0.13 if value == 0 else 0.12), f'{error:.2f}',
                ha='center', va='center', color=color, fontsize=11,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})


def main():
    q = 0.1
    chosen_r = 0.2
    r = np.linspace(0, 0.5, 501)
    effective = q + r - 2 * q * r
    i_xy = float(1 - binary_entropy(q))
    i_yz = 1 - binary_entropy(r)
    i_xz = 1 - binary_entropy(effective)
    assert np.all(i_xz <= i_xy + 1e-14)
    assert np.all(i_xz <= i_yz + 1e-14)
    assert np.allclose([i_xz[0], i_xz[-1], i_yz[-1]], [i_xy, 0, 0])

    colors = {'xy': '#2965a5', 'yz': '#aa531c', 'xz': '#167c60'}
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False})
    fig = plt.figure(figsize=(10, 8.2), layout='constrained', facecolor='white')
    grid = fig.add_gridspec(2, 1, height_ratios=[1.05, 1.55])
    diagram = fig.add_subplot(grid[0])
    diagram.set(xlim=(-0.35, 4.35), ylim=(-0.44, 1.13))
    diagram.axis('off')
    diagram.set_title('Independent noises: two binary symmetric channels', pad=14)
    for x, name in [(0, 'X'), (2, 'Y'), (4, 'Z')]:
        diagram.text(x, 0.93, f'{name}: fair bit', ha='center', fontsize=12, weight='bold')
        for value, y in [(0, 0.66), (1, 0.16)]:
            diagram.add_patch(FancyBboxPatch((x - 0.13, y - 0.10), 0.26, 0.20,
                                             boxstyle='round,pad=0.01',
                                             facecolor='#edf2f7', edgecolor='#42576b'))
            diagram.text(x, y, str(value), ha='center', va='center', fontsize=12)
    draw_channel(diagram, 0, 2, q, colors['xy'])
    draw_channel(diagram, 2, 4, chosen_r, colors['yz'])
    diagram.text(1, 0.94, 'flip q = 0.10', ha='center', color=colors['xy'])
    diagram.text(3, 0.94, 'flip r = 0.20', ha='center', color=colors['yz'])
    diagram.text(2, -0.15, 'Each arrow label is a conditional probability; each input has probability 1/2.',
                 ha='center', fontsize=10)
    diagram.text(2, -0.35, 'Net flip: s = q(1 - r) + (1 - q)r = 0.26',
                 ha='center', fontsize=12, color=colors['xz'])

    ax = fig.add_subplot(grid[1])
    ax.axhline(i_xy, color=colors['xy'], linewidth=2, linestyle='--',
               label=r'$I(X;Y)=1-h_2(0.1)$')
    ax.plot(r, i_yz, color=colors['yz'], linewidth=2.3,
            label=r'$I(Y;Z)=1-h_2(r)$')
    ax.plot(r, i_xz, color=colors['xz'], linewidth=2.7,
            label=r'$I(X;Z)=1-h_2(0.1+0.8r)$')
    ax.axvline(chosen_r, color='#728091', linestyle=':', linewidth=1.2)
    chosen = [i_xy, float(1 - binary_entropy(chosen_r)),
              float(1 - binary_entropy(q + chosen_r - 2*q*chosen_r))]
    for info, key, offset in zip(chosen, ['xy', 'yz', 'xz'], [0.04, 0.03, -0.105]):
        ax.scatter([chosen_r], [info], color=colors[key], s=35, zorder=5)
        ax.annotate(f'{info:.4f} bits', (chosen_r, info),
                    xytext=(chosen_r + 0.018, info + offset),
                    color=colors[key], fontsize=11)
    ax.set(xlim=(0, 0.5), ylim=(-0.025, 1.025),
           xlabel='Second-channel flip probability r  (first-channel q = 0.1)',
           ylabel='Mutual information (bits)',
           title='The cascade stays below both individual-channel bounds')
    ax.set_xticks(np.arange(0, 0.51, 0.1))
    ax.grid(alpha=0.2)
    ax.legend(loc='upper right', fontsize=11)
    fig.savefig(Path.cwd() / 'data-processing-binary-cascade.png', dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
