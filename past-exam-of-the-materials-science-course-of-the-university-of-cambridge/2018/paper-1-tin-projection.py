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

fig,ax=plt.subplots(figsize=(7,6),layout="constrained")
colors=["#253858","#a35012","#007f91","#8b3a82"]
basis=[(0,0,0),(0,.5,.25),(.5,.5,.5),(.5,0,.75)]
for x in [0,1,2]:ax.axvline(x,color="#aab0b5",lw=1)
for y in [0,1,2]:ax.axhline(y,color="#aab0b5",lw=1)
for (bx,by,z),c in zip(basis,colors,strict=True):
    pts=[]
    for i in range(-1,3):
        for j in range(-1,3):
            x=i+bx;y=j+by
            if 0<=x<=2 and 0<=y<=2:pts.append((x,y))
    xx,yy=np.array(pts).T
    ax.scatter(xx,yy,s=100,c=c,label=rf"$z/c={z:g}$",zorder=3)
    for x,y in pts:ax.text(x+.055,y+.055,f"{z:g}",fontsize=8,color=c)
ax.set(xlim=(-.12,2.3),ylim=(-.12,2.2),xticks=[0,.5,1,1.5,2],yticks=[0,.5,1,1.5,2],xlabel=r"$x/a$",ylabel=r"$y/a$",title=r"Original [001] projection of beta-tin; $a=0.5831$ nm")
ax.set_aspect("equal");ax.legend(loc="center left",bbox_to_anchor=(1,.5),fontsize=9)

finish(fig,"paper-1-tin-projection.png")
