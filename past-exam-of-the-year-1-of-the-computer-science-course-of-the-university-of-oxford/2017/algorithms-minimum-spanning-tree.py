"""Plot the solved weighted tree and Boruvka rounds; write the PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), dpi=100, facecolor='white')
pos={'a':(0,0),'b':(1,1),'c':(1,-1),'d':(2,0),'e':(3,1),'f':(3,-1),'g':(5,1),'h':(5,-1)}
edges=[('a','b',13),('a','c',4),('b','c',9),('b','d',11),('c','d',3),('b','e',8),('c','f',2),('d','e',7),('d','f',1),('e','g',10),('e','h',5),('f','h',6),('g','h',12)]
tree={frozenset(e)for e in [('d','f'),('c','f'),('a','c'),('e','h'),('f','h'),('b','e'),('e','g')]}
for panel,ax in enumerate(axes):
    for u,v,w in edges:
        p=np.array(pos[u]);q=np.array(pos[v]);chosen=frozenset((u,v))in tree
        color='#147d64'if chosen else '#c5cbd3'
        if panel and frozenset((u,v))==frozenset(('f','h')):color='#be5814'
        ax.plot([p[0],q[0]],[p[1],q[1]],color=color,lw=3 if chosen else 1.2,zorder=1)
        mid=(p+q)/2
        ax.text(*mid,str(w),ha='center',va='center',color='#122d25'if chosen else '#6b7280',
                bbox={'facecolor':'white','edgecolor':'none','pad':1.2},zorder=2)
    for v,(x,y)in pos.items():
        ax.scatter([x],[y],s=520,facecolor='white',edgecolor='#243b53',zorder=3)
        ax.text(x,y,v,ha='center',va='center',zorder=4,fontsize=14)
    ax.set(xlim=(-.5,5.5),ylim=(-1.65,1.65),aspect='equal')
    ax.axis('off')
axes[0].set_title('Kruskal: seven accepted edges, total 36',fontsize=14)
axes[1].set_title('Borůvka: six round-1 edges, then fh',fontsize=14)
fig.text(.5,.07,'Green: selected tree edges. Right panel orange: the sole new edge in round 2.',ha='center',fontsize=12)
fig.subplots_adjust(left=.02,right=.98,bottom=.15,top=.88,wspace=.07)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white')
plt.close(fig)
