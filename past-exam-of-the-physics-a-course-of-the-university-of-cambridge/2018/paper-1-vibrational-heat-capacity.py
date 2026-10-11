"""Original vibrational heat-capacity activation; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
T=np.logspace(-2,2,800);x=1/T
# Stable expression even at very small T.
y=x*x*np.exp(-x)/(-np.expm1(-x))**2
fig,ax=plt.subplots(figsize=(7.7,4.4),layout='constrained')
ax.semilogx(T,y,lw=2.4,label='Harmonic vibrational contribution')
ax.axhline(1,color='#64748b',lw=1,ls='--',label='Classical limit: R per mole')
ax.set(xlabel=r'Reduced temperature $T/\theta_v$, $\theta_v=\hbar\omega/k_B$',ylabel=r'$C_{V,\mathrm{vib}}/R$ (molar)',ylim=(-.02,1.13),xlim=(.01,100),title='A single diatomic stretching mode freezes out at low temperature')
ax.text(.035,.25,'Excitations\nfrozen out',fontsize=9);ax.text(3,.82,'Vibration active',fontsize=9)
ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
