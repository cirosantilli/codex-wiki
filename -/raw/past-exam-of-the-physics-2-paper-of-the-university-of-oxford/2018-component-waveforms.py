"""Original solution illustration; output the matching PNG into the cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
plt.rcParams.update({"font.size":12,"figure.facecolor":"white"})

t=np.linspace(0,6*np.pi,1000)
fig,axes=plt.subplots(3,1,figsize=(9,6.8),sharex=True,layout="constrained")
for ax,name,current in zip(axes,["Resistor: current in phase","Capacitor: current leads by π/2","Inductor: current lags by π/2"],[np.cos(t),-np.sin(t),np.sin(t)]):
    ax.plot(t/(2*np.pi),np.cos(t),color="#286d88",lw=2,label="Voltage / amplitude")
    ax.plot(t/(2*np.pi),current,color="#b96331",ls="--",lw=2,label="Current / amplitude")
    ax.set(ylim=(-1.25,1.25),yticks=[-1,0,1],title=name,ylabel="Normalized")
    ax.grid(alpha=.2)
axes[0].legend(loc="upper right",fontsize=10,ncol=2)
axes[-1].set(xlabel="Time / period",xlim=(0,3))

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
