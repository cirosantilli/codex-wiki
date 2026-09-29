"""Original normalized top-hat and sinc-squared densities; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(9,3.5),layout='constrained')
axes[0].plot([-1,-.5,-.5,.5,.5,1],[0,0,1,1,0,0],color='#2158a0',lw=2)
axes[0].set(xlabel=r'$x/L$',ylabel=r'$L|\psi(x)|^2$',title='Uniform position density',ylim=(-.05,1.2))
u=np.linspace(-5,5,2501);density=np.sinc(u)**2
axes[1].plot(u,density,color='#b24b18',lw=1.7)
axes[1].set(xlabel=r'$u=pL/(2\pi\hbar)$',ylabel=r'$2\pi\hbar|\widetilde\psi(p)|^2/L$',title=r'$\mathrm{sinc}^2(\pi u)$: nonzero tails',ylim=(-.03,1.08))
for ax in axes:ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-top-hat.png',dpi=155,facecolor='white')
