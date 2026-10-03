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
poly([(0,0),(2,2),(4,0),(2,-2)],"#edf4ff")
poly([(0,0),(-2,2),(-4,0),(-2,-2)],"#edf4ff")
poly([(0,0),(2,2),(0,4),(-2,2)],"#e6f4eb")
poly([(0,0),(2,-2),(0,-4),(-2,-2)],"#f3f3f3")
poly([(2,2),(0,4),(2,6)],"#fff1dc")
poly([(-2,2),(0,4),(-2,6)],"#fff1dc")
line([(-2,2),(0,4),(2,2)],"#bb3322",lw=2.3)
line([(2,2),(2,6)],"#222222",lw=3)
line([(-2,2),(-2,6)],"#222222",lw=3)
line([(-3.8,0),(3.8,0)],"#4167aa","--",1.7)
line([(-2,6),(0,8),(2,6)],"#777777","--")
label(0,2,"trapped region\n$r_-<r<r_+$")
label(2.25,.25,"exterior")
label(-2.25,.25,"exterior")
label(0,-2,"past white-hole block")
label(1.35,4.15,"$0<r<r_-$")
label(-1.35,4.15,"$0<r<r_-$")
label(0,.35,r"$\Sigma$",color="#4167aa")
label(.85,3.4,r"$H^+(\Sigma):\ r=r_-$",color="#aa2211",rotation=-45,fontsize=9)
label(1,.8,r"$r=r_+$",rotation=45,fontsize=9)
label(2.25,5,r"$r=0$",rotation=90)
label(-2.25,5,r"$r=0$",rotation=90)
label(3.3,1.1,r"$\mathcal{I}^+$",fontsize=12)
label(-3.3,1.1,r"$\mathcal{I}^+$",fontsize=12)
label(0,6.9,"further analytic blocks",color="#666666")
ax.set_xlim(-4.8,4.8);ax.set_ylim(-4.5,7.6);ax.set_aspect("equal");ax.axis("off")
ax.set_title("Reissner–Nordstrom: outer and Cauchy horizons")
fig.subplots_adjust(left=.04,right=.96,top=.90,bottom=.08)
fig.text(.5,.025,"One repeating nonextremal block; thick vertical lines are timelike singularities.",ha="center",fontsize=9)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
plt.close(fig)
