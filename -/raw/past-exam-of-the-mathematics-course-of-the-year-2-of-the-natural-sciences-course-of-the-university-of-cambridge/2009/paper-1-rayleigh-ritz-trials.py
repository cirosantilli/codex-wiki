"""Original Dirichlet trial functions and variational bounds; write PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
r=np.linspace(0,1,600);s=r*(1-r);p=r*(1-r*r);q=s*s;E=56-4*np.sqrt(133)
# First row of (K-E M)(1,c)^T=0.
c=-(1/3-E/30)/(1/15-E/140)
improved=s+c*q
fig,axes=plt.subplots(1,2,figsize=(10,4.3),facecolor='white')
for y,label,style in [(np.sin(np.pi*r),'Exact sine','-'),(s,'First trial','--'),(p,'Second trial',':'),(improved,'Improved symmetric trial','-.')]:
 axes[0].plot(r,y/y.max(),style,label=label,lw=1.8)
axes[0].set(xlabel='r',ylabel='Trial function / peak value',title='Shape comparison');axes[0].legend(fontsize=9);axes[0].grid(alpha=.2)
labels=['Exact','First','Second','Improved'];values=[np.pi**2,10,10.5,E]
axes[1].scatter(range(4),values,s=50,c=['black','#247ba0','#d87b27','#278c4a'])
axes[1].axhline(np.pi**2,color='gray',ls='--',lw=1)
for i,v in enumerate(values):axes[1].annotate(f'{v:.6f}',(i,v),(i,v+.035),ha='center',fontsize=9)
axes[1].set_xticks(range(4),labels);axes[1].set(xlim=(-.5,3.5),ylim=(9.8,10.65),ylabel='Rayleigh quotient',title='Upper bounds to the lowest eigenvalue');axes[1].grid(axis='y',alpha=.2)
fig.tight_layout();fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135,facecolor='white');plt.close(fig)
