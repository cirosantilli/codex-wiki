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

fig,ax=plt.subplots(figsize=(12,5.7))
box(ax,0,2.5,'Ln(s) + 3H⁺(aq)',w=3.4)
box(ax,11,2.5,'Ln³⁺(aq) + 3/2 H₂(g)',w=3.8)
box(ax,0,0,'Ln(g) + 3H⁺(aq)',w=3.4)
box(ax,5.5,0,'Ln³⁺(g) + 3H⁺(aq)\n+ 3e⁻(g)',w=3.8,h=1.2)
box(ax,11,0,'Ln³⁺(aq) + 3H⁺(aq)\n+ 3e⁻(g)',w=3.8,h=1.2)
flow(ax,(1.85,2.5),(8.9,2.5),'Overall acid-formation enthalpy')
flow(ax,(0,2),(0,.55));txt(ax,-1.4,1.3,'Atomization\npositive',10)
flow(ax,(1.85,0),(3.3,0));txt(ax,2.65,.6,'I₁+I₂+I₃\npositive',10)
flow(ax,(7.65,0),(8.9,0));txt(ax,8.3,.6,'Hydration\nnegative',10)
flow(ax,(11,.7),(11,2));txt(ax,12.35,1.3,'C_H\ncommon leg',10)
txt(ax,5.5,-1.65,'Large positive ionization terms and large negative hydration nearly cancel.',11,BLUE)
finish(ax,(-2.1,13.7),(-2.2,3.7),'Hess cycle with the electron/hydrogen reference leg retained')
fig.tight_layout()

save(fig,'paper-1-lanthanide-cycle.png')
