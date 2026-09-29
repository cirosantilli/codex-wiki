"""Original explanatory model; no exam image or experimental points copied.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes its same-basename PNG to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})

phi=np.linspace(1e-5,1-1e-5,1600)
N=100
f=lambda x,chi:(x*np.log(x)+(1-x)*np.log1p(-x))/N+chi*x*(1-x)
fig,axes=plt.subplots(1,2,figsize=(8.6,3.5),constrained_layout=True)
for ax,chi in zip(axes,[.01,.03]):
    ax.plot(phi,f(phi,chi),color="#2466a5",lw=2)
    ax.set(xlim=(0,1),xlabel=r"Volume fraction $\phi$",ylabel=r"Mixing $f/(k_BT)$",title=rf"$N_A=N_B=100$, $\chi={chi:.2f}$")
    ax.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
    ax.grid(alpha=.18)
lo,hi=1e-8,.25
for _ in range(80):
    m=(lo+hi)/2
    d=np.log(m/(1-m))/N+.03*(1-2*m)
    if d>0:hi=m
    else:lo=m
b=(lo+hi)/2
sp=(1-np.sqrt(1-2/(N*.03)))/2
ax=axes[1]
ax.plot([b,1-b],[f(b,.03)]*2,"--",color="#ba492c",lw=1.7,label="Common tangent")
ax.scatter([b,1-b],[f(b,.03)]*2,color="#ba492c",s=28,zorder=4)
ax.axvspan(sp,1-sp,color="#e7b443",alpha=.17,label="Unstable curvature")
ax.legend(loc="upper right",fontsize=8)
fig.suptitle("Symmetric polymer-blend model: increasing contact penalty",fontsize=12)

fig.savefig(Path(__file__).stem + ".png", dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
