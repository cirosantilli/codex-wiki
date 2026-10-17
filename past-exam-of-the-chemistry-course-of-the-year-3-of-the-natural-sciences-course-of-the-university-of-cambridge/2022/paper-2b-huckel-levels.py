"""Original analytic illustration. Tested with Python 3.14, NumPy and Matplotlib.
Run from the intended output directory; the PNG is written to the current directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "savefig.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,5),layout="constrained",sharey=True)
n=.5; D=np.sqrt((n-1)**2+4)
levels=[[-2,0,0,2],[-(n+1+D)/2,-(D-n-1)/2,(D-n-1)/2,(n+1+D)/2]]
labels=[[r"$A_{1g}$",r"$E_u$",r"$E_u$",r"$B_{1g}$"],[r"$A_1$",r"$B_1$",r"$A_1$",r"$B_1$"]]
for j,ax in enumerate(axs):
 for k,(e,l) in enumerate(zip(levels[j],labels[j])):
  x=(.35 if k==1 else 1.05) if j==0 and k in (1,2) else .7
  ax.plot([x-.23,x+.23],[e,e],color="#173e62",lw=2)
  ax.text(x,e+.13,l,ha="center")
 ax.axhline(0,color=".7",ls=":",zorder=0)
 ax.set(xlim=(0,1.8),ylim=(-2.5,2.7),xticks=[],title=("Square, n = 1" if j==0 else "Trapezium, illustrative n = 0.5"))
axs[0].set_ylabel(r"$(E-\alpha)/|\beta|$, with $\beta<0$")
fig.suptitle("Four spatial orbitals; each can hold two opposite-spin electrons")
fig.savefig("paper-2b-huckel-levels.png",dpi=165)
plt.close(fig)
