"""Phase curves of the avalanche-front model; PNG output in cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':11, 'figure.facecolor':'white', 'axes.facecolor':'white'})
fig,ax=plt.subplots(figsize=(8.5,4.6),dpi=120)
for c,color in zip((-2.,-.5,0.,.5,2.),('#2878b5','#45a778','#222222','#e49526','#be4b56')):
    lower=max(.06,(-1.5*c)**(1/3) if c<0 else .06)
    x=np.linspace(lower,6,1500)
    v=np.sqrt(np.maximum(0,2*x/3+c/x**2))
    ax.plot(x,v,color=color,lw=2.4 if c==0 else 1.8,ls='--'if c==0 else '-',label=r'$c='+f'{c:g}'+('$ (asymptote)'if c==0 else '$'))
    x0=3.6; x1=3.95
    y0=np.sqrt(2*x0/3+c/x0**2);y1=np.sqrt(2*x1/3+c/x1**2)
    ax.annotate('',xy=(x1,y1),xytext=(x0,y0),arrowprops={'arrowstyle':'->','color':color,'lw':1.6})
ax.set(xlim=(0,6),ylim=(0,3.1),xlabel=r'Front position $x$',ylabel=r'Front speed $\dot x$',title=r'Avalanche trajectories: $\dot x^2=2x/3+c/x^2$')
ax.text(.98,.04,r'Scaled units: $g\sin\alpha=1$'+'\nArrows indicate increasing time.',transform=ax.transAxes,ha='right',va='bottom',fontsize=10)
ax.grid(alpha=.18);ax.legend(loc='upper left',framealpha=.95,ncol=2)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-4-avalanche-phase-plane.png',facecolor='white')
plt.close(fig)
