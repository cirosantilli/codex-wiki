"""Python 3.14; NumPy and Matplotlib in ../pyproject.toml. Output in CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x=np.linspace(-.85,1,1000)
p5=x-x*x/2+x**3/3-x**4/4+x**5/5
p3=1/32+15*x/16-3*x*x/4+7*x**3/12
xx=np.linspace(-1,1,1000)
diff=np.polynomial.chebyshev.chebval(xx,[0,0,0,0,-1/32,1/80])
fig,axs=plt.subplots(1,2,figsize=(9,3.9),facecolor="white")
axs[0].plot(x,np.log1p(x),label="log(1+x)",lw=2)
axs[0].plot(x,p5,label="Fifth-degree Taylor polynomial",ls="--")
axs[0].plot(x,p3,label="Economized cubic",ls=":")
axs[0].set(title="Polynomial reduction away from the singular endpoint",xlabel="x",ylabel="Value")
axs[0].legend(frameon=False,fontsize=8)
axs[1].plot(xx,diff,lw=2)
axs[1].axhline(7/160,color=".6",ls="--");axs[1].axhline(-7/160,color=".6",ls="--")
axs[1].scatter([-1],[-7/160],color="C1",zorder=4)
axs[1].set(title="Added polynomial change is at most 7/160",xlabel="x",ylabel="p5 - p3",xlim=(-1,1))
for ax in axs:ax.spines[["top","right"]].set_visible(False)
fig.tight_layout();fig.savefig("2008-log-economization.png",dpi=150,facecolor="white")
