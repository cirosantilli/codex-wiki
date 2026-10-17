from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(1,2,figsize=(10,3.7))
P=np.linspace(0,1,600)
f=lambda p,r:((1+p)**(5/3)+(1-p)**(5/3))/2-r*(1+p*p)/2
for r in [1.05,1.14,2**(5/3)-2,1.28,1.36]:ax[0].plot(P,f(P,r)-f(0,r),label=fr'$r_s={r:.3f}$')
ax[0].axhline(0,color='black',lw=.6);ax[0].set(xlabel='Polarization P',ylabel=r'$[E(P)-E(0)]/[2AV(n/2)^{5/3}]$',title='Exchange competes with the kinetic cost');ax[0].legend(fontsize=8)
rs=np.linspace(.95,1.42,400);grid=np.linspace(0,1,4001)
opt=[grid[np.argmin(f(grid,r))] for r in rs]
ax[1].plot(rs,opt,lw=2)
for r,label,col in [(10/9,'Local onset','gray'),(2**(5/3)-2,'Endpoint crossing','tab:orange'),(5*2**(2/3)/6,'Full polarization','black')]:ax[1].axvline(r,ls='--',lw=.8,label=label,color=col)
ax[1].set(xlabel=r'Contact interaction parameter $r_s$',ylabel='Minimizing polarization P',ylim=(-.03,1.05),title='Allowing intermediate spin populations');ax[1].legend(fontsize=7,loc='lower right')

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white',bbox_inches='tight')
plt.close(fig)
