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

fig,axs=plt.subplots(2,1,figsize=(11,5.8))
ax=axs[0]
for p,s in [((.5,0),r'$H_2C^-$'),((2.1,0),r'$N^+$'),((3.5,0),'N'),((.5,1.6),'H'),((2.1,1.6),'OAc')]:atom(ax,p,s)
bond(ax,(.5,0),(2.1,0));bond(ax,(2.1,0),(3.5,0),2);ax.plot([2.1,3.5],[-.13,-.13],color='0.2',lw=1.5)
bond(ax,(.5,1.6),(2.1,1.6));curly(ax,(.25,.2),(.5,1.45),rad=-.35);curly(ax,(1.3,1.6),(2,1.65),rad=-.5)
flow(ax,(4.1,.5),(5.1,.5))
atom(ax,(6.1,.5),r'$H_3C-N^+\equiv N$');atom(ax,(8.7,.5),r'$AcO^-$')
finish(ax,(-.6,10),(-.7,2.5),'1. Carbon protonation and acid O–H cleavage')
ax=axs[1]
for p,s in [((.6,0),r'$AcO^-$'),((2.8,0),r'$CH_3$'),((4.6,0),r'$N^+\equiv N$')]:atom(ax,p,s)
bond(ax,(2.8,0),(4.1,0));curly(ax,(1.0,.1),(2.65,.1),rad=-.5);curly(ax,(3.55,0),(4.5,.12),rad=-.55)
flow(ax,(5.4,0),(6.3,0));atom(ax,(8,0),r'$AcOCH_3+N_2$')
finish(ax,(-.6,10),(-1.0,1.9),'2. Acetate attacks methyl carbon; the C–N pair leaves with nitrogen')
fig.tight_layout()

save(fig, 'paper-1-diazo-methylation.png')
