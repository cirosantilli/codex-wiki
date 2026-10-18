"""Original Oxford 2025 QFT diagram. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from the desired output directory. The only saved artifact is the
corresponding opaque PNG in the current directory; this script never chdir()s.
Arrows follow positive conserved charge, not necessarily particle travel.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

LIGHT="#333333"
HEAVY="#175e97"

def setup(ax, title=""):
    ax.set(xlim=(-0.35,6.35),ylim=(-0.35,4.35),aspect="equal")
    ax.axis("off")
    ax.set_title(title,fontsize=13,pad=12)

def label(ax,p,text,**kw):
    ax.text(*p,text,ha="center",va="center",fontsize=12,**kw)

def edge(ax,a,b,heavy=False,arrow=0,dashed=True):
    a=np.array(a,dtype=float);b=np.array(b,dtype=float)
    color=HEAVY if heavy else LIGHT
    normal=np.array([-(b-a)[1],(b-a)[0]])/np.linalg.norm(b-a)
    offsets=(-0.035,0.035) if heavy else (0,)
    for off in offsets:
        pts=np.array([a+off*normal,b+off*normal])
        ax.plot(pts[:,0],pts[:,1],color=color,lw=1.8,ls="--" if dashed else "-")
    if arrow:
        start=a+(.39 if arrow>0 else .61)*(b-a)
        end=a+(.61 if arrow>0 else .39)*(b-a)
        ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=14,color=color,lw=1.5))

def vertex(ax,p):
    ax.plot(*p,"o",color="black",ms=5)

def save(fig):
    out=Path.cwd()/(Path(__file__).stem+".png")
    out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(out,dpi=145,facecolor="white",transparent=False,bbox_inches="tight")
    plt.close(fig)
    print(out)


fig,ax=plt.subplots(figsize=(7,3.8),facecolor="white");setup(ax,r"2(c)(i): $\phi\phi\to\phi\phi$")
l=(2,2);r=(4,2)
for a in [(.1,3.6),(.1,.4)]:edge(ax,a,l,arrow=1)
for b in [(5.9,3.6),(5.9,.4)]:edge(ax,r,b,arrow=1)
edge(ax,l,r,heavy=True,arrow=1)
for v in [l,r]:vertex(ax,v)
for p,t in [((.7,3.9),r"$\phi(p_1)$"),((.7,.1),r"$\phi(p_2)$"),((5.3,3.9),r"$\phi(p_3)$"),((5.3,.1),r"$\phi(p_4)$"),((3,2.75),r"$\bar\Phi\;(+2)$"),((3,1.25),r"$q=p_1+p_2$")]:label(ax,p,t)
fig.tight_layout();save(fig)
