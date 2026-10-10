"""Original dimensionless neutral-kaon illustration, not a historical fit.

Python 3.14 / matplotlib 3.10 / NumPy 2.3. Run from _media.
Intensities omit a common production and decay-amplitude scale; they are
not a complete normalized decay-channel probability model.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

TAU_S, TAU_L = 1.0, 8.0
RHO, ETA, DELTA_M = .35, .06*np.exp(.8j), 1.6

def components(t):
    short = RHO*np.exp(-t/(2*TAU_S))
    long = ETA*np.exp(-t/(2*TAU_L)-1j*DELTA_M*t)
    return short, long

def intensity(t):
    short, long = components(t)
    return np.abs(short+long)**2

if __name__ == '__main__':
    plt.rcParams.update({'font.size':11, 'font.family':'DejaVu Sans'})
    fig, (top, bot) = plt.subplots(2, 1, figsize=(10, 7), dpi=100, sharex=True, facecolor='white')
    t = np.linspace(0, 24, 2001)
    top.semilogy(t, np.exp(-t/TAU_S), color='#b84433', lw=2.4, label=r'$K_S$: $e^{-t/\tau_S}$')
    top.semilogy(t, np.exp(-t/TAU_L), color='#2268a1', lw=2.4, label=r'$K_L$: $e^{-t/\tau_L}$')
    top.set(ylim=(1e-5, 1.2), ylabel='Single-state survival factor')
    top.legend(loc='upper right'); top.grid(alpha=.2)
    top.set_title('Waiting suppresses the short-lived component', loc='left', fontsize=12)
    short, long = components(t)
    incoherent = abs(short)**2+abs(long)**2
    bot.semilogy(t, intensity(t), color='#493884', lw=2.5, label='Coherent two-pion intensity')
    bot.semilogy(t, incoherent, '--', color='#d18322', lw=1.8, label='Sum with interference omitted')
    bot.semilogy(t, abs(long)**2, ':', color='#2268a1', lw=1.8, label='Long-lived contribution alone')
    bot.set(xlim=(0, 24), ylim=(1e-4, .3), ylabel='Two-pion intensity (arbitrary scale)', xlabel=r'Dimensionless proper time $t$')
    bot.set_title('Shared final state: add amplitudes before squaring', loc='left', fontsize=12)
    bot.legend(loc='upper right', fontsize=10); bot.grid(alpha=.2)
    fig.suptitle('Chosen kaon mixture and two-pion interference', fontsize=17, y=.975)
    fig.text(.5, .917, r'$\tau_S=1,\quad\tau_L=8,\quad\rho=0.35,\quad\eta_{\pi\pi}=0.06e^{0.8i},\quad\Delta m=1.6$', ha='center', fontsize=12)
    fig.text(.5, .015, 'Illustration only: no historical fit; intensities are not normalized channel probabilities.', ha='center', color='#555555', fontsize=10)
    fig.subplots_adjust(left=.12, right=.97, bottom=.11, top=.85, hspace=.28)
    fig.savefig(Path(__file__).stem+'.png', facecolor='white', dpi=100)
    plt.close(fig)
