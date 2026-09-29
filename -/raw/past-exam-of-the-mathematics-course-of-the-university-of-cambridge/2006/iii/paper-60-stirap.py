"""Original STIRAP sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes paper-60-stirap.png to the caller's CWD. Honors MPLCONFIGDIR.
The population panel shows the instantaneous ideal dark state, not a simulation.
"""
import os
import tempfile
from pathlib import Path

if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp(prefix='paper-60-stirap-mpl-')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(-0.3, 8.3, 1601)
    omega12 = np.where((t > 0) & (t < 6), np.sin(np.pi * t / 6) ** 2, 0.0)
    omega23 = np.where((t > 2) & (t < 8), np.sin(np.pi * (t - 2) / 6) ** 2, 0.0)
    theta = np.arctan2(omega23, omega12)
    theta[t >= 6] = np.pi / 2
    fig, axes = plt.subplots(2, 1, figsize=(9, 6), dpi=140, sharex=True, facecolor='white')
    axes[0].plot(t, omega12, color='#1765ad', lw=2.8, label=r'$\Omega_{12}$: target-side coupling first')
    axes[0].plot(t, omega23, color='#db6815', lw=2.8, label=r'$\Omega_{23}$: initial-side coupling second')
    axes[0].set_ylabel(r'coupling / $\Omega_0$')
    axes[0].set_title('Counter-intuitive STIRAP: level 3 to level 1')
    axes[0].legend(loc='upper right', fontsize=9)
    axes[1].plot(t, np.cos(theta) ** 2, color='#1765ad', lw=2.8, label=r'$P_3=\cos^2\theta$')
    axes[1].plot(t, np.sin(theta) ** 2, color='#db6815', lw=2.8, label=r'$P_1=\sin^2\theta$')
    axes[1].plot(t, np.zeros_like(t), color='#333333', ls='--', lw=1.6, label=r'$P_2=0$ (ideal dark state)')
    axes[1].set_ylabel('ideal dark-state population')
    axes[1].set_xlabel(r'time / $T$')
    axes[1].legend(loc='center right', fontsize=9)
    for ax in axes:
        ax.set_facecolor('white')
        ax.set_ylim(-0.06, 1.13)
        ax.set_xlim(-0.3, 8.3)
        ax.grid(alpha=0.2)
        ax.axvline(4, color='#777777', lw=1, ls=':')
    axes[1].annotate(r'equal couplings: $(|3\rangle-|1\rangle)/\sqrt{2}$', xy=(4, 0.5), xytext=(0.35, 0.67), fontsize=10, arrowprops={'arrowstyle': '->', 'color': '#555555'})
    fig.tight_layout()
    fig.savefig(Path.cwd() / 'paper-60-stirap.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
