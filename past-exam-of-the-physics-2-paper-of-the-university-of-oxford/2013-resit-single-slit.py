"""Original CP2 2013 resit figure; Python 3.14, NumPy and Matplotlib root dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

x=np.linspace(-4,4,4001);intensity=np.sinc(x)**2
fig,ax=plt.subplots(figsize=(8,4.2),layout="constrained")
ax.plot(x,intensity,color="#146b9c",lw=2.3)
for s in [-1,1]:
    ax.axvline(s,color=".5",lw=1,ls=":");ax.plot(s,0,"o",color="#d76c20",ms=5)
ax.annotate("Central maximum",xy=(0,.9),xytext=(1.3,.82),arrowprops={"arrowstyle":"-","color":".4"})
ax.set(xlim=(-4,4),ylim=(-.035,1.08),xlabel=r"$w\sin\theta/\lambda$",ylabel=r"$I/I(0)$",title="Single-slit Fraunhofer diffraction")
ax.grid(alpha=.18)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white",metadata={"Software":"Original CP2 solution figure"})
plt.close(fig)
