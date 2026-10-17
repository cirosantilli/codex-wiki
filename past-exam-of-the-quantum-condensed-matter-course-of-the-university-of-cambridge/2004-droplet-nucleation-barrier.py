"""Original dimensionless capillarity free energies for two supersaturation signs."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2.15,700)
fig,axes=plt.subplots(1,2,figsize=(9.0,4.4),layout="constrained")
axes[0].plot(x,x*x+2*x**3/3,color="#287fa8",lw=2)
axes[0].set(title=r"$\mu_l>\mu_v$: stable vapor",ylim=(-.2,12))
axes[0].scatter([0],[0],color="#287fa8",zorder=5)
axes[1].plot(x,x*x-2*x**3/3,color="#ad6531",lw=2)
axes[1].scatter([0,1],[0,1/3],color=["#287fa8","#ad6531"],zorder=5)
axes[1].axvline(1,color="#777777",ls="--",lw=.9)
axes[1].annotate("Critical radius",xy=(1,1/3),xytext=(1.15,.52),arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=10)
axes[1].annotate("Growth lowers free energy",xy=(1.95,-1.14),xytext=(.25,-1.55),arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=10)
axes[1].set(title=r"$\mu_l<\mu_v$: nucleation barrier",ylim=(-2.15,.72))
for ax in axes:
    ax.axhline(0,color="#777777",lw=.7)
    ax.set(xlim=(0,2.15),xlabel=r"$R/R_0$, with $R_0=2\Gamma/(n_l|\mu_l-\mu_v|)$",ylabel=r"$\Delta G/(4\pi\Gamma R_0^2)$")
    ax.grid(alpha=.14)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
