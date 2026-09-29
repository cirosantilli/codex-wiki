"""Original asymptotic comparison plots; output matching PNG to CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
fig, axes=plt.subplots(1,3,figsize=(10.6,4.8),layout="constrained")
first,middle,last=axes
n=np.geomspace(1,100000,401)
first.loglog(n,1000*n,color="#2855a6",lw=2.2,label=r"$1000n$")
first.loglog(n,n*n,color="#c45b12",lw=2.2,label=r"$n^2$")
first.scatter([1000],[1000000],color="#333333",s=40,zorder=3)
first.axvline(1000,color="#888888",ls=":",lw=1)
first.set(xlabel=r"Input size $n$",ylabel="Stipulated operation count",
          title="Finite-input ordering can reverse")
first.legend(frameon=False,loc="upper left")
n=np.geomspace(1,10000000,501)
middle.loglog(n,1+100000/n,color="#087e8b",lw=2.2)
middle.axhline(2,color="#c45b12",ls="--",lw=1.4)
middle.axvline(100000,color="#888888",ls=":",lw=1)
middle.scatter([100000],[2],color="#333333",s=40,zorder=3)
middle.text(1200,2.6,r"$C=2$",color="#c45b12")
middle.text(220,1600,r"$(n^2+10^5n)/n^2$",color="#087e8b",fontsize=12)
middle.set(xlabel=r"Input size $n$",ylabel="Normalized ratio",
           title=r"An eventual $O(n^2)$ bound",ylim=(.8,200000))
n=np.arange(0,19)
ratio=1+.6*(2/3)**n
last.plot(n,ratio,"-o",color="#7d3c98",markersize=4,lw=2)
last.axhline(1,color="#333333",ls="--",lw=1.2)
last.axhline(1.01,color="#888888",ls=":",lw=1.2)
last.scatter([11],[1+.6*(2/3)**11],color="#c45b12",s=52,zorder=3)
last.text(4.5,1.42,r"$(3\cdot2^n+5\cdot3^n)/(5\cdot3^n)$",fontsize=11)
last.text(8.2,1.19,"Less than 1%\nat n = 11",color="#c45b12",fontsize=11)
last.set(xlabel=r"Exponent $n$",ylabel="Normalized ratio",
         title="The largest base dominates",xlim=(-.5,18.5),ylim=(.96,1.65))
for ax in axes:ax.grid(alpha=.16,which="both")
fig.suptitle("Asymptotic scales, constants, and explicit thresholds",fontsize=17)
fig.supxlabel("Analytical examples; no hardware runtime or measured performance is asserted",fontsize=11)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
