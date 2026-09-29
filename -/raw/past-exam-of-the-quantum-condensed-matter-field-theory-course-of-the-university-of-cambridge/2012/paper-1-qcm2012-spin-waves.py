"""Original harmonic Heisenberg spectra; Python 3.14, NumPy, Matplotlib.
These are one-dimensional harmonic reference spectra, not an ordered AF ground state.
Writes the basename PNG to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
k = np.linspace(0, np.pi, 1001)
fig, ax = plt.subplots(figsize=(7.8, 4.8), layout='constrained')
ax.plot(k/np.pi, 2*(1-np.cos(k)), label='Ferromagnet: quadratic near 0', color='#2763a1')
ax.plot(k/np.pi, 2*np.abs(np.sin(k)), label='Antiferromagnet: linear near 0', color='#b45c22')
ax.set(xlabel=r'$k/\pi$ (unit lattice spacing)', ylabel=r'Energy / $J_H S$', xlim=(0, 1), ylim=(0, 4.4))
ax.set_title('One-dimensional harmonic spectra')
ax.text(.5, .97, 'AF ordered reference fails in 1D: divergent vacuum depletion', transform=ax.transAxes, ha='center', va='top', fontsize=10)
ax.legend(loc='center left', fontsize=10)
ax.grid(alpha=.2)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=145, facecolor='white')
