"""Original square-wave Fourier approximations, including jump midpoint values."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(8.4,4.3),layout="constrained")
for a,b,y in [(-5,0,0),(0,5,6),(5,10,0),(10,15,6)]:
    ax.plot([a,b],[y,y],color="#222222",lw=2.2,label="Wave on open intervals" if a==-5 else None)
    ax.scatter([a,b],[y,y],facecolors="white",edgecolors="#222222",s=26,zorder=5)
x=np.linspace(-5,15,2200)
for count,color in [(3,"#c27c2c"),(15,"#277bab")]:
    n=np.arange(1,2*count,2)[:,None]
    partial=3+12/np.pi*np.sum(np.sin(n*np.pi*x[None,:]/5)/n,axis=0)
    ax.plot(x,partial,color=color,lw=1.2,label=f"{count} odd harmonics")
ax.scatter([-5,0,5,10,15],[3]*5,color="#7b4191",s=27,zorder=6,label="Series value at each jump")
ax.axhline(3,color="#777777",ls=":",lw=.8)
ax.set(xlim=(-5.25,15.25),ylim=(-1,7),xticks=[-5,0,5,10,15],yticks=[0,3,6],xlabel="x",ylabel="Value",title="Period 10: midpoint convergence and Gibbs oscillations")
ax.grid(alpha=.15);ax.legend(loc="upper right",fontsize=9)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
