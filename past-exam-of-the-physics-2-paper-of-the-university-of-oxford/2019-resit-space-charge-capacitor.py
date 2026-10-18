"""Illustrate the analytic space-charge solution. Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12, 'axes.titlesize': 13, 'figure.facecolor': 'white'})
u = np.linspace(0, 1, 801)
fig, axes = plt.subplots(2, 2, figsize=(10, 6.4), layout='constrained')
for col, delta in enumerate((0.15, 0.8)):
    potential = delta * (1-u) + u*(1-u)/2
    field = delta + u - 0.5
    axes[0, col].plot(u, potential, color='#1f5f99', linewidth=2.5)
    axes[1, col].plot(u, np.abs(field), color='#b24a22', linewidth=2.5)
    axes[0, col].set_title(rf'$\delta={delta:g}$: ' + ('field reverses' if col == 0 else 'field retains its sign'))
    for row in range(2):
        ax = axes[row, col]
        ax.set_xlim(0, 1)
        ax.set_xlabel(r'$u=x/d$')
        ax.grid(alpha=0.22)
        ax.axhline(0, color='black', linewidth=0.7)
    if col == 0:
        for row in range(2):
            axes[row, col].axvline(0.5-delta, color='#777777', linestyle=':', linewidth=1.4)
axes[0, 0].set_ylabel(r'$\epsilon_0(V-V_2)/(\rho d^2)$')
axes[1, 0].set_ylabel(r'$\epsilon_0|E_x|/(\rho d)$')
fig.suptitle('Fixed positive space charge between prescribed-potential plates', fontsize=15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
