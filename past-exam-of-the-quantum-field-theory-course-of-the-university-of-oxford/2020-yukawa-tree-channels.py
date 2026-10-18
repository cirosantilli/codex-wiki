"""Draw original momentum-labelled Yukawa tree channels (Python 3.14)."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def fermion(ax, start, end, reverse=False):
    start, end = np.array(start), np.array(end)
    ax.plot(*zip(start, end), color='#172b4d', lw=1.9)
    first, last = (0.61, 0.42) if reverse else (0.42, 0.61)
    ax.annotate('', xy=start + last * (end - start),
                xytext=start + first * (end - start),
                arrowprops={'arrowstyle': '-|>', 'color': '#172b4d', 'lw': 1.4,
                            'mutation_scale': 13})


def scalar(ax, start, end, label, label_xy):
    ax.plot(*zip(start, end), '--', color='#b54708', lw=1.8, dashes=(4, 3))
    ax.text(*label_xy, label, color='#8c3606', ha='center', va='center', fontsize=12,
            bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1.5})


def prepare(ax, title):
    ax.set(xlim=(-0.07, 1.07), ylim=(-0.09, 1.1))
    ax.axis('off')
    ax.set_title(title, fontsize=14, weight='bold', pad=6)


def exchange(ax, title, species=(1, 2), crossed=False, anti=False):
    prepare(ax, title)
    a, b = (0.42, 0.74), (0.42, 0.26)
    incoming = [(0.01, 0.92), (0.01, 0.08)]
    outgoing = [(0.99, 0.92), (0.99, 0.08)]
    fermion(ax, incoming[0], a)
    fermion(ax, incoming[1], b, reverse=anti)
    fermion(ax, a, outgoing[1] if crossed else outgoing[0])
    fermion(ax, b, outgoing[0] if crossed else outgoing[1], reverse=anti)
    scalar(ax, a, b, r'$q_u=p_1-p_4$' if crossed else r'$q_t=p_1-p_3$', (0.20, 0.50))
    for node in (a, b):
        ax.plot(*node, 'o', color='#172b4d', ms=4)
    labels = [(incoming[0], rf'$f_{species[0]}(p_1)$', 0.07),
              (incoming[1], rf'$\bar f_{species[1]}(p_2)$' if anti else rf'$f_{species[1]}(p_2)$', -0.07),
              (outgoing[0], rf'$f_{species[0]}(p_3)$', 0.07),
              (outgoing[1], rf'$\bar f_{species[1]}(p_4)$' if anti else rf'$f_{species[1]}(p_4)$', -0.07)]
    for point, label, offset in labels:
        ax.text(point[0], point[1] + offset, label, fontsize=13, ha='center', va='center')


def annihilation(ax):
    prepare(ax, '(iii) Same species: s channel')
    a, b = (0.32, 0.5), (0.68, 0.5)
    ends = [(0.01, 0.92), (0.01, 0.08), (0.99, 0.92), (0.99, 0.08)]
    fermion(ax, ends[0], a)
    fermion(ax, ends[1], a, reverse=True)
    fermion(ax, b, ends[2])
    fermion(ax, b, ends[3], reverse=True)
    scalar(ax, a, b, r'$q_s=p_1+p_2$', (0.5, 0.72))
    for node in (a, b):
        ax.plot(*node, 'o', color='#172b4d', ms=4)
    for point, label, dy in zip(ends, [r'$f_1(p_1)$', r'$\bar f_1(p_2)$',
                                      r'$f_1(p_3)$', r'$\bar f_1(p_4)$'],
                                [0.07, -0.07, 0.07, -0.07]):
        ax.text(point[0], point[1] + dy, label, ha='center', va='center', fontsize=13)


fig, axes = plt.subplots(3, 2, figsize=(10.6, 9.4), facecolor='white')
fig.subplots_adjust(left=0.07, right=0.94, bottom=0.055, top=0.91, hspace=0.55, wspace=0.38)
fig.suptitle('Scalar exchange in Yukawa theory', fontsize=19, weight='bold', y=0.975)
exchange(axes[0, 0], '(i) Distinct species: t channel')
axes[0, 1].axis('off')
axes[0, 1].text(0.5, 0.64, r'$p_1+p_2=p_3+p_4$', fontsize=16, ha='center')
axes[0, 1].text(0.5, 0.38, 'Arrows: fermion flow\nDashed lines: scalar\nCrossings carry no vertex',
                fontsize=13, ha='center', va='center', linespacing=1.6)
exchange(axes[1, 0], '(ii) Identical fermions: t channel', species=(1, 1))
exchange(axes[1, 1], '(ii) Identical fermions: u channel', species=(1, 1), crossed=True)
exchange(axes[2, 0], '(iii) Same species: t channel', species=(1, 1), anti=True)
annihilation(axes[2, 1])
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
            dpi=110, facecolor='white', transparent=False,
            metadata={'Software': 'Matplotlib'})
plt.close(fig)
