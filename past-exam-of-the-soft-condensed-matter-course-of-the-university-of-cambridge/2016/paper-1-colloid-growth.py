"""Original explanatory model; no exam image or experimental points copied.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes its same-basename PNG to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})

x=np.linspace(.055,8,1500)
r=np.linspace(1,7,700)
fig,axes=plt.subplots(1,2,figsize=(8.6,3.5),constrained_layout=True)
for k,color,label in [(1.,"#2466a5","Longer-range repulsion"),(3.,"#ba492c","Shorter-range repulsion")]:
    u=12*np.exp(-k*x)-2/x
    axes[0].plot(x,u,color=color,lw=2,label=label)
axes[0].axhline(0,color=".55",lw=.8)
axes[0].set(xlim=(0,8),ylim=(-8,6),xlabel="Surface gap (arbitrary length)",ylabel="Pair potential (arbitrary energy)",title="Qualitative barrier, not fitted data")
axes[0].legend(fontsize=8,loc="lower right")
axes[1].plot(r,1-1/r,color="#347748",lw=2)
axes[1].axhline(1,color=".55",ls="--",lw=1,label="Reservoir limit")
axes[1].scatter([1],[0],color="#347748",zorder=4)
axes[1].set(xlim=(1,7),ylim=(-.03,1.08),xlabel=r"Distance $r/a$",ylabel=r"$(c-c_s)/(c_\infty-c_s)$",title="Quasi-steady exterior concentration")
axes[1].legend(fontsize=8,loc="lower right")
for ax in axes:ax.grid(alpha=.18)

fig.savefig(Path(__file__).stem + ".png", dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
