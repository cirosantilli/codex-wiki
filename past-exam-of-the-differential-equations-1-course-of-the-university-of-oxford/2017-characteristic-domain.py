"""Original domain-of-dependence diagram in physical and transformed coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(10.5,4.7),dpi=100,facecolor='white')
s=np.linspace(1/12,7/12,401)
rleft=.5+np.abs(s-1/3);rright=1-np.abs(s-1/3)
y=(3*s)**(2/3)
ax=axes[0];ax.fill_betweenx(y,rleft**2,rright**2,color='#d8e9f5')
ax.plot(rleft**2,y,color='#1264a3',lw=2);ax.plot(rright**2,y,color='#1264a3',lw=2)
ax.plot([.25,1],[1,1],color='#bb4a1c',lw=3,label='given data segment')
ax.scatter([.25,1],[1,1],color='#bb4a1c',s=22,zorder=4)
ax.set(xlim=(.15,1.1),ylim=(.25,1.58),xlabel='x',ylabel='y',title='Original coordinates')
ax.legend(loc='upper right',fontsize=9)
ax=axes[1];ax.fill_betweenx(s,rleft,rright,color='#d8e9f5')
ax.plot(rleft,s,color='#1264a3',lw=2);ax.plot(rright,s,color='#1264a3',lw=2)
ax.plot([.5,1],[1/3,1/3],color='#bb4a1c',lw=3)
ax.scatter([.5,1],[1/3,1/3],color='#bb4a1c',s=22,zorder=4)
ax.set(xlim=(.4,1.1),ylim=(0,.67),xlabel=r'$r=\sqrt{x}$',ylabel=r'$s=y^{3/2}/3$',title='Characteristic diamond')
ax.set_yticks([1/12,1/3,7/12],['1/12','1/3','7/12'])
ax.set_xticks([.5,.75,1],['1/2','3/4','1'])
ax.set_aspect('equal',adjustable='box')
for ax in axes:
    ax.grid(alpha=.18);ax.spines[['top','right']].set_visible(False)
fig.suptitle('Where the finite Cauchy-data segment uniquely determines u',fontsize=14)
fig.subplots_adjust(left=.075,right=.98,top=.83,bottom=.14,wspace=.35)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',dpi=100)
plt.close(fig)
