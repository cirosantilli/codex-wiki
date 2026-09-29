"""Stresslet directions; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Only writes the PNG basename to cwd; leaves MPLCONFIGDIR to the caller.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

x=np.linspace(-2,2,17)
X,Z=np.meshgrid(x,x)
r2=X*X+Z*Z
safe=np.maximum(r2,.04)
fig,axes=plt.subplots(1,2,figsize=(10.4,4.4),dpi=100,facecolor="white")
for ax,S,along,title in zip(axes,[1.,-.5],["x","z"],[
        r"Instantaneous pusher: $S>0,\ \mathbf{e}=\hat{\mathbf{x}}$",
        r"Leading mean puller: $\widetilde S=-S/2,\ \widetilde{\mathbf{e}}=\hat{\mathbf{z}}$"]):
    projection=X if along=="x" else Z
    factor=S*(3*projection*projection/safe-1)
    ux=factor*X/safe**1.5
    uz=factor*Z/safe**1.5
    speed=np.hypot(ux,uz)
    mask=(r2<.12)|(speed<1e-6)
    ux=np.ma.masked_where(mask,ux/np.maximum(speed,1e-12))
    uz=np.ma.masked_where(mask,uz/np.maximum(speed,1e-12))
    ax.quiver(X,Z,ux,uz,color="#2166ac",angles="xy",scale_units="xy",scale=7,
              width=.004,headwidth=3.7,headlength=4.8,pivot="mid")
    ax.add_patch(Circle((0,0),.34,facecolor="#eeeeee",edgecolor="#aaaaaa",zorder=3))
    if along=="x":ax.plot([-.24,.24],[0,0],color="#333333",linewidth=4,zorder=4)
    else:ax.plot([0,0],[-.24,.24],color="#333333",linewidth=4,zorder=4)
    ax.set(xlim=(-2.15,2.15),ylim=(-2.15,2.15),xlabel="x",ylabel="z",title=title)
    ax.set_aspect("equal")
    ax.axhline(0,color="0.85",linewidth=.6,zorder=0)
    ax.axvline(0,color="0.85",linewidth=.6,zorder=0)
    ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks([-2,-1,0,1,2])
fig.text(.5,.015,"Arrows show velocity direction in an x–z section. Gray cores exclude the singular origin.",ha="center",fontsize=9)
fig.tight_layout(rect=(0,.03,1,1),pad=1.3)
fig.savefig(Path.cwd()/"paper-80-stresslet-average.png",dpi=100,facecolor="white",transparent=False)
plt.close(fig)
