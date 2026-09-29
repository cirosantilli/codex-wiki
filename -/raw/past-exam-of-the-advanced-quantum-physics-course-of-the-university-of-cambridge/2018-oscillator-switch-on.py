"""Original exponential-force excitation sketch; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

u = np.logspace(-2.5, 2.5, 700)
fig, ax = plt.subplots(figsize=(8, 4.8), layout='constrained')
ax.semilogx(u, u*u/(1+u*u), lw=2.4, label=r'Original basis: $p_1/\eta^2$ (weak force)')
ax.semilogx(u, 1/(1+u*u), lw=2.1, ls='--', label=r'Instantaneous basis: $\langle n\rangle/\eta^2$')
ax.axhline(1, lw=.8, ls=':', color='#64748b')
ax.axvline(1, lw=.8, ls=':', color='#64748b')
ax.plot([1], [.5], 'o', color='#334155', ms=5)
ax.set(xlim=(u[0], u[-1]), ylim=(-.025, 1.13), xlabel=r'Switching time $\omega_0\tau$', ylabel='Scaled excitation', title='Slow following of a displaced ground state')
ax.text(.009, .12, 'rapid switch', fontsize=10)
ax.text(30, .12, 'adiabatic', fontsize=10)
ax.legend(loc='upper center', fontsize=9)
ax.grid(alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
