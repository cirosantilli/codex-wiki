from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(9.2,4.5));density=np.logspace(-3,3,650);q=np.sqrt(density);r=(1-q)/(1+q);t=2/(1+q);R=r*r;Tr=q*t*t
ax.semilogx(density,r,color="#b44d38",lw=2,label="Reflected r");ax.semilogx(density,t,color="#236a9b",lw=2,label="Transmitted t");ax.axhline(0,color="#888888",lw=.8);ax.scatter([4,4],[-1/3,2/3],color=["#b44d38","#236a9b"],zorder=4)
ax.set(ylim=(-1.1,2.1),xlabel=r"$\rho_2/\rho_1$",ylabel="Signed displacement coefficient",title="Displacement amplitudes");ax.legend(fontsize=10)
bx.semilogx(density,R,color="#b44d38",lw=2,label=r"$\mathcal{R}=r^2$");bx.semilogx(density,Tr,color="#236a9b",lw=2,label=r"$\mathcal{T}=\sqrt{\rho_2/\rho_1}\ t^2$");bx.scatter([4,4],[1/9,8/9],color=["#b44d38","#236a9b"],zorder=4)
bx.set(ylim=(-.04,1.04),xlabel=r"$\rho_2/\rho_1$",ylabel="Outgoing / incident power",title="Power fractions sum to one");bx.legend(fontsize=10,loc="lower center")
for aa in [ax,bx]:aa.axvline(4,color="#777777",ls="--",lw=.8);aa.grid(alpha=.16,which="both")
fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
