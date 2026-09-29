#!/usr/bin/env python3
"""Python 3.14; matplotlib/numpy from the repository pyproject.toml. Output in CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
fig,axs=plt.subplots(1,2,figsize=(11,5.3),facecolor='white',gridspec_kw={'width_ratios':[1,1.35]})
ax=axs[0];pos={'r':(0,0),'a':(-1,-1),'b':(1,-1),'c':(-1.6,-2),'1':(-.35,-2),'2':(-2,-3),'3':(-1.2,-3),'4':(.6,-2),'5':(1.4,-2)}
edges=[('r','a'),('r','b'),('a','c'),('a','1'),('c','2'),('c','3'),('b','4'),('b','5')]
blue={'a','b','2','3'}
for a,b in edges:ax.plot(*zip(pos[a],pos[b]),color='#303030',lw=1.7,zorder=1)
for name,(x,y) in pos.items():
 ax.scatter([x],[y],s=600,color='#c6e5f5' if name in blue else 'white',edgecolor='#222222',zorder=3)
 ax.text(x,y,name,ha='center',va='center',fontsize=12,zorder=4)
ax.set_title('Plane tree: 9 vertices, 8 edges',fontsize=13);ax.set_xlim(-2.55,2);ax.set_ylim(-3.5,.6);ax.set_aspect('equal');ax.axis('off')
ax=axs[1]
# Radial loops have a common endpoint O. Nested angular sectors encode the rooted tree.
loops=[('a',.10,3.04,4.3),('b',-3.04,-.10,4.3),('c',.27,1.80,3.0),('1',1.95,2.80,1.7),('2',.45,.98,1.1),('3',1.14,1.67,1.1),('4',-2.80,-1.85,2.0),('5',-1.55,-.35,2.4)]
for name,lo,hi,rad in loops:
 th=np.linspace(lo,hi,700);rr=rad*np.sin(np.pi*(th-lo)/(hi-lo));xy=np.c_[rr*np.cos(th),rr*np.sin(th)]
 ax.add_patch(Polygon(xy,closed=True,facecolor='#c6e5f5' if name in blue else 'white',edgecolor='#222222',lw=1.1))
 # Put the region label near its farthest point, leaving child sectors closer to O.
 mid=(lo+hi)/2;fac=.87 if name in ['a','b','c'] else .70
 ax.text(fac*rad*np.cos(mid),fac*rad*np.sin(mid),name,ha='center',va='center',fontsize=11)
ax.scatter([0],[0],s=45,color='#111111',zorder=10);ax.annotate('O',(0,0),xytext=(12,-6),textcoords='offset points',fontsize=11)
ax.text(-3.0,4.25,'r (outer face)',fontsize=10)
ax.set_title('Plane dual: 1 vertex, 8 loops, 9 faces',fontsize=13);ax.set_xlim(-3.2,3.2);ax.set_ylim(-4.7,4.7);ax.set_aspect('equal');ax.axis('off')
fig.suptitle('Two face colours follow the bipartition of the original tree',fontsize=14,y=.98)
fig.tight_layout(rect=(0,0,1,.94));fig.savefig(Path.cwd()/'2007-tree-and-dual.png',dpi=160,facecolor='white');plt.close(fig)
