"""Original 2012 Oxford Short Options figure; Python 3.14, NumPy and Matplotlib root dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

u=np.linspace(0,5,1001);stable=np.linspace(0,4,1001)
fig,ax=plt.subplots(1,2,figsize=(9.8,4.2),layout="constrained")
ax[0].axvspan(0,4,color="#27835b",alpha=.10,label="Strictly stable: 0 < u < 4")
ax[0].plot(u,2-u,color="#146b9c",lw=2.3)
for value in [-2,2]:ax[0].axhline(value,color=".5",ls=":",lw=1)
ax[0].plot([0,4],[2,-2],"o",mfc="white",mec="#146b9c",mew=1.5,ms=6)
ax[0].set(xlim=(0,5),ylim=(-3.3,2.5),ylabel=r"$\mathrm{tr}\,M=2-u$",title="Both transverse planes: same trace")
ax[0].legend(loc="upper right",fontsize=9)
mu=np.arccos(1-stable/2)/np.pi
ax[1].plot(stable,mu,color="#146b9c",lw=2.3)
ax[1].plot([0,4],[0,1],"o",mfc="white",mec="#146b9c",mew=1.5,ms=6)
ax[1].set(xlim=(0,5),ylim=(-.04,1.09),ylabel=r"$\mu/\pi$",title="Full-cell phase advance")
for a in ax:a.set_xlabel(r"$u=L_1L_2/f^2$");a.grid(alpha=.17)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white",metadata={"Software":"Original Oxford Short Options figure"})
plt.close(fig)
