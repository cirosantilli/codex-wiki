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

fig=plt.figure(figsize=(11,5));phi=(1+np.sqrt(5))/2
v=np.array([(0,a,b*phi) for a in [-1,1] for b in [-1,1]]+[(a,b*phi,0) for a in [-1,1] for b in [-1,1]]+[(a*phi,0,b) for a in [-1,1] for b in [-1,1]])
edges=[(i,j) for i in range(12) for j in range(i) if np.isclose(np.linalg.norm(v[i]-v[j]),2)]
co=1
nei=[j for j in range(12) if j!=co and (max(co,j),min(co,j)) in edges]
ca,cb=next((a,b) for a in nei for b in nei if a<b and (max(a,b),min(a,b)) in edges)
for index,title,metal in [(121,'B₁₂H₁₂²⁻',False),(122,'CpCoC₂B₉H₁₁',True)]:
 ax=fig.add_subplot(index,projection='3d')
 for i,j in edges:ax.plot(*np.stack([v[i],v[j]]).T,color='0.55',lw=.8)
 for i,p in enumerate(v):
  color=ORANGE if metal and i==co else ('0.1' if metal and i in [ca,cb] else BLUE)
  ax.scatter(*p,s=90,c=color);ax.text(*(p*1.12),'Co' if metal and i==co else ('C' if metal and i in [ca,cb] else 'B'),fontsize=9)
 ax.view_init(16,25);ax.set_axis_off();ax.set_title(title+'\n12 vertices, 26 skeletal electrons',fontsize=12)
fig.text(.5,.03,'Terminal H and external Cp omitted; two adjacent C vertices are black.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.06,1,1))

save(fig,'paper-1-closo-icosahedra.png')
