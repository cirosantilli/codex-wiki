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

fig,axs=plt.subplots(1,2,figsize=(12,4.4))
a=axs[0];panel(a)
fermion(a,(.3,4),(2.3,2.8));fermion(a,(.3,1.6),(2.3,2.8),reverse=True)
wave(a,(2.3,2.8),(4.3,2.8));fermion(a,(4.3,2.8),(6.3,4.1),color="#b62626")
fermion(a,(6.3,4.1),(9,5.2),color="#1b57ad");fermion(a,(4.3,2.8),(9,.7),color="#b62626",reverse=True)
wave(a,(6.3,4.1),(9,2.9),gluon=True)
for x,y,s in [(.5,4.5,r"$e^-$"),(.5,1.1,r"$e^+$"),(3.3,3.3,r"$\gamma^*$"),(5.1,4.2,r"$q_r$"),(8,5.6,r"$q_b$"),(8.1,2.3,r"$g_{r\bar b}$"),(8.4,.2,r"$\bar q_{\bar r}$")]:text(a,x,y,s)
a.set_title("Resolved gluon emission")
a=axs[1];panel(a)
A=(3,4.3);B=(3,1.3);C=(6.3,2.8)
fermion(a,B,A,color="#1b57ad");fermion(a,A,C,color="#b62626");fermion(a,C,B,color="#b62626")
wave(a,(.5,5),A,gluon=True);wave(a,(.5,.6),B,gluon=True)
a.plot([C[0],9],[C[1],C[1]],"--",color="black",lw=1.6)
for x,y,s in [(1,5.55,r"$g_{r\bar b}$"),(1,.1,r"$g_{b\bar r}$"),(2.25,2.8,r"$t_b$"),(5.4,4.1,r"$t_r$"),(5.4,1.45,r"$t_r$"),(9,3.3,r"$h$"),(7,2.1,r"$m_t/v$")]:text(a,x,y,s)
a.set_title("A colour component of the top loop")
fig.suptitle("Both complete processes conserve colour",y=.99)
fig.tight_layout();save(fig)
