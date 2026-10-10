"""Compare bounded secant slopes with the square-root cusp.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Save an opaque white PNG with this script's basename in the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    # Check many pairs, including pairs crossing the absolute-value corner.
    grid = np.linspace(-3, 3, 301)
    differences = np.abs(grid[:, None] - grid[None, :])
    assert np.all(np.abs(np.abs(grid[:, None]) - np.abs(grid[None, :]))
                  <= differences + 1.e-14)
    assert np.all(np.abs(np.sin(grid[:, None]) - np.sin(grid[None, :]))
                  <= differences + 1.e-14)
    h = np.array([1., .25, .0625, .015625])
    ratios = np.sqrt(h) / h
    assert np.allclose(ratios, [1, 2, 4, 8])
    for radius in [1., 2., 4.]:
        x, y = radius, radius - 1.e-4
        ratio = abs(x*x-y*y) / abs(x-y)
        assert np.isclose(ratio, 2*radius-1.e-4)
    assert np.isclose(3*.01, .03) and np.isclose(5*.01, .05)

    fig, axes = plt.subplots(1, 3, figsize=(12.2, 5.1), dpi=110, facecolor='white')
    colors = ['#276b92', '#438048', '#9a4b3c']
    x = np.linspace(-1, 1, 501)
    axes[0].plot(x, np.abs(x), color=colors[0], lw=2.5)
    axes[0].plot([.15, .85], [.15, .85], 'o', color=colors[0], ms=6)
    axes[0].text(-.65, 1.045, 'Corner at zero\nNo derivative there', fontsize=11,
                 va='top', color=colors[0])
    axes[0].set(xlim=(-1.05, 1.05), ylim=(-.08, 1.12),
                title=r'$f(x)=|x|$', xlabel='x', ylabel='f(x)')
    axes[0].text(.5, -.26, r'$||x|-|y||\leq|x-y|$', transform=axes[0].transAxes,
                 ha='center', fontsize=12)
    axes[0].text(.5, -.36, 'One bound works across the corner.', transform=axes[0].transAxes,
                 ha='center', fontsize=10.5)

    x = np.linspace(-np.pi, np.pi, 501)
    axes[1].plot(x, np.sin(x), color=colors[1], lw=2.5)
    endpoints = np.array([-.65, 1.5])
    axes[1].plot(endpoints, np.sin(endpoints), color='#aeb6bf', ls='--', lw=1.5)
    axes[1].scatter(endpoints, np.sin(endpoints), color=colors[1], s=35, zorder=3)
    axes[1].set(xlim=(-np.pi, np.pi), ylim=(-1.15, 1.15),
                title=r'$f(x)=\sin x$', xlabel='x', ylabel='f(x)')
    axes[1].set_xticks([-np.pi, 0, np.pi], [r'$-\pi$', '0', r'$\pi$'])
    axes[1].text(.5, -.26, r'$|\sin x-\sin y|\leq|x-y|$', transform=axes[1].transAxes,
                 ha='center', fontsize=12)
    axes[1].text(.5, -.36, 'Derivative magnitude is at most one.', transform=axes[1].transAxes,
                 ha='center', fontsize=10.5)

    x = np.linspace(0, 1, 801)
    axes[2].plot(x, np.sqrt(x), color=colors[2], lw=2.5, label=r'$\sqrt{x}$')
    for value, slope, color in zip(h[:3], ratios[:3], ['#9ba6b2', '#32769e', '#cc8a2d']):
        axes[2].plot([0, value], [0, np.sqrt(value)], color=color, ls='--', lw=1.7)
        axes[2].scatter([value], [np.sqrt(value)], color=color, s=35, zorder=3)
    axes[2].set(xlim=(-.03, 1.03), ylim=(-.08, 1.12),
                title=r'$f(x)=\sqrt{x}$', xlabel='x', ylabel='f(x)')
    axes[2].text(.43, .23, 'h       secant slope\n1       1\n1/4    2\n1/16  4\n1/64  8',
                 fontsize=11, bbox={'facecolor': 'white', 'edgecolor': '#d3d8dd', 'pad': 5})
    axes[2].text(.5, -.26, r'$\sqrt{h}/h=1/\sqrt{h}\to\infty$',
                 transform=axes[2].transAxes, ha='center', fontsize=12)
    axes[2].text(.5, -.36, 'No finite bound near zero.', transform=axes[2].transAxes,
                 ha='center', fontsize=10.5)
    for ax in axes:
        ax.axhline(0, color='#bdc4cb', lw=.7)
        ax.axvline(0, color='#bdc4cb', lw=.7)
        ax.grid(color='#e6e9ec', lw=.6)
        ax.spines[['top', 'right']].set_visible(False)
        ax.title.set_fontsize(14)
    fig.suptitle('Lipschitz continuity bounds every secant slope', fontsize=16, y=.96)
    fig.subplots_adjust(left=.065, right=.975, bottom=.31, top=.81, wspace=.34)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
