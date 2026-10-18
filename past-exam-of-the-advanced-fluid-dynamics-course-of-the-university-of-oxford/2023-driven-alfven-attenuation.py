"""Original first-order driven-Alfven-wave model; write PNG only in cwd.

Tested with Python3.14, NumPy2.3.5, Matplotlib3.10.7; root pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
eps = .05
x = np.linspace(0, 15, 1801)
amp = np.exp(-np.pi*eps*x)
energy = amp*amp
la, le = 1/(np.pi*eps), 1/(2*np.pi*eps)
fig, axes = plt.subplots(1, 2, figsize=(10.6, 4), dpi=130, facecolor='white')
ax = axes[0]
ax.plot(x, amp*np.cos(2*np.pi*x), color='#196c9b', lw=1.1, label='Wave amplitude')
ax.plot(x, amp, color='#5c3d1a', ls='--', lw=1.4, label='Amplitude envelope')
ax.plot(x, -amp, color='#5c3d1a', ls='--', lw=1.4)
ax.axvline(la, color='#555555', ls=':', lw=1)
ax.text(la+.2, 1.02, r'$L_A/\lambda$', fontsize=11)
ax.set(xlabel=r'Distance $z/\lambda$', ylabel='Normalized real wave', ylim=(-1.15, 1.18), title='First-order spatially damped wave')
ax.legend(loc='lower right', fontsize=9, frameon=False)
ax = axes[1]
ax.semilogy(x, amp, color='#5c3d1a', lw=2, label='Amplitude envelope')
ax.semilogy(x, energy, color='#a63637', lw=2, label='Mean energy')
ax.axhline(np.exp(-1), color='#888888', ls=':', lw=1)
ax.plot([la, le], [np.exp(-1)]*2, 'o', color='#333333', ms=4)
ax.annotate(r'$L_A=2L_E$', xy=(la, np.exp(-1)), xytext=(7.9, .62),
            arrowprops={'arrowstyle': '->', 'color': '#333333'})
ax.text(le-.2, .26, r'$L_E$', ha='right')
ax.set(xlabel=r'Distance $z/\lambda$', ylabel='Normalized envelope or energy', ylim=(.007, 1.25), title='Energy attenuates twice as rapidly')
ax.legend(loc='lower left', fontsize=9, frameon=False)
for ax in axes:
    ax.set_xlim(0, 15)
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(alpha=.18)
fig.suptitle(r'Weak magnetic diffusion: $\epsilon=\eta_m\omega/v_A^2=0.05$', fontsize=13)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
