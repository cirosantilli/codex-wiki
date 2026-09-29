#!/usr/bin/env python3
"""Leading composite boundary-layer sketches. Python 3.14, NumPy 2.3, Matplotlib 3.10.
Writes an opaque PNG basename to the caller's CWD; preserves MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    a, epsilon = 0.3, 0.0002
    x = np.linspace(a, 1, 1800)
    fig, axes = plt.subplots(2, 2, figsize=(8.6, 5.8), sharex=True, sharey=True,
                             layout='constrained', facecolor='white')
    for ax, (left, right) in zip(axes.flat, [(-1, -1), (-1, 1), (1, -1), (1, 1)]):
        xi_l = (x-a) / np.sqrt(epsilon)
        xi_r = (1-x) / np.sqrt(epsilon)
        shift_l = left * 2 / np.sqrt(a) * np.arccosh(np.sqrt(1.5))
        shift_r = right * 2 * np.arccosh(np.sqrt(1.5))
        layer_l = 1.5*a / np.cosh(np.sqrt(a)*(xi_l-shift_l)/2)**2
        layer_r = 1.5 / np.cosh((xi_r-shift_r)/2)**2
        ax.plot(x, -x+layer_l+layer_r, color='#175e97', lw=2, label='Leading composite')
        ax.plot(x, -x, color='#777777', lw=1, ls=':', label='Outer branch')
        ax.axhline(0, color='#a64712', lw=1.3, ls='--', label='Exact zero solution')
        ax.scatter([a, 1], [0, 0], color='black', s=14, zorder=4)
        ax.set_title(('Direct' if left<0 else 'Excursion')+' left; '+
                     ('direct' if right<0 else 'excursion')+' right', fontsize=10)
        ax.set_facecolor('white')
        ax.grid(alpha=.18)
        ax.set_ylim(-1.04, .58)
        ax.set_xlim(a, 1)
    for ax in axes[1]: ax.set_xlabel('x')
    for ax in axes[:,0]: ax.set_ylabel('y')
    axes[0,0].legend(fontsize=8, loc='lower left')
    fig.suptitle(r'Formal endpoint layers: $a=0.3$, $\alpha=\beta=0$, $\epsilon=0.0002$')
    fig.savefig('paper-76-boundary-layers.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
