"""Proper-rotation mirror test. Run from _media.

Tested: Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Enumerates all label-respecting matchings and fits proper orthogonal rotations.
"""
from itertools import permutations
from pathlib import Path
import json
import matplotlib.pyplot as plt
import numpy as np

V = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
S = np.diag([-1., 1., 1.])
Q = np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]], float)
COLORS = {'A': '#bb4a24', 'B': '#08699b', 'C': '#6e4096',
          'D': '#237e43', 'H': '#686868'}


def best_rotation_error(labels):
    """Minimum Frobenius residual over legal matchings and SO(3) rotations."""
    source = V @ S.T
    errors = []
    for order in permutations(range(4)):
        if any(labels[j] != labels[order[j]] for j in range(4)):
            continue
        target = V[list(order)]
        u, _, vt = np.linalg.svd(source.T @ target)
        correction = np.diag([1., 1., np.linalg.det(u @ vt)])
        rotation_row = u @ correction @ vt
        assert np.isclose(np.linalg.det(rotation_row), 1.)
        errors.append(np.linalg.norm(source @ rotation_row - target))
    return min(errors), len(errors)


def draw(ax, points, labels, title, targets=False):
    ax.set_proj_type('ortho')
    ax.view_init(elev=22, azim=-90)
    for i, p in enumerate(points):
        ax.plot([0, p[0]], [0, p[1]], [0, p[2]], color='#777777',
                lw=2, ls='--' if p[1] > 0 else '-')
        ax.scatter(*p, s=390, color=COLORS[labels[i]], edgecolors='white',
                   linewidths=1.4, depthshade=False)
        ax.text(*p, labels[i], ha='center', va='center',
                fontsize=14, color='white', fontweight='bold', zorder=100)
    if targets:
        for i, p in enumerate(V):
            ax.scatter(*p, s=720, facecolors='none', edgecolors=COLORS[labels[i]],
                       linewidths=2, depthshade=False)
    ax.scatter(0, 0, 0, s=130, color='#444444', depthshade=False)
    ax.set(xlim=(-1.65, 1.65), ylim=(-1.65, 1.65), zlim=(-1.65, 1.65))
    ax.set_box_aspect((1, 1, 1))
    ax.set_axis_off()
    ax.set_title(title, fontsize=12, pad=-8)


def main():
    assert np.allclose(Q.T @ Q, np.eye(3)) and np.isclose(np.linalg.det(Q), 1.)
    assert np.allclose(Q @ np.array([0., 1., 1.]), [0., 1., 1.])
    mirror = V @ S.T
    turned = mirror @ Q.T
    assert np.allclose(turned, V[[0, 1, 3, 2]])
    chiral_error, chiral_matchings = best_rotation_error('ABCD')
    achiral_error, achiral_matchings = best_rotation_error('ABHH')
    assert chiral_error > 1 and achiral_error < 1e-12
    fig = plt.figure(figsize=(9, 6), facecolor='white')
    for row, labels in enumerate(['ABCD', 'ABHH']):
        titles = ['Original', 'Mirror: x → −x',
                  'Half-turn: C/D mismatch' if row == 0 else 'Half-turn: exact match']
        for col, points in enumerate([V, mirror, turned]):
            draw(fig.add_subplot(2, 3, 3 * row + col + 1, projection='3d'),
                 points, labels, titles[col], targets=col == 2)
    fig.subplots_adjust(left=.09, right=.99, bottom=.14, top=.87, hspace=.22, wspace=.03)
    fig.suptitle('Identical groups change the superposition test', fontsize=18, y=.96)
    fig.text(.025, .67, 'CHIRAL', rotation=90, va='center', fontsize=13, fontweight='bold')
    fig.text(.025, .32, 'ACHIRAL', rotation=90, va='center', fontsize=13, fontweight='bold')
    fig.text(.5, .08, 'Actual 180° spatial rotation about (0, 1, 1); det Q = +1',
             ha='center', fontsize=12)
    fig.text(.5, .04, 'Outlines = original target groups • distinct C/D cannot exchange • identical H/H can',
             ha='center', fontsize=10, color='#555555')
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white')
    plt.close(fig)
    print(json.dumps({'proper_rotation_det': float(np.linalg.det(Q)),
                      'axis': [0, 1, 1], 'label_mapping': [0, 1, 3, 2],
                      'minimum_proper_rotation_residual_ABCD': chiral_error,
                      'minimum_proper_rotation_residual_ABHH': achiral_error,
                      'legal_matchings': [chiral_matchings, achiral_matchings],
                      'dimensions': [1080, 720]}))


if __name__ == '__main__':
    main()
