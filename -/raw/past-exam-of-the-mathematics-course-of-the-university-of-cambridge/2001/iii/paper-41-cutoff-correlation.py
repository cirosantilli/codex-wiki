"""Original density-spectrum and correlation plot; save the PNG to cwd.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def normalized_correlation(q):
    """xi(r)/xi(0) for P(k)=A*k on [0,K], with q=K*r."""
    q = np.asarray(q, dtype=float)
    answer = np.empty_like(q)
    small = np.abs(q) < 0.05
    x = q[small]
    answer[small] = 1 - x*x/9 + x**4/240 - x**6/12600
    x = q[~small]
    answer[~small] = 4*(-x*x*np.cos(x)+2*x*np.sin(x)+2*(np.cos(x)-1))/x**4
    return answer


def main():
    assert float(normalized_correlation(0)) == 1
    assert float(normalized_correlation(5)) < 0
    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white',
                         'axes.facecolor': 'white', 'savefig.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(7.875, 3.25), dpi=160)
    left, right = axes
    left.plot([0, 1], [0, 1], lw=2.4, color='#2166ac')
    left.plot([1, 1.5], [0, 0], lw=2.4, color='#2166ac')
    left.plot(1, 1, 'o', color='#2166ac', ms=5)
    left.plot(1, 0, 'o', mec='#2166ac', mfc='white', ms=5, zorder=4)
    left.axvline(1, ls='--', color='0.55', lw=1)
    left.set(xlim=(0, 1.5), ylim=(-0.05, 1.13), xlabel=r'$k/K$',
             ylabel=r'$P(k)/(AK)$', title='Nonnegative spectrum with a cutoff')
    left.text(0.98, 1.08, r'$K=k_{\rm max}$', ha='right', va='top', fontsize=9)
    q = np.linspace(0, 18, 1801)
    values = normalized_correlation(q)
    right.axhline(0, color='0.4', lw=0.8)
    right.plot(q, values, color='#2166ac', lw=2.1)
    right.fill_between(q, values, 0, where=values < 0, color='#d6604d', alpha=0.4)
    right.set(xlim=(0, 18), ylim=(-0.2, 1.06), xlabel=r'$Kr$',
              ylabel=r'$\xi(r)/\xi(0)$', title='Oscillating spatial correlation')
    right.annotate('Negative correlation\nis allowed',
                   xy=(5, float(normalized_correlation(5))), xytext=(7.0, 0.38),
                   arrowprops={'arrowstyle': '->', 'color': '#b2182b'},
                   color='#b2182b', fontsize=9)
    for axis in axes:
        axis.grid(alpha=0.18)
    fig.tight_layout(pad=1.1, w_pad=2.0)
    fig.savefig(Path('paper-41-cutoff-correlation.png'), dpi=160, transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
