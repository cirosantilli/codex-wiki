"""Draw exact square-function tolerance comparisons; Python 3.14, matplotlib 3.10."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12, 'axes.labelsize': 11})
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.6), layout='constrained')
    fig.set_facecolor('white')
    fig.suptitle(r'One output tolerance $\varepsilon=0.4$: the domain matters for $f(x)=x^2$', fontsize=15)
    blue, orange, purple = '#1764a0', '#bb5a13', '#7254a3'
    ax = axes[0]
    a = np.linspace(0, 8, 300)
    ax.plot(a, 0.4 / (2 * a + 1), color=blue, lw=2.5)
    ax.axhline(0.1, color=orange, ls='--', lw=1.8, label=r'$\delta=0.1$ for $[0,2]$')
    ax.scatter([0, 1, 2, 4, 8], 0.4 / (2 * np.array([0, 1, 2, 4, 8]) + 1), color=blue, zorder=3)
    ax.axvspan(0, 2, color=orange, alpha=0.08)
    ax.set(xlim=(0, 8), ylim=(0, 0.43), xlabel=r'Base location $a\geq0$', ylabel=r'Sufficient input half-width $\delta$', title='Local windows can shrink')
    ax.text(3.0, 0.29, r'$\delta(a)=\dfrac{0.4}{2|a|+1}$', fontsize=12, color=blue)
    ax.text(3.0, 0.20, 'A local choice alone\ndoes not rule out\na common tolerance.', fontsize=10)
    ax.legend(loc='upper right', bbox_to_anchor=(1, 0.34), fontsize=9)
    ax = axes[1]
    h = np.linspace(0, 0.14, 250)
    ax.axvspan(0, 0.1, color=blue, alpha=0.08)
    ax.axhline(0.4, color=orange, ls='--', lw=1.8, label=r'Output tolerance $\varepsilon$')
    ax.axvline(0.1, color=blue, ls=':', lw=1.8)
    ax.plot(h, 4*h, color=blue, lw=2.3, label=r'Bound $4h$')
    ax.plot(h, 4*h-h*h, color=purple, lw=2, label=r'Pair $2-h,2$: $4h-h^2$')
    ax.scatter([0.08], [0.3136], color=purple, zorder=4)
    ax.annotate('(0.08, 0.3136)', (0.08, 0.3136), xytext=(0.024, 0.17), fontsize=9, arrowprops={'arrowstyle': '->', 'color': purple})
    ax.set(xlim=(0, 0.14), ylim=(0, 0.59), xlabel=r'Input distance $h=|x-y|$', ylabel=r'Output distance $|x^2-y^2|$', title=r'On $[0,2]$: one width works')
    ax.legend(loc='upper left', fontsize=8)
    ax.text(0.01, 0.035, r'$h<0.1\ \Rightarrow\ |x^2-y^2|<0.4$', fontsize=10)
    ax = axes[2]
    n = np.arange(1, 25)
    h = 1/n
    ax.scatter(h, 2+1/n**2, c=blue, s=26, zorder=3)
    ax.axhline(2, color=blue, ls=':', lw=1.5)
    ax.axhline(0.4, color=orange, ls='--', lw=1.8)
    ax.set(xlim=(-0.04, 1.07), ylim=(0, 3.25), xlabel=r'Input distance $1/n$', ylabel=r'Output distance $2+1/n^2$', title=r'On $\mathbb{R}$: no width works')
    ax.text(0.28, 1.45, r'$x_n=n,\quad y_n=n+1/n$', fontsize=11)
    ax.annotate('Inputs get closer;\noutputs stay above 2.', (1/24, 2+1/24**2), xytext=(0.30, 2.70), fontsize=10, arrowprops={'arrowstyle': '->', 'color': blue})
    ax.text(0.30, 0.52, r'$\varepsilon=0.4$', color=orange)
    for ax in axes:
        ax.set_facecolor('white')
        ax.grid(alpha=0.17)
        ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(Path(__file__).stem+'.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
