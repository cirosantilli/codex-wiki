"""Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; cwd PNG only."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,3,figsize=(13.2,4.4),dpi=100,facecolor='white')
x=np.linspace(-2,2,100);X,Y=np.meshgrid(x,x)
for ax,eps,gamma,title in zip(axs,[1,0,1],[0,1,1],['(i) Pure strain: xy = constant','(ii) Rigid rotation: circles','(iii) Simple shear: x − y = constant']):
    U=eps*X-gamma*Y;V=gamma*X-eps*Y
    ax.streamplot(x,x,U,V,density=.9,color='#2166ac',linewidth=1,arrowsize=1.2)
    if gamma==0:
        ax.axhline(0,color='0.4',linewidth=.8,linestyle='--')
        ax.axvline(0,color='0.4',linewidth=.8,linestyle='--')
    if eps==gamma:
        ax.plot([-2,2],[-2,2],color='#a33426',linewidth=1.6,label='Stationary line')
        ax.legend(loc='upper left',fontsize=8,framealpha=1)
    ax.set(xlim=(-2,2),ylim=(-2,2),xlabel='x',ylabel='y',title=title)
    ax.set_aspect('equal');ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks([-2,-1,0,1,2])
fig.tight_layout(pad=1.2)
fig.savefig(Path.cwd()/'paper-2-streamlines.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
