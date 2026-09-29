"""Original, exactly specified lossless two-channel thickness toy model.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5; no SciPy.
Run from _media; writes the script basename with a .png extension to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


CENTRAL = '#1769aa'
DIFFRACTED = '#c26413'
HIGHLIGHT = '#7d3d8d'


def amplitudes(tau):
    """Incident-current normalized amplitudes at dimensionless thickness tau."""
    return np.cos(tau), 1j * np.sin(tau)


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    tau = np.linspace(0.0, np.pi, 901)
    a0, ag = amplitudes(tau)
    p0, pg = np.abs(a0)**2, np.abs(ag)**2
    assert np.allclose(p0 + pg, 1.0, rtol=0, atol=1e-14)
    chosen = np.array([np.pi / 4, 3 * np.pi / 4])
    xchosen, gchosen = amplitudes(chosen)
    assert np.allclose(np.abs(xchosen)**2, [0.5, 0.5])
    assert np.allclose(np.abs(gchosen)**2, [0.5, 0.5])

    fig, axes = plt.subplots(1, 2, figsize=(10, 5.1), dpi=120, facecolor='white',
                             gridspec_kw={'width_ratios': [1.2, 1]})
    ax = axes[0]
    ax.plot(tau, p0, color=CENTRAL, lw=2.4, label=r'$p_0=\cos^2\tau$ (central)')
    ax.plot(tau, pg, color=DIFFRACTED, lw=2.4, label=r'$p_g=\sin^2\tau$ (diffracted)')
    ax.plot(tau, p0 + pg, color='#66717c', lw=1.5, ls='--', label=r'$p_0+p_g=1$')
    for t in chosen:
        ax.axvline(t, color=HIGHLIGHT, lw=1, ls=':')
        ax.scatter([t], [0.5], color=HIGHLIGHT, s=45, zorder=5)
    ax.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi],
                  ['0', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$'])
    ax.set(xlim=(0, np.pi), ylim=(-0.025, 1.08),
           xlabel=r'Dimensionless thickness $\tau=\kappa t$',
           ylabel='Fraction of incident current', title='Different thicknesses, same fractions')
    ax.legend(loc='lower left', bbox_to_anchor=(0.01, 0.08), ncol=1,
               fontsize=9, frameon=True, framealpha=0.9, borderaxespad=0)
    ax.grid(alpha=0.2)

    ax = axes[1]
    circle = np.linspace(0, 2*np.pi, 501)
    ax.plot(np.cos(circle), np.sin(circle), color='#bcc3ca', ls='--')
    ax.plot(a0.real, (-1j * ag).real, color='#495765', lw=2)
    ax.axhline(0, color='#c6ccd2', lw=0.8)
    ax.axvline(0, color='#c6ccd2', lw=0.8)
    ax.scatter(xchosen, (-1j*gchosen).real, color=HIGHLIGHT, s=55, zorder=5)
    ax.annotate(r'$\tau=\pi/4$', (xchosen[0], (-1j*gchosen[0]).real),
                xytext=(0.08, 1.10), fontsize=11, color=HIGHLIGHT,
                arrowprops={'arrowstyle': '->', 'color': HIGHLIGHT})
    ax.annotate(r'$\tau=3\pi/4$', (xchosen[1], (-1j*gchosen[1]).real),
                xytext=(-1.2, 1.1), fontsize=11, color=HIGHLIGHT,
                arrowprops={'arrowstyle': '->', 'color': HIGHLIGHT})
    ax.text(0, -0.62, r'Both: $p_0=p_g=1/2$' + '\nDifferent amplitude signs',
            ha='center', va='center', fontsize=11, color=HIGHLIGHT)
    ax.set(xlim=(-1.3, 1.3), ylim=(-1.12, 1.32), aspect='equal',
           xlabel=r'$A_0=\cos\tau$', ylabel=r'$-iA_g=\sin\tau$',
           title='Different amplitude signs')
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    fig.suptitle('Exactly two channels, no absorption or detector loss', fontsize=16, y=0.98)
    fig.text(0.5, 0.025, 'Original analytical toy model • hypothetical parameters • no measured data',
             ha='center', fontsize=10, color='#586574')
    fig.subplots_adjust(top=0.82, bottom=0.19, left=0.065, right=0.98, wspace=0.32)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
