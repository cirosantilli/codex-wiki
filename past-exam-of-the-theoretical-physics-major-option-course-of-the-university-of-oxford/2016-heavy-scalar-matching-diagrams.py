"""Original geometry; Python 3.14 with numpy/matplotlib. Writes exactly one PNG in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False,metadata={"Software":"Matplotlib"})
    plt.close(fig)

def line(ax,p,q,arrow=False,dashed=False):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle="->" if arrow else "-",lw=1.7,color="#202020",linestyle="--" if dashed else "-",mutation_scale=11,shrinkA=0,shrinkB=0))
def ext(ax,p,q,text,reverse=False):
    line(ax,q,p,True) if not reverse else line(ax,p,q,True)
    ax.text(q[0],q[1],text,ha="center",va="center",color="#165b91",fontsize=10,bbox={"facecolor":"white","edgecolor":"none","pad":1.5})
fig,axs=plt.subplots(1,3,figsize=(11,3.8),layout="constrained")
for ax in axs:ax.set(xlim=(-1.8,1.8),ylim=(-1.3,1.3),aspect="equal");ax.axis("off")
x=(-.55,0);z=(.55,0);a=axs[0];line(a,x,z,dashed=True)
ext(a,x,(-1.55,.9),"p1 (+)");ext(a,x,(-1.55,-.9),"p2 (-)",True)
ext(a,z,(1.55,.9),"p3 (+)",True);ext(a,z,(1.55,-.9),"p4 (-)")
a.text(0,.2,"heavy M",ha="center");a.set_title("Full theory: s channel")
a=axs[1];x=(0,.6);z=(0,-.6);line(a,x,z,dashed=True)
ext(a,x,(-1.55,1.),"p1 (+)");ext(a,x,(1.55,1.),"p3 (+)",True)
ext(a,z,(-1.55,-1.),"p2 (-)",True);ext(a,z,(1.55,-1.),"p4 (-)")
a.text(.2,0,"heavy M",ha="left");a.set_title("Full theory: t channel")
a=axs[2];x=(0,0)
for q,label,reverse in [((-1.55,.9),"p1 (+)",False),((-1.55,-.9),"p2 (-)",True),((1.55,.9),"p3 (+)",True),((1.55,-.9),"p4 (-)",False)]:ext(a,x,q,label,reverse)
a.set_title("Effective theory: contact -4i lambda")
for ax,ps in [(axs[0],[(-.55,0),(.55,0)]),(axs[1],[(0,.6),(0,-.6)]),(axs[2],[(0,0)])]:
    for p in ps:ax.plot(*p,"o",color="black",ms=5)
fig.suptitle("Heavy-scalar exchange and its low-energy contact interaction",fontsize=14)
save(fig)
