"""Original semicircular least-destruction path. Save PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(7.1, 4.5), layout='constrained')
    xx, yy = np.meshgrid(np.linspace(-1.35, 1.35, 240), np.linspace(0.12, 1.68, 220))
    ax.pcolormesh(xx, yy, np.minimum(1/yy, 5), cmap='Greens', shading='nearest', alpha=0.45, vmin=0, vmax=5)
    x = np.linspace(-1, 1, 400)
    y = np.sqrt(2-x*x)
    ax.plot(x, y, color='#174ea6', lw=2.7, label=r'Minimizer: $y=\sqrt{2-x^2}$')
    ax.plot([-1, 1], [1, 1], '--', color='#aa3344', lw=1.7, label='Straight competitor')
    ax.scatter([-1, 1], [1, 1], color='#111111', s=28, zorder=5)
    ax.text(-1.03, 0.88, r'$(-1,1)$', ha='right', fontsize=10)
    ax.text(1.03, 0.88, r'$(1,1)$', ha='left', fontsize=10)
    ax.annotate(r'Maximum height $\sqrt{2}$', xy=(0, np.sqrt(2)), xytext=(-0.6, 1.58),
                arrowprops={'arrowstyle':'->', 'color':'#333333'}, fontsize=10)
    ax.text(0, 0.45, 'Darker background: more undergrowth', ha='center', fontsize=10, color='#254f2a')
    ax.legend(loc='lower center', frameon=True, facecolor='white', fontsize=10)
    ax.axhline(0, color='#555555', lw=1)
    ax.set(xlim=(-1.45, 1.45), ylim=(0, 1.75), xlabel='x', ylabel='y',
           title='A longer geometric path destroys less undergrowth')
    ax.set_aspect('equal', adjustable='box')
    fig.savefig(Path.cwd() / 'paper-1-q9-minimum-destruction-path.png', dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
