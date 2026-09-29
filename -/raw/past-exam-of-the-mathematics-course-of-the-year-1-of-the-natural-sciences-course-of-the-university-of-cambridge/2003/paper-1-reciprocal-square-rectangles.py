"""Original unit-rectangle comparison for a reciprocal-square tail."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(5,10,1000)
fig,ax=plt.subplots(figsize=(7.3,4.3),layout="constrained")
for n in range(6,11):
    ax.bar(n-1,1/n**2,width=1,align="edge",color="#b6b6b6",alpha=.24,edgecolor="#555555",lw=.8,label=r"Height $1/n^2$ on $[n-1,n]$" if n==6 else None)
ax.plot(x,1/x**2,color="#b26a31",lw=2,label=r"Upper curve $x^{-2}$")
ax.plot(x,1/(x+1)**2,color="#287da5",lw=2,label=r"Lower curve $(x+1)^{-2}$")
ax.set(xlim=(5,10),ylim=(0,.043),xticks=np.arange(5,11),xlabel="x",ylabel="Height",title="Integrating the bounds and summing the unit rectangles")
ax.legend(loc="upper right",fontsize=9);ax.grid(alpha=.14)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
