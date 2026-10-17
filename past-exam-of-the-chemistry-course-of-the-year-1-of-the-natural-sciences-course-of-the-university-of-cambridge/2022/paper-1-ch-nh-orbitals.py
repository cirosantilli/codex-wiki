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

fig,axs=plt.subplots(1,2,figsize=(11,6),sharey=True)
for ax,label,shift,npi in [(axs[0],'CH',0,1),(axs[1],'NH',-.8,2)]:
    # The relative shifts are schematic, not numerical orbital energies.
    ao=[(-4.5+shift,r'$2s$'),(-.2+shift,r'$2p$')]
    for y,t in ao:
        ax.plot([.1,.9],[y,y],color='0.35');txt(ax,.5,y+.35,t)
    ax.plot([4.1,4.9],[-1,-1],color='0.35');txt(ax,4.5,-.6,r'H $1s$')
    levels=[(-5+shift,r'$\sigma_s$',2),(-2.5+shift,r'$\sigma_b$',2),(2.5+shift,r'$\sigma^*$',0)]
    for y,t,n in levels:
        ax.plot([1.7,3.2],[y,y],color=BLUE,lw=2);txt(ax,3.65,y,t)
        if n:txt(ax,2.45,y+.28,r'$\uparrow\downarrow$',16,BLUE)
    for x in [1.8,2.75]:ax.plot([x,x+.6],[-.2+shift,-.2+shift],color=BLUE,lw=2)
    txt(ax,3.7,-.2+shift,r'$\pi_x,\pi_y$')
    txt(ax,2.1,.12+shift,r'$\uparrow$',16,BLUE)
    if npi==2:txt(ax,3.05,.12+shift,r'$\uparrow$',16,BLUE)
    for ya,_ in ao:
        for ym in [-5+shift,-2.5+shift,2.5+shift]:ax.plot([.9,1.7],[ya,ym],ls=':',lw=.7,color='0.6')
    for ym in [-5+shift,-2.5+shift,2.5+shift]:ax.plot([3.2,4.1],[ym,-1],ls=':',lw=.7,color='0.6')
    ax.annotate('',(.05,3.5),(.05,-6.7),arrowprops={'arrowstyle':'->'})
    txt(ax,.2,3.65,'Energy',10)
    ax.set(xlim=(-.1,5.2),ylim=(-7,4));ax.axis('off');ax.set_title(label+f': {npi} unpaired electron'+('s' if npi>1 else ''))
fig.suptitle('Valence orbitals only; ordering and occupancy schematic, not measured gaps',fontsize=12)
fig.tight_layout(rect=(0,0,1,.94))

save(fig, 'paper-1-ch-nh-orbitals.png')
