"""Generate the original adjustment sketches in the caller's cwd.
Tested with Python 3.14, NumPy 2.3.5 and matplotlib 3.10.7.
MPLCONFIGDIR is supplied by the caller and is never overridden here.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def profiles(s, r):
    height = -0.5 * (np.exp(-np.abs(s-r)) - np.exp(-np.abs(s+r)))
    velocity = np.where(np.abs(s) <= r, np.exp(-r)*np.cosh(s), -np.sinh(r)*np.exp(-np.abs(s)))
    return height, velocity


def main():
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.2), dpi=100, facecolor='white')
    for col, (r, extent) in enumerate([(0.2, 4), (4, 8)]):
        s = np.linspace(-extent, extent, 1601)
        h, u = profiles(s, r)
        axes[0, col].plot(s, h, color='#006e9c', linewidth=2)
        for lo, hi, inside in [(-extent, -r, False), (-r, r, True), (r, extent, False)]:
            part = np.linspace(lo, hi, 501)
            v = np.exp(-r)*np.cosh(part) if inside else -np.sinh(r)*np.exp(-np.abs(part))
            axes[1, col].plot(part, v, color='#a53f00', linewidth=2)
        inner = np.exp(-r)*np.cosh(r)
        outer = -np.sinh(r)*np.exp(-r)
        for edge in [-r, r]:
            axes[1, col].plot([edge, edge], [outer, inner], '--', color='#a53f00', linewidth=1)
            axes[1, col].scatter([edge, edge], [outer, inner], s=20, color='#a53f00', zorder=4)
        for row in range(2):
            ax = axes[row, col]
            ax.set_facecolor('white')
            ax.axhline(0, color='0.55', linewidth=0.7)
            for edge in [-r, r]:
                ax.axvline(edge, color='0.65', linestyle=':', linewidth=1)
            ax.set_xlim(-extent, extent)
            ax.grid(alpha=0.16)
            ax.set_xlabel(r'$y/\lambda$')
        axes[0, col].set_title(('Narrow strip' if col == 0 else 'Wide strip') + f': $a/\\lambda={r:g}$')
        axes[0, col].set_ylabel(r'$c\eta_f/(HU)$')
        axes[1, col].set_ylabel(r'$u_f/U$')
        axes[1, col].set_ylim(-0.6, 1.12)
    fig.suptitle('Geostrophic adjustment of a finite-width current', fontsize=15)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig('paper-79-adjustment-profiles.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
