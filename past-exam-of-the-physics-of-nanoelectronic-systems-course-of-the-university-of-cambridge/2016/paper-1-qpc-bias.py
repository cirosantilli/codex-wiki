"""Original explanatory model/schematic; no source figure or data copied.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes its same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle,FancyArrowPatch
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})

fig,axes=plt.subplots(1,2,figsize=(8.7,3.7),constrained_layout=True)
x=np.linspace(-.15,4.55,1600);tops=np.arange(5)+.5;wx=.12
trans=lambda e:1/(1+np.exp(np.clip(-2*np.pi*(np.asarray(e)[...,None]-tops)/wx,-700,700)))
t=trans(x)
for j in range(4):axes[0].plot(x,t[:,j],lw=1.5,label=rf"Mode {j}")
axes[0].set(xlim=(x[0],x[-1]),ylim=(-.02,1.08),xlabel=r"Energy $(E-U_0)/(\hbar\omega_y)$",ylabel="Transmission",title=r"Saddle transmission, $\omega_x/\omega_y=0.12$")
axes[0].legend(fontsize=8,loc="lower right")
for v,col,label in [(0,"#2466a5","Zero bias"),(.6,"#ba492c",r"Symmetric $eV=0.6\hbar\omega_y$")]:
    g=.5*np.sum(trans(x+v/2)+trans(x-v/2),axis=1)
    axes[1].plot(x,g,color=col,lw=1.8,label=label)
axes[1].set(xlim=(x[0],x[-1]),ylim=(-.1,4.6),xlabel=r"$(E_F-U_0)/(\hbar\omega_y)$",ylabel=r"Differential conductance / $(2e^2/h)$",title="Rigid spectrum, zero temperature")
axes[1].legend(fontsize=8,loc="upper left")
for ax in axes:ax.grid(alpha=.15)

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
