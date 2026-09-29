"""Python 3.14; numpy/matplotlib. Output is written in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
u=np.linspace(0,2,700);v=np.maximum.reduce([np.full_like(u,1.5),2.5-2*u,2-2*u/3])
fig,ax=plt.subplots(figsize=(6.5,4.4),layout='constrained',facecolor='white')
ax.fill_between(u,v,3.4,color='#bee1d1',alpha=.7,label='Dual feasible region')
ax.plot(u,v,color='#27674c',lw=2.3)
ax.plot(u,(21-6*u)/11,color='#b3483e',ls='--',lw=1.5,label='$6u+11v=21$')
for p,label,offset in[((.75,1.5),'A = (3/4, 3/2)',(12,-28)),((.375,1.75),'B = (3/8, 7/4)',(18,15)),((0,2.5),'C = (0, 5/2)',(13,10))]:
 ax.scatter(*p,color='#263c46',s=28,zorder=5);ax.annotate(label,p,xytext=offset,textcoords='offset points',fontsize=9)
ax.set(xlabel='$u$: resource R price',ylabel='$v$: resource S price',title='Dual region and original optimal price',xlim=(-.05,2),ylim=(.25,3.4))
ax.legend(loc='upper right',fontsize=9);ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/'2011-as2-dual-feasible.png',dpi=145,facecolor='white')
