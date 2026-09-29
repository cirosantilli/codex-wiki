"""Original educational diagram; Python 3.14, NumPy and Matplotlib. Saves a basename PNG to the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
s=np.logspace(-3,2,1000);msd=2*(s+np.expm1(-s))
fig,ax=plt.subplots(figsize=(6.7,4),layout='constrained');ax.loglog(s,msd,color='#225c91',lw=2,label='Equilibrium inertial Langevin result');ax.loglog(s,s*s,color='#b25424',ls='--',label=r'Ballistic: $(t/\tau)^2$');ax.loglog(s,2*s,color='#388773',ls=':',label=r'Diffusive: $2t/\tau$');ax.axvline(1,color='#888',ls=':',lw=1)
ax.set(xlabel=r'$t/\tau$',ylabel=r'$\langle\Delta x^2\rangle/(D\tau)$',xlim=(1e-3,100),ylim=(5e-7,2e3),title='One-coordinate displacement with thermal initial velocity');ax.legend(fontsize=9);ax.grid(alpha=.2,which='both')
fig.savefig('paper-1-tsp2014-brownian.png',dpi=150,facecolor='white');plt.close(fig)
