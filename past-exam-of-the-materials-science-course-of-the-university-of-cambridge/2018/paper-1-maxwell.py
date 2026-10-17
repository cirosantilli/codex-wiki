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

q=np.logspace(-3,3,1000);x=np.sqrt(q)
fig,axs=plt.subplots(1,2,figsize=(10,4.8),layout="constrained")
ax=axs[0];ax.semilogx(q,q/(1+q),color="#253858",label=r"Reference: $k=k_0,\ \tau=\tau_0$");ax.semilogx(q,1.2*.16*q/(1+.16*q),color="#a35012",label=r"Illustrative warmer: $1.2k_0,\ 0.4\tau_0$")
ax.axvline(1,color="#253858",ls=":");ax.axvline(6.25,color="#a35012",ls=":");ax.axhline(1,color="#253858",ls="--",alpha=.3);ax.axhline(1.2,color="#a35012",ls="--",alpha=.3)
ax.set(xlabel=r"Squared frequency $q=(\omega\tau_0)^2$",ylabel=r"Storage modulus $E'/k_0$",ylim=(0,1.3),title="Relaxation crossover and warmer curve")
ax.text(.0015,.32,"Dashpot-dominated",fontsize=8);ax.text(9,.55,"Spring-dominated",fontsize=8);ax.legend(fontsize=8,loc="lower right");ax.grid(alpha=.18)
ax=axs[1];ax.loglog(q,x/(1+x*x),label=r"Fixed strain: $W/(\pi k\varepsilon_0^2)$",color="#007f91");ax.loglog(q,1/x,label=r"Fixed stress: $W/(\pi\sigma_0^2/k)$",color="#8b3a82")
ax.axvline(1,color="#777777",ls=":");ax.scatter([1],[.5],color="#007f91",zorder=4)
ax.set(xlabel=r"Squared frequency $(\omega\tau)^2$",ylabel="Dissipated energy per cycle (normalized)",title="The imposed amplitude changes the loss law")
ax.legend(fontsize=8);ax.grid(alpha=.18)
finish(fig,"paper-1-maxwell.png")
