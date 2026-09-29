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

q=np.linspace(0,3,400)
fig,axs=plt.subplots(1,3,figsize=(10.5,4.2),layout="constrained")
for ax,m in zip(axs,[1,0,-1],strict=True):
 en=np.sqrt(q*q+m*m);ax.plot(q,en,color="#253858",lw=2);ax.plot(q,-en,color="#a35012",lw=2)
 ax.axhline(0,color="#aaaaaa",lw=.8)
 ax.set(xlim=(0,3),ylim=(-3.4,3.4),xlabel=r"$\hbar ck$ (energy units)",title=f"Mass coefficient V = {m:+d}")
 ax.grid(alpha=.15)
 if m:
  ax.annotate("",xy=(0,1),xytext=(0,-1),arrowprops=dict(arrowstyle="<->",color="#007f91",lw=1.5))
  ax.text(.15,.05,r"Gap $2|V|$",fontsize=9,color="#007f91")
  ax.text(.25,2.65,"Upper-band spin at k=0:\n"+("+z" if m>0 else "-z"),fontsize=9)
 else:ax.text(.22,2.65,"Branches meet at the origin",fontsize=9)
axs[0].set_ylabel("Energy")
fig.supxlabel("Opposite masses of equal magnitude have identical energies, but different spinors",fontsize=10)
finish(fig,"paper-1-dirac-bands.png")
