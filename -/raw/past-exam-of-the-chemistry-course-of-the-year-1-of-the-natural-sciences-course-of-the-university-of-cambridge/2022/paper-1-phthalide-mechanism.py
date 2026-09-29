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

fig,axs=plt.subplots(1,2,figsize=(12,5))
for i,ax in enumerate(axs):
    pts=benzene(ax)
    top=pts[0];bottom=pts[5];u=(2,1);v=(2,-1)
    bond(ax,top,u);bond(ax,bottom,v)
    bond(ax,u,(2,2));atom(ax,(2,2),'Me');bond(ax,u,(3.05,1.5));atom(ax,(3.05,1.5),'Me')
    bond(ax,v,(2,-2),2);atom(ax,(2,-2),'O')
    if i==0:
        bond(ax,u,(3.3,.3));atom(ax,(3.3,.3),r'$O^-$')
        bond(ax,v,(3.3,-1));atom(ax,(3.3,-1),'OMe')
        curly(ax,(3.2,.15),(2.12,-.85),rad=-.5);curly(ax,(2.07,-1.4),(2.05,-1.9),rad=.6)
        txt(ax,1,-2.8,'After two Me additions to one ester; magnesium omitted',10)
        title='Ortho alkoxide attacks the remaining ester'
    else:
        o=(2.9,0);bond(ax,u,o);bond(ax,o,v);atom(ax,o,'O')
        txt(ax,1,-2.8,'3,3-Dimethylphthalide; five-membered lactone',11,BLUE)
        title='Collapse expels methoxide; work-up completes trapping'
    finish(ax,(-1.8,4),(-3.2,2.8),title)
fig.tight_layout()

save(fig, 'paper-1-phthalide-mechanism.png')
