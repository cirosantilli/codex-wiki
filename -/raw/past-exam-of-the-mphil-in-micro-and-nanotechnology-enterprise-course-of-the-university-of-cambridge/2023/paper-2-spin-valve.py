"""Original explanatory diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import os
import numpy as np
os.environ.setdefault("MPLCONFIGDIR", "/tmp/cambridge-nano2-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, RegularPolygon, FancyArrowPatch, Wedge
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "savefig.facecolor": "white"})

fig,axs=plt.subplots(1,3,figsize=(11,3.6),layout="constrained")
H=np.linspace(-3,3,1000)
for ax,width in zip(axs[:2],[.015,.28]):
    for direction,color,ls in [(1,"#246c99","-"),(-1,"#b23a37","--")]:
        if direction==1:
            msoft=np.tanh((H-.65)/width);mhard=np.tanh((H-1.8)/width)
        else:
            msoft=np.tanh((H+.65)/width);mhard=np.tanh((H+1.8)/width)
        ax.plot(H,1+.4*(1-msoft*mhard)/2,color=color,ls=ls,label="Increasing H" if direction==1 else "Decreasing H")
    ax.set(xlabel="In-plane magnetic field H",ylabel="Resistance (schematic)",yticks=[1,1.4],yticklabels=[r"$R_P$",r"$R_{AP}$"])
axs[0].set_title("Separate, abrupt switching");axs[0].legend(fontsize=8)
axs[1].set_title("Distributed switching fields")
d=np.linspace(.2,5,200);axs[2].plot(d,1/(1+d),color="#246c99")
axs[2].set(xlabel="Spacer thickness (arbitrary units)",ylabel=r"$(R_{AP}-R_P)/R_P$",title="Common spacer dilutes the ratio",yticks=[])
fig.suptitle("Ideal pseudo spin valve; roughness may also introduce coupling or spin-memory loss",fontsize=11)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145)
