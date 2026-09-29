"""Original weak-excitation two-pulse prediction; Python 3.14, numpy/matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-2.2,2.2,6601)
envelope=np.sinc(x)**2
probability=envelope*np.cos(10*np.pi*x)**2
fig, ax=plt.subplots(figsize=(9,4.3),dpi=100,facecolor='white')
ax.set_facecolor('white')
ax.plot(x,probability,color='#225ea8',linewidth=1.5,label='Two-pulse probability')
ax.plot(x,envelope,color='#d95f0e',linestyle='--',linewidth=1.8,label='Coherent envelope')
ax.set(xlim=(-2.2,2.2),ylim=(-.03,1.08),xlabel=r'Detuning $\delta\tau_p/(2\pi)$',ylabel=r'$P_e/(\Omega\tau_p)^2$',title=r'Weak-pulse Ramsey spectrum: $T=10\tau_p$')
ax.axvline(0,color='0.75',linewidth=.6,zorder=0)
ax.grid(alpha=.2)
ax.legend(loc='upper right',framealpha=1)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False,metadata={'Software':'codex-wiki'})
plt.close(fig)
