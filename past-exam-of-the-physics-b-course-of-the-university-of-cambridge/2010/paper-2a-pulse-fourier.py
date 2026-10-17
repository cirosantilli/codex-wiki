from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})

# Normalized period T=1, illustrative width/period delta=0.15.
delta=.15
t=np.linspace(-1,1,6001)
r=(t+.5)%1-.5
f=np.where(np.abs(r)<=delta/2,1/delta,0.)
fig,axs=plt.subplots(2,2,figsize=(10.4,6.8),constrained_layout=True)
axs[0,0].plot(t,f,color='#2166ac',lw=1.6)
axs[0,0].set(title='Unit-area pulse train',ylabel=r'$T f(t)$',ylim=(-.3,7.3))
terms=[np.ones_like(t)]+[2*np.sinc(n*delta)*np.cos(2*np.pi*n*t) for n in (1,2,3)]
for n,term in enumerate(terms[:3]):
    axs[0,1].plot(t,term,lw=1.5,label='constant' if n==0 else f'harmonic n={n}')
axs[0,1].set(title='First three series terms',ylabel='Normalized contribution')
axs[0,1].legend(fontsize=9,ncol=1)
axs[1,0].plot(t,f,color='.65',lw=1,label='pulse train')
axs[1,0].plot(t,sum(terms[:3]),color='#b2182b',label='constant + n=1,2')
axs[1,0].plot(t,sum(terms),color='#2166ac',ls='--',label='constant + n=1,2,3')
axs[1,0].set(title='Partial sums',ylabel='Normalized amplitude',ylim=(-2,7.3))
axs[1,0].legend(fontsize=9)
for ax in [axs[0,0],axs[0,1],axs[1,0]]:
    ax.set(xlim=(-1,1),xlabel=r'$t/T$')
    ax.grid(alpha=.18)
z=np.linspace(0,2.5,1200);n=np.arange(17);zn=n*delta
axs[1,1].plot(z,np.sinc(z),color='#2166ac',label='sinc envelope')
axs[1,1].stem(zn,np.sinc(zn),linefmt='C3-',markerfmt='C3o',basefmt=' ')
axs[1,1].axvline(1,color='.5',ls=':',label='first envelope zero')
axs[1,1].axhline(0,color='.6',lw=.8)
axs[1,1].set(title='Fourier coefficients',xlabel=r'$n\Delta T/T$',ylabel=r'$a_n/(2/T)$',xlim=(0,2.5))
axs[1,1].legend(fontsize=9);axs[1,1].grid(alpha=.18)
fig.suptitle(r'Rectangular pulse Fourier series: illustrative $\Delta T/T=0.15$',fontsize=13)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
