"""Render original genotype DAG and triangulated moral graph; output to cwd."""
from pathlib import Path
from itertools import combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

parents = {'A':('U','V'),'C':('U','V'),'B':('P','Q'),'D':('R','S'),'F':('A','B'),'M':('C','D'),'X':('F','M'),'Y':('F','M')}
pos = {'P':(0.3,3),'Q':(1.1,3),'U':(2.3,3),'V':(3.1,3),'R':(4.3,3),'S':(5.1,3),'B':(0.7,2),'A':(2.1,2),'C':(3.3,2),'D':(4.7,2),'F':(1.4,1),'M':(4,1),'X':(2.1,0),'Y':(3.3,0)}
fig, axes=plt.subplots(1,2,figsize=(12.5,6),dpi=120,facecolor='white')
for ax in axes:
    ax.set(xlim=(-0.1,5.5),ylim=(-0.65,3.65),aspect='equal');ax.axis('off')
    for node,(x,y) in pos.items():
        ax.add_patch(Circle((x,y),.17,facecolor='white',edgecolor='#18394b',lw=1.8,zorder=3))
        ax.text(x,y,node,ha='center',va='center',fontsize=13,zorder=4)
for child,ps in parents.items():
    for parent in ps:
        axes[0].add_patch(FancyArrowPatch(pos[parent],pos[child],arrowstyle='-|>',mutation_scale=13,shrinkA=13,shrinkB=13,lw=1.2,color='#365d72',zorder=1))
edges={tuple(sorted((c,p))) for c,ps in parents.items() for p in ps}|{tuple(sorted(ps)) for ps in parents.values()}
for u,v in sorted(edges):
    axes[1].plot([pos[u][0],pos[v][0]],[pos[u][1],pos[v][1]],color='#59717d',lw=1.2,zorder=1)
for u,v in [('A','C'),('A','M')]:
    axes[1].plot([pos[u][0],pos[v][0]],[pos[u][1],pos[v][1]],color='#bf4c26',lw=2.2,ls='--',zorder=2)
axes[0].set_title('Ancestry DAG: each node is a genotype',fontsize=13,pad=16)
axes[1].set_title('Moral graph with fill edges AC and AM',fontsize=13,pad=16)
axes[0].text(2.7,-.55,'Six unrelated great-grandparents; F and M are first cousins',ha='center',fontsize=10)
axes[1].text(2.7,-.55,'Dashed orange edges triangulate the graph; they are not ancestry',ha='center',fontsize=10)
fig.subplots_adjust(left=.025,right=.985,bottom=.08,top=.91,wspace=.13)
fig.savefig(Path.cwd()/'paper-39-pedigree.png',facecolor='white',transparent=False)
plt.close(fig)
