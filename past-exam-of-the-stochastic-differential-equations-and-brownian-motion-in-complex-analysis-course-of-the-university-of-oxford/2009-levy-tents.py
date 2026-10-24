"""Python 3.14; NumPy and Matplotlib in ../pyproject.toml. PNG output in CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
rng=np.random.default_rng(2009101)
t=np.linspace(0,1,4097)
base=rng.normal()*t
levels=[]
for n in range(7):
 count=2**n
 heights=rng.normal(size=count)*2**(-(n+2)/2)
 local=t*count
 indices=np.minimum(local.astype(int),count-1)
 shape=1-np.abs(2*(local-indices)-1)
 levels.append(heights[indices]*shape)
fig,axs=plt.subplots(2,1,figsize=(8,5.6),sharex=True,facecolor="white")
axs[0].plot(t,levels[3],color="C0",lw=1.5)
axs[0].axhline(0,color="0.5",lw=.7)
axs[0].set(title="Eight disjoint tents at level 3",ylabel=r"$X_3(t)$")
partial=base.copy()
for n,level in enumerate(levels):
 partial+=level
 if n in (0,2,6):
  axs[1].plot(t,partial.copy(),lw=1.6,label=f"Through level {n}")
axs[1].set(title="Partial sums remain continuous",xlabel="t",ylabel="Path value",xlim=(0,1))
axs[1].legend(frameon=False,fontsize=9)
for ax in axs:ax.spines[["top","right"]].set_visible(False)
fig.tight_layout()
fig.savefig("2009-levy-tents.png",dpi=150,facecolor="white")
