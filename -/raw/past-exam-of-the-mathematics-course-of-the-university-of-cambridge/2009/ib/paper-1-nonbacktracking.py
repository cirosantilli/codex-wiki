"""Original directed-edge type chain. Python 3.14, Matplotlib 3.10.7.
Writes paper-1-nonbacktracking.png in caller CWD; preserves MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
fig,ax=plt.subplots(figsize=(8.5,4.8),dpi=120,facecolor='white');ax.set_facecolor('white')
pos={'OO':(0,2),'OI':(3,2),'IO':(0,0),'II':(3,0),'T':(5.6,1)}
for label,(x,y) in pos.items():
 ax.add_patch(FancyBboxPatch((x-.48,y-.3),.96,.6,boxstyle='round,pad=.05',fc='#edf4fc' if label!='T' else '#e7f3e5',ec='#345b80',lw=1.5,zorder=3))
 ax.text(x,y,label if label!='T' else 'Hit',ha='center',va='center',fontsize=14,zorder=4)
def edge(a,b,label,rad=0):
 x,y=pos[a];u,v=pos[b]
 dx,dy=u-x,v-y
 ta=min(.53/abs(dx) if dx else float('inf'),.35/abs(dy) if dy else float('inf'))
 tb=ta
 start=(x+ta*dx,y+ta*dy);end=(u-tb*dx,v-tb*dy)
 ax.add_patch(FancyArrowPatch(start,end,arrowstyle='->',mutation_scale=14,lw=1.6,color='#345b80',shrinkA=4,shrinkB=4,connectionstyle=f'arc3,rad={rad}'))
 dx,dy=u-x,v-y;ax.text((x+u)/2-rad*dy*.65,(y+v)/2+rad*dx*.65+.11,label,ha='center',va='center',fontsize=12,bbox=dict(fc='white',ec='none',pad=1.5))
edge('OO','OI',r'$1/2$');edge('OI','II',r'$2/3$');edge('IO','OO',r'$1$');edge('II','IO',r'$1/3$');edge('OI','T',r'$1/3$');edge('II','T',r'$1/3$')
for key,label,dy in [('OO',r'$1/2$',1),('II',r'$1/3$',-1)]:
 x,y=pos[key]
 ax.add_patch(FancyArrowPatch((x-.3,y+.35*dy),(x+.3,y+.35*dy),connectionstyle=f'arc3,rad={-1.5*dy}',arrowstyle='->',mutation_scale=14,color='#345b80',lw=1.6))
 ax.text(x,y+.85*dy,label,ha='center',fontsize=12)
ax.text(2.7,-1.18,'O = outer vertex; I = inner vertex\nThe initial move chooses OO with probability 2/3 and OI with probability 1/3.',ha='center',fontsize=10,color='#333333')
ax.set_xlim(-1,6.4);ax.set_ylim(-1.55,3.25);ax.axis('off');ax.set_title('Memory of one edge makes the walk Markov',fontsize=14,pad=10)
fig.tight_layout();fig.savefig('paper-1-nonbacktracking.png',facecolor='white',transparent=False);plt.close(fig)
