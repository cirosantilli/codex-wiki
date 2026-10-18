from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

rho = np.linspace(0, 13, 1000)
r20 = (2-rho)*np.exp(-rho/2)/(2*np.sqrt(2))
r21 = rho*np.exp(-rho/2)/np.sqrt(24)
plt.rcParams.update({'font.size': 12})
fig, ax = plt.subplots(figsize=(8.4, 4.6), layout='constrained', facecolor='white')
ax.plot(rho, r20, label=r'$2s:\ a_0^{3/2}R_{20}$', lw=2.5, color='#1261a0')
ax.plot(rho, r21, label=r'$2p:\ a_0^{3/2}R_{21}$', lw=2.5, color='#c14a14')
ax.axhline(0, color='0.35', lw=0.8)
ax.scatter([2], [0], color='#1261a0', zorder=4)
ax.annotate('2s radial node', xy=(2, 0), xytext=(3.5, .25), arrowprops={'arrowstyle':'->'}, fontsize=11)
ax.set(xlabel=r'Radius $r/a_0$', ylabel=r'Scaled radial wavefunction $a_0^{3/2}R$', xlim=(0, 13), ylim=(-.16,.76), title='Hydrogen radial wavefunctions, n = 2')
ax.grid(alpha=.2); ax.legend(loc='upper right'); ax.set_facecolor('white')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=110, facecolor='white', transparent=False)
