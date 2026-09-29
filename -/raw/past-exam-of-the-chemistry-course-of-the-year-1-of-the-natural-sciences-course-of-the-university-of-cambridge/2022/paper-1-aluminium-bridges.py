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

fig,axs=plt.subplots(1,2,figsize=(11,5))
for ax,bridge,terminal in [(axs[0],'Cl','Cl'),(axs[1],'Me','Me')]:
    a=(0,0);b=(3,0);up=(1.5,.9);dn=(1.5,-.9)
    for p in [up,dn]:bond(ax,a,p);bond(ax,p,b);atom(ax,p,bridge)
    for c,x in [(a,-1),(b,4)]:
        atom(ax,c,'Al')
        for y in [-1,1]:bond(ax,c,(x,y));atom(ax,(x,y),terminal)
    if bridge=='Cl':
        txt(ax,1.5,2.0,'Lone-pair donation; full pair per added contact',10,BLUE)
        txt(ax,1.5,-2.0,'Formal single bonds; bridging contacts weaker',10)
        title='Chloride bridges: localized donor–acceptor model'
    else:
        txt(ax,1.5,2.0,'One pair shared over each Al–C–Al bridge',10,BLUE)
        txt(ax,1.5,-2.0,'Terminal order 1; each bridge contact formally ½',10)
        couple(ax,(.2,.1),(2.8,.1),'shared 2e',rad=-.8,offset=(0,1.45))
        title='Methyl bridges: three centres, two electrons'
    finish(ax,(-2,5),(-2.6,2.6),title)
fig.tight_layout()

save(fig, 'paper-1-aluminium-bridges.png')
