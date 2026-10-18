"""Original entropy and counting plots; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False})
fig, (entropy, counting) = plt.subplots(1, 2, figsize=(10, 4.5), layout='constrained', facecolor='white')
t = np.linspace(0.006, 6, 1200)
k = 1/t
q = np.exp(-2*k)
g = 3 + 3*q + q*q + q**3
gprime = -6*q - 4*q*q - 6*q**3
s = (np.log(g) - k*gprime/g)/3
entropy.plot(np.r_[0,t], np.r_[np.log(3)/3,s], color='#225d91', lw=2)
entropy.axhline(np.log(3)/3, color='#9c4937', ls='--', label=r'Residual: $\ln 3/3$')
entropy.axhline(np.log(2), color='#666666', ls=':', label=r'Independent spins: $\ln 2$')
entropy.set(xlabel=r'Temperature $k_B T/J$', ylabel=r'Entropy per site $s/k_B$', xlim=(0,6), ylim=(0,0.76), title='Thermodynamic-limit entropy')
entropy.legend(loc='lower right', fontsize=10)
entropy.grid(alpha=0.2)
m = np.arange(1,19)
counts = 3.**m+1
counting.semilogy(m, counts, 'o-', color='#377b46', lw=1.5, markersize=4, label=r'$g_M=3^M+1$')
counting.semilogy(m, 3.**m, '--', color='#8b6a30', label=r'$3^M$')
counting.set(xlabel=r'Number of triangle cells $M$', ylabel='Number of ground states', title=r'Exponential degeneracy on $3M$ sites', xticks=[1,4,7,10,13,16,18])
counting.legend(fontsize=10)
counting.grid(alpha=0.2)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', transparent=False)
