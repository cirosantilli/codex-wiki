"""Original explanatory diagram; no exam or published illustration copied.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes a same-basename PNG to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})

st=np.logspace(-3,3,900);drift=2*st/(1+st*st)
fig,axes=plt.subplots(1,2,figsize=(8.6,3.7),constrained_layout=True)
axes[0].semilogx(st,drift,color="#2466a5",lw=2)
axes[0].axvline(1,color=".6",ls="--",lw=1)
axes[0].scatter([1],[1],color="#ba492c",zorder=4)
axes[0].text(1.3,.96,"Fastest at St = 1",fontsize=9)
axes[0].set(xlim=(1e-3,1e3),ylim=(0,1.12),xlabel=r"Stokes number $\mathrm{St}=\Omega_Kt_s$",ylabel=r"Inward drift $-v_{pr}/(\eta v_K)$",title="Test particles, stationary radial gas")
axes[0].grid(alpha=.17)
x=np.linspace(-1,1,700);p=1+.7*np.exp(-(x/.34)**2)
axes[1].plot(x,p,color="#347748",lw=2)
axes[1].axvline(0,color=".65",ls=":",lw=1)
for y in [1.26,1.43]:
    axes[1].annotate("",xy=(-.08,y),xytext=(-.78,y),arrowprops=dict(arrowstyle="->",color="#ba492c",lw=1.7))
    axes[1].annotate("",xy=(.08,y),xytext=(.78,y),arrowprops=dict(arrowstyle="->",color="#ba492c",lw=1.7))
axes[1].text(0,1.75,"Pressure maximum",ha="center",fontsize=9)
axes[1].text(0,1.07,"Solids drift toward the maximum",ha="center",fontsize=9,color="#ba492c")
axes[1].set(xlim=(-1,1),ylim=(.97,1.85),xlabel=r"Radial position relative to trap (schematic)",ylabel="Gas pressure (arbitrary units)",title="Pressure-support contribution only",xticks=[-1,0,1],yticks=[])

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
