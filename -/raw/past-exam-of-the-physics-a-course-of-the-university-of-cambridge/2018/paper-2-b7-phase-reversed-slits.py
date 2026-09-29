"""Original solution figure; tested with Python 3.14.4.
Uses NumPy 2.3.5 and Matplotlib 3.10.7 from the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
fig, axes = plt.subplots(3, 1, figsize=(9.3, 6.3), sharex=True, layout="constrained")
th = np.linspace(-44,44,9000)
u=th/4
base=np.sin(np.pi*u)**2
env=np.sinc(th/20)**2
axes[0].plot(th,np.cos(np.pi*u)**2,color="#1565a8",lw=1.1)
axes[1].plot(th,base,color="#ca6720",lw=1.1)
axes[2].plot(th,base*env,color="#1565a8",lw=1.4)
axes[2].plot(th,env,color="#ca6720",ls="--",lw=1.2,label="single-slit envelope")
for ax, title in zip(axes,["Narrow slits, no phase plate: central bright fringe", "Narrow slits, relative phase π: central dark fringe", "Finite width a = 0.020 mm, centre spacing D = 0.100 mm, relative phase π"]):
    ax.set_title(title,fontsize=10)
    ax.set_ylim(0,1.18)
    ax.set_ylabel("Relative intensity")
    ax.grid(alpha=.15)
axes[0].annotate("",xy=(4,1.05),xytext=(0,1.05),arrowprops={"arrowstyle":"<->"})
axes[0].text(2,1.12,"4 mrad",ha="center",fontsize=9)
for x in [-40,-20,20,40]:
    axes[2].axvline(x,color="0.55",ls=":",lw=1)
axes[2].legend(frameon=False,fontsize=8,loc="upper right")
axes[2].set_xlabel(r"Small-angle coordinate $\theta$ (mrad); interference zeros at 0, ±4, ±8, …")
axes[2].set_xticks([-40,-20,0,20,40])
axes[2].set_xlim(-44,44)
fig.suptitle("λ = 400 nm; envelope zeros at ±20, ±40, … mrad")
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=135)
