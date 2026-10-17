"""Original atmospheric-chemistry illustration; Python 3.14, NumPy, Matplotlib.
Output is a PNG basename in the current working directory, not the source directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","savefig.facecolor":"white"})

eps=np.linspace(0,.4,401)
fig,axs=plt.subplots(1,2,figsize=(10,4.4),layout="constrained",sharey=True)
for ax,A,title in zip(axs,[.5,.7],["Marine baseline A = 0.5","Continental baseline A = 0.7"]):
 s=(1+eps)**(1/3);exact=s*A/(1-A+s*A)-A;linear=A*(1-A)*eps/3
 ax.plot(100*eps,exact,color="#174e78",lw=2,label="Finite-change optical model")
 ax.plot(100*eps,linear,color="#bd6438",ls="--",label="Initial derivative")
 e=.1;ds=1.1**(1/3)*A/(1-A+1.1**(1/3)*A)-A
 ax.axvline(10,color=".65",ls=":")
 ax.scatter([10],[ds],color="#174e78",zorder=5)
 ax.text(12,ds,f"ΔA = {ds:.5f}",va="top")
 ax.set(title=title,xlabel="Droplet-number increase (%)",xlim=(0,40),ylim=(0,.035))
axs[0].set_ylabel("Absolute cloud-albedo increase ΔA")
axs[0].legend(frameon=False,fontsize=9,loc="upper left")
fig.suptitle("Fixed water content and thickness; independently specified starting albedos")
fig.savefig("paper-id-cloud-susceptibility.png",dpi=165)
plt.close(fig)
