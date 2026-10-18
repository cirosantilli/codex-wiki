"""Plot analytic annulus fields; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    u = np.linspace(-5, 5, 1801)
    potential = np.sqrt(u*u+4)-np.sqrt(u*u+1)
    field = u*(1/np.sqrt(u*u+1)-1/np.sqrt(u*u+4))
    peak = 2**(2/3)/np.sqrt(1+2**(2/3))
    epeak = peak*(1/np.sqrt(peak*peak+1)-1/np.sqrt(peak*peak+4))
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.4), layout='constrained')
    axes[0].plot(u, potential, color='#1c6591', lw=2.5)
    axes[0].set(title='Potential: even about the centre', ylabel=r'$2\epsilon_0 V/(\sigma a)$', xlabel=r'$x/a$')
    axes[1].plot(u, field, color='#147d63', lw=2.5, label='Exact axial field')
    tangent = np.linspace(-0.8, 0.8, 101)
    axes[1].plot(tangent, tangent/2, '--', color='#b76b20', label='Small-displacement tangent')
    axes[1].axvline(peak, color='#555555', ls=':', lw=1.5)
    axes[1].plot([peak], [epeak], 'o', color='#333333')
    axes[1].annotate(r'$x_{\rm max}/a\approx %.3f$' % peak, (peak, epeak), xytext=(1.4, 0.33), arrowprops={'arrowstyle': '->', 'color': '#444444'}, fontsize=11)
    axes[1].set(title='Electric field: odd and restoring for −Q', ylabel=r'$2\epsilon_0 E_x/\sigma$', xlabel=r'$x/a$', ylim=(-0.4, 0.4))
    axes[1].legend(loc='lower right', fontsize=9)
    for ax in axes:
        ax.axhline(0, color='#777777', lw=0.8)
        ax.axvline(0, color='#777777', lw=0.8)
        ax.grid(alpha=0.2)
        ax.set_xlim(-5, 5)
    fig.suptitle(r'Uniform charged annulus: $b=2a$, $\sigma>0$', fontsize=16)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
