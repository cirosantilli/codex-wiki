"""Original figure. Tested Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Run from the desired image directory; writes an opaque white PNG to CWD.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

Z=np.linspace(0,1,300);U=(1-(2/3))*Z-Z**2/2
fig,ax=plt.subplots(figsize=(5.6,4.5),dpi=100,facecolor="white")
ax.axvline(0,color="gray",ls=":");ax.plot(U,Z,color="#226cb2",lw=2.5)
ax.axhline(0,color="black",lw=2);ax.axhline(1,color="#6093b2",lw=1)
for z in [.17,.4,.62,.82,.98]:
 u=(1-(2/3))*z-z*z/2
 ax.annotate("",xy=(u,z),xytext=(0,z),arrowprops=dict(arrowstyle="->",color="#a33c28",lw=1.3))
ax.set(xlabel=r"$u/(\rho g h^2\sin\alpha/\mu)$ (positive downslope)",ylabel="$z/h$",ylim=(-.025,1.04),xlim=(-.56,.14),title="Zero net flux")
ax.grid(alpha=.2);fig.tight_layout();fig.savefig("paper-1-zero-flux.png",facecolor="white",transparent=False)
