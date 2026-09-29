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

y=np.linspace(-4,4,1400);xi_minus=1.4;xi_plus=.7;f=np.where(y<0,np.exp(y/xi_minus),np.exp(-y/xi_plus))
fig,axs=plt.subplots(1,3,figsize=(12,4.5),layout="constrained")
ax=axs[0];ax.plot(y,f,lw=2,color="#253858",label="Amplitude / peak");ax.plot(y,f*f,lw=1.5,ls="--",color="#a35012",label="Density / peak")
ax.axvline(0,color="#aaaaaa",ls=":");ax.text(-3.6,.82,r"$V_-<0$",fontsize=11);ax.text(1.7,.82,r"$V_+>0$",fontsize=11)
ax.set(xlabel="Transverse position y (relative units)",ylabel="Normalized profile",title="Original asymmetric step-mass mode",ylim=(0,1.1));ax.legend(fontsize=8,loc="upper right")
ax=axs[1];k=np.linspace(-2.8,2.8,300);ax.plot(k,-k,color="#007f91",lw=2)
ax.axhline(0,color="#aaaaaa",lw=.8);ax.axvline(0,color="#aaaaaa",lw=.8);ax.text(-2.4,1.6,r"Slope $-\hbar c$",fontsize=11)
ax.set(xlabel=r"Longitudinal wavevector $k_x$ (relative units)",ylabel="Energy (relative units)",title="A single chiral interface branch",xlim=(-2.8,2.8),ylim=(-2.8,2.8));ax.grid(alpha=.15)
ax=axs[2];x=np.linspace(-6,4,600)
for t,color in [(0,"#253858"),(1.5,"#a35012"),(3,"#8b3a82")]:
 ax.plot(x,np.exp(-(x+t)**2),color=color,label=f"ct = {t:g}")
ax.annotate("",xy=(-4.6,.72),xytext=(-2.7,.72),arrowprops=dict(arrowstyle="->",color="#111111",lw=1.3))
ax.text(-4.4,.8,"Rigid motion",fontsize=9)
ax.set(xlabel="Longitudinal position x (relative units)",ylabel="Packet density (relative units)",title=r"$g(x+ct)$ travels towards negative x",ylim=(0,1.15));ax.legend(fontsize=8,loc="upper right")
fig.supxlabel("The transverse profile stays fixed; the longitudinal velocity is -c and the transverse current is zero",fontsize=10)
finish(fig,"paper-1-dirac-interface.png")
