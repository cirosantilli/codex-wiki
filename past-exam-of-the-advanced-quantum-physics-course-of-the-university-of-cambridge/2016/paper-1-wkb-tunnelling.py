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

fig,axs=plt.subplots(1,2,figsize=(10,4.5),layout="constrained")
x=np.linspace(-3,3,1200);V=np.exp(-x*x);E=.4;turn=np.sqrt(-np.log(E))
ax=axs[0];ax.plot(x,V,lw=2,color="#253858",label="Smooth barrier");ax.axhline(E,color="#a35012",lw=1.4,label="Particle energy")
ax.fill_between(x,E,V,where=V>E,color="#e5ba54",alpha=.45)
for xx,label in [(-turn,r"$x_1$"),(turn,r"$x_2$")]:
 ax.axvline(xx,color="#777777",ls=":",lw=1);ax.text(xx,.04,label,ha="center",fontsize=11)
ax.text(0,.76,"Forbidden\nregion",ha="center",fontsize=11)
ax.text(-2,.54,"Allowed",ha="center",fontsize=9);ax.text(2,.54,"Allowed",ha="center",fontsize=9)
ax.set(xlim=(-3,3),ylim=(0,1.12),xlabel="Position (relative units)",ylabel="Energy (relative units)",title="Original barrier and action construction");ax.legend(fontsize=8,loc="upper right")
ax=axs[1];S=np.linspace(0,5,400);ax.semilogy(S,np.exp(-2*S),lw=2,color="#007f91")
ax.axvspan(0,1,color="#eeeeee");ax.text(.12,.004,"Small action:\nleading opaque-barrier\nformula not reliable",fontsize=8)
ax.set(xlim=(0,5),ylim=(2e-5,1.2),xlabel=r"Forbidden action $S_B/\hbar$",ylabel="Leading transmission probability",title=r"$T\simeq\exp(-2S_B/\hbar)$")
ax.grid(alpha=.2)
finish(fig,"paper-1-wkb-tunnelling.png")
