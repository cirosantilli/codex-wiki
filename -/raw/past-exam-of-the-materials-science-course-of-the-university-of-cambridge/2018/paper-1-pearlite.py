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

theta=np.pi/6;period=1.;ridge=.17;etch=.15
x=np.linspace(-.1,3.4,1800);u=x%period
h=np.where(u<ridge,0,np.where(u>period-etch/np.tan(theta),(u-period)*np.tan(theta),-etch))
y=np.linspace(-.8,.15,550);X,Y=np.meshgrid(x,y)
phase=((X-Y/np.tan(theta))%period)<ridge
solid=Y<=h[None,:]
image=np.ones((*phase.shape,3));image[solid & ~phase]=[.80,.86,.90];image[solid & phase]=[.40,.47,.54]
fig,axs=plt.subplots(2,1,figsize=(9,5.8),layout="constrained")
ax=axs[0];ax.imshow(image,origin="lower",extent=(x[0],x[-1],y[0],y[-1]),aspect="auto");ax.plot(x,h,color="#253858",lw=1.6);ax.axhline(0,color="#999999",ls="--",lw=1)
ax.set(ylim=(-.8,.18),xlim=(0,3),ylabel="Depth (micrometers)",title="Inclined cementite plates after preferential ferrite etching")
ax.plot([.55,.55],[0,-.57],color="#a35012",ls=":");ax.plot([.55,1.42],[-.5,0],color="#a35012",lw=1.2)
ax.text(.5,-.66,"Surface normal",fontsize=8);ax.text(1.04,-.22,"60 degrees to normal",fontsize=8,rotation=22)
ax.text(2.1,-.65,"Dark: cementite\nLight: ferrite",fontsize=9)
xx=x[::3];hh=h[::3];R=.04
accessible=np.max(hh[None,:]-(xx[:,None]-xx[None,:])**2/(2*R),axis=1)
ax=axs[1];ax.plot(x,h,color="#253858",label="Ideal top-accessible etched surface");ax.plot(xx,accessible,color="#a35012",label="Illustrative finite-tip envelope")
ax.set(xlim=(0,3),ylim=(-.18,.035),xlabel="Surface position (micrometers)",ylabel="Relative height (micrometers)",title="Inclined faces and tip shape change apparent ridge widths")
ax.legend(fontsize=8,loc="lower right");ax.grid(alpha=.15)
fig.suptitle("Synthetic geometry: phase fraction0.17, not a reproduction of the source AFM trace")
finish(fig,"paper-1-pearlite.png")
