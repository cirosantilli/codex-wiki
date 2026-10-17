"""Original independent-band cross-section; write PNG to the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(6.6,6.2),facecolor='white')
q=np.linspace(0,2*np.pi,500);radius=np.sqrt(8*np.pi/3)
ax.plot(radius*np.cos(q),radius*np.sin(q),color='#247ba0',lw=2.5,label=r'$\gamma$: circular cylinder')
for s in [-1,1]:
    ax.axvline(s*2*np.pi/3,color='#ba3434',ls='--',lw=2,label=r'$A$: $k_xa=\pm2\pi/3$' if s==1 else None)
    ax.axhline(s*2*np.pi/3,color='#459348',ls='-.',lw=2,label=r'$B$: $k_ya=\pm2\pi/3$' if s==1 else None)
ax.set(xlim=(-np.pi,np.pi),ylim=(-np.pi,np.pi),xlabel=r'$k_xa$',ylabel=r'$k_ya$',title='Equal band filling; negative cosine hopping')
ax.set_xticks([-np.pi,0,np.pi], [r'$-\pi$','0',r'$\pi$'])
ax.set_yticks([-np.pi,0,np.pi], [r'$-\pi$','0',r'$\pi$'])
ax.set_aspect('equal');ax.grid(alpha=.18)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.12),fontsize=10)
fig.text(.5,.02,r'All sheets extend along $k_z$; crossings are unhybridized in this model.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.09,1,1))
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135,facecolor='white')
plt.close(fig)
