"""Schematic absorber distribution, not an observational fit.
Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; preserves MPLCONFIGDIR.
Writes only the same-basename opaque PNG to the caller's CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    x = np.unique(np.r_[np.linspace(12, 22, 700), 17.2, np.log10(2e20)])
    damp = np.log10(2e20)
    # Relative per-unit-column distribution. Slopes are illustrative only.
    logf = np.where(x <= 17.2, -1.5 * (x - 13),
                    np.where(x <= damp, -1.5 * (17.2 - 13) - (x - 17.2),
                             -1.5 * (17.2 - 13) - (damp - 17.2) - 2 * (x - damp)))
    logf -= np.maximum(x - 21.4, 0) ** 2 * 2
    fig, ax = plt.subplots(figsize=(7.4, 4.5), layout='constrained', facecolor='white')
    ax.axvspan(12, 17.2, color='C0', alpha=0.07)
    ax.axvspan(17.2, damp, color='C1', alpha=0.07)
    ax.axvspan(damp, 22, color='C2', alpha=0.07)
    ax.plot(x, logf, color='black')
    for knot in [17.2, damp]:
        ax.axvline(knot, color='0.5', linestyle='--', linewidth=1)
    ax.text(14.4, 0.65, 'Lyman-alpha forest', ha='center', fontsize=10)
    ax.text(18.7, 0.65, 'Lyman-limit\nsystems', ha='center', fontsize=10)
    ax.text(21.15, 0.65, 'Damped\nsystems', ha='center', fontsize=10)
    ax.text(12.3, -12.0, 'Schematic shapes; arbitrary normalization\nDistribution per unit column, not per log bin', fontsize=9)
    ax.set(xlabel=r'$\log_{10}[N_{\rm HI}/(\mathrm{cm}^{-2})]$',
           ylabel=r'$\log_{10}[f_X(N)/f_X(10^{13}\,\mathrm{cm}^{-2})]$',
           title='Neutral-hydrogen column distribution near redshift 3', xlim=(12, 22), ylim=(-13.5, 2))
    ax.grid(alpha=0.15)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
