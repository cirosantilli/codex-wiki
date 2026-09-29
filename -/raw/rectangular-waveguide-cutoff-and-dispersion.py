"""Original TE10 dispersion and evanescence; Python 3.14 / matplotlib 3.10.7.

Uses only numpy 2.3.5 and matplotlib. Run from _media to emit this basename.png.
All values follow a stipulated a=30 mm, b=12 mm vacuum guide with ideal walls.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig, (ax, decay) = plt.subplots(1, 2, figsize=(10.8, 4.9))
    fig.subplots_adjust(left=0.085, right=0.97, bottom=0.20, top=0.78, wspace=0.35)
    fig.suptitle(r'$\mathrm{TE}_{10}$ cutoff: propagating phase versus spatial decay', fontsize=15, y=0.97)
    fig.text(0.5, 0.87, r'Chosen vacuum guide: $a=30$ mm, $b=12$ mm; '
             r'$f_c=c/(2a)\approx4.997$ GHz; ideal conducting walls', ha='center')
    q = np.linspace(0, 1.9, 601)
    ax.plot(q, np.sqrt(1 + q*q), color='#1670b6', linewidth=2.7,
            label=r'$\omega/\omega_c=\sqrt{1+q^2}$')
    ax.plot(q, q, color='#a7adb3', linestyle=':', label=r'$\omega=c\beta$ reference')
    ax.plot([0, .75], [0, 1.25], color='#ba5b26', linewidth=1.8)
    tang_q = np.array([0, 1.8])
    ax.plot(tang_q, 1.25 + 0.6 * (tang_q - .75), color='#308459', linestyle='--', linewidth=1.8)
    ax.plot(.75, 1.25, 'o', color='#1670b6', zorder=4)
    ax.annotate(r'$f=1.25f_c$' + '\n' + r'$q=3/4$', (.75, 1.25), (.90, 2.05),
                arrowprops={'arrowstyle': '->', 'color': '#505963'}, fontsize=10)
    ax.text(1.08, .45, r'Secant: $v_{\rm ph}/c=5/3$', color='#a34b1b', fontsize=10)
    ax.text(.83, .97, r'Tangent: $v_g/c=3/5$', color='#236841', fontsize=10)
    ax.plot(0, 1, 'o', color='#c45131', clip_on=False)
    ax.text(.04, 1.10, 'cutoff', color='#b4472c', fontsize=10)
    ax.set(xlim=(0, 1.9), ylim=(0, 2.35), xlabel=r'Axial wavenumber $q=\beta a/\pi$',
           ylabel=r'Frequency $\omega/\omega_c=f/f_c$')
    ax.set_title('Above cutoff: real positive axial wavenumber', fontsize=11, pad=10)
    ax.legend(loc='upper left', fontsize=8, frameon=False)
    ax.grid(alpha=.18)
    z = np.linspace(0, 60, 601)
    alpha_per_mm = np.pi / 50
    envelope = np.exp(-alpha_per_mm * z)
    decay.plot(z, envelope, color='#7f4ba0', linewidth=2.7)
    decay.axhline(1 / np.e, color='#b4bcc4', linestyle=':', linewidth=1)
    decay.axvline(50 / np.pi, color='#b4bcc4', linestyle=':', linewidth=1)
    decay.plot([50 / np.pi, 50], [1 / np.e, np.exp(-np.pi)], 'o', color='#7f4ba0')
    decay.annotate(r'$1/\alpha=15.92$ mm', (50 / np.pi, 1 / np.e), (24, .57),
                   arrowprops={'arrowstyle': '->', 'color': '#505963'}, fontsize=10)
    decay.annotate(r'$e^{-\pi}\approx0.0432$', (50, np.exp(-np.pi)), (34, .23),
                   arrowprops={'arrowstyle': '->', 'color': '#505963'}, fontsize=10)
    decay.text(22, .87, r'$f=0.8f_c\approx3.997$ GHz' + '\n' + r'$\beta=i\alpha,\quad\alpha=20\pi\ {\rm m}^{-1}$',
               fontsize=10, color='#693d87')
    decay.set(xlim=(0, 60), ylim=(0, 1.07), xlabel='Distance into guide (mm)',
              ylabel=r'Normalized amplitude $e^{-\alpha z}$')
    decay.set_title('Below cutoff: a single decaying branch', fontsize=11, pad=10)
    decay.grid(alpha=.18)
    fig.text(.5, .065, 'Calculated fields, not measured data. Below-cutoff decay persists even with perfectly conducting walls.',
             ha='center', fontsize=10, color='#3e4952')
    fig.savefig(Path(__file__).stem + '.png', dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
