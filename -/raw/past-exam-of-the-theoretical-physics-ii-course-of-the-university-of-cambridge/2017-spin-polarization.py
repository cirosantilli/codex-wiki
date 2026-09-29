"""Render thermal spin polarization to a PNG in the working directory."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    u = np.linspace(-4.2, 4.2, 801)
    fig, ax = plt.subplots(figsize=(8, 4), dpi=120, facecolor='white')
    ax.set_facecolor('white')
    ax.axvspan(-4.2, 0, color='#f9e7da', alpha=0.6)
    ax.axvspan(0, 4.2, color='#dceef9', alpha=0.6)
    ax.axhline(0, color='0.5', lw=0.8)
    ax.axvline(0, color='0.5', lw=0.8)
    for level in (-1, 1):
        ax.axhline(level, color='0.4', lw=0.9, ls='--')
    ax.plot(u, np.tanh(u), color='#174f89', lw=2.8)
    ax.scatter([0], [0], color='#174f89', s=25, zorder=4)
    ax.text(-2.1, 0.75, 'Population inversion\n(negative temperature)',
            ha='center', va='center', fontsize=10)
    ax.text(2.1, -0.75, 'Positive temperature',
            ha='center', va='center', fontsize=10)
    ax.annotate('Maximally mixed', xy=(0, 0), xytext=(0.35, -0.34),
                fontsize=10, arrowprops={'arrowstyle': '-', 'color': '0.4'})
    ax.set(xlim=(-4.2, 4.2), ylim=(-1.15, 1.15),
           xlabel=r'Dimensionless inverse temperature $u=\beta\gamma\hbar B/2$',
           ylabel=r'Mean spin $2\langle S_z\rangle/\hbar$',
           title=r'Thermal spin polarization: $\gamma B>0$')
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.grid(alpha=0.17)
    fig.tight_layout()
    fig.savefig(Path('2017-spin-polarization.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
