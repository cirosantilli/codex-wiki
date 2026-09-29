"""Original universal bulk/sliding search balance; Python 3.14, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
s=np.geomspace(.08,12.5,700)
fig,ax=plt.subplots(figsize=(7.3,4.6),constrained_layout=True,facecolor='white')
ax.plot(s,.5/s,color='#1864ab',ls='--',lw=2,label='Bulk relocation cost')
ax.plot(s,.5*s,color='#d9480f',ls=':',lw=2.3,label='Local sliding cost')
ax.plot(s,.5*(s+1/s),color='#2b8a3e',lw=2.4,label='Total mean search time')
ax.axvline(1,color='.5',ls=':',lw=1);ax.plot([1],[1],'o',color='#2b8a3e')
ax.text(1.17,1.18,'Equal costs at the optimum',fontsize=10)
ax.set(xscale='log',yscale='log',xlabel=r'$\lambda/\lambda_*$',ylabel=r'Time / $\tau_{min}$',ylim=(.035,8),title='Facilitated search balances relocation and local exploration')
ax.grid(alpha=.14,which='both');ax.legend(frameon=False,fontsize=10,loc='upper center')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
