"""Original ring-magnon dispersion sketch; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
N = 32
ell = np.arange(-N+1, N)
xq = 2*np.pi*ell/N
fig, ax = plt.subplots(figsize=(9, 4.7), layout='constrained')
ax.axvspan(-np.pi, np.pi, color='#dbeafe', alpha=.5, label='One Brillouin zone')
ax.plot(x, 1-np.cos(x), color='#2563eb', lw=2.2, label=r'$1-\cos(qa)$')
ax.scatter(xq, 1-np.cos(xq), s=13, color='#334155', zorder=3, label='Allowed samples, N = 32')
near = np.linspace(-1, 1, 100)
ax.plot(near, near**2/2, ls='--', lw=1.5, color='#dc2626', label=r'Near zero: $(qa)^2/2$')
ax.plot([-2*np.pi,2*np.pi],[0,0], 'o', mfc='white', mec='#2563eb', ms=6, zorder=5, clip_on=False)
ax.set(xlim=(-2*np.pi, 2*np.pi), ylim=(-.08, 2.2), xlabel=r'Wavenumber $qa$', ylabel=r'Excitation energy $(E-E_0)/J$', title='The extended-zone plot repeats the same N independent modes')
ax.set_xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi], [r'$-2\pi$',r'$-\pi$', '0',r'$\pi$',r'$2\pi$'])
ax.legend(ncol=2, loc='upper center', fontsize=9)
ax.grid(alpha=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
