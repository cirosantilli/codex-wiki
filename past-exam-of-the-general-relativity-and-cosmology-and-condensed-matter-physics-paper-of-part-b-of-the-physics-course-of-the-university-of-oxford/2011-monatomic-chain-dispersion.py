"""Generate the Oxford 2011 monatomic-chain dispersion sketch (Python 3.14)."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    q = np.linspace(-1, 1, 801)
    fig, ax = plt.subplots(figsize=(6.7, 3.6), layout='constrained')
    ax.plot(q, 2*np.abs(np.sin(np.pi*q/2)), color='#155b8a', lw=2.3,
            label=r'$\omega/\sqrt{K/m}=2|\sin(ka/2)|$')
    qt = np.linspace(0, .57, 100)
    ax.plot(qt, np.pi*qt, '--', color='#bd542a', lw=1.6,
            label=r'Initial tangent: $\omega=vk$')
    ax.annotate(r'$v=a\sqrt{K/m}$', xy=(.34, np.pi*.34), xytext=(.38, .64),
                arrowprops={'arrowstyle':'->', 'color':'#bd542a'}, color='#9c4121')
    ax.axhline(0, color='black', lw=.7)
    ax.axvline(0, color='black', lw=.7)
    ax.set(xlim=(-1.04, 1.04), ylim=(-.08, 2.25),
           xlabel=r'$ka/\pi$', ylabel=r'$\omega/\sqrt{K/m}$',
           title='One acoustic branch in the first Brillouin zone')
    ax.set_xticks([-1,-.5,0,.5,1])
    ax.legend(loc='upper center', fontsize=9, frameon=False)
    ax.grid(alpha=.17)
    fig.savefig(Path.cwd()/'2011-monatomic-chain-dispersion.png', dpi=130,
                facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
