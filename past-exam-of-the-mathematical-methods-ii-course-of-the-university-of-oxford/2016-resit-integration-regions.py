"""Original region plots for horizontal slicing and two coordinate maps."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import numpy as np

fig,axes=plt.subplots(2,2,figsize=(10.4,8.8),layout='constrained')
ax=axes[0,0];x=np.linspace(-1,0,400)
ax.fill_between(x,x,0,color='#f5d98f');ax.fill_between(x,0,x*x,color='#b5d9f1')
ax.plot(x,x,color='#a64b1f',label=r'$y=x$');ax.plot(x,x*x,color='#176ca6',label=r'$y=x^2$');ax.plot([-1,-1],[-1,1],color='.25')
for y,color in [(-.4,'#a64b1f'),(.4,'#176ca6')]:ax.plot([-1,y if y<0 else -np.sqrt(y)],[y,y],color=color,lw=3)
ax.axhline(0,color='.4',lw=.8);ax.set(title='Horizontal slices: split at y = 0',xlabel='x',ylabel='y',xlim=(-1.15,.15),ylim=(-1.12,1.15));ax.legend(fontsize=9)
ax=axes[0,1];x=np.linspace(.68,1.77,600);lo=np.maximum(x,1/x);hi=np.minimum(2*x,3/x);ax.fill_between(x,lo,hi,where=lo<=hi,color='#b5d9f1')
xx=np.linspace(.6,1.9,600)
for yy,label in [(xx,'u = 1'),(2*xx,'u = 2'),(1/xx,'v = 1'),(3/xx,'v = 3')]:ax.plot(xx,yy,lw=1.5,label=label)
ax.set(title='u = y/x, v = xy: original region',xlabel='x',ylabel='y',xlim=(.58,1.92),ylim=(.5,2.7));ax.legend(fontsize=8,ncol=2)
ax=axes[1,0];ax.add_patch(Rectangle((1,1),1,2,facecolor='#b5d9f1',edgecolor='#176ca6',lw=2));ax.set(title='The same region in (u, v)',xlabel='u',ylabel='v',xlim=(.5,2.5),ylim=(.5,3.5));ax.set_xticks([1,2]);ax.set_yticks([1,3])
ax=axes[1,1];corners=[(.5,.5),(1,0),(2,1),(1.5,1.5)];ax.add_patch(Polygon(corners,closed=True,facecolor='#f5d98f',edgecolor='#a64b1f',lw=2))
for xy,label in [((.72,.13),'x + y = 1'),((1.44,1.45),'x + y = 3'),((.62,.99),'x − y = 0'),((1.67,.40),'x − y = 1')]:ax.text(*xy,label,fontsize=8,rotation=35 if '−'in label else -35)
ax.set(title='u = x − y, v = x + y',xlabel='x',ylabel='y',xlim=(.25,2.3),ylim=(-.25,1.8),aspect='equal')
for ax in axes.flat:ax.grid(alpha=.14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=135,facecolor='white')
