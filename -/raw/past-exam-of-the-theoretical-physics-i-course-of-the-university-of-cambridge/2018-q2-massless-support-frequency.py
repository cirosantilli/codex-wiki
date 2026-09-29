"""Original massless-support oscillation curve; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    ratio = np.geomspace(0.03, 30, 601)
    frequency = ratio/np.sqrt(1+ratio**2)
    fig, ax = plt.subplots(figsize=(6.8, 4.1), layout='constrained')
    ax.semilogx(ratio, frequency, color='#174ea6', lw=2.5, label=r'$\omega/\omega_0=r/\sqrt{1+r^2}$')
    soft = np.geomspace(0.03, 0.8, 120)
    ax.semilogx(soft, soft, '--', color='#bb5566', lw=1.5, label=r'Soft-spring limit: $\omega\simeq\omega_1$')
    ax.axhline(1, color='#777777', ls=':', lw=1.1, label=r'Fixed-support limit: $\omega=\omega_0$')
    ax.annotate('Stiff spring', xy=(10, 10/np.sqrt(101)), xytext=(2.5, 0.70),
                arrowprops={'arrowstyle':'->', 'color':'#555555'}, fontsize=10)
    ax.set(xlim=(0.03, 30), ylim=(0, 1.1), xlabel=r'Stiffness scale $r=\omega_1/\omega_0$',
           ylabel=r'One finite frequency $\omega/\omega_0$', title='The support is massless: only one finite mode')
    ax.legend(loc='center left', frameon=False, fontsize=9)
    ax.grid(alpha=0.16)
    fig.savefig(Path.cwd() / '2018-q2-massless-support-frequency.png', dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
