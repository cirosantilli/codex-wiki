"""Original Ising-chain dispersion curves; Python 3.14, NumPy, Matplotlib.
Writes the basename PNG to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
k = np.linspace(-np.pi, np.pi, 1001)
fig, axs = plt.subplots(1, 2, figsize=(10, 4.2), layout='constrained')
for g, color in [(0, '#696969'), (.5, '#289475'), (1, '#286aaf')]:
    axs[0].plot(k / np.pi, 2 * np.sqrt(1 + g*g - 2*g*np.cos(k)), label=f'g = {g:g}', color=color)
g = 5
axs[1].plot(k / np.pi, 2*np.sqrt(1 + g*g - 2*g*np.cos(k)), color='#a24c22', label='Exact, g = 5')
axs[1].plot(k / np.pi, 2*g - 2*np.cos(k), '--', color='#424242', label='Leading large-g form')
axs[0].set_title('Flat band and critical gap closing')
axs[1].set_title('Strong-field band')
for ax in axs:
    ax.set(xlabel=r'$k/\pi$', ylabel=r'Energy $\epsilon_k/J$', xlim=(-1, 1))
    ax.grid(alpha=.2)
    ax.legend(fontsize=10)
axs[0].set_ylim(0, 4.4)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=145, facecolor='white')
