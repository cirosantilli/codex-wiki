"""Continuous population growth and equilibria; Python 3.14, NumPy/Matplotlib per pyproject.toml."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    b, delta, r = 1., 1., 3.
    n = np.linspace(0, 3, 700)
    f = n*(r/(1+b*n*n)-delta)
    star = np.sqrt((r-delta)/(b*delta))
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), layout='constrained')
    ax = axes[0]
    ax.axhline(0, color='#555f68', lw=.9)
    ax.plot(n, f, color='#176da5', lw=2)
    ax.scatter([0, star], [0, 0], color='#263238', zorder=4, s=25)
    for start, stop in [(.28,.7), (2.45,1.95)]:
        ax.annotate('', xy=(stop,.09), xytext=(start,.09),
                    arrowprops={'arrowstyle':'->', 'color':'#c05b1f', 'lw':1.6})
    ax.annotate(r'$N^*$', (star,0), xytext=(0,-19), textcoords='offset points', ha='center')
    ax.set(xlabel=r'Population $N$', ylabel=r'Growth rate $f(N)$',
           title=r'Growth curve: $r=3$, $b=\delta=1$', xlim=(0,3))
    ax = axes[1]
    rp = np.linspace(delta, 3.5, 600)
    ax.plot([0,delta], [0,0], color='#176da5', lw=2.3, label='Stable')
    ax.plot([delta,3.5], [0,0], color='#c15b21', lw=2, ls='--', label='Unstable')
    ax.plot(rp, np.sqrt((rp-delta)/(b*delta)), color='#176da5', lw=2.3)
    ax.scatter([delta], [0], color='#263238', zorder=5, s=30)
    ax.axvline(delta, color='#a8afb5', ls=':', lw=.9)
    ax.text(1.8, 1.72, r'$N^*=\sqrt{(r-\delta)/(b\delta)}$', fontsize=10)
    ax.set(xlabel=r'Recruitment parameter $r$', ylabel='Nonnegative steady population',
           title=r'Bifurcation diagram: $b=\delta=1$', xlim=(0,3.5), ylim=(-.15,1.9), xticks=[0,1,2,3])
    ax.legend(frameon=False, loc='upper left')
    for ax in axes:
        ax.spines[['top','right']].set_visible(False)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=150, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
