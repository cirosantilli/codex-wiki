"""Plot the spring-charge energy barrier. Python 3.14; project pyproject.toml.

Run from the matching _media directory. Write only the PNG in the current directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    s = np.linspace(0.15, 1, 900)
    fig, ax = plt.subplots(figsize=(7.4, 4.2), layout='constrained')
    fig.set_facecolor('white')
    for ell, color, label in [
        (1.95, '#1966a6', r'$\ell_1<\ell<\ell_2$: collision'),
        (2.00, '#9a6000', r'$\ell=\ell_2$: asymptotic approach'),
        (2.20, '#a02040', r'$\ell>\ell_2$: turning point'),
    ]:
        relative_potential = 0.5 * (1-s)**2 + (1-1/s)/ell**3
        ax.plot(s, relative_potential, color=color, lw=2, label=label)
    ell = 2.2
    turning = (1 + np.sqrt(1-8/ell**3))/2
    ax.plot([turning, 1], [0, 0], 'o', color='#a02040', ms=5)
    ax.plot(0.5, 0, 'o', color='#9a6000', ms=5)
    ax.axhline(0, color='#333333', lw=0.8)
    ax.annotate('released from rest', xy=(1, 0), xytext=(0.73, 0.034),
                arrowprops={'arrowstyle': '->', 'color': '#333333'}, fontsize=10)
    ax.annotate('forbidden barrier', xy=(0.39, 0.041), xytext=(0.18, 0.068),
                arrowprops={'arrowstyle': '->', 'color': '#a02040'}, fontsize=10,
                color='#a02040')
    ax.set(xlim=(0.15, 1.03), ylim=(-0.065, 0.105),
           xlabel=r'Position $s=x/\ell$', ylabel=r'$(V-E)/(k\ell^2)$',
           title='Motion is allowed where the curve is at or below zero')
    ax.grid(alpha=0.2)
    ax.legend(loc='lower right', fontsize=9, framealpha=1)
    fig.savefig('mathematics-iv-q4-collision-threshold.png', dpi=150,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
