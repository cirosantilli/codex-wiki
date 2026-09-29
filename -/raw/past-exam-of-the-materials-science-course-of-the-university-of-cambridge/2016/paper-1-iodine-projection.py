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

fig,ax=plt.subplots(figsize=(6.5,7.4),layout="constrained")
b,c=.480,.978;bond=.267;dy=bond*np.sin(np.pi/6)/2;dz=bond*np.cos(np.pi/6)/2
ax.add_patch(Rectangle((0,0),b,c,fc="#f8fafb",ec="#253858",lw=1.5))
centers=[(0,0,0,"A"),(.5,0,.5,"A"),(0,.5,.5,"B"),(.5,.5,0,"B")]
for y0,z0,h,label in centers:
 for j in [-1,0,1]:
  for k in [-1,0,1]:
   y,z=y0+j,z0+k
   if not (0<=y<=1 and 0<=z<=1):continue
   color="#253858" if h==0 else "#a35012"
   sign=-1 if label=="A" else 1
   xs=np.array([y*b-dy,y*b+dy]);ys=np.array([z*c-sign*dz,z*c+sign*dz])
   ax.plot(xs,ys,color=color,lw=3,zorder=3)
   ax.scatter(xs,ys,color=color,s=65,zorder=4)
   ax.text(y*b+.016,z*c+.017,f"{label}: x/a={h:g}",fontsize=8,color=color,zorder=6)
for y in [.25,.75]:ax.axvline(y*b,color="#007f91",ls="--",lw=1.1)
for z in [.25,.75]:ax.axhline(z*c,color="#8b3a82",ls="-.",lw=1.1)
for y in [.25,.75]:
 for z in [0,.5,1]:
  ax.scatter([y*b],[z*c],marker="D",s=32,c="#111111",zorder=7)
ax.set(xlim=(-.10,b+.17),ylim=(-.17,c+.17),xlabel=r"$y$ (nm), direction [010]",ylabel=r"$z$ (nm), direction [001]",title="Calculated iodine projection and symmetry traces")
ax.set_aspect("equal");fig.supxlabel("Dashed vertical: c-glide\nDash-dot horizontal: a-glide\nDiamonds: 2_1 axes along the view",fontsize=9)
finish(fig,"paper-1-iodine-projection.png")
