"""Original explanatory figure. Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained');m=np.linspace(-1.3,.55,1000);astar=2/9
for a,col,lab in [(.24,'#2871a1','a = 0.24: ordered metastable'),(astar,'#6a509a','a = 2/9: coexistence'),(.15,'#b34f28','a = 0.15: ordered stable')]:axs[0].plot(m,a*m*m/2+m**3/3+m**4/4,color=col,label=lab)
axs[0].scatter([0,-2/3],[0,0],color='#6a509a',zorder=4);axs[0].set(xlabel='magnetization m',ylabel='F − F₀',ylim=(-.015,.04),title='Cubic-quartic potentials, b = d = 1');axs[0].legend(fontsize=8,loc='upper left')
a=np.linspace(-.12,.3,1000);disc=np.maximum(0,1-4*a);morder=(-1-np.sqrt(disc))/2;stable=a<=astar;axs[1].plot(a[stable],morder[stable],color='#b34f28',lw=2);axs[1].plot(a[a>=astar],np.zeros(np.sum(a>=astar)),color='#b34f28',lw=2,label='global minimum')
meta=(a>astar)&(a<.25);axs[1].plot(a[meta],morder[meta],color='#2871a1',ls='--',label='metastable minimum');meta0=(a>0)&(a<astar);axs[1].plot(a[meta0],np.zeros(np.sum(meta0)),color='#2871a1',ls='--')
axs[1].plot([astar,astar],[-2/3,0],color='#6a509a',ls=':');axs[1].axvline(0,c='gray',ls=':',lw=1);axs[1].axvline(.25,c='gray',ls=':',lw=1);axs[1].annotate('jump at a = 2/9',xy=(astar,-.35),xytext=(.01,-.35),arrowprops={'arrowstyle':'->'},fontsize=9)
axs[1].set(xlabel='quadratic coefficient a',ylabel='selected magnetization',title='Equilibrium jump precedes the a = 0 spinodal',ylim=(-1.2,.1));axs[1].legend(loc='lower left',fontsize=8)
for ax in axs:ax.grid(alpha=.18);ax.axhline(0,c='gray',lw=.6)
fig.suptitle('Illustrative first-order Landau transition with a symmetry-breaking cubic term')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
