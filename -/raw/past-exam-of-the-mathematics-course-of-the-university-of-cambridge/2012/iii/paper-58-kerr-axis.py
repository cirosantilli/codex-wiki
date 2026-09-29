"""Original schematic for Paper 58. Python 3.14; root matplotlib/numpy dependencies.
Caller supplies MPLCONFIGDIR; output is this script's basename PNG in cwd only.
"""
from pathlib import Path
import os
if not os.environ.get("MPLCONFIGDIR"):
    raise RuntimeError("Set MPLCONFIGDIR to a caller-owned writable cache directory")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
plt.rcParams.update({"font.size": 10, "axes.titlesize": 13})
fig,ax=plt.subplots(figsize=(8,6),facecolor="white")
def poly(points, color="white", edge="#333333", alpha=1):
    ax.add_patch(Polygon(points, closed=True, facecolor=color, edgecolor=edge, lw=1.4, alpha=alpha))
def line(points, color="#333333", style="-", lw=1.5):
    xs,ys=zip(*points);ax.plot(xs,ys,color=color,ls=style,lw=lw)
def label(x,y,s,**kw): ax.text(x,y,s,ha="center",va="center",**kw)
poly([(0,0),(2,2),(4,0),(2,-2)],"#e8f1ff")
poly([(0,0),(-2,2),(-4,0),(-2,-2)],"#e8f1ff")
poly([(0,0),(2,2),(0,4),(-2,2)],"#e6f4eb")
poly([(0,4),(2,6),(4,4),(2,2)],"#fff0d9")
poly([(0,4),(-2,6),(-4,4),(-2,2)],"#fff0d9")
line([(0,0),(2,2)],"#315b9b",lw=2)
line([(-2,2),(0,4),(2,2)],"#bb4b2a",lw=2)
line([(2,2),(2,6)],"#777777","--")
line([(-2,2),(-2,6)],"#777777","--")
line([(-2,6),(0,8),(2,6)],"#777777","--")
pts=[(1.8,-.5),(.9,1.4),(1.4,2.8),(2.5,4.5),(2,5.95)]
line(pts,"#97269a",lw=2.4)
ax.annotate("",xy=(2.12,5.63),xytext=(2.42,4.72),arrowprops={"arrowstyle":"->","color":"#97269a","lw":2})
label(2.5,0,"positive-$r$\nexterior",fontsize=9)
label(-2.4,0,"other exterior",fontsize=9)
label(0,2.2,"$r_-<r<r_+$")
label(2.7,3.7,"negative sheet",fontsize=9)
label(-2.7,4,"inner static\nextension",fontsize=9)
label(.55,3.8,r"$r=r_-$",rotation=-45,fontsize=9)
label(.9,.8,r"$r=r_+$",rotation=45,fontsize=9)
label(2.07,5.15,"$r=0$ regular",rotation=90,fontsize=8)
label(3.3,5.05,r"$\mathcal{I}^+_{r<0}$",fontsize=10)
label(0,6.9,"further horizon blocks",color="#666666")
ax.set_xlim(-4.7,4.7);ax.set_ylim(-2.6,7.6);ax.set_aspect("equal");ax.axis("off")
ax.set_title("Kerr symmetry axis: energetic continuation")
fig.subplots_adjust(left=.04,right=.96,top=.90,bottom=.08)
fig.text(.5,.025,"Axis restriction only: the off-axis ring is absent. Purple path is timelike.",ha="center",fontsize=9)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
plt.close(fig)
