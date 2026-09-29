"""Original plane-wave calculation; Python 3.14/numpy 2.3.5/matplotlib 3.10.7.

Run from the mirrored _media directory. H/E_L has diagonal (n-alpha)^2
and adjacent entries -lambda/(2E_L). No source figures are reused.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def spectrum(alpha, depth, cutoff=18):
    n = np.arange(-cutoff, cutoff+1)
    off = np.full(len(n)-1, -depth/2)
    return np.array([np.linalg.eigvalsh(np.diag((n-a)**2) + np.diag(off, 1) + np.diag(off, -1))[:2] for a in alpha])


def main():
    alpha = np.linspace(-1, 1, 501)
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 3.7), layout='constrained')
    for ax, depth, title in zip(axes, [0, 0.18, 8], ['Free ring', 'Weak potential', 'Deep potential']):
        values = spectrum(alpha, depth)
        for j, color in enumerate(['#236bc0', '#c26712']):
            ax.plot(alpha, values[:, j], color=color, lw=2, label=fr'$\epsilon_{j}/E_L$')
        ax.set(xlim=(-1, 1), xlabel=r'$\alpha=aL/(2\pi\hbar)$', title=fr'{title}: $\lambda/E_L={depth:g}$')
        ax.set_xticks([-1, -0.5, 0, 0.5, 1])
        ax.grid(alpha=0.18)
        ax.set_ylabel(r'$E/E_L$')
        if depth == 8:
            for j in range(2):
                ax.axhline(-depth + np.sqrt(2*depth)*(j+0.5), ls='--', color='0.45', lw=1, label='harmonic estimate' if j == 0 else None)
            ax.set_ylim(-6.8, -1.0)
        else:
            ax.set_ylim(-0.09, 1.1)
        ax.legend(fontsize=8, loc='upper center')
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
