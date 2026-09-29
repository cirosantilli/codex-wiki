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

fig,ax=plt.subplots(figsize=(12,5.7))
atom(ax,(.4,1),r'$C_6H_{11}Br$');flow(ax,(1.5,1.25),(3,2.25),'Mg, dry ether');atom(ax,(4.8,2.25),r'$C_6H_{11}MgBr$')
flow(ax,(1.5,.75),(3,-.5),'base, heat');atom(ax,(4.4,-.5),'Cyclohexene');flow(ax,(5.8,-.5),(6.8,-.5),'peracid')
t=np.arange(6)*np.pi/3;pts=np.column_stack([np.cos(t),np.sin(t)])*.7+[8,-.5];ring(ax,pts)
o=(9.0,-.02);bond(ax,pts[0],o);bond(ax,pts[1],o);atom(ax,o,'O')
flow(ax,(6,2.25),(10,2.25),'epoxide, then aqueous H⁺')
# Product is drawn in a fresh orientation; solid OH and dashed Cy show relative anti stereochemistry.
q=np.column_stack([np.cos(t),np.sin(t)])*.85+[11,0];ring(ax,q)
wedge(ax,q[1],(11.8,1.7),True);atom(ax,(11.8,1.7),'OH')
wedge(ax,q[0],(12.7,.05),False);atom(ax,(13.1,.05),'Cy')
txt(ax,11.3,-1.5,'trans-1,2 relationship; racemic pair',11,BLUE)
txt(ax,6.8,-2.2,'Cy = cyclohexyl. Both six-carbon units come from the starting bromide.',11)
finish(ax,(-1.1,14),(-2.7,3.2),'Two-branch carbon-conserving synthesis and anti epoxide opening')
fig.tight_layout()

save(fig, 'paper-1-trans-cyclohexanol-synthesis.png')
