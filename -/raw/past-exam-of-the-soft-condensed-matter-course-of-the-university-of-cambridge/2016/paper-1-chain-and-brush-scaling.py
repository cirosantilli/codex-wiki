"""Original explanatory model; no exam image or experimental points copied.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes its same-basename PNG to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})

x=np.logspace(-2,3,1000)
w=2*(x+np.expm1(-x))
sigma=np.logspace(-3,-.15,600)
fig,axes=plt.subplots(1,2,figsize=(8.6,3.7),constrained_layout=True)
axes[0].loglog(x,w,lw=2,color="#2466a5",label="Worm-like chain")
axes[0].loglog(x,x*x,ls=":",color="#ba492c",label=r"Rod $L^2$")
axes[0].loglog(x,2*x,ls="--",color="#347748",label=r"Long coil $2\ell_pL$")
axes[0].set(xlim=(1e-2,1e3),ylim=(8e-5,3e3),xlabel=r"Contour length $L/\ell_p$",ylabel=r"$\langle R^2\rangle/\ell_p^2$",title="Stiffness crossover")
axes[0].legend(fontsize=8)
axes[1].loglog(sigma,sigma**(1/3),lw=2,color="#2466a5",label=r"Good solvent: slope $1/3$")
axes[1].loglog(sigma,sigma,lw=2,color="#ba492c",label=r"Dense poor solvent: slope $1$")
axes[1].axhline(1,color=".55",ls=":",lw=1)
axes[1].set(xlim=(1e-3,1),ylim=(8e-4,1.2),xlabel=r"Reduced grafting density $\sigma a^2$",ylabel=r"Normalized height $h/(Na)$",title="Illustrative uniform-brush laws")
axes[1].legend(fontsize=8,loc="lower right")
for ax in axes:ax.grid(alpha=.18,which="major")

fig.savefig(Path(__file__).stem + ".png", dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
