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

fig,axs=plt.subplots(2,1,figsize=(12,6))
ax=axs[0]
atom(ax,(.2,0),r'$BrCH_2C(Me)_2OAc$');flow(ax,(2.2,0),(3.1,0),'OH⁻')
atom(ax,(4.5,0),r'$BrCH_2C(Me)_2O^-$')
flow(ax,(6.3,0),(7.2,0),'intramolecular attack')
a=(8.1,0);b=(9.7,0);o=(8.9,1.1);ring(ax,[a,b,o]);atom(ax,a,r'$CH_2$');atom(ax,b,r'$CMe_2$');atom(ax,o,'O')
txt(ax,9,-.75,'Primary C–Br substitution; Br⁻ leaves',10)
finish(ax,(-1.5,11.7),(-1.3,2),'1. Acyl hydrolysis gives bromohydrin; alkoxide cyclizes to epoxide')
ax=axs[1]
a=(.2,0);b=(1.8,0);o=(1,1.1);ring(ax,[a,b,o]);atom(ax,a,r'$CH_2$');atom(ax,b,r'$CMe_2$');atom(ax,o,r'$OH^+$')
atom(ax,(3.3,.8),r'$Br^-$');curly(ax,(2.95,.7),(1.97,.1),rad=.25);curly(ax,(1.5,.65),(1.13,1.13),rad=-.55)
flow(ax,(3.7,0),(4.5,0));atom(ax,(6.1,0),r'$HOCH_2C(Br)(Me)_2$')
flow(ax,(7.7,0),(8.6,0),'AcCl, Et₃N');atom(ax,(10.25,0),r'$AcOCH_2C(Br)(Me)_2$')
finish(ax,(-1.5,12),(-1.3,2.1),'2. Acidic opening at tertiary carbon; 3. primary alcohol reacylation')
fig.tight_layout()

save(fig, 'paper-1-epoxide-regioselectivity.png')
