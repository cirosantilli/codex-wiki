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

x=np.linspace(0,1.1,550);eg=(1-np.sqrt(1+16*x*x))/2;mo=.5-2*x;Pd=.5*(1-1/np.sqrt(1+16*x*x))
fig,axs=plt.subplots(1,3,figsize=(12,4.3),layout="constrained")
ax=axs[0];ax.plot(x,mo,color="#253858",lw=2);ax.axhline(0,color="#777777",lw=1);ax.axvline(.25,color="#a35012",ls=":")
ax.scatter([.25],[0],color="#a35012",zorder=3);ax.text(.29,.08,"Trial energies equal",fontsize=8)
ax.set(xlim=(0,1.1),ylim=(-1.8,.65),xlabel=r"$|t|/U$",ylabel=r"$(E_\phi-E_\psi)/U$",title="Requested trial-energy difference");ax.grid(alpha=.15)
ax=axs[1];ax.plot(x,np.zeros_like(x),label="Covalent trial",color="#8b3a82");ax.plot(x,mo,label="Bonding-orbital trial",color="#253858");ax.plot(x,eg,label="Optimized two-state singlet",color="#007f91",lw=2)
ax.set(xlim=(0,1.1),ylim=(-1.8,.65),xlabel=r"$|t|/U$",ylabel=r"$(E-2E_0)/U$",title="Continuous ground-state interpolation");ax.grid(alpha=.15);ax.legend(fontsize=8)
ax=axs[2];ax.plot(x,Pd,color="#a35012",lw=2);ax.axhline(.5,color="#777777",ls="--")
ax.set(xlim=(0,1.1),ylim=(0,.55),xlabel=r"$|t|/U$",ylabel="Double-occupancy probability",title="Charge fluctuations are suppressed at small hopping")
ax.grid(alpha=.15)
fig.suptitle("Original calculation in the on-site-only two-center model",fontsize=13)
finish(fig,"paper-1-two-site-bond.png")
