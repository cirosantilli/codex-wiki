"""Original disconnected-domain antiderivatives; output matching PNG to CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size":12,"figure.facecolor":"white"})
fig,(left,right)=plt.subplots(1,2,figsize=(10.6,4.8),layout="constrained")
negative=np.linspace(-3,-.08,501)
positive=np.linspace(.08,3,501)
for x in (negative,positive):
    left.plot(x,np.log(np.abs(x)),color="#777777",lw=1.3,ls="--",
              label=r"Reference $\log|x|$" if x is negative else None)
left.plot(negative,np.log(-negative)+2,color="#2855a6",lw=2.6,label=r"$C_-=2$")
left.plot(positive,np.log(positive)-1,color="#087e8b",lw=2.6,label=r"$C_+=-1$")
left.scatter([-1,1],[2,-1],color=["#2855a6","#087e8b"],s=48,zorder=3)
left.text(-2.75,3.05,r"$x<0$: choose $C_-$",color="#2855a6",fontsize=12)
left.text(.28,.65,r"$x>0$: choose $C_+$",color="#087e8b",fontsize=12)
left.set(xlim=(-3,3),ylim=(-4.5,3.65),xlabel=r"$x$",ylabel=r"$F(x)$",
         title="A separate constant on each interval")
left.legend(frameon=False,loc="lower left",fontsize=11)
for x in (negative,positive):
    right.plot(x,1/x,color="#333333",lw=2.6)
right.text(-2.6,7,r"$F'(x)=1/x$",fontsize=16)
right.set(xlim=(-3,3),ylim=(-13.5,13.5),xlabel=r"$x$",ylabel=r"$g(x)$",
          title="The same derivative on both components")
for ax in (left,right):
    ax.axhline(0,color="#aaaaaa",lw=.8)
    ax.axvline(0,color="#c45b12",lw=1.2,ls=":")
    ax.grid(alpha=.15)
fig.suptitle(r"On $\mathbb{R}\setminus\{0\}$, one initial value cannot fix both constants",fontsize=16)
fig.supxlabel("The dotted vertical line marks excluded x = 0; no continuity across that missing point is required",
              fontsize=11)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
