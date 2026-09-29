# Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7. Run in desired output directory.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
fig,axs=plt.subplots(1,2,figsize=(10,5),sharex=True,sharey=True)
x=np.linspace(-3,3,900);y=np.linspace(-3,3,900);X,Y=np.meshgrid(x,y)
plus=(X>0)|(Y>0);minus=((X>0)&(X*X+Y*Y<4))|((X<0)&(Y<2))
for ax,M,title in zip(axs,[plus,minus],[r'$D_+$: matching plus branches',r'$D_-$: matching minus branches']):
    ax.contourf(X,Y,M.astype(float),levels=[.5,1.5],colors=['#dceaf5'])
    th=np.linspace(-np.pi/2,np.pi/2,300);ax.plot(np.cos(th),np.sin(th),'#0d6b40',lw=3,label='initial data')
    ax.plot([-3,0],[1,1],'#0d6b40',lw=3)
    ax.axhline(0,color='.6',lw=.7);ax.axvline(0,color='.6',lw=.7)
    ax.set(xlim=(-3,3),ylim=(-3,3),aspect='equal',xlabel='$x$',title=title);ax.grid(alpha=.15)
axs[0].plot([-3,0],[0,0],'r--',lw=1.5);axs[0].plot([0,0],[-3,0],'r--',lw=1.5)
axs[1].plot(2*np.cos(th),2*np.sin(th),'r--',lw=1.5,label='zero-gradient boundary')
axs[1].plot([-3,0],[2,2],'r--',lw=1.5);axs[1].plot([0,0],[-3,0],'r--',lw=2,label='excluded seam')
axs[1].plot(0,0,'o',mfc='white',mec='red',ms=6);axs[1].annotate('excluded focus',(0,0),(-2.6,-.8),arrowprops={'arrowstyle':'->'},fontsize=9)
axs[0].set_ylabel('$y$');axs[0].legend(loc='lower left');axs[1].legend(loc='lower left',fontsize=8)
fig.suptitle('Shading shows the open domains covered by the initial characteristic charts')
fig.tight_layout();fig.savefig(Path('2008-charpit-domains.png'),dpi=150,facecolor='white');plt.close(fig)
