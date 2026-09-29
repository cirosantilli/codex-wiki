"""Python 3.14; NumPy and Matplotlib in ../pyproject.toml. Output in CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x=np.linspace(0,1,700);kernel=np.minimum(x,1-x)**2/2
fig,ax=plt.subplots(figsize=(6.6,3.7),facecolor="white")
ax.plot(x,kernel,lw=2.5,color="C0")
ax.fill_between(x,0,kernel,color="C0",alpha=.15)
ax.axvline(.5,color=".6",ls="--",lw=.8)
ax.text(.15,.017,"Area = 1/24",fontsize=11)
ax.set(xlabel="t / h",ylabel="K(t) / h²",title="Midpoint-rule Peano kernel",xlim=(0,1),ylim=(0,.145))
ax.spines[["top","right"]].set_visible(False)
fig.tight_layout();fig.savefig("2008-midpoint-peano.png",dpi=150,facecolor="white")
