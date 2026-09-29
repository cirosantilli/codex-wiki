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


fig,axs=plt.subplots(1,2,figsize=(11,3.9),facecolor="white")
for ax,title in zip(axs,[r"2(c)(ii): contact $-ig$",r"2(c)(ii): $s$-channel $\bar\phi$ exchange"]):setup(ax,title)
ax=axs[0];v=(3,2)
for a,b,h,ar in [((.3,3.5),v,False,1),((.3,.5),v,True,-1),(v,(5.7,3.5),False,1),(v,(5.7,.5),True,-1)]:edge(ax,a,b,heavy=h,arrow=ar)
vertex(ax,v)
ax=axs[1];l=(2,2);r=(4,2)
for a,b,h,ar in [((.3,3.5),l,False,1),((.3,.5),l,True,-1),(r,(5.7,3.5),False,1),(r,(5.7,.5),True,-1)]:edge(ax,a,b,heavy=h,arrow=ar)
edge(ax,l,r,arrow=-1);vertex(ax,l);vertex(ax,r);label(ax,(3,2.75),r"$\bar\phi\;(-1)$");label(ax,(3,1.2),r"$q=p_1+p_2$")
for ax in axs:
 for p,t in [((.6,3.95),r"$\phi(p_1),+1$"),((.6,.05),r"$\Phi(p_2),-2$"),((5.4,3.95),r"$\phi(p_3),+1$"),((5.4,.05),r"$\Phi(p_4),-2$")]:label(ax,p,t)
fig.tight_layout(w_pad=2);save(fig)
