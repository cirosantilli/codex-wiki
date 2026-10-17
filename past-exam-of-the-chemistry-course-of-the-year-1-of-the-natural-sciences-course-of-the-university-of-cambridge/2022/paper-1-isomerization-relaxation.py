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
R=8.3145;K1=np.exp(2230/R/298);f1=K1/(1+K1);f2=2.31/3.31;k=.00104+.00104/2.31
x=np.linspace(0,3000,500);f=f2+(f1-f2)*np.exp(-k*x)
ax.plot([-450,0],[f1,f1],color=BLUE,lw=2);ax.plot(x,f,color=BLUE,lw=2)
ax.axvline(0,color='0.5',ls=':');ax.axhline(f1,color='0.55',ls='--',lw=.8);ax.axhline(f2,color='0.55',ls='--',lw=.8)
th=np.log(2)/k;fm=(f1+f2)/2;ax.scatter([th],[fm],color=ORANGE,zorder=4)
ax.annotate('Half of the displacement\n465 s',(th,fm),(1000,fm+.002),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.text(2200,f1+.0005,r'$[trans]_{eq1}/C_{tot}$',fontsize=11);ax.text(2200,f2+.0005,r'$[trans]_{eq2}/C_{tot}$',fontsize=11)
ax.text(-350,f1-.002,'Jump',fontsize=10)
ax.set(xlabel='Time after temperature jump (s)',ylabel=r'$[trans]/C_{tot}$',xlim=(-450,3200),ylim=(f2-.002,f1+.003))
ax.set_title('Continuous concentration; lower trans fraction after heating')
ax.spines[['top','right']].set_visible(False);fig.tight_layout()

save(fig, 'paper-1-isomerization-relaxation.png')
