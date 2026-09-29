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


fig,axs=plt.subplots(2,3,figsize=(11,6.7),facecolor="white")
for ax in axs.flat:setup(ax)
ax=axs[0,0];edge(ax,(.4,2),(5.6,2),arrow=1);label(ax,(3,3.3),r"Light: charge arrow $+1$");label(ax,(3,.8),r"$i/(p^2-m^2+i0)$")
ax=axs[0,1];edge(ax,(.4,2),(5.6,2),heavy=True,arrow=1);label(ax,(3,3.3),r"Heavy: charge arrow $+2$");label(ax,(3,.8),r"$i/(p^2-M^2+i0)$")
ax=axs[0,2]
label(ax,(3,2.8),"Single dashed: light\nDouble dashed: heavy")
ax.text(3,.9,"Arrows count positive charge.\nAll vertex momenta incoming.",ha="center",fontsize=10)
ax=axs[1,0];v=(3,2)
for a,ar,h,txt in [((.6,3.6),1,False,r"$\phi$"),((5.4,3.6),-1,False,r"$\phi^\dagger$"),((.6,.4),-1,True,r"$\Phi$"),((5.4,.4),1,True,r"$\Phi^\dagger$")]:
 edge(ax,a,v,arrow=ar,heavy=h);label(ax,(a[0],a[1]+(.35 if a[1]>2 else -.35)),txt)
vertex(ax,v);label(ax,(3,2.55),r"$-ig$")
for ax,conj in [(axs[1,1],False),(axs[1,2],True)]:
 v=(3,2)
 for a in [(.5,3.2),(.5,.8)]:edge(ax,a,v,arrow=-1 if conj else 1)
 edge(ax,v,(5.5,2),heavy=True,arrow=-1 if conj else 1);vertex(ax,v)
 label(ax,(.5,3.8),r"$\phi^\dagger$" if conj else r"$\phi$");label(ax,(.5,.2),r"$\phi^\dagger$" if conj else r"$\phi$")
 label(ax,(5.6,2.6),r"$\Phi^\dagger$" if conj else r"$\Phi$");label(ax,(3,3.1),r"$-ih$")
fig.tight_layout(h_pad=1.5,w_pad=1.5);save(fig)
