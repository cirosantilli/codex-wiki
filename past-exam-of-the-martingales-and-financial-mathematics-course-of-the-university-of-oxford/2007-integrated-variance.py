"""Original variance comparison. Python3.14, NumPy, Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,1,400)
fig,(ax,bx)=plt.subplots(1,2,figsize=(9,4),facecolor="white")
ax.plot(t,1+t,color="#2166ac",lw=2,label=r"$\sigma(t)/\alpha=1+t$")
ax.plot(t,np.full_like(t,1.5),color="#b2182b",ls="--",lw=2,label="arithmetic mean = 3/2")
ax.set(xlabel="time",ylabel="scaled volatility",ylim=(.8,2.2),title="Same arithmetic average")
ax.legend(fontsize=9)
bx.bar([0,1],[7/3,9/4],color=["#2166ac","#b2182b"],width=.55)
bx.set(xticks=[0,1],xticklabels=["true path","constant mean"],ylabel=r"total variance / $\alpha^2$",
       ylim=(0,2.8),title="Different integrated squares")
bx.text(0,7/3+.08,r"$7/3$",ha="center",fontsize=12)
bx.text(1,9/4+.08,r"$9/4$",ha="center",fontsize=12)
for a in[ax,bx]:a.spines[["top","right"]].set_visible(False)
fig.tight_layout();fig.savefig("2007-integrated-variance.png",dpi=150,facecolor="white")
