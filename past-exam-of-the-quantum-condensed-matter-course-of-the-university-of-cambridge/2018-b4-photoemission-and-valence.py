"""Original photoemission energies and illustrative pi bands; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, (energy, band) = plt.subplots(1, 2, figsize=(10.2, 4.7), layout='constrained')
    ei, ef, vacuum = -3, 16.5, 3.8
    for y, label, color in [(ei, r'$E_i$', '#174ea6'), (0, r'$E_F$', '#333333'),
                             (vacuum, r'$E_{\rm vac}$', '#777777'), (ef, r'$E_f$', '#bb5566')]:
        energy.hlines(y, 0.35, 2.7, color=color, lw=1.5)
        energy.text(0.29, y, label, ha='right', va='center', fontsize=11, color=color)
    energy.annotate('', xy=(1.0, ef), xytext=(1.0, ei),
                    arrowprops={'arrowstyle':'->', 'lw':2, 'color':'#aa7722'})
    energy.text(1.1, 8, r'$\hbar\omega=E_f-E_i$', fontsize=11, color='#885511')
    for x, y0, y1, text in [(2.2, ei, 0, r'$E_B$'), (2.2, 0, vacuum, r'$\phi$'),
                              (2.4, vacuum, ef, r'$E_{\rm kin}$')]:
        energy.annotate('', xy=(x, y1), xytext=(x, y0),
                        arrowprops={'arrowstyle':'<->', 'color':'#333333'})
        energy.text(x+0.12, (y0+y1)/2, text, va='center', fontsize=11)
    energy.set(xlim=(-0.1, 3.0), ylim=(-4.8, 19), title='Photoemission energy balance',
               ylabel=r'Energy (example scale, $E_F=0$)')
    energy.set_xticks([])
    energy.set_yticks([])
    energy.spines[['top', 'right', 'bottom']].set_visible(False)
    energy.annotate('', xy=(-0.05, 18.4), xytext=(-0.05, -4.5), arrowprops={'arrowstyle':'->'})

    q = np.linspace(0, 1.18, 600)
    hopping = 2.8
    gamma_k = -hopping*np.abs(1+2*np.cos(2*np.pi*q/3))
    gamma_m = -hopping*np.sqrt(1+8*np.cos(np.pi*q/2)**2)
    band.plot(q, gamma_k, color='#174ea6', lw=2.4, label=r'$\Gamma K$: reaches $E_F$')
    band.plot(q, gamma_m, color='#bb5566', lw=2.4, label=r'$\Gamma M$: finite binding at edge')
    band.axhline(0, color='#777777', lw=0.9, ls='--')
    band.axvline(1, color='#888888', lw=0.9, ls=':')
    band.scatter([1, 1], [0, -hopping], color=['#174ea6', '#bb5566'], s=28, zorder=4)
    band.text(1.03, 0.12, r'$K$', color='#174ea6', fontsize=11)
    band.text(1.03, -hopping-0.45, r'$M$', color='#bb5566', fontsize=11)
    band.set(xlim=(0, 1.18), ylim=(-9, 1.0), xlabel=r'$k_\parallel/k_{\rm edge}$ (each direction)',
             ylabel=r'Pi-band energy relative to $E_F$ (eV)', title='Qualitative 2D pi-band model')
    band.set_xticks([0, 0.5, 1], [r'$\Gamma$', '0.5', 'edge'])
    band.legend(loc='lower right', fontsize=9, frameon=False)
    band.grid(alpha=0.15)
    fig.savefig(Path.cwd() / '2018-b4-photoemission-and-valence.png', dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
