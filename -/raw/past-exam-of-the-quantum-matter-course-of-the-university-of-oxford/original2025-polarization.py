"""Python 3.14, NumPy and Matplotlib; write same-basename PNG to Path.cwd()."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/oxford-2025-quantum-matter-mpl')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    out = Path.cwd()
    u = np.linspace(1e-6, np.pi / 2, 1800)
    v = -np.pi * np.sin(u) / (u + np.sin(u) * np.cos(u))
    x = .5 - u / np.pi
    fig, ax = plt.subplots(figsize=(7.3, 3.7), layout='constrained')
    for endpoint in (0, 1):
        ax.plot([-2.65, -2], [endpoint, endpoint], color='#126782', lw=2.6)
    ax.plot(v, x, color='#126782', lw=2.6)
    ax.plot(v, 1 - x, color='#126782', lw=2.6)
    ax.plot([-np.pi / 2, -.8], [.5, .5], color='#126782', lw=2.6)
    for a in (-2, -np.pi / 2):
        ax.axvline(a, color='.6', ls=':', lw=1)
    ax.set(xlim=(-2.65, -.8), ylim=(-.06, 1.06), xlabel=r'$V/|t|$',
           ylabel=r'Minimizing spin-up fraction $x$', title='Fermi-sea variational ground states')
    ax.set_xticks([-2.5, -2, -np.pi / 2, -1], ['$-2.5$', '$-2$', r'$-\pi/2$', '$-1$'])
    ax.set_yticks([0, .5, 1], ['$0$', '$1/2$', '$1$'])
    ax.text(-2.56, .49, 'Fully polarized\n(two choices)', fontsize=10, va='center')
    ax.text(-1.79, .49, 'Partial\npolarization', fontsize=10, ha='center')
    ax.text(-1.15, .58, 'Unpolarized', fontsize=10, ha='center')
    ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(out / (Path(__file__).stem + '.png'), dpi=150, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
