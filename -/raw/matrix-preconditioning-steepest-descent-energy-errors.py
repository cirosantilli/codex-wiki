"""Original exact rational steepest-descent histories for a constructed system.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; the output basename matches this script's basename.
"""
from fractions import Fraction as F
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

A = ((F(1), F(1, 5)), (F(1, 5), F(100)))
solution = [F(2495, 2499), F(20, 2499)]


def dot(u, v):
    return sum(a * b for a, b in zip(u, v, strict=True))


def matvec(v):
    return [dot(row, v) for row in A]


def history(diagonal, steps):
    x, r = [F(0), F(0)], [F(1), F(1)]
    initial = dot(solution, matvec(solution)) / 2
    errors = [F(1)]
    for _ in range(steps):
        if all(value == 0 for value in r):
            break
        z = [a / d for a, d in zip(r, diagonal, strict=True)]
        az = matvec(z)
        alpha = dot(r, z) / dot(z, az)
        x = [a + alpha * b for a, b in zip(x, z, strict=True)]
        r = [a - alpha * b for a, b in zip(r, az, strict=True)]
        assert r == [F(1) - v for v in matvec(x)]
        error = [a - b for a, b in zip(x, solution, strict=True)]
        errors.append(dot(error, matvec(error)) / (2 * initial))
    return errors


plain = history([F(1), F(1)], 16)
scaled = history([F(1), F(100)], 8)
assert plain == [F(81675, 85007)**k for k in range(17)]
assert scaled == [F(3267, 8500700)**k for k in range(9)]
plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12, 'figure.facecolor': 'white'})
fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.7), layout='constrained')
fig.suptitle('Steepest descent: exact energy-error histories', fontsize=14)
for ax, cost in zip(axes, [False, True], strict=True):
    for values, charge, label, color, marker in [
        (plain, 1, r'Unpreconditioned ($M=I$)', '#b45a35', 'o'),
        (scaled, 2 if cost else 1, r'Jacobi scaling ($M=\mathrm{diag}(1,100)$)', '#245b85', 's'),
    ]:
        indices = np.arange(len(values))
        if not cost:
            indices = indices[:9]
            values = values[:9]
        ax.semilogy(charge * indices, [float(v) for v in values], marker=marker,
                    markersize=4, color=color, linewidth=2, label=label)
    ax.set(xlabel='Declared work units' if cost else 'Iterations',
           ylabel=r'Relative energy error $E_k/E_0$', ylim=(1e-28, 2),
           title='One vs two work units per step' if cost else 'Identical starting point: x = 0')
    ax.set_xticks(np.arange(0, 17 if cost else 9, 4 if cost else 2))
    ax.set_yticks([10.0**(-i) for i in range(0, 29, 4)])
    ax.grid(alpha=0.2, which='major')
axes[0].legend(loc='lower left', fontsize=9, framealpha=1)
fig.supxlabel('One unit for A times a vector; one for a diagonal solve. Setup and vector operations excluded.\nConstructed example and declared cost model; no runtime measurements.', fontsize=10)
fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
plt.close(fig)
