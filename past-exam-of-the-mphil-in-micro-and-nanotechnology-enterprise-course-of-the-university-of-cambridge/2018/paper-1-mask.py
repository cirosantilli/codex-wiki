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

xx=np.linspace(-40,220,1300);yy=np.linspace(-12,108,600);X,Y=np.meshgrid(xx,yy)
def covered(shift=(0,0)):
    inside=np.zeros_like(X,dtype=bool)
    for i in range(-2,5):
        for j in range(-4,6):
            cx=i*(70+15*np.sqrt(3))+shift[0];cy=i*15+j*30+shift[1]
            dx=np.maximum(np.abs(X-cx)-35,0)
            inside|=dx*dx+(Y-cy)**2<=15**2
    return inside
mask=covered();open1=~mask;open2=open1 & ~covered((2,0))
fig,axs=plt.subplots(3,1,figsize=(8.5,6),layout="constrained")
from matplotlib.colors import ListedColormap
for ax,data,title,cmap in zip(axs,[mask,open1,open2],["Projected dense parallel rounded-rod mask","Metal islands through one layer","Two layers: second shifted 2 nm horizontally"],[ListedColormap(["white","#9aa4af"]),ListedColormap(["white","#a95d04"]),ListedColormap(["white","#007f91"])],strict=True):
    ax.imshow(data,origin="lower",extent=(xx[0],xx[-1],yy[0],yy[-1]),cmap=cmap,interpolation="nearest")
    ax.set(xlim=(-15,200),ylim=(0,90),ylabel="y (nm)",title=title);ax.set_aspect("equal")
axs[-1].set_xlabel("x (nm); one explicitly specified packing and normal rays")
finish(fig,"paper-1-mask.png")
