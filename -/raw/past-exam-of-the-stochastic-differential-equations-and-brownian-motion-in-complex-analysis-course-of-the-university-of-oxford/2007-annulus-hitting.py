"""Generate PNG in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
fig,axs=plt.subplots(1,2,figsize=(9,4),facecolor="white",layout="constrained")
ax=axs[0]
ax.add_patch(Circle((0,0),3,facecolor="#e5f1f8",edgecolor="#12679b",lw=2))
ax.add_patch(Circle((0,0),.5,facecolor="white",edgecolor="#b23c41",lw=2))
ax.add_patch(Circle((0,0),1.4,fill=False,edgecolor="0.5",ls="--"))
ax.scatter([1.4],[0],color="black",s=25)
ax.text(1.45,.15,r"Start: $|Z|=R$",fontsize=10)
ax.text(-.1,-.2,r"$0$",ha="center")
ax.text(-.8,.6,r"$\widetilde R$",color="#b23c41",fontsize=12)
ax.text(-2.4,2,r"$\widehat R$",color="#12679b",fontsize=12)
ax.set(xlim=(-3.4,3.4),ylim=(-3.3,3.4),aspect="equal",title="Which circle is hit first?")
ax.axis("off")
ax=axs[1];rout=np.geomspace(1.001,1e6,600)
for rin in[.5,.1,.01]:
 p=np.log(rout)/np.log(rout/rin)
 ax.plot(rout,p,label=fr"$\widetilde R={rin}$",lw=2)
ax.set(xscale="log",xlabel=r"Outer radius $\widehat R$ (start radius 1)",ylabel="Inner-circle hitting probability",ylim=(0,1.03),title=r"$\log\widehat R/\log(\widehat R/\widetilde R)\to1$")
ax.grid(alpha=.2);ax.legend(frameon=False,loc="lower right")
fig.savefig("2007-annulus-hitting.png",dpi=160,facecolor="white")
