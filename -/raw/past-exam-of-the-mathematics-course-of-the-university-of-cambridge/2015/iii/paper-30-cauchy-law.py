"""Plot the proved Cauchy law. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-6,6,1201)
density=1/(np.pi*(1+x*x))
cdf=.5+np.arctan(x)/np.pi
fig,axs=plt.subplots(1,2,figsize=(9,3.6),dpi=100,facecolor="white")
for ax in axs:
    ax.set_facecolor("white")
    ax.grid(alpha=.2)
    ax.set(xlim=(-6,6),xlabel=r"$x$")
axs[0].plot(x,density,lw=2.5,color="#255b91")
axs[0].set(title="Standard Cauchy density",ylabel=r"$1/[\pi(1+x^2)]$",ylim=(0,.35))
axs[1].plot(x,cdf,lw=2.5,color="#26724d")
axs[1].axhline(.5,color="#777777",ls=":",lw=1)
axs[1].set(title="CDF = probability of positive divergence",
           ylabel=r"$1/2+\arctan(x)/\pi$",ylim=(0,1))
fig.subplots_adjust(left=.075,right=.975,bottom=.17,top=.85,wspace=.32)
fig.savefig(Path.cwd()/"paper-30-cauchy-law.png",facecolor="white",transparent=False)
plt.close(fig)
