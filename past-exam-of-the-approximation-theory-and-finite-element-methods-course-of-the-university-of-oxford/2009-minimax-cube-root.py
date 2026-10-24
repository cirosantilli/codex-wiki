"""Python 3.14; NumPy and Matplotlib in ../pyproject.toml. Output in CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x=np.linspace(0,1,1500);e=1/(3*np.sqrt(3));critical=e
fig,axs=plt.subplots(1,2,figsize=(9,3.8),facecolor="white")
axs[0].plot(x,np.cbrt(x),label=r"$x^{1/3}$",lw=2.2)
axs[0].plot(x,x+e,label=r"$p^*(x)=x+1/(3\sqrt{3})$",lw=2)
axs[0].set(xlabel="x",ylabel="Value",title="Best uniform linear approximation")
axs[0].legend(frameon=False,fontsize=9)
err=np.cbrt(x)-x-e
axs[1].plot(x,err,lw=2)
axs[1].axhline(e,color=".5",ls="--");axs[1].axhline(-e,color=".5",ls="--")
axs[1].scatter([0,critical,1],[-e,e,-e],color="C1",zorder=5)
axs[1].text(.03,e+.01,"+E");axs[1].text(.03,-e-.04,"-E")
axs[1].set(xlabel="x",ylabel="Signed error",title="Three alternating extremal errors",ylim=(-.26,.26))
for ax in axs:ax.spines[["top","right"]].set_visible(False);ax.set_xlim(0,1)
fig.tight_layout();fig.savefig("2009-minimax-cube-root.png",dpi=150,facecolor="white")
