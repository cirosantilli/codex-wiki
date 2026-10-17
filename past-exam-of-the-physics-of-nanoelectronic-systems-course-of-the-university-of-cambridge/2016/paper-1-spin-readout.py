"""Original explanatory model/schematic; no source figure or data copied.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes its same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle,FancyArrowPatch
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})

fig,axes=plt.subplots(1,2,figsize=(8.7,3.7),constrained_layout=True)
ax=axes[0]
ax.plot([0,1],[0,0],color=".3",lw=2);ax.text(.5,-.1,"Reservoir",ha="center",fontsize=9)
ax.plot([2,3],[.45,.45],color="#ba492c",lw=2);ax.text(3.08,.45,"Excited spin",va="center",fontsize=9,color="#ba492c")
ax.plot([2,3],[-.45,-.45],color="#2466a5",lw=2);ax.text(3.08,-.45,"Ground spin",va="center",fontsize=9,color="#2466a5")
ax.axhline(0,color=".65",ls="--",lw=1)
ax.annotate("",xy=(.85,.05),xytext=(2,.45),arrowprops=dict(arrowstyle="->",color="#ba492c",lw=1.6))
ax.annotate("",xy=(2,-.45),xytext=(.85,-.05),arrowprops=dict(arrowstyle="->",color="#2466a5",lw=1.6))
ax.text(1.5,.7,"Escape then refill gives a charge pulse",ha="center",fontsize=9)
ax.text(1.5,-.78,r"$\mu_g<\mu_{res}<\mu_e$",ha="center",fontsize=11)
ax.set(xlim=(-.2,4.5),ylim=(-1,1),title="Single-dot energy-selective readout");ax.axis("off")
ax=axes[1]
for y,label,col,outcome in [(.5,"Singlet","#2466a5","(0,2): transfer"),(-.5,"Triplet","#ba492c","(1,1): blocked")]:
    for x in [.4,1.2]:ax.add_patch(Circle((x,y),.17,facecolor="#ededed",edgecolor=".4"))
    ax.scatter([.4,1.2],[y,y],s=27,c=col,zorder=5)
    ax.text(.8,y+.28,label+" (1,1)",ha="center",fontsize=9,color=col)
    ax.annotate("",xy=(2.13,y),xytext=(1.55,y),arrowprops=dict(arrowstyle="->"if y>0 else"-[",color=col,lw=1.8))
    ax.text(2.2,y,outcome,va="center",fontsize=10,color=col)
ax.text(1.9,-.95,"Only the (0,2) singlet is energetically accessible",ha="center",fontsize=8)
ax.set(xlim=(0,4),ylim=(-1.15,1.15),title="Double-dot spin-to-charge conversion");ax.axis("off")

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
