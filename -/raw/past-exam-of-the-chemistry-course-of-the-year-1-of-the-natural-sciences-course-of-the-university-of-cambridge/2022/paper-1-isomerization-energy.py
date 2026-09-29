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

fig,ax=plt.subplots(figsize=(8,5))
x=np.linspace(0,1,250);E=9*np.sin(np.pi*x)**2-2.23*(3*x*x-2*x*x*x)
ax.plot(x,E,color=BLUE,lw=2);i=E.argmax();xt=x[i];Et=E[i]
ax.hlines([0,-2.23,Et],[0,.66,.1],[.4,1,.9],ls='--',colors='0.65',lw=.8)
ax.annotate('',(.22,Et),(.22,0),arrowprops={'arrowstyle':'<->','color':ORANGE});ax.text(.24,Et/2,r'$E_{a,1}$',color=ORANGE)
ax.annotate('',(.82,Et),(.82,-2.23),arrowprops={'arrowstyle':'<->','color':ORANGE});ax.text(.84,(Et-2.23)/2,r'$E_{a,-1}$',color=ORANGE)
ax.text(.02,-.6,'cis');ax.text(.88,-2.9,'trans');ax.text(.4,-3.8,'Trans lower by 2.23 kJ mol⁻¹',color=BLUE)
ax.set(xlabel='Reaction coordinate',ylabel='Relative energy (kJ mol⁻¹)',ylim=(-4.7,10))
ax.set_xticks([]);ax.set_yticks([0,-2.23]);ax.set_title('Barrier height illustrative; only the difference is specified')
ax.spines[['top','right']].set_visible(False);fig.tight_layout()

save(fig, 'paper-1-isomerization-energy.png')
