"""Original Oxford CP2 2014 solution figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

t=np.linspace(0,6,700)
fig,ax=plt.subplots(1,2,figsize=(9.6,3.8),layout="constrained")
for ratio,color,label in [(1,"#146b9c",r"$C=C_0$"),(.5,"#d76c20",r"$C=C_0/2$")]:
    ax[0].plot(t,np.exp(-t/ratio),color=color,lw=2.3,label=label)
    ax[1].plot(t,ratio*(-np.expm1(-t/ratio)),color=color,lw=2.3,label=label)
ax[0].set(title="Current: same initial value",ylabel=r"$I/(V/R)$",ylim=(-.03,1.08))
ax[1].set(title="Charge: different final values",ylabel=r"$Q/(C_0 V)$",ylim=(-.03,1.08))
for a in ax:
    a.set(xlabel=r"$t/(RC_0)$",xlim=(0,6));a.grid(alpha=.2);a.legend()
ax[1].axhline(.5,color="#d76c20",ls=":",lw=1)
ax[1].axhline(1,color="#146b9c",ls=":",lw=1)
fig.suptitle("Charging at fixed R and V; smaller C gives a shorter time constant",fontsize=14)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, facecolor="white", metadata={"Software":"Oxford CP2 original Matplotlib figure"})
plt.close(fig)
