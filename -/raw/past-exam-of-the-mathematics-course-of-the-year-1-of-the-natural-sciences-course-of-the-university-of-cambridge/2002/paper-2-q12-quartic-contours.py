"""Nine stationary points of a quartic. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    x, y = np.meshgrid(np.linspace(-1.7, 1.7, 901), np.linspace(-2.15, 2.15, 1001))
    z = x**4-y**4-x*x+4*y*y
    fig, ax = plt.subplots(figsize=(7.2, 7.8), dpi=120, layout='constrained')
    cs = ax.contour(x, y, z, levels=[-2, -.15, .5, 2, 3.5, 3.9, 5, 8], colors='#91a7b6', linewidths=1.05)
    ax.clabel(cs, fmt='%g', fontsize=8)
    ax.contour(x, y, z, levels=[0], colors='#ba7121', linewidths=1.9)
    ax.plot([], [], color='#ba7121', lw=1.9, label=r'$f=0$')
    t = np.linspace(0, 2*np.pi, 1500)
    ax.plot(np.sqrt(2.5)*np.cos(t), np.sqrt(2.5)*np.sin(t), color='#834ca3', lw=1.9, label=r'$f=15/4$: circle and hyperbola')
    xx = np.linspace(-1.7, 1.7, 1000)
    for sign in [-1, 1]:
        ax.plot(xx, sign*np.sqrt(xx*xx+1.5), color='#834ca3', lw=1.9)
    a, b = 1/np.sqrt(2), np.sqrt(2)
    ax.scatter([0, 0], [-b, b], marker='^', s=80, c='#c94742', edgecolors='white', linewidths=.6, zorder=6, label=r'Maxima: $f=4$')
    ax.scatter([-a, a], [0, 0], marker='v', s=80, c='#1d78a0', edgecolors='white', linewidths=.6, zorder=6, label=r'Minima: $f=-1/4$')
    sx, sy = [0], [0]
    for x0 in [-a, a]:
        for y0 in [-b, b]:
            sx.append(x0)
            sy.append(y0)
    ax.scatter(sx, sy, marker='x', s=55, c='#222222', linewidths=1.8, zorder=7, label=r'Saddles: $f=0$ or $15/4$')
    ax.axhline(0, c='.75', lw=.65, zorder=0)
    ax.axvline(0, c='.75', lw=.65, zorder=0)
    ax.set(xlim=(-1.7, 1.7), ylim=(-2.15, 2.15), xlabel='x', ylabel='y', title=r'$f(x,y)=x^4-y^4-x^2+4y^2$'+'\nNine stationary points and their contours')
    ax.set_aspect('equal')
    ax.legend(loc='upper center', bbox_to_anchor=(.5, -.11), ncol=2, fontsize=9, frameon=False)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
