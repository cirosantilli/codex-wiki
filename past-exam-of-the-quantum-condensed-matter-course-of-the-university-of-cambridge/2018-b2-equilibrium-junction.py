"""Original equilibrium junction and carrier profiles; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-3.2, 3.2, 601)
    shift = np.log(1e5)*np.tanh(1.3*x)
    ec = 15-shift
    n = np.exp(shift)
    p = np.exp(-shift)
    fig, (band, carriers) = plt.subplots(1, 2, figsize=(9.8, 4.2), layout='constrained')
    for ax in [band, carriers]:
        ax.axvspan(-1.2, 1.2, color='#fff1d4', zorder=0)
        ax.axvline(0, lw=0.8, color='#888888')
        ax.set(xlim=(-3.2, 3.2), xlabel='Position: p side to n side')
        ax.set_xticks([-2.5, 0, 2.5], ['p bulk', 'junction', 'n bulk'])
    band.plot(x, ec, color='#174ea6', lw=2.2, label=r'$E_C$')
    band.plot(x, ec-30, color='#bb5566', lw=2.2, label=r'$E_V$')
    band.axhline(0, color='#111111', ls='--', lw=1.2, label=r'$E_F$')
    band.set(ylabel=r'Energy relative to $E_F$ ($k_BT$ units)', ylim=(-30, 30),
             title='Band edges fall from p to n')
    band.text(-0.65, -23, '−', fontsize=22, ha='center', color='#995522')
    band.text(0.65, -23, '+', fontsize=22, ha='center', color='#995522')
    band.text(0, -28, 'Fixed acceptor / donor charge', ha='center', fontsize=8)
    band.legend(loc='upper right', frameon=False, fontsize=10)
    carriers.semilogy(x, n, color='#174ea6', lw=2.2, label=r'Electrons $n/n_i$')
    carriers.semilogy(x, p, color='#bb5566', lw=2.2, label=r'Holes $p/n_i$')
    carriers.axhline(1, color='#888888', ls=':', lw=1)
    carriers.set(ylim=(1e-6, 1e6), ylabel=r'Concentration relative to $n_i$',
                 title='Majority and minority populations exchange')
    carriers.text(-2.75, 2e4, 'holes: majority', color='#bb5566', fontsize=9)
    carriers.text(1.3, 1e4, 'electrons:\nmajority', color='#174ea6', va='top', fontsize=9)
    carriers.text(-2.75, 1e-4, 'electrons:\nminority', color='#174ea6', fontsize=9)
    carriers.text(1.3, 1e-4, 'holes: minority', color='#bb5566', fontsize=9)
    carriers.legend(loc='center left', frameon=True, facecolor='white', fontsize=9)
    fig.savefig(Path.cwd() / '2018-b2-equilibrium-junction.png', dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
