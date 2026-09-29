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

a=.348;lam=.1937;N=np.array([3,4,8,11,12]);labels=["111","200","220","311","222"]
chi=2*np.arcsin(lam*np.sqrt(N)/(2*a))
fig,axs=plt.subplots(2,1,figsize=(11,5.7),layout="constrained",gridspec_kw={"height_ratios":[2,1]})
ax=axs[0];h=np.linspace(-.23,.23,400)
colors=["#253858","#007f91","#a35012","#8b3a82","#5b7028"]
for th,label,color in zip(chi,labels,colors,strict=True):
 phi=np.degrees(np.arccos(np.cos(th)*np.sqrt(1+h*h)))
 for sgn in [-1,1]:ax.plot(sgn*phi,h,color=color,lw=1.8)
 ax.text(np.degrees(th),.245,label,ha="center",fontsize=9,color=color)
for p in [-180,0,180]:ax.axvline(p,color="#999999",ls=":",lw=1.2)
ax.text(0,-.30,"Forward-beam hole",ha="center",fontsize=8);ax.text(-180,-.30,"Incident hole",ha="left",fontsize=8)
ax.set(xlim=(-184,184),ylim=(-.34,.31),xlabel="Angle around cylindrical film (degrees)",ylabel=r"Height / camera radius",title="Original unwrapped-film geometry; intensities not modeled",yticks=[])
ax=axs[1]
ax.hlines(0,0,180,color="#aaaaaa")
for th,label,color in zip(chi,labels,colors,strict=True):
 t=np.degrees(th);ax.vlines(t,0,1,color=color,lw=2);ax.text(t,1.08,f"{label}\n{t:.1f} deg",ha="center",fontsize=9,color=color)
ax.axvspan(90,180,color="#e5edf5",alpha=.5)
ax.set(xlim=(0,180),ylim=(0,1.6),xlabel=r"Scattering angle $2\theta$ (degrees)",yticks=[],title="Forward reflections below 90 degrees; back reflections above 90 degrees")
finish(fig,"paper-1-diffraction-camera.png")
