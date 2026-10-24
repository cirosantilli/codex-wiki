"""Original Brownian maximum-tail plot. Python3.14, NumPy, Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(1,15,500);lo=2/np.pi*np.arctan(1/x);hi=np.minimum(1,2*lo)
fig,ax=plt.subplots(figsize=(7,4.5),facecolor="white")
ax.fill_between(x,lo,hi,color="#d8e9f5",label=r"bounds for $\mathbb{P}(X^*>\lambda)$")
ax.plot(x,lo,color="#2166ac",ls="--");ax.plot(x,hi,color="#2166ac",ls="--")
ax.plot(x,1/x,color="#b2182b",lw=2,label=r"$\mathbb{P}(Y^*>\lambda)=1/\lambda$")
ax.set(xlabel=r"level $\lambda\geq1$",ylabel="tail probability",xlim=(1,15),ylim=(0,1.03),
       title="Maxima before first real-axis hit, starting at i")
ax.legend(frameon=False);ax.spines[["top","right"]].set_visible(False)
ax.grid(alpha=.15);fig.tight_layout()
fig.savefig("2008-exit-maxima.png",dpi=150,facecolor="white")
