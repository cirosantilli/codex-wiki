"""Plot viscous swing amplification and ideal Keplerian MRI growth.
Writes the PNG basename to caller CWD. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def early_minimum(re):
    lo, hi = 1.0, 3 * re**(1 / 3)
    for _ in range(70):
        mid = (lo + hi) / 2
        if (1 + mid * mid)**2 - 2 * re * mid < 0:
            lo = mid
        else:
            hi = mid
    return -(lo + hi) / 2


fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.8), facecolor='white')
for re, color in [(100, '#555555'), (1000, '#1767a6'), (10000, '#993c83')]:
    t0 = early_minimum(re)
    t = np.linspace(t0, 15, 2500)
    g = lambda x: x + x**3 / 3
    gain = (1 + t0*t0) / (1 + t*t) * np.exp(-(g(t) - g(t0)) / re)
    axes[0].plot(t, gain, color=color, lw=1.8, label=f'Re = {re:,}')
axes[0].axvline(0, ls=':', color='#888888', lw=1)
axes[0].set_yscale('log')
axes[0].set_xlim(-30, 15)
axes[0].set_ylim(0.05, 600)
axes[0].set_xlabel(r'Shearing-wave tilt $T=k_x/k_y$')
axes[0].set_ylabel(r'Energy gain $E(T)/E(T_-)$')
axes[0].set_title('Hydrodynamic growth is transient', fontsize=11)
axes[0].legend(frameon=False, fontsize=9, loc='upper left')

x = np.linspace(0, 2, 1600)
a = x*x
s2 = (np.sqrt(1 + 16*a) - 1 - 2*a) / 2
growth = np.sqrt(np.maximum(s2, 0))
axes[1].plot(x, growth, color='#1767a6', lw=2)
axes[1].axvspan(np.sqrt(3), 2, color='#eeeeee')
axes[1].axvline(np.sqrt(3), color='#777777', ls=':', lw=1)
axes[1].plot(np.sqrt(15)/4, 0.75, 'o', color='#993c83', ms=6)
axes[1].annotate(r'$\gamma_{\max}=3\Omega/4$', xy=(np.sqrt(15)/4, 0.75),
                 xytext=(1.10, 0.88), fontsize=10,
                 arrowprops={'arrowstyle':'-', 'color':'#993c83'})
axes[1].text(0.3, 0.19, 'Unstable', fontsize=10)
axes[1].text(1.87, 0.17, 'Stable', fontsize=9, ha='center')
axes[1].set_xlim(0, 2)
axes[1].set_ylim(0, 1)
axes[1].set_xlabel(r'Magnetic frequency $\omega_A/\Omega$')
axes[1].set_ylabel(r'Exponential MRI growth rate $\gamma/\Omega$')
axes[1].set_title('MRI has a growing normal mode', fontsize=11)
for ax in axes:
    ax.set_facecolor('white')
    ax.grid(True, color='#dddddd', lw=0.6)
fig.tight_layout()
fig.savefig(Path.cwd() / 'paper-73-shear-instabilities.png', dpi=130,
            facecolor='white', transparent=False)
plt.close(fig)
