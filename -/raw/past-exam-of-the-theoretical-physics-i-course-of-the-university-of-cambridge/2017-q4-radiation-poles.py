"""Original figure; tested with Python 3.14.4.
Uses NumPy 2.3.5 and Matplotlib 3.10.7 from the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
fig,ax=plt.subplots(1,2,figsize=(9.2,4),layout="constrained")
for eps,col,marker in [(.12,"#1565a8","o"),(-.12,"#ca6720","^")]:
 roots=np.roots([-1j*eps,-1,0,1])
 for a in ax:a.scatter(roots.real,roots.imag,color=col,marker=marker,s=50,label=f"ε = {eps:+.2f}")
for a in ax:
 a.axhline(0,color=".4",lw=1);a.axvline(0,color=".7",lw=.8)
 a.set_xlabel(r"$\operatorname{Re}\omega$");a.set_ylabel(r"$\operatorname{Im}\omega$")
 a.grid(alpha=.13);a.legend(frameon=False,fontsize=9)
ax[0].set(xlim=(-1.35,1.35),ylim=(-.16,.16),title="Slow poles near ±1")
ax[0].text(0,.115,"growth",ha="center",fontsize=9)
ax[0].text(0,-.135,"decay",ha="center",fontsize=9)
ax[1].set(xlim=(-1.35,1.35),ylim=(-9.8,9.8),title="All three poles: fast scale ≈ i/ε")
ax[1].annotate("positive ε: runaway",xy=(0,8.45),xytext=(-1.2,5.3),arrowprops={"arrowstyle":"->"},fontsize=9)
ax[1].annotate("negative ε: fast decay",xy=(0,-8.45),xytext=(-1.2,-5.4),arrowprops={"arrowstyle":"->"},fontsize=9)
fig.suptitle("No nonzero sign puts every pole below the real axis")
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135)
