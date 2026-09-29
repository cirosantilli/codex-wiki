"""Original alternating-spring phonon curves; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-1, 1, 601)
    ratio = 0.2
    root = np.sqrt(1 + ratio**2 + 2*ratio*np.cos(np.pi*x))
    acoustic = np.sqrt(np.maximum(0, 1 + ratio - root))
    optical = np.sqrt(1 + ratio + root)
    fig, ax = plt.subplots(figsize=(6.4, 3.8), layout='constrained')
    ax.plot(x, acoustic, color='#174ea6', lw=2.4, label='Acoustic: in-phase at origin')
    ax.plot(x, optical, color='#bb5566', lw=2.4, label='Optical: out-of-phase at origin')
    ax.axhline(np.sqrt(2), color='#888888', ls=':', lw=1.1,
               label=r'Strong-bond scale $\sqrt{2K/m}$')
    ax.set(xlim=(-1, 1), ylim=(0, 1.85), xlabel=r'Wavevector $q\ell/\pi$',
           ylabel=r'Frequency $\omega/\sqrt{K/m}$', title=r'Two branches, one primitive cell ($K^\prime/K=0.2$)')
    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax.legend(loc='center', fontsize=9, frameon=False)
    ax.grid(alpha=0.18)
    fig.savefig(Path.cwd() / '2018-q1a-alternating-springs.png', dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
