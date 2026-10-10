"""Finite open Anderson chain; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; --sites (40..100), --disorder (full box width / t), and
--seed expose the model controls. Energies and hopping use t=1 by default.
"""
import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def spectrum(epsilon, hopping=1.0):
    n = len(epsilon)
    h = np.diag(epsilon) - hopping * (np.eye(n, k=1) + np.eye(n, k=-1))
    energy, vectors = np.linalg.eigh(h)
    # Test the returned vectors, rather than silently renormalizing them.
    np.testing.assert_allclose(vectors.T @ vectors, np.eye(n), atol=2e-14, rtol=0)
    np.testing.assert_allclose(h @ vectors, vectors * energy, atol=2e-14, rtol=0)
    np.testing.assert_allclose(np.sum(abs(vectors) ** 2, axis=0), 1, atol=2e-14, rtol=0)
    return energy, vectors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sites', type=int, default=80)
    parser.add_argument('--disorder', type=float, default=6.0)
    parser.add_argument('--seed', type=int, default=20261015)
    parser.add_argument('--hopping', type=float, default=1.0)
    args = parser.parse_args()
    if not 40 <= args.sites <= 100 or args.disorder < 0 or args.hopping <= 0:
        parser.error('require 40 <= sites <= 100, disorder >= 0, hopping > 0')
    n, t = args.sites, args.hopping
    epsilon = t * args.disorder * np.random.default_rng(args.seed).uniform(-0.5, 0.5, n)
    energy, vectors = spectrum(epsilon, t)
    j = np.argmin(abs(energy))
    probability = abs(vectors[:, j]) ** 2
    participation = 1 / np.sum(probability ** 2)
    clean_energy, clean_vectors = spectrum(np.zeros(n), t)
    # Pick the lower central standing wave unambiguously in the clean chain.
    m = n // 2
    clean_probability = abs(clean_vectors[:, m - 1]) ** 2
    sites = np.arange(1, n + 1)
    exact = np.sqrt(2 / (n + 1)) * np.sin(m * np.pi * sites / (n + 1))
    np.testing.assert_allclose(clean_probability, exact ** 2, atol=2e-14, rtol=0)
    clean_p = 1 / np.sum(clean_probability ** 2)
    np.testing.assert_allclose(clean_p, 2 * (n + 1) / 3, atol=2e-12, rtol=0)
    assert 1 - 1e-12 <= participation <= n + 1e-12
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(3, 1, figsize=(8.2, 7.4), sharex=True,
                             gridspec_kw={'height_ratios': [1, 1.3, 1.3]})
    fig.suptitle(f'One random chain, one normalized eigenstate: N = {n}, W/t = {args.disorder:g}', fontsize=14)
    axes[0].plot(sites, epsilon / t, color='#b56c24', lw=1.1)
    axes[0].axhline(energy[j] / t, color='#235f93', ls='--', label=f'Selected E/t = {energy[j]/t:.3f}')
    axes[0].set_ylabel(r'On-site energy $\epsilon_n/t$')
    axes[0].legend(loc='upper right', fontsize=10)
    axes[1].plot(sites, probability, color='#235f93', lw=1.4, label=f'Random chain: P = {participation:.2f}')
    axes[1].plot(sites, clean_probability, color='#777777', lw=0.9, alpha=0.9, label=f'Clean standing wave: P = {clean_p:.0f}')
    axes[1].set_ylabel(r'Probability $|\psi_n|^2$')
    axes[1].legend(loc='upper right', fontsize=10)
    axes[2].semilogy(sites, probability, color='#235f93', lw=1.2)
    axes[2].semilogy(sites, clean_probability, color='#777777', lw=0.9, alpha=0.8)
    axes[2].set_ylabel(r'$|\psi_n|^2$ (log scale)')
    axes[2].set_ylim(max(probability.min() / 3, 1e-32), 1)
    axes[2].set_xlabel('Site n; open ends (no bond from N to 1)')
    for ax in axes:
        ax.grid(alpha=0.2)
        ax.set_xlim(1, n)
    fig.subplots_adjust(left=0.11, right=0.98, top=0.91, bottom=0.11, hspace=0.16)
    fig.text(0.5, 0.012, f'Chosen model, seed {args.seed}; no absorption, fitted tail, or measured data.', ha='center', fontsize=10)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
    print(json.dumps({'N': n, 'W_over_t': args.disorder, 'seed': args.seed,
                      'selected_energy_over_t': float(energy[j]/t), 'P': float(participation),
                      'peak_site': int(np.argmax(probability) + 1), 'clean_P': float(clean_p),
                      'normalization_residual': float(abs(probability.sum() - 1)),
                      'checks': ['all eigenvector normalizations', 'orthogonality', 'eigenvalue residuals',
                                 'analytic clean standing wave', 'clean P = 2(N+1)/3', 'P bounds']}))


if __name__ == '__main__':
    main()
