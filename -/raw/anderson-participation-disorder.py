"""Participation in finite open Anderson chains; no inferred critical disorder.

Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7. Run from _media.
Each sample uses the four eigenstates nearest E=0; plotted samples are their
mean participation ratios, not pooled eigenstates. The same underlying
random potential is scaled across W within each realization and size.
"""
import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def sample_participation(unit_potential, width):
    n = len(unit_potential)
    h = np.diag(width * unit_potential) - np.eye(n, k=1) - np.eye(n, k=-1)
    energy, vectors = np.linalg.eigh(h)
    np.testing.assert_allclose(np.sum(abs(vectors) ** 2, axis=0), 1, atol=2e-14, rtol=0)
    np.testing.assert_allclose(vectors.T @ vectors, np.eye(n), atol=2e-14, rtol=0)
    np.testing.assert_allclose(h @ vectors, vectors * energy, atol=2e-14, rtol=0)
    p = 1 / np.sum(abs(vectors) ** 4, axis=0)
    assert np.all(p >= 1 - 1e-12) and np.all(p <= n + 1e-12)
    return float(np.mean(p[np.argsort(abs(energy), kind='stable')[:4]]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sizes', type=int, nargs='+', default=[40, 80])
    parser.add_argument('--realizations', type=int, default=24)
    parser.add_argument('--seed', type=int, default=20261016)
    args = parser.parse_args()
    if any(not 40 <= n <= 100 or n % 2 for n in args.sizes) or not 4 <= args.realizations <= 64:
        parser.error('sizes must be even in 40..100; realizations must be 4..64')
    widths = np.array([0, 0.5, 1, 2, 3, 4, 6, 8.0])
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8))
    fig.suptitle('Disorder reduces participation; finite samples vary', fontsize=14)
    summaries = []
    for i, n in enumerate(args.sizes):
        rng = np.random.default_rng(np.random.SeedSequence([args.seed, n]))
        potentials = rng.uniform(-0.5, 0.5, (args.realizations, n))
        values = np.array([[sample_participation(v, w) for w in widths] for v in potentials])
        np.testing.assert_allclose(values[:, 0], 2 * (n + 1) / 3, atol=2e-12, rtol=0)
        low, mid, high = np.quantile(values, [0.1, 0.5, 0.9], axis=0)
        color = ['#235f93', '#b56c24', '#487542'][i % 3]
        for ax, scale in zip(axes, [1, n]):
            for row in values:
                ax.plot(widths, row / scale, color=color, alpha=0.12, lw=0.65)
            ax.fill_between(widths, low / scale, high / scale, color=color, alpha=0.12)
            ax.plot(widths, mid / scale, 'o-', color=color, label=f'N = {n}: median, 10–90% band', ms=4)
        summaries.append({'N': n, 'median_P': mid.tolist(), 'q10_P': low.tolist(), 'q90_P': high.tolist()})
    axes[0].set_ylabel('Mean P of four states nearest E = 0')
    axes[1].set_ylabel('Mean P / N of the same four states')
    axes[0].set_ylim(bottom=0)
    axes[1].set_ylim(0, 0.8)
    for ax in axes:
        ax.set_xlabel('Disorder W/t (full uniform box width)')
        ax.grid(alpha=0.2)
        ax.legend(fontsize=9, loc='upper right')
        ax.set_xlim(0, 8)
    fig.subplots_adjust(left=0.075, right=0.985, top=0.87, bottom=0.20, wspace=0.25)
    fig.text(0.5, 0.018, f'{args.realizations} realizations per size, seed {args.seed}; faint lines are samples. No universal threshold is inferred.', ha='center', fontsize=10)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
    print(json.dumps({'widths': widths.tolist(), 'realizations': args.realizations, 'seed': args.seed,
                      'state_selection': 'four eigenstates closest to E=0, sample mean P',
                      'summaries': summaries, 'checks': ['all eigenvector normalizations', 'orthogonality',
                      'eigenvalue residuals', 'all P bounds', 'analytic clean P for every realization']}))


if __name__ == '__main__':
    main()
