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

def line(ax,p,q,rad=0):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle="-",connectionstyle=f"arc3,rad={rad}",lw=1.6,color="#202020",shrinkA=0,shrinkB=0))
def loop(ax,p,angle,r=.25):
    center=(p[0]+r*np.cos(angle),p[1]+r*np.sin(angle))
    ax.add_patch(Circle(center,r,fill=False,lw=1.5,color="#202020"))
def vertex(ax,p,n):
    ax.plot(*p,marker="o" if n==4 else "s",color="#202020",ms=5)
def panel(ax,n,r,title):
    ax.set(xlim=(-1.65,1.65),ylim=(-1.1,1.1),aspect="equal");ax.axis("off");ax.set_title(title,fontsize=12)
    if r is None:
        p=(0,0);vertex(ax,p,n)
        angles=[np.pi/2+2*np.pi*j/(n//2) for j in range(n//2)]
        for angle in angles:loop(ax,p,angle,.32)
    else:
        p=(-.65,0);q=(.65,0);vertex(ax,p,n);vertex(ax,q,n)
        for curvature in (np.linspace(-.9,.9,r) if r else []):line(ax,p,q,float(curvature))
        k=(n-r)//2
        aa={0:[],1:[np.pi],2:[np.pi/2,-np.pi/2],3:[np.pi/2,np.pi,-np.pi/2]}[k]
        for angle in aa:loop(ax,p,angle)
        for angle in aa:loop(ax,q,np.pi-angle)
fig,axs=plt.subplots(3,3,figsize=(11,8),layout="constrained")
specs=[(4,None,"First order: -lambda / 8"),(6,None,"First order: -mu / 48"),
(4,0,"lambda squared: 1/128 (disconnected)"),(4,2,"lambda squared: 1/16"),(4,4,"lambda squared: 1/48"),
(6,0,"mu squared: 1/4608 (disconnected)"),(6,2,"mu squared: 1/256"),(6,4,"mu squared: 1/192"),(6,6,"mu squared: 1/1440")]
for ax,(n,r,title) in zip(axs.ravel(),specs):panel(ax,n,r,title)
fig.suptitle("Thermal oscillator vacuum graphs: quartic (circle) and sextic (square) vertices",fontsize=14)
fig.supxlabel("Each line is G(tau - tau prime), each self-loop is G(0); integrate each vertex from 0 to beta.",fontsize=11)
save(fig)
