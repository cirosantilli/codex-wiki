"""Compute and plot Jacobi errors and eigenmodes for an original system.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; emits this script's basename.png into the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 4.]])
    xstar = np.array([1., 2., 3.])
    b = a @ xstar
    d = np.diag(a)
    iteration = np.eye(3) - a / d[:, None]
    q = np.sqrt(2.) / 4.
    modes = np.array([[.5, 1/np.sqrt(2), .5],
                      [1/np.sqrt(2), 0, -1/np.sqrt(2)],
                      [.5, -1/np.sqrt(2), .5]])
    k = np.arange(17)
    x = np.zeros(3)
    errors = []
    for _ in k:
        errors.append(x - xstar)
        # Evaluate every coordinate from the same old vector.
        x = x + (b - a @ x) / d
    errors = np.asarray(errors)
    coefficients = errors @ modes.T
    norms = np.linalg.norm(errors, axis=1)
    exact_norms = 2*np.sqrt(3)*q**k[1:]
    np.testing.assert_allclose(norms[1:], exact_norms, rtol=2e-8, atol=1e-15)
    np.testing.assert_allclose(iteration @ modes.T,
                               modes.T * np.array([q, 0, -q]), atol=2e-16)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), dpi=120, facecolor='white')
    fig.subplots_adjust(left=.085, right=.97, top=.76, bottom=.19, wspace=.28)
    fig.suptitle('Jacobi convergence: error size and persistent mode shapes',
                 fontsize=19, y=.97)
    fig.text(.5, .865, r'$A=\mathrm{tridiag}(-1,4,-1),\quad x_*=(1,2,3)^T,\quad x^{(0)}=0$'
             '\nComputed iterates; no experimental measurements', ha='center', va='center', fontsize=13)
    left, right = axes
    colors = ['#2563a6', '#6b7280', '#ba4e17']
    left.semilogy(k, norms, 'o', ms=5, color='#111827', label=r'computed $\|e^{(k)}\|_2$')
    left.semilogy(k[1:], exact_norms, '--', color='#111827', lw=1.6,
                  label=r'exact $2\sqrt{3}\,q^k$ ($k\geq1$)')
    for j, label in [(0, r'$|c_+^{(k)}|$'), (2, r'$|c_-^{(k)}|$')]:
        left.semilogy(k, np.abs(coefficients[:, j]), '-', color=colors[j],
                      lw=1.8, label=label)
    left.set(xlabel='Sweep k', ylabel='Absolute error / mode coefficient',
             title=r'$q=\sqrt{2}/4\approx0.3536$', xlim=(-.2, 16.2))
    left.set_xticks(np.arange(0, 17, 4))
    left.grid(True, which='major', alpha=.22)
    left.legend(fontsize=10, loc='upper right')
    left.text(.02, .05, 'Zero mode disappears after sweep 1.',
              transform=left.transAxes, fontsize=10,
              bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .9})
    labels = [r'$u_+$: factor $+q$', r'$u_0$: factor $0$', r'$u_-$: factor $-q$']
    for j, (color, label, marker) in enumerate(zip(colors, labels, ['o', 's', '^'])):
        right.plot([1, 2, 3], modes[j], marker=marker, color=color, lw=2,
                   ms=7, label=label)
    right.axhline(0, color='#64748b', lw=.8)
    right.set(xlabel='Coordinate j', ylabel='Normalized eigenvector component',
              title='Shapes stay fixed; coefficients change',
              xticks=[1, 2, 3], xlim=(.8, 3.2), ylim=(-.86, .86))
    right.grid(True, alpha=.22)
    right.text(2, .76, labels[0], ha='center', color=colors[0], fontsize=11)
    right.text(2, -.80, labels[2], ha='center', color=colors[2], fontsize=11)
    right.text(1.35, -.75, labels[1], ha='center', color=colors[1], fontsize=11)
    fig.text(.5, .05, 'The negative mode changes sign each sweep.  '
             'After sweep 1, the total error shrinks by q per sweep.',
             ha='center', fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
