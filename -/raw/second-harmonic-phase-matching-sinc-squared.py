"""Original undepleted plane-wave SHG curves; numpy.sinc(u)=sin(pi*u)/(pi*u)."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def relative_intensity(q, length_ratio):
    """q=Delta k L0/(2 pi); result normalized by C I_pump^2 L0^2."""
    return length_ratio**2 * np.sinc(length_ratio*np.asarray(q))**2


def main():
    plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(9, 5.8), dpi=100, facecolor='white')
    fig.subplots_adjust(left=.105, right=.97, bottom=.23, top=.82)
    q = np.linspace(-2.15, 2.15, 2201)
    for r, color, style in [(1, '#236a9f', '-'), (2, '#c25b20', '--')]:
        ax.plot(q, relative_intensity(q, r), style, color=color, lw=2.2,
                label=rf'$L={r}L_0$' + (' = 1 mm' if r == 1 else ' = 2 mm'))
    ax.set(xlim=(-2.15, 2.15), ylim=(-.08, 4.4),
           xlabel=r'Phase mismatch $q=\Delta k L_0/(2\pi)$',
           ylabel=r'Harmonic intensity $I_{2\omega}/(C I_\omega^2 L_0^2)$')
    ax.set_xticks(np.arange(-2, 2.01, .5))
    ax.set_yticks(np.arange(5))
    ax.grid(alpha=.2)
    ax.legend(loc='upper left', framealpha=1, edgecolor='#dddddd')
    ax.scatter([.5, 1], [0, 0], c=['#c25b20', '#236a9f'], s=45, zorder=5)
    ax.annotate('First zero, 2 mm', xy=(.5, 0), xytext=(.7, 1.5), color='#a84c19',
                arrowprops={'arrowstyle': '->', 'color': '#a84c19'})
    ax.annotate('First zero, 1 mm', xy=(1, 0), xytext=(1.12, .75), color='#236a9f',
                arrowprops={'arrowstyle': '->', 'color': '#236a9f'})
    fig.suptitle('Longer interaction: taller matched peak, narrower acceptance', fontsize=15, y=.96, weight='bold')
    fig.text(.5, .867, r'$I_{2\omega}=C I_\omega^2 L^2\,\mathrm{sinc}^2(\Delta k L/2)$', ha='center', fontsize=14)
    fig.text(.5, .115, r'$\mathrm{sinc}(x)=\sin(x)/x$, with $\mathrm{sinc}(0)=1$; chosen $L_0=1\,\mathrm{mm}$.', ha='center')
    fig.text(.5, .065, 'Same pump and prefactor for both curves. Uniform lossless medium; pump depletion neglected.', ha='center', fontsize=9)
    fig.text(.5, .025, 'Calculated model curves, not measurements.', ha='center', fontsize=10, color='#52616b')
    fig.savefig(Path(__file__).stem+'.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
