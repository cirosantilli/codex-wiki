"""Show equal regression summaries with different residual shapes; save to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.arange(-2, 3, dtype=float)
    fitted = 3+x
    patterns = [.2*np.array([2., -1., -2., -1., 2.]),
                .2*np.sqrt(7/5)*np.array([1., -2., 0., 2., -1.])]
    labels = ['Quadratic residual component', 'Alternating residual component']
    colors = ['#b9652a', '#237c96']
    design = np.column_stack([np.ones_like(x), x])
    plt.rcParams.update({'font.size': 12})
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.3), layout='constrained', facecolor='white')
    xx = np.linspace(-2.15, 2.15, 250)
    for i, (residual, label, color) in enumerate(zip(patterns, labels, colors)):
        y = fitted+residual
        coefficients = np.linalg.lstsq(design, y, rcond=None)[0]
        assert np.allclose(coefficients, [3, 1])
        assert np.allclose(design.T@residual, [0, 0])
        assert np.isclose(residual@residual, .56)
        assert np.isclose(1-(residual@residual)/np.sum((y-y.mean())**2), 125/132)
        axes[0, i].plot(xx, 3+xx, color='#667c90', lw=2, label='Identical fit: 3 + x')
        axes[0, i].scatter(x, y, s=65, color=color, zorder=3, label='Constructed data')
        axes[0, i].set(title=label, xlabel='Predictor x', ylabel='Response y', ylim=(.5, 5.8))
        axes[0, i].legend(loc='upper left', fontsize=10)
        axes[1, i].axhline(0, color='#87929c', lw=1)
        axes[1, i].vlines(fitted, 0, residual, color=color, lw=1.5)
        axes[1, i].scatter(fitted, residual, color=color, s=65, zorder=3)
        if i == 0:
            axes[1, i].plot(3+xx, .2*(xx*xx-2), color=color, lw=2, alpha=.8,
                            label=r'Exact pattern: $0.2(x^2-2)$')
            axes[1, i].legend(loc='lower center', fontsize=10)
        axes[1, i].set(xlabel='Fitted response', ylabel='Residual',
                      xlim=(.6, 5.4), ylim=(-.68, .65), title='Subtract the same fitted trend')
        for ax in axes[:, i]:
            ax.grid(alpha=.2)
    fig.suptitle('Same slope, intercept, RSS = 0.56 and R² = 125/132 ≈ 0.947', fontsize=15)
    fig.savefig(Path.cwd() / 'regression-residual-patterns.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
