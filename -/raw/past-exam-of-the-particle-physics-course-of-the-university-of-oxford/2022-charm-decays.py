from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
def panel(ax):
    ax.set(xlim=(0,10), ylim=(0,6), aspect="equal")
    ax.axis("off")
def text(ax,x,y,s,**kw):
    ax.text(x,y,s,ha="center",va="center",**kw)
def fermion(ax,a,b,color="black",reverse=False):
    a,b=np.array(a,dtype=float),np.array(b,dtype=float)
    ax.plot([a[0],b[0]],[a[1],b[1]],color=color,lw=1.7)
    u,v=(b,a) if reverse else (a,b)
    ax.add_patch(FancyArrowPatch(u+.43*(v-u),u+.63*(v-u),arrowstyle="-|>",mutation_scale=12,color=color,lw=1.5))
def wave(ax,a,b,color="#5b4890",gluon=False):
    a,b=np.array(a,dtype=float),np.array(b,dtype=float)
    t=np.linspace(0,1,350); d=b-a; n=np.array([-d[1],d[0]])/np.linalg.norm(d)
    z=a[:,None]+d[:,None]*t+n[:,None]*(.10*np.sin(2*np.pi*7*t))
    if gluon:z+=d[:,None]/np.linalg.norm(d)*(.07*np.sin(2*np.pi*14*t))
    ax.plot(z[0],z[1],color=color,lw=1.4)
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False)
    plt.close(fig)

fig,axs=plt.subplots(2,1,figsize=(9.3,8.2))
for ax,sbar,down,kaon,v1,v2,title in [
    (axs[0],r"$\bar s$",r"$d$",r"$K^0=d\bar s$",r"$V_{cs}$",r"$V_{ud}^*$","Cabibbo-favoured"),
    (axs[1],r"$\bar d$",r"$s$",r"$\bar K^0=s\bar d$",r"$V_{cd}$",r"$V_{us}^*$","Doubly Cabibbo-suppressed")]:
    panel(ax);a=(3,3.3);b=(5.3,2.5)
    fermion(ax,(.7,4.8),(8.4,4.8));fermion(ax,(.7,3.3),a,reverse=True)
    fermion(ax,a,(8.4,.8),reverse=True);wave(ax,a,b)
    fermion(ax,b,(8.4,3.8),reverse=True);fermion(ax,b,(8.4,1.8))
    for x,y,s in [(.6,5.3,r"$u$ (spectator)"),(.6,2.85,r"$\bar c$"),(8.2,5.3,r"$u$"),(8.2,3.35,r"$\bar u$"),(8.2,2.25,down),(8.2,.35,sbar),(9.25,4.3,r"$\pi^0$"),(9.1,1.25,kaon),(3.4,3.9,v1),(5.2,1.95,v2),(4.6,3.4,r"$W^-$")]:text(ax,x,y,s)
    ax.plot([8.8,8.95,8.95,8.8],[4.8,4.8,3.8,3.8],color="gray")
    ax.plot([8.8,8.95,8.95,8.8],[1.8,1.8,.8,.8],color="gray")
    ax.set_title(title)
fig.suptitle(r"$\bar D^0=(\bar c u)$ internal-emission diagrams",y=.99)
fig.tight_layout();save(fig)
