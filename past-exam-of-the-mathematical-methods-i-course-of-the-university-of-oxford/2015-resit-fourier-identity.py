from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.titlesize':13,'figure.facecolor':'white','axes.facecolor':'white'})
fig,axs=plt.subplots(1,2,figsize=(11,4.5),layout='constrained');x=np.linspace(-np.pi,np.pi,1501)
def partial(x,N):
 n=np.arange(1,N+1)[:,None];return 2*np.sum((-1.)**(n+1)*np.sin(n*x[None,:])/n,axis=0)
ax=axs[0];ax.plot(x/np.pi,x/np.pi,'--',c='.2',lw=2,label='identity function')
for N,color in [(3,'#009E73'),(9,'#D55E00'),(35,'#0072B2')]:ax.plot(x/np.pi,partial(x,N)/np.pi,label=f'{N} terms',color=color,lw=1.5)
ax.scatter([-1,1],[0,0],c='black',s=35,zorder=4);ax.scatter([-1,1],[-1,1],facecolor='white',edgecolor='black',s=40,zorder=4);ax.set(xlabel=r'$x/\pi$',ylabel=r'function value / $\pi$',xlim=(-1.02,1.02),ylim=(-1.3,1.3));ax.legend(loc='upper left',fontsize=10);ax.grid(alpha=.2);ax.set_title('Interior convergence; endpoints sum to zero')
ax=axs[1];x=np.linspace(.78*np.pi,1.22*np.pi,1600)
for xx in [x[x<np.pi],x[x>np.pi]]:ax.plot(xx/np.pi,((xx+np.pi)%(2*np.pi)-np.pi)/np.pi,'--',c='.2',lw=2)
for N,color in [(9,'#D55E00'),(35,'#0072B2')]:ax.plot(x/np.pi,partial(x,N)/np.pi,label=f'{N} terms',color=color,lw=1.6)
ax.scatter([1],[0],c='black',s=35,zorder=4);ax.set(xlabel=r'$x/\pi$',ylabel=r'periodic extension / $\pi$',ylim=(-1.3,1.3));ax.grid(alpha=.2);ax.legend(loc='upper right',fontsize=10);ax.set_title('Endpoint detail of the periodic extension')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white');plt.close(fig)
