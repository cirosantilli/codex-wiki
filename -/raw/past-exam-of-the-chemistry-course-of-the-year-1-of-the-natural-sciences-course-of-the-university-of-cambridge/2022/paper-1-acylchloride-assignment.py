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

fig,axs=plt.subplots(2,1,figsize=(8.4,5.8))
for i,ax in enumerate(axs):
    c=(1.8,0);co=(3.5,0)
    for q,s in [((.2,1),r'$CH_3$'),((.2,-1),r'$CH_3$'),(co,'C')]:bond(ax,c,q);atom(ax,q,s)
    atom(ax,c,'CH');bond(ax,co,(3.5,1.2),2);atom(ax,(3.5,1.2),'O');bond(ax,co,(5.1,0));atom(ax,(5.1,0),'Cl')
    if i==0:
        for x,y,s in [(.1,1.4,'18.9'),(.1,-1.4,'18.9'),(1.8,-.4,'46.3'),(3.5,-.4,'178.1')]:txt(ax,x,y,s,11,BLUE)
        title='Carbon assignment (two equivalent methyls)'
    else:
        txt(ax,-.15,1.6,'1.308, 6H total, d',10,BLUE);txt(ax,2.25,-1.25,'2.976, 1H, septet',10,BLUE)
        couple(ax,(.35,.95),(1.7,.1),'6.9 Hz',rad=-.7,offset=(.4,.65));couple(ax,(.35,-.95),(1.7,-.1),'6.9 Hz',rad=.7,offset=(-.6,-.2))
        title='Separate proton assignment'
    finish(ax,(-1.5,5.8),(-1.8,2.0),title)
fig.tight_layout()

save(fig, 'paper-1-acylchloride-assignment.png')
