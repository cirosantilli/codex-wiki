"""Original explanatory figure; Python 3.14 and root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","axes.facecolor":"white"})

fig,axs=plt.subplots(1,3,figsize=(11.5,3.7),layout="constrained")
ax=axs[0];ax.plot([1,1],[1,2],color="#2e7d32",lw=2);x=np.linspace(1,15/8,200);ax.plot(x,3-x,color="#2e7d32",lw=2);x=np.linspace(15/8,2,60);ax.plot(x,3-x,color="#c62828",lw=3);ax.plot([2,1],[1,1],color="#c62828",lw=2)
for xy,label,off in [((1,1),"A",(-13,-14)),((1,2),"B",(-13,5)),((2,1),"C",(5,-10))]:ax.scatter(*xy,color="#222",s=18);ax.annotate(label,xy,xytext=off,textcoords="offset points")
ax.scatter([1.5],[1.5],color="#1565c0",zorder=5);ax.annotate("Highest T",(1.5,1.5),xytext=(1.56,1.72),arrowprops={"arrowstyle":"->"},fontsize=8)
ax.scatter([15/8],[9/8],color="#c62828",zorder=5);ax.annotate("Heat reverses",(15/8,9/8),xytext=(1.45,.8),arrowprops={"arrowstyle":"->"},fontsize=8)
ax.annotate("",(1,1.75),xytext=(1,1.35),arrowprops={"arrowstyle":"->","color":"#2e7d32"});ax.annotate("",(1.28,1),xytext=(1.7,1),arrowprops={"arrowstyle":"->","color":"#c62828"})
ax.set(xlabel=r"$V/V_0$",ylabel=r"$p/p_0$",title="Green: heat in; red: heat out",xlim=(.85,2.15),ylim=(.7,2.15))
x=np.linspace(1,2,500);axs[1].plot(x,x*(3-x),color="#1565c0",lw=2);axs[1].scatter([1.5],[2.25],color="#d84315");axs[1].set(xlabel=r"$V/V_0$ on B to C",ylabel=r"$T/T_0$",title="Temperature peaks inside the branch")
q=7.5-4*x;axs[2].plot(x,q,color="#222",lw=1.5);axs[2].fill_between(x,0,q,where=q>=0,color="#66bb6a",alpha=.5);axs[2].fill_between(x,0,q,where=q<0,color="#ef5350",alpha=.6);axs[2].axhline(0,color="#999",lw=.8);axs[2].axvline(15/8,color="#c62828",ls=":");axs[2].set(xlabel=r"$x=V/V_0$ on B to C",ylabel=r"$\delta Q/(p_0V_0\,dx)$",title="Net branch heat hides a reversal")
for ax in axs:ax.grid(alpha=.15)

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
