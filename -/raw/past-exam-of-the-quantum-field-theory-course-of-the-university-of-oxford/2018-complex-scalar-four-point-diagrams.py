"""Original diagram; tested with Python 3.14, NumPy and Matplotlib. Output only in caller CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, PathPatch
from matplotlib.path import Path as MplPath
plt.rcParams.update({"font.size":11,"axes.titlesize":11,"figure.facecolor":"white","savefig.facecolor":"white"})
COLOR="#126782"
def edge(ax,a,b,rad=0,arrow=True):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>" if arrow else "-",mutation_scale=10,connectionstyle=f"arc3,rad={rad}",color=COLOR,lw=1.6,shrinkA=1,shrinkB=1))
def dot(ax,p,label=None):
    ax.scatter(*p,s=23,color="#222222",zorder=4)
    if label:ax.text(p[0]+.025,p[1]-.045,label,fontsize=9,color="#333333")
def loop(ax,p,r=.11,sign=1,arrow=True):
    t=np.linspace(-np.pi/2,3*np.pi/2,140)
    xs=p[0]+r*np.cos(t);ys=p[1]+sign*r*(1+np.sin(t))
    ax.plot(xs,ys,color=COLOR,lw=1.6)
    if arrow:
        j=56
        ax.add_patch(FancyArrowPatch((xs[j],ys[j]),(xs[j+7],ys[j+7]),arrowstyle="-|>",mutation_scale=10,color=COLOR,lw=1.6))
def clean(ax):
    ax.set(xlim=(-.05,1.05),ylim=(-.07,1.12));ax.set_aspect("equal");ax.axis("off")
def external_labels(ax,points):
    for name,p in points.items():
        ax.text(p[0]-.035 if p[0]<.5 else p[0]+.015,p[1]+.03,"$"+name[0]+"_"+name[1]+"$",ha="right" if p[0]<.5 else "left",fontsize=10)

fig,axes=plt.subplots(2,4,figsize=(12.8,6.25),layout="constrained")
ext={'x1':(.06,.84),'x2':(.06,.16),'y1':(.94,.84),'y2':(.94,.16)}
for ax in axes.flat:clean(ax);external_labels(ax,ext)
# C(u,v) is drawn from its first argument to its second.
ax=axes[0,0];z=(.5,.5)
for name,p in ext.items():edge(ax,p,z) if name.startswith('x') else edge(ax,z,p)
dot(ax,z,'z');ax.set_title("Tree: order λ, S = 1")
ax=axes[0,1];z=(.32,.5);w=(.68,.5)
for name in ['x1','x2']:edge(ax,ext[name],z)
for name in ['y1','y2']:edge(ax,w,ext[name])
edge(ax,z,w,.5);edge(ax,z,w,-.5);dot(ax,z,'z');dot(ax,w,'w');ax.set_title("Same-arrow bubble: S = 2")
for ax,ys,title in [(axes[0,2],['y1','y2'],"Mixed bubble t: S = 1"),(axes[0,3],['y2','y1'],"Mixed bubble u: S = 1")]:
    z=(.5,.72);w=(.5,.28)
    edge(ax,ext['x1'],z);edge(ax,z,ext[ys[0]]);edge(ax,ext['x2'],w);edge(ax,w,ext[ys[1]])
    edge(ax,z,w,.5);edge(ax,w,z,.5);dot(ax,z,'z');dot(ax,w,'w');ax.set_title(title)
for ax,leg in zip(axes[1],['x1','x2','y1','y2']):
    w=(.53,.5);z=(.28,.81 if leg[1]=='1' else .19) if leg[0]=='x' else (.76,.81 if leg[1]=='1' else .19)
    for name,p in ext.items():
        target=z if name==leg else w
        edge(ax,p,target) if name[0]=='x' else edge(ax,target,p)
    edge(ax,z,w) if leg[0]=='x' else edge(ax,w,z)
    loop(ax,z,.095,1 if leg[1]=='1' else -1);dot(ax,z,'z');dot(ax,w,'w')
    ax.set_title("Tadpole on $"+leg[0]+"_"+leg[1]+"$: S = 1")
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,transparent=False)
plt.close(fig)
