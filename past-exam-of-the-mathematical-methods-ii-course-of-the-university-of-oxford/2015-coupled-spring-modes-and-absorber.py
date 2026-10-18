from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(9.8,4.6));x=np.arange(4)
ax.plot(x,[0,1,1,0],"o-",color="#236a9b",lw=2,label="Symmetric: equal sign");ax.plot(x,[0,1,-1,0],"s--",color="#b64c37",lw=1.8,label="Antisymmetric: opposite sign");ax.axhline(0,color="#888888",lw=.8)
ax.set(xticks=x,xticklabels=["Wall",r"$m_1$",r"$m_2$","Wall"],ylim=(-1.5,1.7),ylabel="Relative signed displacement",title="Symmetric two-mass mode shapes");ax.grid(alpha=.15);ax.legend(loc="upper right",fontsize=9)
mu=.1;pole=1/(1+mu)
for lo,hi in [(.65,pole-.003),(pole+.003,1.35)]:
 q=np.linspace(lo,hi,500);error=q-1;ratio=error/(mu+(1+mu)*error);bx.plot(q,ratio,color="#236a9b",lw=2)
bx.axvline(pole,color="#a44734",ls="--",lw=1.2);bx.axhline(0,color="#888888",lw=.8);bx.scatter([1],[0],color="#a44734",s=35,zorder=4);bx.annotate("Cancellation",(1,0),xytext=(1.04,-1.5),arrowprops=dict(arrowstyle="->",color="#a44734"),fontsize=11)
bx.text(pole-.01,3.3,"Pole",ha="right",color="#a44734",fontsize=11);bx.set(xlim=(.65,1.35),ylim=(-4,4),xlabel=r"$q=k/(m\omega^2)$",ylabel=r"$A/[-F_0/(M\omega^2)]$",title=r"Free-pair absorber: $m/M=0.1$");bx.grid(alpha=.15)
fig.text(.26,.025,"Mode shapes show displacement patterns, not spring geometry.",ha="center",fontsize=9);fig.tight_layout(rect=(0,.05,1,1))

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
