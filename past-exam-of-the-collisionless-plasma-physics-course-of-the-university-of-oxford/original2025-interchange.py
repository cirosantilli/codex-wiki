"""Plot the kinetic-interchange threshold; Python 3.14, NumPy/Matplotlib.

Run from the desired image directory. Writes only original2025-interchange.png
in the current working directory. Dependencies are in the root pyproject.toml.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    u = np.linspace(0, 2, 601)
    unstable = np.linspace(0, 1, 301)
    stable = np.linspace(1, 2, 301)
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.9), layout='constrained')
    ax = axes[0]
    ax.axvspan(0, 1, color='#e9aa5b', alpha=.23)
    ax.axvspan(1, 2, color='#8ab2d2', alpha=.20)
    ax.plot(u, u*u-1, color='#363d4b', linewidth=2.3)
    ax.axhline(0, color='#333333', linewidth=.8)
    ax.set_ylabel(r'$\omega^2/\omega_I^2$')
    ax.set_title('Drive versus magnetic tension')
    ax.text(.46, 1.6, 'unstable', ha='center', color='#895018')
    ax.text(1.48, -.66, 'oscillatory', ha='center', color='#245b8b')
    ax = axes[1]
    ax.plot(unstable, np.sqrt(np.maximum(1-unstable**2, 0)), color='#ad631d', linewidth=2.3, label=r'growth $\gamma/\omega_I$')
    ax.plot(stable, np.sqrt(stable**2-1), color='#245b8b', linewidth=2.3, label=r'frequency $|\omega|/\omega_I$')
    ax.set_title('Time dependence of the displacement')
    ax.set_ylabel('Positive rate or frequency')
    ax.legend(loc='upper left', frameon=False, fontsize=10)
    ax.set_ylim(0, 2.05)
    for ax in axes:
        ax.axvline(1, color='#777777', linestyle='--', linewidth=.9)
        ax.set_xlabel(r'$|k_\parallel|/k_c$')
        ax.set_xlim(0, 2)
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(alpha=.13)
    fig.savefig(Path.cwd() / 'original2025-interchange.png', dpi=140, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
