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


fig,axs=plt.subplots(1,3,figsize=(11,3.6),facecolor="white")
for ax,title in zip(axs,[r"Vertex: $-ig\gamma^5$","One-point fermion loop","Three-point fermion loop"]): setup(ax,title)
ax=axs[0];v=(3,2)
edge(ax,(.2,2),v,arrow=1,dashed=False);edge(ax,v,(5.8,2),arrow=1,dashed=False)
edge(ax,v,(3,4));vertex(ax,v)
label(ax,(.7,2.5),r"$\psi$");label(ax,(5.3,2.5),r"$\psi$");label(ax,(3.5,3.8),r"$\phi$")
ax=axs[1];theta=np.linspace(0,2*np.pi,200);cx,cy,r=3.7,2,1.1
ax.plot(cx+r*np.cos(theta),cy+r*np.sin(theta),color=LIGHT,lw=1.8)
a=np.pi/2;ax.add_patch(FancyArrowPatch((cx+r*np.cos(a-.18),cy+r*np.sin(a-.18)),(cx+r*np.cos(a+.18),cy+r*np.sin(a+.18)),arrowstyle="-|>",mutation_scale=14,color=LIGHT))
edge(ax,(.2,2),(cx-r,2));vertex(ax,(cx-r,2));label(ax,(1.2,2.5),r"$\phi$");label(ax,(3.7,.3),r"$\mathrm{tr}[\gamma^5(\gamma^\mu k_\mu+M)]=0$")
ax=axs[2];vs=[(1.6,1.1),(4.4,1.1),(3,3.5)]
for i in range(3):edge(ax,vs[i],vs[(i+1)%3],arrow=1,dashed=False);vertex(ax,vs[i])
for v,end in zip(vs,[(.1,.4),(5.9,.4),(3,4.3)]):edge(ax,v,end)
label(ax,(3,.0),r"$N_{\triangle}=0$")
fig.tight_layout(w_pad=1.8);save(fig)
