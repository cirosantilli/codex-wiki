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

k=np.sqrt(1-10**(-.005/2.5))
fig,axes=plt.subplots(1,2,figsize=(8.2,3.7),constrained_layout=True)
for ax,b in zip(axes,[0.,.8]):
    x14=np.sqrt((1+k)**2-b*b);x0=np.sqrt(1-b*b)
    ax.add_patch(Circle((0,0),1,facecolor="#f7dda0",edgecolor="#a86e13",lw=1.5))
    ax.add_patch(Circle((0,0),1+k,fill=False,edgecolor=".7",ls=":",lw=1))
    ax.plot([-1.25,1.25],[b,b],color="#2466a5",lw=1.5)
    for x in [-x14,0,x14]:
        ax.add_patch(Circle((x,b),k,facecolor="#2466a5" if x==0 else "white",edgecolor="#2466a5",lw=1.5))
    ax.annotate("",xy=(x14,b+.19),xytext=(-x14,b+.19),arrowprops=dict(arrowstyle="<->",color="#2466a5",lw=1.5))
    ax.text(0,b+.23,r"Finite-radius contact span",ha="center",va="bottom",fontsize=9,color="#2466a5")
    ax.plot([-x0,x0],[b-.16,b-.16],color=".25",lw=2)
    ax.text(0,b-.2,"Point-centre span",ha="center",va="top",fontsize=9,color=".25")
    ax.plot([0,0],[0,b],color=".45",ls="--",lw=1)
    ax.set(xlim=(-1.32,1.32),ylim=(-1.2,1.5),aspect="equal",title=rf"$b={b:g}$, $R_p/R_\star={k:.4f}$")
    ax.axis("off")
fig.suptitle("Straight-track sky projection: contact conventions matter",fontsize=12)

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
