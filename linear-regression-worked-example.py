"""Plot a constructed least-squares fit and its residuals; save a PNG to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.arange(5, dtype=float)
    y = np.array([1., 2., 2., 4., 5.])
    design = np.column_stack([np.ones_like(x), x])
    coefficients = np.linalg.lstsq(design, y, rcond=None)[0]
    fitted = design @ coefficients
    residual = y-fitted
    rss = residual @ residual
    r2 = 1-rss/np.sum((y-y.mean())**2)
    assert np.allclose(coefficients, [.8, 1])
    assert np.allclose(design.T @ residual, [0, 0])
    assert np.isclose(rss, .8)
    assert np.isclose(r2, 25/27)
    plt.rcParams.update({'font.size': 12})
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.9), layout='constrained', facecolor='white')
    xx = np.linspace(-.2, 4.2, 200)
    axes[0].plot(xx, coefficients[0]+coefficients[1]*xx, color='#2571a4',
                 lw=2.5, label=r'Fitted mean $\widehat y=0.8+x$')
    axes[0].vlines(x, np.minimum(y, fitted), np.maximum(y, fitted),
                   color='#b65032', lw=2.2, label='Residual deviations')
    axes[0].scatter(x, y, color='#2571a4', s=60, zorder=3, label='Constructed observations')
    axes[0].scatter(x, fitted, color='#d67720', marker='x', s=55, zorder=3, label='Fitted values')
    axes[0].set(xlabel='Predictor x', ylabel='Response y', xlim=(-.3, 4.4), ylim=(.4, 5.5),
                title='One fitted trend through five observations')
    axes[0].legend(loc='upper left', fontsize=9)
    axes[0].grid(alpha=.2)

    axes[1].axhline(0, color='#87929c', lw=1)
    axes[1].vlines(fitted, 0, residual, color='#b65032', lw=2)
    axes[1].scatter(fitted, residual, color='#b65032', s=60, zorder=3)
    for fi, ri in zip(fitted, residual):
        axes[1].annotate('%+.1f' % ri, (fi, ri), xytext=(0, 10 if ri >= 0 else -20),
                         textcoords='offset points', ha='center', fontsize=11)
    axes[1].set(xlabel='Fitted response', ylabel='Residual: observed - fitted',
                xlim=(.4, 5.2), ylim=(-1, .7), title='Residuals sum to zero and are orthogonal to x')
    axes[1].grid(alpha=.2)
    axes[1].text(3, .51, 'RSS = 0.8;  R² = 25/27 ≈ 0.926', ha='center', fontsize=11)
    fig.suptitle('Least squares separates a fitted component from an orthogonal residual', fontsize=15)
    fig.savefig(Path.cwd() / 'linear-regression-worked-example.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
