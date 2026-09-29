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

fig,axs=plt.subplots(3,2,figsize=(8.5,8))
for j,V in enumerate(["W","Z"]):
    for i,kind in enumerate(["Mass term","One Higgs","Two Higgs"]):
        ax=axs[i,j];panel(ax);c=(5,2.7)
        wave(ax,(1,1.5),c);wave(ax,c,(9,1.5))
        left=r"$W^+$" if V=="W" else r"$Z$";right=r"$W^-$" if V=="W" else r"$Z$"
        text(ax,1,1,left);text(ax,9,1,right)
        if i==0:
            ax.plot([4.7,5.3],[2.4,3],color="black");ax.plot([4.7,5.3],[3,2.4],color="black")
            text(ax,5,4,r"$m_W^2 W^+W^-$" if V=="W" else r"$\frac{1}{2}m_Z^2 Z^2$")
        else:
            for x in ([5] if i==1 else [3.2,6.8]):
                ax.plot([5,x],[2.7,4.8],"--",color="black",lw=1.5);text(ax,x,5.3,r"$h$")
        ax.set_title(kind+": "+V)
fig.suptitle("Terms from the Higgs kinetic energy",y=.99)
fig.tight_layout();save(fig)
