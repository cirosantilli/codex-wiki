from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(1,2,figsize=(9,3.7));u=np.linspace(.1,16,600)
em=(u-np.sqrt(u*u+16))/2;ep=(u+np.sqrt(u*u+16))/2
ax[0].plot(u,em,label='Lowest singlet',lw=2);ax[0].plot(u,np.zeros_like(u),label='Three triplets',lw=2);ax[0].plot(u,u,'--',color='gray',label='Antisymmetric doublon');ax[0].plot(u,ep,':',color='black',label='Upper singlet')
ax[0].set(xlabel=r'$U/|t|$',ylabel=r'$E/|t|$',title='Exact two-site spectrum',ylim=(-2.1,18));ax[0].legend(fontsize=8)
ax[1].plot(u,-em,label='Exact singlet-triplet gap',lw=2);mask=u>2;ax[1].plot(u[mask],4/u[mask],'--',label=r'Large-U estimate $4t^2/U$')
ax[1].set(xlabel=r'$U/|t|$',ylabel=r'$J/|t|$',ylim=(0,2.1),title='Virtual charge fluctuations generate exchange');ax[1].legend(fontsize=8)

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white',bbox_inches='tight')
plt.close(fig)
