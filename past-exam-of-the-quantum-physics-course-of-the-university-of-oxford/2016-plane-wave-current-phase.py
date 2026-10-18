from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(-2*np.pi, 2*np.pi, 1000)
plt.rcParams.update({'font.size': 12})
fig, axes = plt.subplots(2, 1, figsize=(8.4, 5.3), sharex=True, layout='constrained', facecolor='white', gridspec_kw={'height_ratios':[2,1]})
axes[0].plot(u, np.cos(u), label=r'${\rm Re}(\psi/A)=\cos(kx)$', lw=2.2)
axes[0].plot(u, np.sin(u), label=r'${\rm Im}(\psi/A)=\sin(kx)$', lw=2.2, ls='--')
axes[0].set(ylabel=r'Wavefunction / $A$', ylim=(-1.25,1.25), title='Positive phase gradient: probability current to the right')
axes[0].legend(loc='upper right', fontsize=10)
axes[1].plot(u, np.ones_like(u), color='#317844', lw=2.5)
axes[1].set(ylabel=r'$|\psi|^2/|A|^2$', xlabel=r'Position $kx$ (positive $k$)', ylim=(0,1.5), xlim=(u[0],u[-1]))
for ax in axes:
 ax.axhline(0,color='0.4',lw=.7); ax.grid(alpha=.2); ax.set_facecolor('white')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=110, facecolor='white', transparent=False)
