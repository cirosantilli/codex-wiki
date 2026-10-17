"""Original analytic illustration. Tested with Python 3.14, NumPy and Matplotlib.
Run from the intended output directory; the PNG is written to the current directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "savefig.facecolor": "white"})

a=np.linspace(-7,9,1801); E=.5+4/((a-1)**2+2)
fig,ax=plt.subplots(figsize=(7.7,3.7),layout="constrained")
ax.plot(a,E,color="#173e62",lw=2,label=r"$\mathcal{E}(a)=1/2+4/[(a-1)^2+2]$")
ax.axhline(.5,color=".4",ls="--",label="Ground-state infimum")
ax.scatter([1],[2.5],color="#b64526",zorder=3)
ax.annotate("a = 1: exact n = 2 state\nmaximum, not minimum",xy=(1,2.5),xytext=(3.2,2),arrowprops={"arrowstyle":"->","color":".25"})
ax.set(xlabel="Trial parameter a",ylabel="Reduced energy",ylim=(.35,2.85),title="Unconstrained minimization does not recover this excited state")
ax.legend(frameon=False,loc="upper left")
fig.savefig("paper-2b-variational-quotient.png",dpi=165)
plt.close(fig)
