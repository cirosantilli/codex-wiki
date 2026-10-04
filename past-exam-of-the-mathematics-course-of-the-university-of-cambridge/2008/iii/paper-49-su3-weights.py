"""Draw exact SU(3) weights from interlacing patterns; write PNG to cwd."""
from collections import Counter
from pathlib import Path
import math
import matplotlib.pyplot as plt
import numpy as np

ROOTS = ((2, 0), (-1, 3), (1, 3))  # coordinates (2 H1, 2 sqrt(3) H2)

def weights(a, b):
    result = Counter()
    for upper in range(b, a + b + 1):
        for lower in range(b + 1):
            for bottom in range(lower, upper + 1):
                result[(2 * bottom - upper - lower,
                        3 * (upper + lower) - 2 * (a + 2 * b))] += 1
    assert sum(result.values()) == (a + 1) * (b + 1) * (a + b + 2) // 2
    return result

def xy(point):
    return np.array((point[0] / 2, point[1] / (2 * math.sqrt(3))))

def hull(points):
    points = sorted(points)
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower, upper = [], []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]

fig, axes = plt.subplots(2, 3, figsize=(12, 7.4), dpi=100, facecolor='white')
navy, muted = '#173c65', '#8598ac'
rootax = axes[0, 0]
for i, root in enumerate(ROOTS, 1):
    vector = xy(root)
    for sign in (-1, 1):
        rootax.annotate('', xy=sign * vector, xytext=(0, 0),
                        arrowprops={'arrowstyle': '-|>', 'color': navy if sign == 1 else muted,
                                    'lw': 1.7, 'mutation_scale': 15})
    rootax.text(*(1.18 * vector), rf'$\alpha_{i}$', ha='center', va='center', fontsize=14)
rootax.set(title='Three root directions', xlim=(-1.5, 1.5), ylim=(-1.22, 1.22))
rootax.text(0, -1.14, r'$\alpha_3=\alpha_1+\alpha_2$', fontsize=12, ha='center')

specs = [(1, 0, r'$\mathbf{3}$'), (0, 1, r'$\overline{\mathbf{3}}$'),
         (1, 1, r'$\mathbf{8}$'), (3, 0, r'$\mathbf{10}$'), (2, 2, r'$\mathbf{27}$')]
for ax, (a, b, label) in zip(axes.flat[1:], specs):
    data = weights(a, b)
    for point in data:
        for du, dv in ROOTS:
            neighbor = (point[0] + du, point[1] + dv)
            if neighbor in data:
                segment = np.array([xy(point), xy(neighbor)])
                ax.plot(segment[:, 0], segment[:, 1], color='#d7e0e9', lw=1.2, zorder=1)
    boundary = hull(data)
    path = np.array([xy(p) for p in boundary + boundary[:1]])
    ax.plot(path[:, 0], path[:, 1], color=muted, lw=1.4, zorder=2)
    for point, multiplicity in data.items():
        x, y = xy(point)
        ax.scatter([x], [y], s=65 if multiplicity == 1 else 290, color=navy, zorder=3)
        if multiplicity > 1:
            ax.text(x, y, str(multiplicity), color='white', ha='center', va='center',
                    fontsize=13, fontweight='bold', zorder=4)
    values = np.array([xy(p) for p in data])
    xmin, ymin = values.min(axis=0); xmax, ymax = values.max(axis=0)
    ax.set(xlim=(xmin - 0.38, xmax + 0.38), ylim=(ymin - 0.38, ymax + 0.38))
    ax.set_title(label + rf'    Dynkin labels $({a},{b})$', fontsize=14, pad=13)
for ax in axes.flat:
    ax.set_aspect('equal', adjustable='box')
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['bottom', 'left']].set_color('#bcc7d2')
    ax.tick_params(labelsize=10, colors='#52677e')
    ax.set_xlabel(r'$H_1$ weight', fontsize=11)
    ax.set_ylabel(r'$H_2$ weight', fontsize=11)
fig.suptitle(r'$SU(3)$ root directions and weight multiplicities', fontsize=19, y=0.985)
fig.text(0.5, 0.018, 'Each plain dot has multiplicity 1; numbers mark coincident states. '
         'Lines follow the three root directions.', ha='center', fontsize=12, color=navy)
fig.subplots_adjust(left=0.07, right=0.98, top=0.87, bottom=0.11, wspace=0.4, hspace=0.48)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
