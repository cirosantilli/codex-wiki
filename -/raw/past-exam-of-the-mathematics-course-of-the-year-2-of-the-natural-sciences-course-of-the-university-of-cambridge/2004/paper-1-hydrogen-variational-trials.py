"""Original variational energy curves for two radial hydrogen trial families."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,2,figsize=(8.8,4.4),layout="constrained",sharey=True)
alpha=np.linspace(.15,2.5,700);beta=np.linspace(1.5,12,800)
axes[0].plot(alpha,alpha**2/2-alpha,color="#287ea8",lw=2)
axes[1].plot(beta,5/beta**2-2.5/beta,color="#a46a2f",lw=2)
axes[0].scatter([1],[-.5],color="#287ea8",s=35,zorder=5)
axes[1].scatter([4],[-5/16],color="#a46a2f",s=35,zorder=5)
axes[0].annotate(r"$\alpha=1,\quad E=-1/2$",xy=(1,-.5),xytext=(1.3,-.34),arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=11)
axes[1].annotate(r"$\beta=4,\quad E=-5/16$",xy=(4,-5/16),xytext=(5,-.1),arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=11)
axes[0].set(xlabel="Exponential parameter α",title=r"$\psi(r)=e^{-\alpha r}$",xlim=(.15,2.5))
axes[1].set(xlabel="Support radius β",title=r"$\psi(r)=\max(1-r/\beta,0)$",xlim=(1.5,12))
for ax in axes:
    ax.axhline(-.5,color="#666666",ls="--",lw=.9,label="Exact ground-state energy")
    ax.set_ylim(-.58,.72);ax.grid(alpha=.15)
axes[0].set_ylabel("Energy in atomic units")
axes[1].legend(loc="upper right",fontsize=9)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
