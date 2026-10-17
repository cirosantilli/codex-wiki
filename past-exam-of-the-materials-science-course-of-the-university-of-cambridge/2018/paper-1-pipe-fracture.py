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

fig,axs=plt.subplots(1,3,figsize=(11,4),layout="constrained")
ax=axs[0];ax.set(xlim=(0,10),ylim=(0,10),title="Closed-end axial balance");ax.axis("off")
ax.add_patch(Circle((5,4.7),2.2,fc="#e5edf5",ec="#253858",lw=2));ax.add_patch(Circle((5,4.7),1.8,fc="white",ec="#253858",lw=1.2))
arrow(ax,(5,4.7),(6.8,4.7));ax.text(5.9,4.9,"r",fontsize=10)
arrow(ax,(5,6.5),(5,8.8));ax.text(5,9.05,r"$P\pi r^2$",ha="center",fontsize=12)
arrow(ax,(2.8,3),(2.8,1));arrow(ax,(7.2,3),(7.2,1));ax.text(5,.4,r"Wall force $\sigma_z 2\pi rt$",ha="center",fontsize=11)
ax=axs[1];ax.set(xlim=(0,10),ylim=(0,10),title="Longitudinal split: hoop balance");ax.axis("off")
box(ax,2,3,6,3,"Projected pressure area\n2rL",size=10)
arrow(ax,(5,6),(5,8.6));ax.text(5,9,r"$P(2rL)$",ha="center",fontsize=12)
for xx in [2.5,7.5]:arrow(ax,(xx,3),(xx,1.1))
ax.text(5,.5,r"Two wall forces $\sigma_\theta tL$",ha="center",fontsize=11)
ax=axs[2];r=np.linspace(.007,2,800);elastic=1/np.sqrt(r);plastic=2.5*(1-np.exp(-elastic/2.5))
ax.plot(r,elastic,"--",color="#888888",label="Elastic singular extrapolation");ax.plot(r,plastic,color="#007f91",label="Schematic ductile redistribution")
ax.axvspan(0,.13,color="#e5ba54",alpha=.25);ax.set(xlim=(0,2),ylim=(0,5),xlabel="Distance ahead of tip (relative)",ylabel="Tensile stress (relative)",title="Finite plastic process zone")
ax.legend(fontsize=7,loc="upper right");ax.grid(alpha=.15)
finish(fig,"paper-1-pipe-fracture.png")
