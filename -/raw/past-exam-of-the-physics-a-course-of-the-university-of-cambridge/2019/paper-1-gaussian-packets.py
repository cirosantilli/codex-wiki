"""Original free-packet and harmonic-width comparison; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 4.4), layout='constrained')
x = np.linspace(-6, 12, 1200)
for t, color in [(0, '#2563eb'), (1, '#d97706'), (2, '#059669')]:
    width = np.sqrt(1+t*t)
    center = 2*t
    rho = np.exp(-(x-center)**2/(2*width**2))/(np.sqrt(2*np.pi)*width)
    axes[0].plot(x, rho, color=color, lw=2, label=rf'$t/\tau={t}$')
    axes[0].axvline(center, color=color, lw=.8, ls=':')
axes[0].set(xlabel=r'$x/\sigma_0$', ylabel=r'$\sigma_0|\psi|^2$', title=r'Free packet: $p_0\tau/(m\sigma_0)=2$', ylim=(0, .43))
axes[0].legend()
t = np.linspace(0, 2*np.pi, 600)
axes[1].plot(t, np.sqrt(1+t*t), lw=2, label='Free, τ = 1/ω')
axes[1].plot(t, np.ones_like(t), lw=2, label='Harmonic coherent state')
r = .6
axes[1].plot(t, np.sqrt(np.exp(-2*r)*np.cos(t)**2 + np.exp(2*r)*np.sin(t)**2), lw=2, label='Harmonic squeezed state')
axes[1].set(xlabel=r'Time $\omega t$', ylabel=r'Width $\sigma_x/\sqrt{\hbar/(2m\omega)}$', title='Hamiltonian and initial state set the width', xlim=(0, 2*np.pi))
axes[1].legend(loc='upper left', fontsize=8.5)
for ax in axes: ax.grid(alpha=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
