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

fig,ax=plt.subplots(figsize=(8.5,5.4),layout="constrained")
ax.add_patch(Rectangle((0,0),10,6,fc="#e9eef1",ec="#253858",lw=1.5))
for x in np.arange(-2,12,.40):
 ax.add_patch(Polygon([[x,0],[x+.10,0],[x+2.10,6],[x+2,6]],closed=True,fc="#a35012",ec="none",clip_on=True))
primary=[np.array([[.5,.6],[2.4,.6],[2.8,1.9],[2.1,3.1],[.8,3.4],[.3,2.0]]),np.array([[4.7,2.6],[6.2,1.3],[7.9,2.1],[8.7,3.8],[7.9,5.2],[6.3,5.6],[5,4.7]])]
for p in primary:ax.add_patch(Polygon(p,fc="#ffffff",ec="#253858",lw=1.7,zorder=3))
for x,y in [(1,1),(1.5,2.4),(2.1,1.4),(5.6,3.3),(6.5,4.8),(7.8,3.6),(6.9,2.9)]:ax.add_patch(Circle((x,y),.07,fc="#a35012",zorder=4))
ax.text(1.55,2,"Primary\nAg phase",ha="center",fontsize=10,zorder=6);ax.text(6.8,4,"Primary Ag",ha="center",fontsize=11,zorder=6)
ax.text(3.75,5.6,"Lamellar eutectic\nAg + Cu",ha="center",fontsize=10,bbox=dict(fc="white",ec="none",alpha=.85))
ax.text(4.6,.48,"Small Cu precipitates may develop\nas Ag loses solid solubility",ha="center",fontsize=9,bbox=dict(fc="white",ec="none",alpha=.9))
ax.set(xlim=(-.1,10.1),ylim=(-.1,6.1),aspect="equal",title="Original schematic room-temperature constituent arrangement")
ax.axis("off");fig.supxlabel("White/light: Ag   |   Brown: Cu   |   Drawing area is not a mass-fraction measurement",fontsize=9)
finish(fig,"paper-1-ag-cu-microstructure.png")
