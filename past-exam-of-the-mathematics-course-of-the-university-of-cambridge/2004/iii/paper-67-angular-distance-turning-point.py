"""Original distance-maximum sketch; tested with root Python/NumPy/Matplotlib pins.
Output is an opaque same-basename PNG in the caller's CWD.
Preserves the caller's MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def maximum_redshift(w):
    alpha = 1.5 * (1 + np.asarray(w))
    exponent = np.ones_like(alpha)
    np.divide(np.log(alpha), alpha - 1, out=exponent, where=alpha != 1)
    return np.expm1(exponent)


def main():
    w = np.unique(np.r_[np.linspace(-0.995, 0.999, 1200), -1 / 3, 0, 1 / 3])
    fig, ax = plt.subplots(figsize=(7.0, 4.5), layout='constrained', facecolor='white')
    ax.plot(w, maximum_redshift(w))
    points = [(-1 / 3, np.e - 1, r'$w=-1/3$'), (0, 1.25, r'$w=0$'),
              (1 / 3, 1, r'$w=1/3$')]
    for wp, zp, label in points:
        ax.scatter(wp, zp, color='C0', zorder=3)
        ax.annotate(label, (wp, zp), xytext=(6, 9), textcoords='offset points', fontsize=9)
    ax.scatter(1, np.sqrt(3) - 1, facecolors='white', edgecolors='C0', zorder=3)
    ax.annotate(r'$z_m\to\infty$', (-0.96, 70), fontsize=11)
    ax.set(xlabel=r'Equation-of-state parameter $w$', ylabel=r'Maximum redshift $z_m$ (log scale)',
           title='Angular diameter distance turning point', xlim=(-1, 1.02), ylim=(0.65, 160), yscale='log')
    ax.grid(alpha=0.2, which='both')
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
