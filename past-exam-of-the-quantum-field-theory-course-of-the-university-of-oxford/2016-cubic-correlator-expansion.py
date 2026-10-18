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

fig,axs=plt.subplots(2,4,figsize=(12,6),layout="constrained")
a=axs.ravel()
setup(a[0],"One-point tadpole: 1/2")
node(a[0],(0,0));loop(a[0],(0,0));ext(a[0],(0,0),(-1.35,0),1)
setup(a[1],"Free two-point term: 1")
edge(a[1],(-1.2,0),(1.2,0));a[1].text(-1.45,0,"1",color=BLUE);a[1].text(1.3,0,"2",color=BLUE)
setup(a[2],"Two-point bubble: 1/2")
x=(-.5,0);z=(.5,0)
edge(a[2],x,z,.6);edge(a[2],x,z,-.6);node(a[2],x);node(a[2],z)
ext(a[2],x,(-1.45,0),1);ext(a[2],z,(1.45,0),2)
setup(a[3],"Connected tadpole: 1/2")
x=(-.55,0);z=(.65,0)
node(a[3],x);node(a[3],z);edge(a[3],x,z);loop(a[3],z)
ext(a[3],x,(-1.45,.8),1);ext(a[3],x,(-1.45,-.8),2)
setup(a[4],"Product of one-point terms: 1/4")
for p,q,label in [((-.7,0),(-1.55,-.6),1),((.7,0),(1.55,-.6),2)]:
    node(a[4],p);loop(a[4],p);ext(a[4],p,q,label)
for n,name in [(5,"Free line x vacuum theta: 1/12"),(6,"Free line x vacuum dumbbell: 1/8")]:
    setup(a[n],name)
    edge(a[n],(-1.2,-.8),(1.2,-.8));a[n].text(-1.5,-.8,"1",color=BLUE);a[n].text(1.3,-.8,"2",color=BLUE)
    x=(-.55,.25);z=(.55,.25);node(a[n],x);node(a[n],z);edge(a[n],x,z)
    if n==5:edge(a[n],x,z,.65);edge(a[n],x,z,-.65)
    else:loop(a[n],x,.23);loop(a[n],z,.23)
    a[n].text(0,-1.25,"CANCELLED by vacuum denominator",ha="center",color="#a23b24",fontsize=9)
setup(a[7],"Conventions")
a[7].text(0,.2,"Each internal vertex: (-i lambda)\nEach line: free Feynman propagator\nIntegrate every internal vertex\nNumbers shown: multiplicative weights\nExternal points labelled 1 and 2",ha="center",va="center",fontsize=10,linespacing=1.7)
fig.suptitle("Cubic theory: one- and two-point Wick contractions",fontsize=15)
save(fig)
