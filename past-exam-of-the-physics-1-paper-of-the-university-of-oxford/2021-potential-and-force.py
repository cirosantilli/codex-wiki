"""Plot Oxford Physics 1 (2021), question 3. Python 3.14; NumPy, Matplotlib."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    x = np.linspace(-5, 5, 2001)
    potential = -x / (1 + x**2)
    force = (1 - x**2) / (1 + x**2)**2
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.1), layout='constrained')
    for ax in axes:
        ax.axhline(0, color='0.35', linewidth=0.8)
        ax.axvline(0, color='0.35', linewidth=0.8)
        ax.set(xlim=(-5, 5), xlabel=r'$x/A$, where $A=|a|>0$')
        ax.grid(alpha=0.18)
    ax = axes[0]
    ax.plot(x, potential, color='#2166ac', linewidth=2.3)
    ax.set(title=r'Potential energy ($k>0$)', ylabel=r'$AU/k$')
    ax.scatter([-1, 1], [0.5, -0.5], c=['#b2182b', '#1b7837'], s=48, zorder=3)
    ax.annotate('Unstable equilibrium', (-1, 0.5), xytext=(-4.7, 0.63),
                arrowprops={'arrowstyle': '->', 'color': '#b2182b'}, color='#b2182b')
    ax.annotate('Stable equilibrium', (1, -0.5), xytext=(0.5, -0.73),
                arrowprops={'arrowstyle': '->', 'color': '#1b7837'}, color='#1b7837')
    ax.set(ylim=(-0.85, 0.85), yticks=[-0.5, 0, 0.5])
    ax = axes[1]
    ax.plot(x, force, color='#762a83', linewidth=2.3)
    ax.scatter([-1, 1], [0, 0], c=['#b2182b', '#1b7837'], s=40, zorder=3)
    ax.scatter([-np.sqrt(3), 0, np.sqrt(3)], [-1/8, 1, -1/8], color='#762a83', s=27, zorder=3)
    ax.annotate(r'$F(0)=k/A^2$', (0, 1), xytext=(0.7, 1.02))
    ax.annotate(r'Minima at $x=\pm\sqrt{3}A$', (-np.sqrt(3), -1/8), xytext=(-4.7, -0.42),
                arrowprops={'arrowstyle': '->', 'color': '#762a83'})
    ax.set(title=r'Force: $F=-dU/dx$', ylabel=r'$A^2F/k$', ylim=(-0.55, 1.25), yticks=[-0.125, 0, 0.5, 1])
    output = Path.cwd() / Path(__file__).with_suffix('.png').name
    fig.savefig(output, dpi=110, facecolor='white', transparent=False,
                metadata={'Software': 'Oxford Physics 1 (2021) figure generator'})
    plt.close(fig)


if __name__ == '__main__':
    main()
