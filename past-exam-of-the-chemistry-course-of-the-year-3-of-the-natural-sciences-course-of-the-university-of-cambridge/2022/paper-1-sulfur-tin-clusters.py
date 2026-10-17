"""Original solution schematic; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Writes its own PNG basename to the current working directory.
"""
from pathlib import Path
import sys
for candidate in Path(__file__).resolve().parents:
    if (candidate / 'tools' / 'chemistry_diagram.py').exists():
        sys.path.insert(0, str(candidate))
        break
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
from tools.chemistry_diagram import atom, bond, ring, wedge, curly, flow, finish, save, BLUE, ORANGE, GREEN

def txt(ax,x,y,s,size=11,color='0.15',ha='center'):
    ax.text(x,y,s,ha=ha,va='center',fontsize=size,color=color)
def couple(ax,a,b,label,rad=.3,offset=(0,0)):
    ax.add_patch(FancyArrowPatch(a,b,connectionstyle=f'arc3,rad={rad}',arrowstyle='<->',mutation_scale=10,color=BLUE,lw=1.3))
    m=(np.asarray(a)+np.asarray(b))/2+np.asarray(offset)
    txt(ax,*m,label,10,BLUE)
def benzene(ax,c=(0,0),scale=1):
    t=np.deg2rad([30,90,150,210,270,330]);pts=np.column_stack([np.cos(t),np.sin(t)])*scale+np.asarray(c)
    ring(ax,pts,{0:2,2:2,4:2});return pts
def carbonyl(ax,c,left,right,oxy='O',tetra=False,down=None):
    x,y=c;o=(x,y+1);bond(ax,c,o,1 if tetra else 2);atom(ax,o,oxy)
    for q,label in [(left[0],left[1]),(right[0],right[1])]:bond(ax,c,q);atom(ax,q,label)
    if down:bond(ax,c,down[0]);atom(ax,down[0],down[1])
    return o

def box(ax,x,y,s,w=2.6,h=.8,color=BLUE,size=11):
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.08',fc='white',ec=color,lw=1.2))
    if '$' not in s and len(s)>29:
        import textwrap
        s='\n'.join(textwrap.wrap(s,width=29))
    elif '$' in s and len(s)>35:
        size=min(size,8.5)
    txt(ax,x,y,s,size,color)
def route(rows,title,figsize=(12,6)):
    fig,ax=plt.subplots(figsize=figsize)
    for i,row in enumerate(rows):
        y=-i*1.7
        for j,entry in enumerate(row):
            x=j*4
            if j%2==0:box(ax,x,y,entry,w=3.35,h=1.05,size=11)
            else:flow(ax,(x-1.7,y),(x+1.7,y));txt(ax,x,y+.4,entry,10)
    finish(ax,(-2,18),(-len(rows)*1.7+.3,1.4),title)
    fig.tight_layout();return fig

fig,axs=plt.subplots(1,2,figsize=(11,5))
ax=axs[0];pts=[(-1,-1),(1,-1),(1,1),(-1,1)];ring(ax,pts)
for p in pts:atom(ax,p,'S')
ax.add_patch(Circle((0,0),.58,fill=False,ec=BLUE,lw=1.4));txt(ax,0,0,'6π e⁻',11,BLUE)
txt(ax,0,-1.75,'8 σ e⁻ + 8 lone-pair e⁻ + 6 π e⁻',11)
finish(ax,(-2.5,2.5),(-2.5,2.5),'S₄²⁺: square-planar ring, 22 valence electrons')
ax=axs[1];p=np.array([[-1,-.3],[1,-.3],[0,.6],[0,1.65],[0,-1.65]])
for i,j in [(0,1),(1,2),(2,0)]+[(i,j) for i in [3,4] for j in [0,1,2]]:bond(ax,p[i],p[j],style='dashed' if (i,j)==(2,0) else 'solid')
for v in p:atom(ax,v,'Sn')
txt(ax,0,-2.1,'Five lone pairs removed: 22 − 10 = 12 skeletal e⁻',10,BLUE)
finish(ax,(-2.5,2.5),(-2.7,2.5),'Sn₅²⁻: trigonal bipyramid, six skeletal pairs')
fig.tight_layout()

save(fig,'paper-1-sulfur-tin-clusters.png')
