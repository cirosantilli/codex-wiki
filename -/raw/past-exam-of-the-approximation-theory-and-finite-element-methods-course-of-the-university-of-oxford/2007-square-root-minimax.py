"""Generate 2007-square-root-minimax.png in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x=np.linspace(0,1,1001)
u=np.sqrt(1-x);p=9/8-x
fig,axs=plt.subplots(1,2,figsize=(9,3.6),facecolor="white",layout="constrained")
axs[0].plot(x,u,label=r"$\sqrt{1-x}$",color="#12679b",lw=2)
axs[0].plot(x,p,label=r"$9/8-x$",color="#b23c41",lw=2)
axs[0].plot(x,1-x,"--",color="0.5",label="Chord")
axs[0].set(title="Best linear uniform approximation",xlabel="$x$",ylabel="Value")
axs[0].legend(frameon=False)
axs[1].plot(x,u-p,color="#12679b",lw=2)
for y in [-1/8,1/8]:axs[1].axhline(y,ls="--",color="0.5",lw=1)
axs[1].scatter([0,.75,1],[-.125,.125,-.125],color="#b23c41",zorder=5)
axs[1].set(title="Three alternating extreme errors",xlabel="$x$",ylabel=r"$\sqrt{1-x}-(9/8-x)$",ylim=(-.16,.16))
for ax in axs:ax.grid(alpha=.2);ax.set_xlim(0,1)
fig.savefig("2007-square-root-minimax.png",dpi=160,facecolor="white")
