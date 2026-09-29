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

fig=plt.figure(figsize=(11,5));ax=fig.add_subplot(121,projection='3d')
p=np.vstack([np.eye(3),-np.eye(3)])
for i in range(6):
    for j in range(i):
        if np.linalg.norm(p[i]-p[j])<1.6:ax.plot(*np.stack([p[i],p[j]]).T,color=BLUE,lw=1.3)
ax.scatter(*p.T,s=95,color=BLUE)
cl=np.array([[a,b,c] for a in [-1,1] for b in [-1,1] for c in [-1,1]])*.65
ax.scatter(*cl.T,s=65,color=ORANGE)
ax.text2D(.1,.02,'Blue: Mo₆ octahedron; orange: eight face-capping Cl',transform=ax.transAxes,fontsize=10)
ax.view_init(elev=16,azim=24);ax.set_axis_off();ax.set_title('MoCl₂: Mo₆Cl₈ inner cluster\nOuter terminal/shared chlorides omitted',fontsize=12)
ax=fig.add_subplot(122)
p=np.array([[0,0],[1,0],[1.5,.866],[1,1.732],[0,1.732],[-.5,.866]])
ring(ax,p)
for i,j in [(0,1),(3,4)]:bond(ax,p[i],p[j],lw=4,color=BLUE)
for i,q in [(2,(2.5,.866)),(5,(-1.5,.866))]:bond(ax,p[i],q,lw=4,color=BLUE);atom(ax,q,'Mo')
for q in p:atom(ax,q,'Mo')
txt(ax,.5,-.75,'Aligned short Mo–Mo pairs (thick blue)',10,BLUE)
finish(ax,(-2.1,3.1),(-1.3,2.8),'α-MoCl₃: paired metal sites in an extended layer')
fig.tight_layout()

save(fig,'paper-1-molybdenum-chlorides.png')
