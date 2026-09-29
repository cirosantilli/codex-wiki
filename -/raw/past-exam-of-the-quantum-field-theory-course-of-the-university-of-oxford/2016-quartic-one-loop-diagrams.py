"""Original diagram geometry; Python 3.14, matplotlib 3.10.7. Writes one PNG in the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans", "savefig.facecolor": "white"})
BLUE="#155f91"
def edge(ax,a,b,rad=0):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-",connectionstyle=f"arc3,rad={rad}",linewidth=1.7,color="#202020",shrinkA=0,shrinkB=0))
def node(ax,p):
    ax.plot(*p,"o",color="#202020",ms=4)
def ext(ax,p,q,label):
    edge(ax,p,q)
    ax.text(q[0],q[1],str(label),ha="center",va="center",color=BLUE,bbox={"facecolor":"white","edgecolor":"none","pad":1.5})
def loop(ax,p,r=.28):
    ax.add_patch(Circle((p[0],p[1]+r),r,fill=False,linewidth=1.7,color="#202020"))
def setup(ax,title):
    ax.set(xlim=(-1.8,1.8),ylim=(-1.35,1.65),aspect="equal")
    ax.axis("off");ax.set_title(title,fontsize=11,pad=3)
def bubble(ax,i,j,k):
    w=(-.75,0);x=(.2,0);z=(1.,0)
    edge(ax,w,x);edge(ax,x,z,.55);edge(ax,x,z,-.55)
    for p in (w,x,z):node(ax,p)
    ext(ax,w,(-1.55,.8),j);ext(ax,w,(-1.55,-.8),k);ext(ax,z,(1.6,0),i)
def chain(ax,i,j,k):
    w=(-.75,0);z=(.25,0);x=(1.15,0)
    edge(ax,w,z);edge(ax,z,x);loop(ax,x)
    for p in (w,z,x):node(ax,p)
    ext(ax,w,(-1.55,.8),j);ext(ax,w,(-1.55,-.8),k);ext(ax,z,(.25,-1.05),i)
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False,metadata={"Software":"Matplotlib"})
    plt.close(fig)

fig,axs=plt.subplots(1,4,figsize=(12,3.5),layout="constrained")
setup(axs[0],"Two-point tadpole: S=2")
node(axs[0],(0,0));loop(axs[0],(0,0),.4);ext(axs[0],(0,0),(-1.35,-.6),1);ext(axs[0],(0,0),(1.35,-.6),2)
for ax,labels,name in zip(axs[1:],[(1,2,3,4),(1,3,2,4),(1,4,2,3)],["s: (12|34)","t: (13|24)","u: (14|23)"]):
    setup(ax,name+"; S=2")
    x=(-.5,0);z=(.5,0);edge(ax,x,z,.6);edge(ax,x,z,-.6);node(ax,x);node(ax,z)
    for p,q,label in zip([x,x,z,z],[(-1.5,.85),(-1.5,-.85),(1.5,.85),(1.5,-.85)],labels):ext(ax,p,q,label)
fig.suptitle("Quartic theory: one-loop 1PI graphs (external labels fixed)",fontsize=15)
save(fig)
