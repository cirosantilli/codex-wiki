import numpy as np
import matplotlib.pyplot as plt
s=np.linspace(0,5,600)
fig,ax=plt.subplots(figsize=(7.3,4.2),layout='constrained')
ax.plot(s,2*s,color='#555',label='Free diffusion: displacement variance')
ax.plot(s,2*(-np.expm1(-s)),color='#2475aa',lw=2.4,label='Trap: equilibrium two-time displacement')
ax.plot(s,-np.expm1(-2*s),color='#c94a39',lw=2.2,label='Trap: variance from a fixed centre')
ax.axhline(2,color='#2475aa',ls=':',alpha=.6);ax.axhline(1,color='#c94a39',ls=':',alpha=.6)
ax.set(xlim=(0,5),ylim=(0,5.5),xlabel=r'Time $t/\tau_\kappa$,  $\tau_\kappa=\zeta/\kappa$',ylabel=r'Variance in units $k_BT/\kappa$',title='Overdamped Brownian displacement; matched diffusion coefficient')
ax.legend(frameon=False,loc='upper left',fontsize=10);ax.grid(alpha=.2)
fig.savefig('paper-1-tsp2012-brownian.png',dpi=150,facecolor='white')
