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

fig,axs=plt.subplots(1,2,figsize=(11,4.7))
ax=axs[0]
basepts=[(-1,-.6),(1,-.6),(1,.6),(-1,.6)];tip=(0,1.9)
ring(ax,basepts)
for p in basepts:bond(ax,p,tip);atom(ax,p,'B')
atom(ax,tip,'B');txt(ax,0,-1.4,'Five vertices, seven skeletal pairs',11,BLUE)
finish(ax,(-2,2),(-2,2.6),'A: nido square-pyramidal skeleton')
ax=axs[1]
x=np.arange(3);n=np.array([5,6,6]);actual=np.array([7,9,9])
ax.bar(x-.18,n+1,width=.35,color='0.75',label='closo reference n+1')
ax.bar(x+.18,actual,width=.35,color=BLUE,label='actual skeletal pairs')
for i,a in enumerate(actual):ax.text(i+.18,a+.15,str(a),ha='center')
ax.set_xticks(x,['A: B₅H₈⁻','B: B₆H₁₁⁻','C: B₆H₁₂']);ax.set_ylim(0,11);ax.set_ylabel('Skeletal electron pairs')
ax.legend(loc='upper left',fontsize=9);ax.set_title('A = nido; B and C = arachno')
ax.spines[['top','right']].set_visible(False);fig.tight_layout()

save(fig,'paper-1-borane-counts.png')
