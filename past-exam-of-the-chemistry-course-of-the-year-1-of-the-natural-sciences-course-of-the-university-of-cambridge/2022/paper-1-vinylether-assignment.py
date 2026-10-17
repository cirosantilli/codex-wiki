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

fig,axs=plt.subplots(2,1,figsize=(11,5.6))
for i,ax in enumerate(axs):
    a=(.6,0);b=(2.2,0);o=(3.4,-.7);d=(4.7,0);e=(6.3,0)
    bond(ax,a,b,2);bond(ax,b,o);bond(ax,o,d);bond(ax,d,e);bond(ax,e,(7.6,-.7))
    atom(ax,o,'O');atom(ax,d,r'$CH_2$');atom(ax,e,r'$CH_2$');atom(ax,(7.6,-.7),'Cl')
    for p,s in [(a,'C'),(b,'CH')]:atom(ax,p,s)
    for q,s in [((-.25,.8),'H'),((-.25,-.8),'H')]:bond(ax,a,q);atom(ax,q,s)
    if i==0:
        for x,y,s in [(.7,-1.3,'87.4'),(2.2,.65,'151.1'),(4.7,-.5,'67.8'),(6.3,-.5,'41.9')]:txt(ax,x,y,s,11,BLUE)
        title='Carbon assignment (ppm)'
    else:
        txt(ax,2.2,1.3,'a: 6.480, 1H, dd',10,BLUE)
        txt(ax,-1.25,1.4,'c: 4.072\n1H, dd',10,BLUE);txt(ax,-1.25,-1.35,'b: 4.220\n1H, dd',10,BLUE)
        txt(ax,4.5,1.3,'d: 3.948, 2H, t',10,BLUE);txt(ax,6.6,1.3,'e: 3.708, 2H, t',10,BLUE)
        couple(ax,(-.05,-.75),(2.05,.15),'trans ~14.3 Hz',rad=.48,offset=(.9,-1.05))
        couple(ax,(-.05,.8),(2.05,.15),'cis ~7 Hz',rad=-.35,offset=(0,.48))
        couple(ax,(-.5,.7),(-.5,-.7),'geminal\n~2–3 Hz',rad=.8,offset=(-.9,0))
        couple(ax,(4.8,.15),(6.2,.15),'5.7 Hz',rad=-.6,offset=(0,.65))
        title='Separate proton assignment (coupling magnitudes approximate)'
    finish(ax,(-2.2,8.0),(-1.9,1.9),title)
fig.tight_layout()

save(fig, 'paper-1-vinylether-assignment.png')
