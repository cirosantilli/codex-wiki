#!/usr/bin/env python3
"""Constructed factor-rotation illustration; outputs its PNG into the CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
The loadings are illustrative values, not participant data.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    loading = np.array([[.8, 0.0], [.6, .1], [.1, .7], [0.0, .8]])
    theta = np.deg2rad(35.0)
    rotation = np.array([[np.cos(theta), -np.sin(theta)],
                         [np.sin(theta), np.cos(theta)]])
    rotated = loading @ rotation
    residual = np.diag(1.0 - np.sum(loading**2, axis=1))
    covariance = loading @ loading.T + residual
    covariance_rotated = rotated @ rotated.T + residual
    assert np.allclose(rotation @ rotation.T, np.eye(2), atol=1e-14)
    assert np.allclose(covariance, covariance_rotated, atol=1e-14)
    assert np.linalg.eigvalsh(covariance).min() > 0
    assert np.allclose(np.diag(covariance), 1.0)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 3.7), dpi=100)
    fig.patch.set_facecolor('white')
    for ax, data, title in zip(axes, [loading, rotated],
                                ['Initial factor loadings', 'After a 35° rotation']):
        ax.set_facecolor('white')
        ax.imshow(data, cmap='RdBu', vmin=-1, vmax=1, aspect='auto')
        ax.set_xticks([0, 1], ['Factor 1', 'Factor 2'])
        ax.set_yticks(range(4), [f'Indicator {j+1}' for j in range(4)])
        ax.set_title(title, fontweight='bold', pad=10)
        for (i, j), value in np.ndenumerate(data):
            ax.text(j, i, f'{value:.2f}', va='center', ha='center',
                    color='white' if abs(value) > .65 else '#172b3a', fontsize=12)
        ax.tick_params(length=0)
        for spine in ax.spines.values():
            spine.set_visible(False)
    fig.suptitle('Different axes, identical modeled covariance',
                 fontsize=15, fontweight='bold', color='#19364b', y=.96)
    fig.text(.5, .105, r'$\Lambda\Lambda^T+\Psi=(\Lambda Q)(\Lambda Q)^T+\Psi$',
             ha='center', fontsize=14, color='#19364b')
    fig.text(.5, .035, 'Constructed example: four indicators, two factors; no study data',
             ha='center', fontsize=10, color='#455e70')
    fig.subplots_adjust(left=.13, right=.98, top=.77, bottom=.23, wspace=.55)
    destination = Path.cwd() / (Path(__file__).stem + '.png')
    fig.savefig(destination, dpi=100, facecolor='white', transparent=False,
                metadata={'Software': 'Original codex-wiki matplotlib generator'})
    plt.close(fig)


if __name__ == '__main__':
    main()
