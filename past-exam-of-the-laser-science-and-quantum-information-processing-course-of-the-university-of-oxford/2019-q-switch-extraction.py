"""Original extraction curve for the ideal Q-switched rate equations; Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1e-5,.99999,1600);r=-np.log1p(-x)/x
r95=-np.log(.05)/.95
fig,ax=plt.subplots(figsize=(7.2,4.3),facecolor='white')
ax.plot(r,x,color='#126782',lw=2.1)
ax.plot([1,r95],[0,.95],'o',color='#a34100')
ax.axhline(1,ls='--',color='#6c737b',lw=1)
ax.plot([r95,r95],[0,.95],':',color='#a34100')
ax.plot([1,r95],[.95,.95],':',color='#a34100')
ax.annotate(r'$r_{95}=3.1534$',(r95,.95),xytext=(4,.75),fontsize=12,arrowprops={'arrowstyle':'->','color':'#a34100'})
ax.text(1.12,.1,'Pulse threshold',fontsize=11)
ax.set(xlim=(.8,7),ylim=(0,1.075),xlabel=r'Over-pumping $r=N_i^*/N_{\rm th}^*$',ylabel=r'Fraction of extractable inversion energy $\beta\eta$',title='Physical nonzero-pulse branch')
ax.grid(alpha=.18);fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
