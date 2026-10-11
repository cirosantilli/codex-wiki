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
fig,axes=plt.subplots(3,1,figsize=(9.3,6.5),layout="constrained")
x=np.linspace(-2,2,1000)
axes[0].plot(x,1+np.cos(2*np.pi*x),color="#1565a8",lw=1.5)
axes[0].scatter([-1.5,-.5,.5,1.5],[0]*4,color="#ca6720",s=15,zorder=4)
axes[0].set_xlabel(r"Optical path difference $x/\lambda$; minima at half-integers")
axes[0].set_title("Monochromatic source")
l1,l2=589e-9,589.6e-9
k1,k2=2*np.pi/l1,2*np.pi/l2
kb,dk=(k1+k2)/2,abs(k1-k2)
d=np.linspace(0,650e-6,3000)
v=np.abs(np.cos(dk*d))
axes[1].plot(d*1e6,1+v,color="#ca6720",lw=1.6,label="fringe envelope")
axes[1].plot(d*1e6,1-v,color="#ca6720",lw=1.6)
axes[1].axhline(1,color="0.5",ls=":")
for j in [1,3]:axes[1].axvline(j*np.pi/(2*dk)*1e6,color="0.6",ls=":")
axes[1].set_xlabel("Mirror displacement d (µm); first visibility zero at 144.7 µm")
axes[1].set_title("Sodium doublet: envelope only (optical fringes are too dense at this scale)")
axes[1].annotate("",xy=(289.4,2.05),xytext=(0,2.05),arrowprops={"arrowstyle":"<->"})
axes[1].text(144.7,2.17,"289.4 µm between revivals",ha="center",fontsize=9)
d=np.linspace(0,2e-6,1500)
axes[2].plot(d*1e6,1+np.cos(2*kb*d)*np.cos(dk*d),color="#1565a8",lw=1.3)
axes[2].set_xlabel("Mirror displacement d (µm); fast fringe period 0.29465 µm")
axes[2].set_title("Sodium doublet: magnified packet near zero path difference")
for ax in axes:
    ax.set_ylabel(r"$I/I_0$");ax.set_ylim(-.05,2.3);ax.grid(alpha=.13)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=135)
