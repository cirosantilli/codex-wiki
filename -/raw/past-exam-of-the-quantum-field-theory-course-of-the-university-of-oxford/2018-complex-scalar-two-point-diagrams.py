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

fig,axes=plt.subplots(1,3,figsize=(10.2,3.15),layout="constrained")
for ax in axes:clean(ax)
edge(axes[0],(.08,.35),(.92,.35));axes[0].text(.04,.25,r"$y_1$");axes[0].text(.89,.25,r"$y_2$");axes[0].set_title("Free mixed propagator")
ax=axes[1];edge(ax,(.08,.12),(.92,.12));z=(.5,.62);loop(ax,z,.135,1);loop(ax,z,.135,-1);dot(ax,z,"z");ax.set_title("Free line × vacuum factor\ncoefficient 1/2");ax.text(.04,.02,r"$y_1$");ax.text(.89,.02,r"$y_2$")
ax=axes[2];z=(.5,.3);edge(ax,(.08,.3),z);edge(ax,z,(.92,.3));loop(ax,z,.19);dot(ax,z,"z");ax.set_title("Connected tadpole\nsymmetry factor S = 1");ax.text(.04,.2,r"$y_1$");ax.text(.89,.2,r"$y_2$")
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,transparent=False)
plt.close(fig)
