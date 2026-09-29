"""Original tensile-elastica plot; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from the desired output directory. The PNG is written to the current directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    z = np.linspace(-5.0, 5.0, 2001)
    x = z - 2*np.tanh(z)
    y = 2/np.cosh(z)
    left, right = 1.0, 2.0
    for _ in range(60):
        mid = (left+right)/2
        if mid-2*np.tanh(mid) > 0:
            right = mid
        else:
            left = mid
    root = (left+right)/2
    crossing_y = 2/np.cosh(root)
    fig, ax = plt.subplots(figsize=(7.4, 3.7), facecolor='white', layout='constrained')
    ax.set_facecolor('white')
    ax.plot(x, y, color='#2563a6', lw=2.4)
    ax.scatter([0], [crossing_y], color='#c14432', s=28, zorder=3)
    ax.annotate('Self-intersection', xy=(0, crossing_y), xytext=(1.35, 1.0),
                arrowprops={'arrowstyle':'->', 'color':'#555555'}, fontsize=10)
    for v in [-3.3, -0.65, 0.65, 3.3]:
        i = np.argmin(np.abs(z-v))
        ax.annotate('', xy=(x[i+30], y[i+30]), xytext=(x[i], y[i]),
                    arrowprops={'arrowstyle':'->', 'color':'#2563a6', 'lw':1.5})
    ax.axhline(0, color='#aaaaaa', lw=0.7, ls='--')
    ax.set(xlabel=r'$x/\ell$', ylabel=r'$y/\ell$', title='Tensile elastica: a loop between horizontal tails', ylim=(-0.18, 2.25))
    ax.set_aspect('equal', adjustable='box')
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=0.16)
    output = Path.cwd()/'2011-tensile-elastica-loop.png'
    fig.savefig(output, dpi=160, facecolor='white')
    plt.close(fig)
    print(output)


if __name__ == '__main__':
    main()
