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

def box(ax,x,y,s,w=2.6,h=.8,color=BLUE,size=11):
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.08',fc='white',ec=color,lw=1.2))
    if '$' not in s and len(s)>29:
        import textwrap
        s='\n'.join(textwrap.wrap(s,width=29))
    elif '$' in s and len(s)>35:
        size=min(size,8.5)
    txt(ax,x,y,s,size,color)
def route(rows,title,figsize=(12,6)):
    fig,ax=plt.subplots(figsize=figsize)
    for i,row in enumerate(rows):
        y=-i*1.7
        for j,entry in enumerate(row):
            x=j*4
            if j%2==0:box(ax,x,y,entry,w=3.35,h=1.05,size=11)
            else:flow(ax,(x-1.7,y),(x+1.7,y));txt(ax,x,y+.4,entry,10)
    finish(ax,(-2,18),(-len(rows)*1.7+.3,1.4),title)
    fig.tight_layout();return fig

fig,axs=plt.subplots(2,1,figsize=(12,7.2))
ax=axs[0]
pent=[(0,0),(-.7,.8),(-1.7,.5),(-1.7,-.5),(-.7,-.8)];ring(ax,pent)
a=(0,0);b=(1.6,0);c=(2.7,.8);d=(1.6,1.6);bond(ax,a,b,2);bond(ax,b,c);bond(ax,c,d,2)
bond(ax,b,(1.6,-1));atom(ax,(1.6,-1),r'$(CH_2)_3Q$');txt(ax,1.6,.45,'d',12,ORANGE)
flow(ax,(4.3,.25),(6.05,.25),'ethylene equivalent')
pent2=np.array(pent)+[8,0];ring(ax,pent2)
hex2=np.array([[8,0],[9,.8],[10.2,.8],[10.8,0],[10.2,-.8],[9,-.8]]);ring(ax,hex2,{1:2});bond(ax,hex2[1],(9,1.7));atom(ax,(9,1.7),r'$(CH_2)_3Q$')
finish(ax,(-2.5,12),(-2,2.4),'Left-hand diene: cyclopentane carbon is terminal; cycloaddition creates a spiro centre')
ax=axs[1]
box(ax,0,1.1,'Br–a–b–c–d–OH',w=3.7)
box(ax,6.8,1.1,'cis acetyl ring–a–b–c–d–OP',w=4)
flow(ax,(2,1.1),(4.6,1.1),'Protect; formylate; diene; DA')
box(ax,0,-.8,'Q–a–b–c–C_d(=O)–CH=CH₂',w=5.5,size=10)
box(ax,7,-.8,'Q–a–b–c–d–OH',w=5.3,size=10)
flow(ax,(6.8,.55),(6.8,-.2),'reduce; methylate; deprotect')
flow(ax,(4.2,-.8),(2.9,-.8));txt(ax,3.55,-.3,'oxidize; vinyl; oxidize',9)
txt(ax,3.5,-2.1,'a,b,c = three linker CH₂ carbons; d = linker-bearing left alkene carbon.',11,ORANGE)
finish(ax,(-3.1,10),(-2.6,2.5),'Four starting-chain carbons retain a traceable identity; the right-hand DA precedes spiro-ring construction')
fig.tight_layout()

save(fig,'paper-1-q12-second-route.png')
