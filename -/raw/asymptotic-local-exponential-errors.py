"""Original local exponential approximation plots; output matching PNG to CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size":12,"figure.facecolor":"white"})
fig,(left,right)=plt.subplots(1,2,figsize=(10.6,4.8),layout="constrained")
h=np.geomspace(1e-4,1,501)
error=np.expm1(h)-h
relative_difference=error/h
left.semilogx(h,relative_difference,color="#087e8b",lw=2.4,
             label=r"$(e^h-1-h)/h$")
left.semilogx(h,h/2,color="#2855a6",ls="--",lw=1.8,
             label=r"Leading approximation $h/2$")
left.axhline(0,color="#888888",lw=.8)
left.set(xlabel=r"Positive increment $h$ (log scale)",
         ylabel="Relative difference against h",
         title=r"$e^h-1\sim h$ as $h\to0$",ylim=(-.035,.8))
left.legend(frameon=False,loc="upper left",fontsize=11)
right.loglog(h,error,color="#087e8b",lw=2.5,label=r"Absolute error $e^h-1-h$")
right.loglog(h,h*h/2,color="#2855a6",ls="--",lw=1.7,label=r"Leading term $h^2/2$")
right.loglog(h,np.e*h*h/2,color="#c45b12",ls=":",lw=2,
             label=r"Bound $e h^2/2$ for $h\leq1$")
right.set(xlabel=r"Positive increment $h$ (log scale)",
          ylabel="Absolute error (log scale)",
          title=r"Quadratic remainder: $e^h-1=h+O(h^2)$")
right.legend(frameon=False,loc="upper left",fontsize=11)
for ax in (left,right):ax.grid(alpha=.16,which="both")
fig.suptitle("A simpler local expression, with a quantified error",fontsize=17)
fig.supxlabel("The plots show positive h; the stated absolute bound is valid for every real |h| ≤ 1",
              fontsize=11)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
