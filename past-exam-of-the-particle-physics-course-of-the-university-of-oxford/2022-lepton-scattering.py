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

fig,ax=plt.subplots(figsize=(7.8,4.2)); panel(ax)
a=(4.8,4.2);b=(4.8,1.5)
fermion(ax,(1,5),a);fermion(ax,a,(8.6,5))
fermion(ax,(1,.7),b);fermion(ax,b,(8.6,.7));wave(ax,a,b)
for x,y,s in [(1,5.5,r"$e^-(p_1)$"),(8.6,5.5,r"$e^-(p_3)$"),(1,.2,r"$\mu^-(p_2)$"),(8.6,.2,r"$\mu^-(p_4)$"),(6,2.85,r"$\gamma^*,\ q=p_1-p_3$"),(3.9,4,r"$-ie\gamma^\mu$"),(3.9,1.8,r"$-ie\gamma^\nu$")]:text(ax,x,y,s)
ax.set_title("One-photon exchange (time runs left to right)",pad=12)
fig.tight_layout();save(fig)
