"""Original schematic hard-core liquid radial distribution, not fitted data."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

r=np.linspace(0,6,1500);g=np.zeros_like(r)
outside=r>=1;u=r[outside]-1
g[outside]=1+1.6*np.exp(-u/1.1)*np.cos(5.2*u)
fig,ax=plt.subplots(figsize=(7.2,4.2),layout="constrained")
ax.axvspan(0,1,color="#aaaaaa",alpha=.17)
ax.plot(r,g,color="#287fa8",lw=2)
ax.axhline(1,color="#666666",ls="--",lw=1,label="Uncorrelated limit")
ax.text(.5,.48,"Excluded\ncore",ha="center",fontsize=12)
ax.annotate("Nearest-neighbor shell",xy=(1,2.6),xytext=(2.15,2.5),arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=11)
ax.annotate("Weaker coordination shells",xy=(2.2,1.53),xytext=(3.0,2.0),arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=11)
ax.set(xlim=(0,6),ylim=(-.06,2.95),xlabel="Separation / effective core diameter",ylabel="g(r)",title="Short-range liquid structure with a finite correlation range")
ax.legend(loc="lower right",fontsize=10);ax.grid(alpha=.14)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
