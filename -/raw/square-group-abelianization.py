"""Illustrate and exhaustively check the square group of order 8 (D8).

Tested with Python 3.14.4. Products act rightmost first and
[x,y] = x^-1 y^-1 x y. Write the PNG to cwd for the Makefile.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


def compose(p, q):
    return tuple(p[q[i]] for i in range(4))


def inverse(p):
    return tuple(p.index(i) for i in range(4))


def power(p, n):
    result = tuple(range(4))
    for _ in range(n):
        result = compose(result, p)
    return result


def verify():
    e, r, s = tuple(range(4)), (1, 2, 3, 0), (0, 3, 2, 1)
    elements = {(i, j): compose(power(r, i), power(s, j))
                for i in range(4) for j in range(2)}
    coordinates = {p: ij for ij, p in elements.items()}
    group = set(coordinates)
    assert len(group) == 8
    assert power(r, 4) == power(s, 2) == e
    assert compose(compose(s, r), s) == inverse(r)
    comm = lambda p, q: compose(compose(compose(inverse(p), inverse(q)), p), q)
    normal = {e, power(r, 2)}
    assert comm(r, s) == power(r, 2)
    assert {comm(p, q) for p in group for q in group} == normal
    assert {p for p in group if all(compose(p, q) == compose(q, p)
                                  for q in group)} == normal
    bits = lambda p: (coordinates[p][0] % 2, coordinates[p][1])
    assert {bits(p) for p in group} == {(0, 0), (1, 0), (0, 1), (1, 1)}
    assert {p for p in group if bits(p) == (0, 0)} == normal
    cosets = {frozenset(compose(p, n) for n in normal) for p in group}
    assert len(cosets) == 4 and all(len(c) == 2 for c in cosets)
    for p in group:
        assert compose(p, inverse(p)) == e == compose(inverse(p), p)
        assert {compose(p, n) for n in normal} == {q for q in group if bits(q) == bits(p)}
        for q in group:
            i, j = coordinates[p]
            k, ell = coordinates[q]
            assert compose(p, q) == elements[((i + (-1) ** j * k) % 4, (j + ell) % 2)]
            assert bits(compose(p, q)) == tuple((a + b) % 2 for a, b in zip(bits(p), bits(q)))
            for t in group:
                assert compose(compose(p, q), t) == compose(p, compose(q, t))
    classes = {frozenset(compose(compose(q, p), inverse(q)) for q in group)
               for p in group}
    assert classes == {frozenset({e}), frozenset({power(r, 2)}),
                       frozenset({r, power(r, 3)}),
                       frozenset({s, elements[(2, 1)]}),
                       frozenset({elements[(1, 1)], elements[(3, 1)]})}
    print('D8 (order 8): checked all 64 products and commutators, 512 associative triples; '
          'derived=center={e,r²}, four cosets, quotient=C2×C2, conjugacy sizes=1,1,2,2,2.')
    return elements


def square(ax, p, title):
    positions = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]])
    closed = np.vstack([positions, positions[0]])
    ax.plot(closed[:, 0], closed[:, 1], color='#8395a2', lw=1.5)
    colors = ['#c57012', '#326ca3', '#367f62', '#945482']
    for original, destination in enumerate(p):
        point = positions[destination]
        ax.scatter(*point, s=350, color=colors[original], zorder=3)
        ax.text(*point, 'ABCD'[original], ha='center', va='center',
                fontsize=12, weight='bold', color='white', zorder=4)
    ax.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), aspect='equal')
    ax.set_title(title, fontsize=14, pad=0)
    ax.axis('off')


def main():
    elements = verify()
    fig = plt.figure(figsize=(10, 6.7), dpi=120, facecolor='white')
    fig.text(.5, .96, 'The square group of order 8: four classes survive',
             ha='center', fontsize=18, weight='bold')
    fig.text(.5, .91, r'$r$: counterclockwise quarter-turn; $s$: reflection in diagonal AC',
             ha='center', fontsize=12)
    columns = [((0, 0), [r'$e$', r'$r^2$'], '#edf5ed'),
               ((1, 0), [r'$r$', r'$r^3$'], '#edf2f9'),
               ((0, 1), [r'$s$', r'$r^2s$'], '#faf1e7'),
               ((1, 1), [r'$rs$', r'$r^3s$'], '#f6edf6')]
    for col, ((i, j), labels, color) in enumerate(columns):
        left = .03 + col * .24
        fig.add_artist(FancyBboxPatch((left, .40), .215, .44,
                       boxstyle='round,pad=.006', facecolor=color,
                       edgecolor='#c6d2da', transform=fig.transFigure, zorder=0))
        fig.text(left + .108, .805, f'bit pair ({i}, {j})', ha='center', fontsize=13)
        for row, label in enumerate(labels):
            square(fig.add_axes([left + .033, .615 - row * .185, .15, .15]),
                   elements[(i + 2 * row, j)], label)
    fig.text(.5, .365, r"$N=D_8'=Z(D_8)=\{e,r^2\}$; each column is one coset of $N$",
             ha='center', fontsize=14)
    ax = fig.add_axes([.055, .065, .39, .25])
    ax.axis('off')
    bit_pairs = [(0, 0), (1, 0), (0, 1), (1, 1)]
    labels = ['00', '10', '01', '11']
    entries = [[f'{(a + c) % 2}{(b + d) % 2}' for c, d in bit_pairs]
               for a, b in bit_pairs]
    table = ax.table(cellText=entries, rowLabels=labels, colLabels=labels,
                     cellLoc='center', loc='center', bbox=[.12, .03, .83, .88])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor('#c6d2da')
        cell.set_facecolor('#edf2f9' if row == 0 or col == -1 else 'white')
    ax.set_title('Quotient operation: add each bit mod 2', fontsize=12, pad=5)
    fig.text(.68, .23, 'First bit: even or odd quarter-turn count\n'
             'Second bit: rotation or reflection\n'
             'A half-turn is forgotten.', ha='center', va='center',
             fontsize=12, linespacing=1.7)
    fig.text(.68, .095, r'$D_8/N\cong C_2\times C_2$', ha='center', fontsize=17)
    fig.text(.5, .023, 'Products act rightmost first. Vertex labels follow the original vertices.',
             ha='center', fontsize=10)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
