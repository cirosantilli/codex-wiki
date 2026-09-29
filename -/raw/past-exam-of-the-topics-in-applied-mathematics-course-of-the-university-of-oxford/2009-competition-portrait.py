"""Original solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(6.5,5),layout='constrained');x=np.linspace(.015,1.6,50);X,Y=np.meshgrid(x,x);U=X*(1-X-Y/2);V=Y*(1-Y-X/2);ax.streamplot(X,Y,U,V,density=1,color='.6',linewidth=.7);n=np.linspace(0,1.6,300);ax.plot(n,2*(1-n),label='n+m/2=1');ax.plot(n,1-n/2,label='m+n/2=1');ax.scatter([0,1,0],[0,0,1],facecolors='white',edgecolors='black',s=40,zorder=4);ax.scatter([2/3],[2/3],color='black',s=40,zorder=4);ax.set(xlabel='n',ylabel='m',xlim=(0,1.6),ylim=(0,1.6),title='Coexistence attracts all positive states (q=1)');ax.legend(fontsize=9)
fig.savefig(Path.cwd()/'2009-competition-portrait.png',dpi=150,facecolor='white');plt.close(fig)
