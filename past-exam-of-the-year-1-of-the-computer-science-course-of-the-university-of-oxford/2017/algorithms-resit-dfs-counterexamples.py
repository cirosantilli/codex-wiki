"""Original directed-graph counterexamples; save PNG in the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch

fig,axes=plt.subplots(1,2,figsize=(11,4.5),dpi=100)
for ax in axes:ax.set(xlim=(-1.8,1.8),ylim=(-1.7,1.8));ax.axis('off');ax.set_aspect('equal')
def node(ax,xy,name,times,color='#e1edf7'):
 ax.add_patch(Circle(xy,.2,facecolor=color,edgecolor='#244a66',lw=1.5,zorder=3))
 ax.text(*xy,name,ha='center',va='center',fontsize=17,zorder=4)
 ax.text(xy[0]+.8 if name=='x' else xy[0],xy[1]+.03 if name=='x' else xy[1]-.4,times,ha='center',va='center',fontsize=11)
def edge(ax,p,q,rad=0,color='#345c77',style='-'):
 ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=17,shrinkA=14,shrinkB=14,connectionstyle=f'arc3,rad={rad}',lw=1.7,color=color,linestyle=style,zorder=2))
ax=axes[0];x=(0,1);u=(-1,-.65);v=(1,-.65)
edge(ax,x,u,.12);edge(ax,u,x,.12,color='#b1602d');edge(ax,x,v)
node(ax,x,'x','d=1, f=6');node(ax,u,'u','d=2, f=3');node(ax,v,'v','d=4, f=5')
ax.set_title('Path u → x → v exists; v is not below u',fontsize=12,pad=12)
ax.text(0,-1.4,'Start at x; inspect its edge to u before v.',ha='center',fontsize=10)
ax=axes[1];a=(-1.15,.15);u=(0,.15);c=(1.15,.15)
edge(ax,u,a,color='#777',style='--');edge(ax,c,u,color='#777',style='--')
node(ax,a,'a','d=1, f=2');node(ax,u,'u','d=3, f=4');node(ax,c,'c','d=5, f=6')
ax.set_title('u has two incident edges, yet its DFS tree is a singleton',fontsize=11,pad=12)
ax.text(0,1.15,'Outer root order: a, u, c',ha='center',fontsize=11)
ax.text(0,-1.4,'Both arrows reach vertices already finished.',ha='center',fontsize=10)
fig.subplots_adjust(left=.035,right=.965,bottom=.07,top=.87,wspace=.25)
fig.savefig(Path.cwd()/'algorithms-resit-dfs-counterexamples.png',facecolor='white')
