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

fig,axes=plt.subplots(1,4,figsize=(12,3.25),layout="constrained")
ax=axes[0];v=np.array([.5,.32]);edge(ax,(.04,.14),v,arrow=False);edge(ax,v,(.96,.14),arrow=False)
for angle in [25,90,155]:
    e=np.array([np.cos(np.deg2rad(angle)),np.sin(np.deg2rad(angle))]);n=np.array([-e[1],e[0]])
    points=[v,v+.75*e+.16*n,v+.75*e-.16*n,v]
    ax.add_patch(PathPatch(MplPath(points,[MplPath.MOVETO,MplPath.CURVE4,MplPath.CURVE4,MplPath.CURVE4]),fill=False,color=COLOR,lw=1.6))
dot(ax,v);ax.set_title("One vertex, k = 4\nthree independent tadpoles");ax.text(.5,-.025,r"$S=2^3\,3!=48$",ha="center");clean(ax)
pairs=[("12 | 34",['1','2','3','4']),("13 | 24",['1','3','2','4']),("14 | 23",['1','4','2','3'])]
for ax,(title,labs) in zip(axes[1:],pairs):
    z=(.32,.5);w=(.68,.5);ext=[(.03,.82),(.03,.18),(.97,.82),(.97,.18)]
    for p,target,label in zip(ext,[z,z,w,w],labs):
        edge(ax,p,target,arrow=False);ax.text(p[0],p[1]+.065,label,ha="center")
    edge(ax,z,w,.5,False);edge(ax,z,w,-.5,False);dot(ax,z);dot(ax,w)
    ax.set_title("Quartic bubble: "+title);ax.text(.5,-.025,r"$S=2$",ha="center");clean(ax)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,transparent=False)
plt.close(fig)
