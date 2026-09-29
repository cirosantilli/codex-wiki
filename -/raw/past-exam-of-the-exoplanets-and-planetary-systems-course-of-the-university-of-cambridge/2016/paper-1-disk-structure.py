"""Original explanatory diagram; no exam or published illustration copied.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes a same-basename PNG to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})

fig,axes=plt.subplots(1,2,figsize=(8.8,3.8),gridspec_kw={"width_ratios":[1.45,1]},constrained_layout=True)
r=np.linspace(.35,5,500);hg=.06*r**1.25;hd=.23*hg
ax=axes[0]
ax.fill_between(r,-hg,hg,color="#b8d9f0",alpha=.9,label="Gas layer")
ax.fill_between(r,-hd,hd,color="#b77948",alpha=.9,label="Settled larger grains")
ax.plot(r,hg,color="#2466a5",lw=1.5);ax.plot(r,-hg,color="#2466a5",lw=1.5)
ax.plot([0,5.2],[0,0],color=".4",lw=.6)
ax.axvline(2.8,color="#347748",ls="--",lw=1.3)
ax.text(2.87,-.7,"Water-ice boundary\n(position schematic)",fontsize=9,color="#347748")
ax.scatter([.1],[0],s=180,c="#e6ac28",marker="*",zorder=5)
ax.text(.1,.16,"Star",ha="center",fontsize=9)
ax.text(3.7,.49,"Irradiated surface",ha="center",fontsize=9)
ax.text(1.2,-.31,"Refractory grains",ha="center",fontsize=9)
ax.text(4.1,-.31,"Grains + ices",ha="center",fontsize=9)
ax.set(xlim=(-.1,5.3),ylim=(-.86,.86),xlabel="Radius: hotter inner disk → cooler outer disk",ylabel="Height (schematic)",title="Flared disk cross-section",xticks=[],yticks=[])
ax.legend(loc="upper left",fontsize=8)
z=np.linspace(-3,3,800)
axes[1].plot(np.exp(-z*z/2),z,color="#2466a5",lw=2,label="Isothermal gas")
axes[1].plot(np.exp(-z*z/(2*.23**2)),z,color="#b77948",lw=2,label="Narrower dust layer")
axes[1].axhline(0,color=".65",lw=.7)
axes[1].set(xlim=(0,1.05),ylim=(-3,3),xlabel=r"Density / own midplane density",ylabel=r"Height $z/H_g$",title="Illustrative vertical profiles")
axes[1].legend(fontsize=8)
axes[1].grid(alpha=.15)

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
