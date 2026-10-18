"""Plot the parabolic O-mode barrier; tested with Python 3.14, NumPy/Matplotlib.

Run from the desired image directory. Writes only original2025-tunnelling.png
in the current working directory. Dependencies are in the root pyproject.toml.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    ratio = 0.75
    xt = np.sqrt(1 - ratio**2)
    x = np.linspace(-1.0, 1.0, 1201)
    q = x*x - xt*xt
    xb = np.linspace(-xt, xt, 801)
    decay = np.sqrt(np.maximum(xt*xt - xb*xb, 0))
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(2, 1, figsize=(7.6, 5.8), sharex=True, layout='constrained')
    ax = axes[0]
    ax.plot(x, q, color='#245b8b', linewidth=2.3)
    ax.axhline(0, color='#333333', linewidth=0.8)
    ax.fill_between(x, q, 0, where=q < 0, color='#e9aa5b', alpha=.3)
    ax.set_ylabel(r'$c^2 k^2/\omega_{pe0}^2$')
    ax.set_title(r'Ordinary-wave barrier: $\omega/\omega_{pe0}=0.75$')
    ax.text(-.92, .42, 'I: propagating', color='#245b8b')
    ax.text(-.22, -.18, 'II: evanescent', color='#895018')
    ax.text(.68, .42, 'III: propagating', color='#245b8b', ha='center')
    ax.set_ylim(-.55, .65)
    ax = axes[1]
    ax.plot(xb, decay, color='#ad631d', linewidth=2.3)
    ax.fill_between(xb, decay, 0, color='#e9aa5b', alpha=.4)
    ax.set_ylabel(r'$c\kappa/\omega_{pe0}$')
    ax.set_xlabel(r'$x/L$')
    ax.text(0, .20, r'$\eta=(\omega_{pe0} L/c)\times\mathrm{shaded\ area}$', ha='center')
    ax.set_ylim(0, .82)
    for ax in axes:
        for v in [-xt, xt]:
            ax.axvline(v, color='#777777', linewidth=.9, linestyle='--')
        ax.spines[['top', 'right']].set_visible(False)
        ax.set_xlim(-1, 1)
        ax.grid(alpha=.13)
    axes[1].set_xticks([-1, -xt, 0, xt, 1], ['−1', r'$-x_T/L$', '0', r'$x_T/L$', '1'])
    fig.savefig(Path.cwd() / 'original2025-tunnelling.png', dpi=140, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
