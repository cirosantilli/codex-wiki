"""Illustrate and exhaustively check S3. Tested with Python 3.14.4.

Products apply the rightmost permutation first; [x,y] = x^-1 y^-1 x y.
The PNG is written to the current working directory for the Makefile.
"""

from itertools import permutations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    return tuple(p.index(i) for i in range(len(p)))


def commutator(p, q):
    return compose(compose(compose(inverse(p), inverse(q)), p), q)


def sign(p):
    inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    return (-1) ** inversions


def verify():
    e = (0, 1, 2)
    x, y = (1, 0, 2), (0, 2, 1)
    a, b = (1, 2, 0), (2, 0, 1)
    group = set(permutations(range(3)))
    even = {e, a, b}
    assert compose(x, y) == a and compose(y, x) == b
    assert commutator(x, y) == b
    assert {commutator(p, q) for p in group for q in group} == even
    assert {p for p in group if sign(p) == 1} == even
    assert {p for p in group if all(compose(p, q) == compose(q, p)
                                  for q in group)} == {e}
    classes = {frozenset(compose(compose(q, p), inverse(q)) for q in group)
               for p in group}
    assert classes == {frozenset({e}), frozenset(even - {e}),
                       frozenset(group - even)}
    for p in group:
        assert compose(p, inverse(p)) == e == compose(inverse(p), p)
        coset = {compose(p, h) for h in even}
        assert coset == {q for q in group if sign(q) == sign(p)}
        for q in group:
            assert compose(p, q) in group
            assert sign(compose(p, q)) == sign(p) * sign(q)
            for t in group:
                assert compose(compose(p, q), t) == compose(p, compose(q, t))
    print('S3: checked all 36 products and commutators, 216 associative triples; '
          'derived=A3, sign quotient=C2, conjugacy sizes=1,2,3, center={e}.')
    return e, x, y, a, b


def triangle(ax, p, title):
    positions = np.array([[0, 1], [-.87, -.5], [.87, -.5]])
    colors = ['#c57012', '#326ca3', '#367f62']
    closed = np.vstack([positions, positions[0]])
    ax.plot(closed[:, 0], closed[:, 1], color='#8395a2', lw=1.5)
    for original, destination in enumerate(p):
        point = positions[destination]
        ax.scatter(*point, s=420, color=colors[original], zorder=3)
        ax.text(*point, str(original + 1), ha='center', va='center',
                color='white', weight='bold', fontsize=13, zorder=4)
    ax.set(xlim=(-1.25, 1.25), ylim=(-.9, 1.4), aspect='equal')
    ax.set_title(title, fontsize=13, pad=0)
    ax.axis('off')


def main():
    e, x, y, a, b = verify()
    fig = plt.figure(figsize=(10, 6.5), dpi=120, facecolor='white')
    fig.text(.5, .96, 'S₃: forcing commutativity leaves only the sign',
             ha='center', fontsize=18, weight='bold')
    for row, (items, color, label) in enumerate([
        ([(e, r'$e$'), (a, r'$(123)$'), (b, r'$(132)$')], '#edf5ed', '+1 (even)'),
        ([(x, r'$(12)$'), ((2, 1, 0), r'$(13)$'), (y, r'$(23)$')], '#edf2f9', '-1 (odd)'),
    ]):
        bottom = .67 - row * .22
        fig.add_artist(FancyBboxPatch((.025, bottom), .95, .2,
                       boxstyle='round,pad=.005', facecolor=color,
                       edgecolor='#c6d2da', transform=fig.transFigure, zorder=0))
        for col, (p, title) in enumerate(items):
            triangle(fig.add_axes([.06 + col * .21, bottom + .015, .16, .16]), p, title)
        fig.text(.72, bottom + .11, 'sign →', fontsize=13, ha='center')
        fig.text(.86, bottom + .11, label, fontsize=14, ha='center', weight='bold')
    fig.text(.5, .41, r"$S_3'=A_3=\{e,(123),(132)\}$;  $S_3/A_3\cong C_2$;  $Z(S_3)=\{e\}$",
             ha='center', fontsize=14)
    fig.text(.5, .34, r'An explicit commutator: $x=(12)$, $y=(23)$',
             ha='center', fontsize=14)
    states = [e]
    for operation in [y, x, y, x]:
        states.append(compose(operation, states[-1]))
    assert states[-1] == b
    for col, (state, title) in enumerate(zip(states, [
            r'$e$', r'$y$', r'$xy$', r'$y^{-1}xy$', r'$x^{-1}y^{-1}xy=(132)$'])):
        triangle(fig.add_axes([.015 + col * .2, .085, .17, .17]), state, title)
        if col < 4:
            operation = [r'$y$', r'$x$', r'$y^{-1}$', r'$x^{-1}$'][col]
            fig.text(.195 + col * .2, .205, '→', fontsize=19, ha='center')
            fig.text(.195 + col * .2, .165, operation, fontsize=11, ha='center')
    fig.text(.5, .035, 'Apply the rightmost factor first. Labels follow the original vertices.',
             ha='center', fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
