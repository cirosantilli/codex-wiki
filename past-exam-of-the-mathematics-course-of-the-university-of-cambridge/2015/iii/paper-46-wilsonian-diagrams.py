"""Connected quartic shell contractions, including the two support-forbidden bridges.
Python 3.14; root pyproject matplotlib/numpy. Only the PNG basename is written to cwd.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Circle
import numpy as np
BLUE='#194b7b'; GRAY='#676767'
def curve(ax,points):
    ax.add_patch(PathPatch(Path(points,[Path.MOVETO,Path.CURVE4,Path.CURVE4,Path.CURVE4]),fill=False,color=BLUE,lw=2))
def vertex(ax,x,y=0): ax.add_patch(Circle((x,y),.046,color=BLUE,zorder=5))
def loop(ax,x,side=1): curve(ax,[(x,0),(x-.65,side*1.15),(x+.65,side*1.15),(x,0)])
def legs(ax,x,count,direction):
    if not count:return
    angles=np.linspace(-.65,.65,count) if count>1 else np.array([0.])
    for a in angles:
        dx=direction*.8*np.cos(a);dy=.8*np.sin(a)
        ax.plot([x,x+dx],[0,dy],'--',lw=1.6,color=GRAY)
        ax.add_patch(Circle((x+dx,dy),.025,fill=False,color=GRAY))
def pair(ax,r,t1,t2):
    x1,x2=-.55,.55
    for bulge in np.linspace(-.55,.55,r) if r>1 else [0.]:
        curve(ax,[(x1,0),(x1+.3,bulge),(x2-.3,bulge),(x2,0)])
    for x,t in [(x1,t1),(x2,t2)]:
        for i in range(t):loop(ax,x,1 if i==0 else -1)
        vertex(ax,x)
    legs(ax,x1,4-r-2*t1,-1);legs(ax,x2,4-r-2*t2,1)
def single(ax,t):
    vertex(ax,0)
    if t==0:
        for a in [np.pi/4,3*np.pi/4,5*np.pi/4,7*np.pi/4]:
            dx,dy=.85*np.cos(a),.85*np.sin(a);ax.plot([0,dx],[0,dy],'--',color=GRAY,lw=1.6)
    elif t==1:loop(ax,0);legs(ax,0,1,-1);legs(ax,0,1,1)
    else:loop(ax,0);loop(ax,0,-1)
fig,axes=plt.subplots(4,3,figsize=(12,12.6),dpi=100,facecolor='white')
items=[('A: existing quartic vertex',('single',0),'order g; 4 low-field legs'),('B: shell tadpole',('single',1),'order g; 2 low-field legs'),('C: double-loop vacuum',('single',2),'order g; field-independent'),('D: single bridge',('pair',1,0,0),'order g²; 6 low-field legs'),('E: bridge + one tadpole',('pair',1,0,1),'order g²; 4 legs; zero by shell support'),('F: bridge + two tadpoles',('pair',1,1,1),'order g²; 2 legs; zero by shell support'),('G: two connecting lines',('pair',2,0,0),'order g²; 4 low-field legs'),('H: two lines + one tadpole',('pair',2,0,1),'order g²; 2 low-field legs'),('I: two lines + two tadpoles',('pair',2,1,1),'order g²; field-independent'),('J: three connecting lines',('pair',3,0,0),'order g²; 2 legs (sunset)'),('K: four connecting lines',('pair',4,0,0),'order g²; field-independent'),('L: Gaussian normalization',('free',),'order g⁰; field-independent')]
for ax,(title,kind,label) in zip(axes.flat,items):
    ax.set_xlim(-1.8,1.8);ax.set_ylim(-1.18,1.25);ax.set_aspect('equal');ax.axis('off');ax.set_title(title,fontsize=11,pad=9)
    if kind[0]=='single':single(ax,kind[1])
    elif kind[0]=='pair':pair(ax,*kind[1:])
    else:ax.add_patch(Circle((0,0),.47,fill=False,color=BLUE,lw=2))
    if title.startswith(('E:','F:')):ax.text(0,-1.02,'ZERO',ha='center',color='#a42822',fontsize=11,fontweight='bold')
    ax.text(.5,-.025,label,ha='center',va='top',transform=ax.transAxes,fontsize=10)
fig.suptitle('Quartic Wilsonian action: connected shell contractions through g²',fontsize=16,y=.977)
fig.text(.5,.023,'Solid blue: shell propagator. Dashed gray: external low field. D may survive when three low momenta sum into the shell.',ha='center',fontsize=10)
fig.subplots_adjust(left=.02,right=.98,bottom=.067,top=.935,hspace=.31,wspace=.06)
fig.savefig('paper-46-wilsonian-diagrams.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
