"""Physical equilibrium-connected extensional stress branches; Python 3.14, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False})
fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.4), constrained_layout=True, facecolor='white')
w = np.linspace(0, 2, 801)
for b, color in [(.1, '#1864ab'), (.5, '#d9480f')]:
    s1 = (2*w-1+np.sqrt((1-2*w)**2+8*b*w))/(2*b)
    # Rationalized physical transverse root avoids subtractive cancellation.
    s2 = -2*w/(1+w+np.sqrt((1+w)**2-4*b*w))
    axes[0].plot(w, s1, color=color, lw=2.2, label=f'b = {b}')
    axes[1].plot(w, s2, color=color, lw=2.2, label=f'b = {b}')
    axes[0].plot([.5], [1/np.sqrt(b)], 'o', color=color, ms=5)
wu = np.linspace(0, .49, 700)
axes[0].plot(wu, 2*wu/(1-2*wu), color='.2', ls='--', lw=1.6, label='b = 0 (physical branch)')
axes[1].plot(w, -w/(1+w), color='.2', ls='--', lw=1.6, label='b = 0')
for ax in axes:
    ax.axvline(.5, color='.6', ls=':', lw=1.2)
    ax.set_xlim(0, 2)
    ax.set_xlabel(r'$W=\lambda\gamma$')
    ax.grid(alpha=.18)
    ax.legend(frameon=False, fontsize=10, loc='upper left' if ax is axes[0] else 'lower left')
axes[0].set_ylim(0, 34)
axes[0].set_ylabel(r'$s_1=\sigma_{11}/(nk_BT)$')
axes[0].set_title('Longitudinal stress: finite-rate pole removed')
axes[0].text(.57, 30.5, r'$W=1/2$: $s_1=1/\sqrt{b}$', fontsize=11)
axes[1].set_ylim(-1.02, .04)
axes[1].set_ylabel(r'$s_2=\sigma_{22}/(nk_BT)$')
axes[1].set_title('Transverse stress: positive conformation')
axes[1].axhline(-1, color='.5', ls=':', lw=1)
axes[1].text(.67, -.97, r'$s_2\to-1$ as $W\to\infty$', fontsize=11)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=130, facecolor='white', transparent=False)
plt.close(fig)
