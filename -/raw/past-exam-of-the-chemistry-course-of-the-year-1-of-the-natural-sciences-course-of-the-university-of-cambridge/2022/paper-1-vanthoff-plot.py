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

fig,ax=plt.subplots(figsize=(7.4,4.8))
x=np.linspace(0,3.5,200);a=-1;b=2
ax.plot(x,a+b*x,color=BLUE,lw=2)
ax.axhline(0,color='0.4',lw=.8);ax.axvline(0,color='0.4',lw=.8)
ax.scatter([0],[a],color=ORANGE,zorder=4)
ax.annotate(r'Intercept $=\Delta_rS^\circ/R$',(0,a),(.7,-1.6),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.annotate(r'Slope $=-\Delta_rH^\circ/R$',(2,3),(1.7,5.4),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.plot([1,2],[1,1],ls='--',color='0.5');ax.plot([2,2],[1,3],ls='--',color='0.5')
ax.set(xlabel=r'$1/T$ (arbitrary horizontal scale)',ylabel=r'$\ln K$',xlim=(-.3,3.7),ylim=(-2.2,7))
ax.set_xticks([0]);ax.set_yticks([0]);ax.set_title('Schematic exothermic case: positive slope')
ax.spines[['top','right']].set_visible(False);fig.tight_layout()

save(fig, 'paper-1-vanthoff-plot.png')
