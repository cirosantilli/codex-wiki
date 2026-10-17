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

fig,axs=plt.subplots(3,1,figsize=(12,9))
ax=axs[0]
carbonyl(ax,(1.1,0),((-.1,0),r'$R^1$'),((2.4,0),'OEt'))
atom(ax,(-.2,1.2),r'$R-MgBr$');curly(ax,(.0,1),(1.0,.15),rad=.1);curly(ax,(1.17,.65),(1.15,1.15),rad=-.7)
flow(ax,(2.9,.4),(3.7,.4));atom(ax,(5,.4),r'$R^1C(O^-)(OEt)R$')
flow(ax,(6.5,.4),(7.2,.4),'−EtO⁻');atom(ax,(8.3,.4),r'$R^1COR$')
flow(ax,(9.3,.4),(10.3,.4),'+R, then H⁺');atom(ax,(11.4,.4),r'$R^1C(OH)R_2$')
finish(ax,(-1,13),(-.9,2.1),'Ester: ketone appears before quench and is attacked again')
ax=axs[1]
carbonyl(ax,(1.1,0),((-.1,0),'Me'),((2.4,0),'OAc'))
atom(ax,(-.2,1.2),r'$nBu-MgBr$');curly(ax,(.1,1),(1.0,.15),rad=.1);curly(ax,(1.17,.65),(1.15,1.15),rad=-.7)
flow(ax,(3,.4),(3.8,.4),'cold')
carbonyl(ax,(5.0,0),((3.7,0),'Me'),((6.3,0),'OAc'),oxy=r'$O^-MgBr^+$',tetra=True,down=((5,-.9),'nBu'))
ax.plot([5.1,6.3],[.9,.15],ls=':',color=GREEN)
flow(ax,(7,.4),(8.2,.4),'aqueous work-up');atom(ax,(10,.4),r'$MeC(=O)nBu$')
finish(ax,(-1,13),(-1.4,2.0),'Anhydride: persistent magnesium-bound addition complex delays ketone release')
ax=axs[2]
atom(ax,(.1,.4),'nBu–MgBr');atom(ax,(2.6,.4),r'$Ph-C\equiv N$');curly(ax,(1,.55),(2.65,.55),rad=-.6)
flow(ax,(4,.4),(4.9,.4));atom(ax,(6.2,.4),r'$PhC(nBu)=N^-MgBr^+$')
flow(ax,(7.9,.4),(9,.4),'H⁺, water');atom(ax,(10.5,.4),r'$PhC(=O)nBu$')
txt(ax,6,-.8,'Ketimine salt → iminium → carbinolamine → ketone + ammonium',11)
finish(ax,(-1,13),(-1.4,2),'Nitrile: nitrogen-anionic intermediate; ketone is generated during hydrolysis')
fig.tight_layout()

save(fig, 'paper-1-grignard-ketones.png')
