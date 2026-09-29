"""Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7; write opaque PNG to cwd."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.mplconfig'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axs=plt.subplots(1,2,figsize=(8.4,4),dpi=100,layout='constrained')
x=np.linspace(-1.2,1.2,100);X,Y=np.meshgrid(x,x)
for ax in axs:
 ax.set(xlim=(-1.15,1.15),ylim=(-1.15,1.15));ax.set_aspect('equal');ax.axhline(0,color='#777777',lw=.7);ax.axvline(0,color='#777777',lw=.7);ax.scatter([0],[0],c='black',s=35,zorder=8);ax.text(.05,.05,'Fixed point',fontsize=8)
axs[0].streamplot(x,x,1.1*X,-.7*Y,density=.65,color='#246a92',linewidth=1.1,arrowsize=1)
axs[0].plot([0,0],[-1.1,1.1],color='#16813d',lw=2.5)
for start,end in [(.75,.35),(-.75,-.35)]:
 axs[0].annotate('',(0,end),(0,start),arrowprops={'arrowstyle':'->','color':'#16813d','lw':2},zorder=10)
axs[0].annotate('Critical surface in h = 0 section',(0,.7),(-1.06,.94),fontsize=8,arrowprops={'arrowstyle':'->','color':'#16813d'})
axs[0].set(xlabel='Relevant thermal field t',ylabel='Irrelevant field w',title='Stable surface and departing trajectories')
axs[1].streamplot(x,x,X,1.4*Y,density=.65,color='#ab4c27',linewidth=1.1,arrowsize=1)
axs[1].set(xlabel='Relevant thermal field t',ylabel='Relevant magnetic field h',title='Two relevant directions: w = 0 section')
fig.suptitle('RG arrows point toward increasing coarse-graining length',fontsize=11)
fig.savefig(Path.cwd()/'paper-49-rg-flows.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
