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

fig,axes=plt.subplots(1,2,figsize=(9,5.4),layout="constrained")
ax=axes[0];ax.set(xlim=(0,10),ylim=(0,12),title="Scanned transmitted-electron imaging");ax.axis("off")
for y,label in [(10.4,"Electron gun + accelerating supply"),(8.5,"Condenser / aperture / probe lens"),(6.6,"Scan coils: raster position"),(4.7,"Thin specimen on stable holder"),(2.8,"Transmitted-electron detectors"),(.9,"Synchronized pixels and display")]:
    box(ax,1,y,8,1.1,label,size=8.5)
for y in [10.4,8.5,6.6,4.7,2.8]:arrow(ax,(5,y),(5,y-.8))
ax.text(.1,6,"Vacuum\ncolumn",fontsize=8,rotation=90,ha="center",va="center")
ax=axes[1];ax.set(xlim=(0,10),ylim=(0,12),title="Contact AFM: constant-deflection mode");ax.axis("off")
box(ax,1,.9,8,.8,"Sample on x-y-z piezo scanner",fc="#d9d9d9")
ax.plot([2,7.2],[5.5,5.2],lw=4,color="#777777");ax.add_patch(Polygon([[6.7,5.25],[7.3,5.2],[7,1.7]],fc="#777777"))
ax.text(3.3,5.9,"Compliant cantilever + sharp tip",fontsize=8,ha="center")
box(ax,.4,9.1,2,1,"Laser",fc="#fff0d8");box(ax,7.3,9.1,2.2,1,"Position\ndetector",fc="#fff0d8")
arrow(ax,(2.1,9.1),(5.2,5.35));arrow(ax,(5.2,5.35),(7.7,9.1))
box(ax,3,7.4,3.7,1,"Deflection error\nrelative to setpoint")
arrow(ax,(7.5,9.1),(6.5,8.4));box(ax,3,3,3.3,1,"Feedback controller")
arrow(ax,(4.7,7.4),(4.7,4));arrow(ax,(4.7,3),(4.7,1.7))
ax.text(6.1,2.25,"z motion = height record",fontsize=8,ha="center")
finish(fig,"paper-1-microscopy.png")
