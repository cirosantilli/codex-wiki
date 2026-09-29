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

fig,axs=plt.subplots(2,4,figsize=(12,6),layout="constrained");a=axs.ravel()
setup(a[0],"Tree (order lambda): S=1")
p=(0,0);node(a[0],p)
for q,label in [((-1.25,-.85),1),((1.25,-.85),2),((0,1.25),3)]:ext(a[0],p,q,label)
setup(a[1],"Triangle (order lambda cubed): S=1")
ps=[(-.65,-.35),(.65,-.35),(0,.7)]
for n in range(3):node(a[1],ps[n]);edge(a[1],ps[n],ps[(n+1)%3])
for p,q,label in zip(ps,[(-1.45,-1.05),(1.45,-1.05),(0,1.45)],[1,2,3]):ext(a[1],p,q,label)
for n,i in enumerate((1,2,3)):
    j,k=[x for x in (1,2,3) if x!=i]
    setup(a[n+2],f"Bubble on branch {i}: S=2");bubble(a[n+2],i,j,k)
    setup(a[n+5],f"Tadpole chain\nmiddle label {i}: S=2");chain(a[n+5],i,j,k)
fig.suptitle("All connected cubic three-point graphs through order lambda cubed",fontsize=14)
fig.supxlabel("All seven loop graphs are order lambda cubed; their weights are 1/S. External labels are fixed.",fontsize=11)
save(fig)
