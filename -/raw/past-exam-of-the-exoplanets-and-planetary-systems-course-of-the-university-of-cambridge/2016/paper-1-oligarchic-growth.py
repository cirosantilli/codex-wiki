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

fig,axes=plt.subplots(1,2,figsize=(8.8,3.7),gridspec_kw={"width_ratios":[1,1.1]},constrained_layout=True)
ax=axes[0];rng=np.random.default_rng(2016)
colors=["#e3eff8","#e3f0e8","#fcf0db"]
for j,(a,col) in enumerate(zip([1,2,3],colors)):
    ax.axvspan(a-.43,a+.43,color=col)
    ax.scatter([a],[0],s=150,color="#2466a5",zorder=5,label="Embryos" if j==0 else None)
    ax.text(a,-.74,f"Feeding zone {j+1}",ha="center",fontsize=9)
x=rng.uniform(.5,3.5,115);y=rng.uniform(-.45,.45,115)
mask=np.abs(y)>.08
ax.scatter(x[mask],y[mask],s=4,c=".35",alpha=.7,label="Small planetesimals")
ax.set(xlim=(.4,3.6),ylim=(-.95,.95),xlabel="Orbital radius (schematic; widths not to scale)",yticks=[],xticks=[],title="Several embryos share a solid reservoir")
ax.legend(fontsize=8,loc="upper center")
m=np.logspace(-1,2,600)
axes[1].loglog(m,m**(1/3),color="#ba492c",lw=2,label="Runaway: fixed background speed")
axes[1].loglog(m,m**(-1/3),color="#2466a5",lw=2,label="Illustrative self-regulated growth")
axes[1].set(xlim=(.1,100),ylim=(.17,6),xlabel=r"Embryo mass $M/M_0$",ylabel=r"Relative fractional growth $(\dot M/M)/(\dot M/M)_0$",title="Stirring changes the mass advantage")
axes[1].grid(alpha=.17)
axes[1].legend(fontsize=8,loc="upper left")

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
