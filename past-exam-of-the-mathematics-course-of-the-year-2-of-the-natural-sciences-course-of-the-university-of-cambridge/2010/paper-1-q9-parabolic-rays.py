"""Original returning-ray geometry; Python 3.14, numpy and matplotlib.

Write the PNG to cwd, normally the mirrored media directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Dimensionless coordinates X=k*x, Y=k*y; choose k*x0=0.8, k*h=0.9.
    X0, H = .8, .9
    heights = [(1-np.sqrt(1-X0**2))/2, (1+np.sqrt(1-X0**2))/2]
    X = np.linspace(-X0, X0, 700)
    fig, ax = plt.subplots(figsize=(8, 4.8), facecolor='white', layout='constrained')
    ax.set_facecolor('white')
    ax.axhspan(0, H, color='#f4f8fa', zorder=0)
    ax.axhline(0, color='#333333', lw=1.3)
    ax.axhline(H, color='#666666', lw=1.1, ls=':')
    for Y0, colour in zip(heights, ['#166a9a', '#b65b20']):
        YY = Y0-X**2/(4*(1-Y0))
        ax.plot(X, YY, color=colour, lw=2.3, label=fr'$Y_0={Y0:.1f}$')
        ax.scatter([0], [Y0], s=22, color=colour)
    ax.scatter([-X0, X0], [0, 0], color='black', s=25, zorder=5)
    ax.text(-.86, H+.025, r'upper boundary: $Y=kh=0.9$', fontsize=10)
    ax.text(-.86, -.09, r'entry $(-X_0,0)$', fontsize=10)
    ax.text(.86, -.09, r'exit $(X_0,0)$', fontsize=10, ha='right')
    ax.annotate('larger speed\nat greater height', xy=(.87, .73), xytext=(.87, .3),
                fontsize=9, ha='center', arrowprops={'arrowstyle': '->', 'color': '#666666'})
    ax.set(xlim=(-1.1, 1.1), ylim=(-.12, 1.02), xlabel='$X=kx$', ylabel='$Y=ky$',
           title=r'Two returning rays when $X_0=0.8$: $(X_0)^2=4Y_0(1-Y_0)$')
    ax.legend(loc='center', bbox_to_anchor=(.5, .48), facecolor='white', framealpha=1)
    ax.grid(alpha=.12)
    fig.savefig(Path('paper-1-q9-parabolic-rays.png'), dpi=160, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
