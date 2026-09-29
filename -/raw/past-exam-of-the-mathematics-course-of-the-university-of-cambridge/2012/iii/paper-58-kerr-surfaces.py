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
fig,ax=plt.subplots(figsize=(7.2,5.6),facecolor="white")
M=1.;a=.8;rp=M+np.sqrt(M*M-a*a);th=np.linspace(0,2*np.pi,900)
re=M+np.sqrt(M*M-a*a*np.cos(th)**2)
xh=np.sqrt(rp*rp+a*a)*np.sin(th);zh=rp*np.cos(th)
xe=np.sqrt(re*re+a*a)*np.sin(th);ze=re*np.cos(th)
ax.fill(xe,ze,color="#ffdfb3",alpha=.75,label="ergoregion")
ax.fill(xh,zh,color="#c9d9ee")
ax.plot(xe,ze,color="#b25b10",lw=2.2,label="outer stationary limit")
ax.plot(xh,zh,color="#22559a",lw=2.2,label="event horizon")
ax.scatter([0,0],[rp,-rp],color="#333333",s=23,zorder=5)
ax.axvline(0,color="#777777",ls="--",lw=1)
ax.annotate("intersection at poles",xy=(0,rp),xytext=(.35,2.08),arrowprops={"arrowstyle":"->"},fontsize=9)
ax.text(0,0,"horizon interior",ha="center")
ax.set_aspect("equal");ax.set_xlim(-2.6,2.6);ax.set_ylim(-2.5,2.5)
ax.set_xlabel("oblate Cartesian $x/M$");ax.set_ylabel("$z/M$")
ax.set_title("Kerr horizon and ergosphere ($a/M=0.8$)")
ax.legend(loc="lower right",fontsize=9);ax.grid(alpha=.12)
fig.subplots_adjust(left=.12,right=.97,top=.88,bottom=.15)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
plt.close(fig)
