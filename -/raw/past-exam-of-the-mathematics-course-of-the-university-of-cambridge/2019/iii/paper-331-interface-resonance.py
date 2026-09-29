"""Plot the analytically derived two-interface instability; write PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,axes=plt.subplots(1,2,figsize=(10,4.8),dpi=100)
a=np.linspace(.02,3,600); e=np.exp(-2*a)
low=2*a/(1+e); high=2*a/(1-e)
ax=axes[0]
ax.fill_between(a,low,high,color='#f0b3ae',label='unstable')
ax.plot(a,low,color='#9d332d');ax.plot(a,high,color='#9d332d')
ax.plot(a,2*a,'--',color='#376b95',label=r'isolated resonance $J=2\alpha$')
ax.set(xlim=(0,3),ylim=(0,6.35),xlabel=r'$\alpha=kh/2$',ylabel='$J$',title='Exact instability window')
ax.legend(loc='upper left',fontsize=10);ax.grid(alpha=.2)
alpha=1.;J=np.linspace(1.5,2.5,900);s=J/(2*alpha)
yminus=1+s-np.sqrt(4*s+s*s*np.exp(-4*alpha))
ax=axes[1]
ax.plot(J,1-np.sqrt(s),'--',color='#818181',label='isolated wave speeds')
ax.plot(J,-1+np.sqrt(s),'--',color='#818181')
ax.plot(J,np.sqrt(np.maximum(yminus,0)),color='#376b95',label=r'coupled $\mathrm{Re}\,\widetilde c$')
ax.plot(J,-np.sqrt(np.maximum(yminus,0)),color='#376b95')
ax.plot(J,np.sqrt(np.maximum(-yminus,0)),color='#b03d34',lw=2,label=r'growth $\mathrm{Im}\,\widetilde c$')
lo=2*alpha/(1+np.exp(-2*alpha));hi=2*alpha/(1-np.exp(-2*alpha))
ax.axvspan(lo,hi,color='#f0b3ae',alpha=.32)
ax.axhline(0,color='black',lw=.7)
ax.set(xlim=(1.5,2.5),xlabel='$J$',ylabel=r'normalized wave speed',title=r'Wave locking at $\alpha=1$')
ax.legend(loc='lower left',fontsize=9);ax.grid(alpha=.2)
fig.subplots_adjust(left=.07,right=.985,bottom=.15,top=.88,wspace=.30)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100)
plt.close(fig)
