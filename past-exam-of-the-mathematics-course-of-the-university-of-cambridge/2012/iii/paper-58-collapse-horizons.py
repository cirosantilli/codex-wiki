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
fig,ax=plt.subplots(figsize=(8,5.2),facecolor="white")
v=np.linspace(-4,2.6,400);r=np.where(v<0,2+v/2,2)
ax.fill_betweenx(np.linspace(0,2.6,100),0,2,color="#eeeeee")
ax.axhline(0,color="#555555",lw=2,label="ingoing shell: $v=0$")
ax.plot(r,v,color="#be3527",lw=2.7,label="event horizon")
ax.plot([2,2],[0,2.6],color="#215cac",ls="--",lw=2.2,label="apparent horizon after the shell")
for start in [-4.8,-3,-1.8]:
    vv=np.linspace(start,0,100);rr=(vv-start)/2
    ax.plot(rr,vv,color="#9e9e9e",lw=1)
ax.text(2.8,-2.2,"flat region\nno apparent horizon",ha="center")
ax.text(.65,1.8,"trapped\nregion",ha="center")
ax.annotate("horizon begins before shell",xy=(0,-4),xytext=(1.2,-4.6),arrowprops={"arrowstyle":"->"},fontsize=9)
ax.set_xlim(0,4);ax.set_ylim(-5,3)
ax.set_xlabel("$r/M$");ax.set_ylabel("$v/M$")
ax.set_title("Thin-shell collapse in ingoing Finkelstein coordinates")
ax.legend(loc="upper right",fontsize=9);ax.grid(alpha=.15)
fig.subplots_adjust(left=.10,right=.97,top=.89,bottom=.14)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
plt.close(fig)
