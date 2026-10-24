"""Original G2 root diagram; Python3.14/numpy/matplotlib; output in CWD."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
alpha=np.array([1.,0.]);beta=np.array([-1.5,np.sqrt(3)/2])
positive=[(1,0,r'$\alpha$'),(0,1,r'$\beta$'),(1,1,r'$\alpha+\beta$'),(2,1,r'$2\alpha+\beta$'),(3,1,r'$3\alpha+\beta$'),(3,2,r'$3\alpha+2\beta$')]
fig,ax=plt.subplots(figsize=(6.8,5.7),layout='constrained',facecolor='white')
for a,b,label in positive:
    point=a*alpha+b*beta
    color='#2464a0' if np.dot(point,point)<2 else '#b55a18'
    for sign in [-1,1]:
        q=sign*point
        ax.annotate('',xy=q,xytext=(0,0),arrowprops={'arrowstyle':'-|>','lw':1.7,'color':color,'mutation_scale':12})
        ax.scatter(*q,s=15,color=color)
    ax.annotate(label,xy=point,xytext=(5 if point[0]>=0 else -5,9 if point[1]>0 else -18),textcoords='offset points',ha='left' if point[0]>=0 else 'right',fontsize=11,color=color)
ax.axhline(0,color='#999999',lw=.7,zorder=-1);ax.axvline(0,color='#999999',lw=.7,zorder=-1)
ax.set(xlim=(-2.1,2.1),ylim=(-2.05,2.15),xlabel=r'$e_1$',ylabel=r'$e_2$',title=r'Twelve roots of $G_2$: lengths $1$ and $\sqrt{3}$')
ax.set_aspect('equal');ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.spines[['top','right']].set_visible(False)
ax.legend(handles=[Line2D([0],[0],color='#2464a0',label='Short roots'),Line2D([0],[0],color='#b55a18',label='Long roots')],loc='lower left',frameon=False)
fig.savefig('2009-g2-roots.png',dpi=150,facecolor='white',bbox_inches='tight')
