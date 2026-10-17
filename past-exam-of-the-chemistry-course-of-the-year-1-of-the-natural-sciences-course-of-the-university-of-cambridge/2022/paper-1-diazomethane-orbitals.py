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
ax=axs[0]
txt(ax,2.3,3.3,r'$H_2C=N^+=N^-\ \leftrightarrow\ H_2C^--N^+\equiv N$',15)
for p,s in [((.7,1.7),'C'),((2.3,1.7),'N'),((3.9,1.7),'N')]:atom(ax,p,s)
bond(ax,(.7,1.7),(2.3,1.7));bond(ax,(2.3,1.7),(3.9,1.7))
for q in [(-.15,2.5),(-.15,.9)]:bond(ax,(.7,1.7),q);atom(ax,q,'H')
for x in [.7,2.3,3.9]:
    ax.add_patch(Circle((x,2.12),.20,fc=BLUE,alpha=.7));ax.add_patch(Circle((x,1.28),.20,fc=ORANGE,alpha=.7))
txt(ax,2.4,.3,'Perpendicular C–N–N system: 4 electrons',11,BLUE)
txt(ax,2.4,-.3,'Orthogonal N–N π bond: 2 electrons',11)
txt(ax,2.4,-.9,'Four σ bonds: 8 electrons; axial lone pair: 2',11)
finish(ax,(-.7,5),(-1.5,4),'Framework and electron accounting')
ax=axs[1]
for y,l,n in [(-1.4,r'$\alpha+\sqrt{2}\beta$',2),(.3,r'$\alpha$ (frontier)',2),(2,r'$\alpha-\sqrt{2}\beta$',0)]:
    ax.plot([0,1.7],[y,y],lw=2,color=BLUE);txt(ax,2.9,y,l,12)
    if n:txt(ax,.85,y+.25,r'$\uparrow\downarrow$',15,BLUE)
ax.annotate('',(-.4,3),(-.4,-2),arrowprops={'arrowstyle':'->'});txt(ax,-.1,3.2,'Energy',10)
txt(ax,1.9,-2.8,'Equal-site model: β < 0; real C/N energies differ',10)
finish(ax,(-1,5),(-3.3,3.8),'Three-site, four-electron π model')
fig.tight_layout()

save(fig, 'paper-1-diazomethane-orbitals.png')
