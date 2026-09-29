"""Original Rabi envelope; Python 3.14/numpy 2.3.5/matplotlib 3.10.7.

Run from the mirrored _media directory. Frequency is scaled by |Omega|.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-4, 4, 801)
    fig, ax = plt.subplots(figsize=(6.8, 4.1), layout='constrained')
    ax.plot(x, 1/(1+x*x), color='#236bc0', lw=2.5)
    ax.hlines(.5, -4, 4, colors='0.55', linestyles='--', lw=1)
    ax.vlines([-1, 1], 0, .5, colors='#c26712', linestyles='--', lw=1.3)
    ax.scatter([-1, 0, 1], [.5, 1, .5], color='#c26712', zorder=3)
    ax.annotate('', xy=(-1, .25), xytext=(1, .25), arrowprops={'arrowstyle':'<->', 'color':'#9244a0', 'lw':1.6})
    ax.text(0, .3, r'$\Delta\omega=2|\Omega|=|\gamma B_x|$', ha='center', color='#9244a0')
    ax.set(xlim=(-4, 4), ylim=(0, 1.08), xlabel=r'Drive detuning $(\omega-\omega_{\rm res})/|\Omega|$', ylabel=r'$\max_t P_{\downarrow}(t)$', title='Transition envelope after optimizing the pulse duration')
    ax.grid(alpha=.18)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
