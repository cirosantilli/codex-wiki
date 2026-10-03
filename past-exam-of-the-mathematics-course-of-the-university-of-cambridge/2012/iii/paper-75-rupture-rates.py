"""Original Paper 75 figure. Python 3.14, root matplotlib/numpy dependencies.
Requires caller-supplied MPLCONFIGDIR; writes basename PNG only to cwd.
"""
from pathlib import Path
import os
if not os.environ.get("MPLCONFIGDIR"):
    raise RuntimeError("Set MPLCONFIGDIR to a caller-owned cache directory")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10})
fig,axes=plt.subplots(1,2,figsize=(8.4,4.6),facecolor="white")
K=np.linspace(.002,4,800);mob=np.sinh(K)**2/(K*(2*K+np.sinh(2*K)))
for ax,G in zip(axes,[0,1]):
    ax.plot(np.r_[0,K],np.r_[.25,(1-G*K*K)*mob],lw=2,color="#225f9c")
    ax.axhline(0,color="#555555",lw=.8)
    ax.set_xlabel(r"$K=kh_0$");ax.set_ylabel(r"$s/(3V/\mu h_0^3)$")
    ax.set_title(r"$\Gamma="+str(G)+r"$");ax.grid(alpha=.2)
    ax.set_xlim(0,4)
axes[0].set_ylim(0,.28);axes[1].axvline(1,color="#999999",ls="--",lw=1)
axes[1].set_ylim(-2,.4)
fig.suptitle("Clean-sheet rupture: attraction and capillary stabilization")
fig.subplots_adjust(left=.09,right=.97,bottom=.17,top=.80,wspace=.36)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
plt.close(fig)
