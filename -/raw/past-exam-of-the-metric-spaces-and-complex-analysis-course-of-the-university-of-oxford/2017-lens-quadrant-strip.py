"""Original three-region conformal-map diagram; output to the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,3,figsize=(12,4.5),dpi=100,facecolor='white')
color='#1264a3';fill='#dcebf6';point='#bc4b1d'
ax=axes[0];x=np.linspace(-1,1,501);upper=np.sqrt(2-x*x)-1
ax.fill_between(x,-upper,upper,color=fill)
ax.plot(x,upper,color=color,ls='--',lw=1.6);ax.plot(x,-upper,color=color,ls='--',lw=1.6)
ax.scatter([-1,1],[0,0],s=30,facecolor='white',edgecolor=color,zorder=4)
ax.scatter([0],[0],s=30,color=point,zorder=5);ax.text(.05,.08,'0',color=point)
ax.set(xlim=(-1.25,1.25),ylim=(-.80,.80),title='A: circular lens',xlabel='Re z',ylabel='Im z')
ax.set_aspect('equal',adjustable='box')
ax=axes[1];ax.fill_between([0,3.0],0,3,color=fill)
ax.plot([0,3],[0,0],ls='--',color=color,lw=1.6);ax.plot([0,0],[0,3],ls='--',color=color,lw=1.6)
ax.annotate('',xy=(2.9,1.9),xytext=(2.35,1.9),arrowprops=dict(arrowstyle='->',color=color))
ax.annotate('',xy=(1.9,2.9),xytext=(1.9,2.35),arrowprops=dict(arrowstyle='->',color=color))
ax.scatter([1],[1],s=30,color=point);ax.text(1.1,1.06,'1 + i',color=point)
ax.set(xlim=(-.3,3),ylim=(-.3,3),title='B: first quadrant',xlabel='Re w',ylabel='Im w')
ax.set_aspect('equal',adjustable='box')
ax=axes[2];ax.fill_between([-1.8,1.8],0,np.pi/2,color=fill)
for yy in (0,np.pi/2):ax.axhline(yy,color=color,ls='--',lw=1.6)
for end,start in [(-1.7,-1.2),(1.7,1.2)]:ax.annotate('',xy=(end,np.pi/4),xytext=(start,np.pi/4),arrowprops=dict(arrowstyle='->',color=color))
ax.scatter([np.log(2)/2],[np.pi/4],s=30,color=point)
ax.annotate(r'$\frac{1}{2}\log2+i\pi/4$',xy=(np.log(2)/2,np.pi/4),xytext=(-.8,1.1),fontsize=10,color=point)
ax.set(xlim=(-1.8,1.8),ylim=(-.35,1.95),title='C: horizontal strip',xlabel=r'Re $\zeta$',ylabel=r'Im $\zeta$')
ax.set_yticks([0,np.pi/4,np.pi/2],['0','π/4','π/2']);ax.set_aspect('equal',adjustable='box')
for ax in axes:
    ax.grid(alpha=.13);ax.spines[['top','right']].set_visible(False)
fig.text(.33,.10,r'$M(z)=(1+i)(1+z)/(1-z)$:  A → B',ha='center',fontsize=12)
fig.text(.75,.10,r'$\zeta=\operatorname{Log}w$:  B → C',ha='center',fontsize=12)
fig.suptitle('Lens → quadrant → strip (all boundaries excluded)',fontsize=15,y=.98)
fig.subplots_adjust(left=.055,right=.985,top=.85,bottom=.24,wspace=.45)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',dpi=100)
plt.close(fig)
