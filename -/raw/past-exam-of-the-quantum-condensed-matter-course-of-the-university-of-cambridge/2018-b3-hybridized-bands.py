"""Original two-band hybridization model; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    k = np.linspace(0, 1.85, 650)
    eps = k*k
    v = 0.12
    root = np.sqrt((eps-1)**2/4 + v*v)
    low = (eps+1)/2-root
    high = (eps+1)/2+root
    kf = 2**(1/3)
    ef = (kf*kf+1)/2-np.sqrt((kf*kf-1)**2/4+v*v)
    fig, (bare, mixed) = plt.subplots(1, 2, figsize=(9.5, 4.3), layout='constrained')
    for ax in [bare, mixed]:
        ax.set(xlim=(0, 1.85), ylim=(-0.13, 3.5), xlabel=r'Wavevector $k/k_0$', ylabel=r'Energy $E/E_d$')
        ax.axvline(1, color='#999999', lw=0.8, ls=':')
        ax.grid(alpha=0.14)
    bare.plot(k, eps, color='#174ea6', lw=2.2, label='Broad orbital band')
    bare.axhline(1, color='#bb5566', lw=2.2, label='Flat orbital band')
    bare.scatter([1], [1], color='#111111', s=25, zorder=4)
    bare.annotate(r'Bare crossing; $\mu_0=E_d$', xy=(1, 1), xytext=(0.15, 1.9),
                  arrowprops={'arrowstyle':'->', 'color':'#444444'}, fontsize=9)
    bare.set_title('No mixing')
    bare.legend(loc='upper left', fontsize=9, frameon=False)
    mixed.plot(k, eps, color='#bbbbbb', lw=1, ls=':')
    mixed.axhline(1, color='#bbbbbb', lw=1, ls=':')
    mixed.plot(k, low, color='#174ea6', lw=2.2, label=r'Lower branch $E_-$')
    mixed.plot(k, high, color='#bb5566', lw=2.2, label=r'Upper branch $E_+$')
    mixed.axhline(ef, color='#777777', lw=1, ls='--')
    mixed.axvline(kf, color='#8844aa', lw=1.4, ls='--')
    mixed.scatter([kf], [ef], color='#8844aa', s=30, zorder=5)
    mixed.annotate(r'$k_F=2^{1/3}k_0$', xy=(kf, ef), xytext=(0.23, 0.28),
                   arrowprops={'arrowstyle':'->', 'color':'#8844aa'}, color='#663388', fontsize=10)
    mixed.annotate('', xy=(1, 1-v), xytext=(1, 1+v), arrowprops={'arrowstyle':'<->', 'color':'#333333'})
    mixed.text(0.78, 1.28, r'$2|V|$', fontsize=10)
    mixed.text(1.72, ef-0.18, r'$\mu$', fontsize=11)
    mixed.set_title(r'Mixing $|V|/E_d=0.12$')
    mixed.legend(loc='upper left', fontsize=9, frameon=False)
    fig.savefig(Path.cwd() / '2018-b3-hybridized-bands.png', dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
