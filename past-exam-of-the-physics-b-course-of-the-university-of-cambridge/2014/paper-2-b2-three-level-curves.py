from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,3,figsize=(10.5,3.6),layout='constrained')
t=np.linspace(.015,5,700);lev=np.array([-1.,0.,1.]);w=np.exp(-np.array([0.,1.,2.])[None,:]/t[:,None]);pr=w/w.sum(axis=1)[:,None];E=pr@lev;C=((pr@lev**2)-E**2)/t**2
ax[0].plot(np.r_[0,t],np.r_[-1,E],lw=2);ax[0].axhline(0,color='gray',ls=':');ax[0].set(xlabel=r'$k_BT/(\mu B_0)$',ylabel=r'$\overline{E}/(\mu B_0)$',title='Warming at fixed nonzero field',ylim=(-1.05,.05))
b=np.linspace(-5,5,700);ener=np.stack([-b,np.zeros_like(b),b],axis=1);w=np.exp(-(ener-ener.min(axis=1)[:,None]));pr=w/w.sum(axis=1)[:,None];mean=(pr*ener).sum(axis=1)
ax[1].plot(b,mean,lw=2,color='#9e4a10');ax[1].plot(b,-np.abs(b),':',color='gray',label=r'$-\mu|B|$ limit');ax[1].set(xlabel=r'$\mu B/(k_BT_0)$',ylabel=r'$\overline{E}/(k_BT_0)$',title='Varying field at fixed temperature');ax[1].legend(fontsize=9)
ax[2].plot(np.r_[0,t],np.r_[0,C],lw=2,color='#367c46');ax[2].set(xlabel=r'$k_BT/(\mu B_0)$',ylabel=r'$C/k_B$',title='Excitation then saturation',ylim=(0,.7));ax[2].annotate('Schottky peak',(.53,.637),(.95,.53),arrowprops=dict(arrowstyle='->'),fontsize=9)
for a in ax:a.grid(alpha=.2);a.title.set_fontsize(11)
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
