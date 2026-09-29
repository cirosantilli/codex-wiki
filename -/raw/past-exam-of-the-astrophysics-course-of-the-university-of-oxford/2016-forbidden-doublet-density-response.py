from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'axes.titlesize':14,'axes.labelsize':13})
fig,ax=plt.subplots(figsize=(8,4.7),dpi=130,facecolor='white')
ne=np.geomspace(10,1e7,1000)
models=[('[O II]',np.array([3.6e-5,1.8e-4]),np.array([.81,.55]),np.array([.3729,.3727]),'#2268a3'),('[Ne IV]',np.array([5.4e-4,4.9e-3]),np.array([.89,.58]),np.array([.2424,.2422]),'#b13939')]
for label,A,Omega,lam,col in models:
 coeff=8.6e-12*Omega/np.array([6,4])/100
 nc=A/coeff/1e6
 low=Omega[0]/Omega[1]*lam[1]/lam[0]
 ratio=low*(1+ne/nc[1])/(1+ne/nc[0])
 ax.semilogx(ne,ratio,color=col,lw=2.5,label=label)
 best=np.sqrt(np.prod(nc));ax.axvline(best,color=col,ls='--',lw=1.2,alpha=.7)
 ax.text(best*1.13,.91 if label=='[O II]' else .67,fr'{best:.2g} cm$^{{-3}}$',color=col,fontsize=10)
ax.set(xlim=(10,1e7),ylim=(0,1.65),xlabel=r'Electron density $n_e$ (cm$^{-3}$)',ylabel=r'Energy-flux ratio $F_{21}/F_{31}$',title=r'Independent-level density diagnostics at $T_e=10^4$ K')
ax.legend(loc='upper right',frameon=False)
ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
