"""Original ideal band-pass responses. Python 3.14, numpy, matplotlib; PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt

u = np.geomspace(1e-4, 1e4, 2000)
fig, axes = plt.subplots(1, 2, figsize=(8.7, 3.6), layout='constrained')
for ratio, color in [(100, '#245c94'), (1, '#a23d25'), (0.01, '#568544')]:
    t1, t2 = np.sqrt(ratio), 1 / np.sqrt(ratio)
    power = (u * t1) ** 2 / ((1 + (u * t1) ** 2) * (1 + (u * t2) ** 2))
    peak = (t1 / (t1 + t2)) ** 2
    axes[0].loglog(u, power, color=color, label=fr'$\tau_1/\tau_2={ratio:g}$')
    if ratio != 0.01:
        label = 'Matched times: Q = 0.5' if ratio == 1 else '100:1 or 1:100 times: Q = 0.099'
        axes[1].semilogx(u, power / peak, color=color, label=label)
axes[0].set(xlabel=r'$\omega/\omega_0$', ylabel=r'$|H|^2/K^2$', ylim=(1e-9, 2), title='Absolute power gain relative to K²')
axes[0].legend(fontsize=8)
axes[1].axhline(0.5, color='0.5', linestyle=':', label='Half-power level')
axes[1].scatter([np.sqrt(2) - 1, np.sqrt(2) + 1], [0.5, 0.5], color='#a23d25', s=18, zorder=4)
axes[1].set(xlabel=r'$\omega/\omega_0$', ylabel='Power / peak power', ylim=(0, 1.08), title='Matched times give the narrowest band')
axes[1].legend(fontsize=7, loc='upper right')
for ax in axes:
    ax.set_xlim(1e-4, 1e4)
    ax.grid(which='both', alpha=0.18)
    ax.axvline(1, color='0.5', linestyle=':', linewidth=0.8)
fig.savefig('paper-1-band-pass.png', dpi=150, facecolor='white')
plt.close(fig)
