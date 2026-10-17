"""Original explanatory figure; Python 3.14, numpy and matplotlib.
Write the same-basename PNG to the current working directory for Make.
No source image or source data file is read.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, Arc
import numpy as np

def box(ax,x,y,w,h,text,fc="#e5edf5",size=9):
    ax.add_patch(Rectangle((x,y),w,h,fc=fc,ec="#253858",lw=1.2))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=size)

def arrow(ax,a,b,text=None):
    ax.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="->",lw=1.3,color="#253858"))
    if text:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2,text,fontsize=8,ha="center",va="bottom")

def finish(fig,name):
    fig.set_facecolor("white")
    fig.savefig(name,dpi=150,facecolor="white",bbox_inches="tight")
    plt.close(fig)

fig,axs=plt.subplots(2,3,figsize=(10,6.4),layout="constrained")
film="#c27812";resist="#a9b2bc";si="#dfe5eb"
def base(ax,title):
    ax.set(xlim=(-.55,1.05),ylim=(-.33,1.37),title=title);ax.set_aspect("equal")
    ax.add_patch(Rectangle((-.55,-.33),1.6,.33,fc=si,ec="none"))
    for x in [-.55,.5]:ax.add_patch(Rectangle((x,0),.55,1,fc=resist,ec="#46515c"))
    ax.set_xlabel("Lateral position (micrometers)");ax.set_ylabel("Height (micrometers)")
for ax,title in zip(axs.flat,["Sputter: partial wall coverage","Normal evaporation: directional","CVD: conformal idealization","Wet etch: isotropic undercut","Ion milling: directional idealization","Real positive-resist profile"],strict=True):base(ax,title)
for ax in axs[0]:
    for x,w,y in [(-.55,.55,1),(.5,.55,1),(0,.5,0)]:ax.add_patch(Rectangle((x,y),w,.2,fc=film,ec="none"))
ax=axs[0,0]
for x in [0,.42]:ax.add_patch(Rectangle((x,.2),.08,.8,fc=film,ec="none"))
ax.text(.25,.65,"Wall thickness\nnot prescribed",ha="center",fontsize=7)
ax=axs[0,2]
for x in [0,.3]:ax.add_patch(Rectangle((x,.2),.2,.8,fc=film,ec="none"))
ax.annotate("0.10 gap",(.25,.65),xytext=(.25,1.26),ha="center",fontsize=8,arrowprops=dict(arrowstyle="->"))
ax=axs[1,0];x=np.linspace(-.2,.7,500);y=np.full_like(x,-.2)
l=x<0;r=x>.5;y[l]=-np.sqrt(np.maximum(.04-x[l]**2,0));y[r]=-np.sqrt(np.maximum(.04-(x[r]-.5)**2,0))
ax.fill_between(x,y,0,color="white");ax.plot(x,y,color="#007f91",lw=2)
ax=axs[1,1];ax.add_patch(Rectangle((0,-.2),.5,.2,fc="white",ec="#007f91",lw=1.5));ax.text(.25,.55,"Mask erosion and\nredeposition may occur",ha="center",fontsize=7)
ax=axs[1,2];ax.patches.clear() if hasattr(ax.patches,"clear") else None
# Cover ideal shapes and add an independently drawn sloped, rounded profile.
ax.add_patch(Rectangle((-.55,0),1.6,1.3,fc="white",ec="none"))
for pts in [[[-.55,0],[.04,0],[-.07,.94],[-.16,1.01],[-.55,1.01]],[[.46,0],[1.05,0],[1.05,1.01],[.67,1.01],[.57,.94]]]:ax.add_patch(Polygon(pts,fc=resist,ec="#46515c"))
ax.text(.25,.45,"Finite slope,\nrounding or\nfloor residue",ha="center",fontsize=7)
finish(fig,"paper-1-deposition-etching.png")
