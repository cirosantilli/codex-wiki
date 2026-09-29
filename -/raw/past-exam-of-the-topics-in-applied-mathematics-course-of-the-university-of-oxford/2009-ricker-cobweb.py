"""Original solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})

def cobweb(ax,r,start,steps):
 u=start
 for j in range(steps):
  nxt=r*u*np.exp(-u);ax.plot([u,u,nxt],[u,nxt,nxt],color='#cf6739',lw=.9);u=nxt
fig,axs=plt.subplots(1,3,figsize=(13,4),layout='constrained')
for ax,r,limit,steps in zip(axs,[2,2,9],[5.2,.82,5.2],[15,22,4]):
 x=np.linspace(0,limit,700);ax.plot(x,r*x*np.exp(-x),label='H(u)');ax.plot(x,x,'--',color='.6',label='Identity');cobweb(ax,r,5,steps);ax.set(xlim=(0,limit),ylim=(0,limit),xlabel='uₙ',ylabel='uₙ₊₁',title=('r=2: initial slump' if ax is axs[0] else 'r=2: recovery enlarged' if r==2 else 'r=9: four updates, u₁=5'));ax.legend(fontsize=8)
fig.savefig(Path.cwd()/'2009-ricker-cobweb.png',dpi=150,facecolor='white');plt.close(fig)
