"""Original exam-solution figure; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Writes an opaque PNG with the same basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6.3,3.3),dpi=100,facecolor="white")
theta=np.linspace(.001,np.pi-.001,600);ax.plot(6+5*np.cos(theta),5*np.sin(theta),color="#245c88",lw=2)
ax.axhline(0,color="#444444",lw=1)
ax.scatter([2,10],[3,3],color="#a5432b",zorder=3)
ax.annotate("(2, 3)",(2,3),xytext=(1.5,3.45));ax.annotate("(10, 3)",(10,3),xytext=(9.5,3.45))
ax.scatter([1,11],[0,0],facecolors="white",edgecolors="#245c88",zorder=3)
ax.set(xlim=(0,12),ylim=(-.2,5.8),xlabel="x",ylabel="y",title="(x − 6)² + y² = 25, y > 0")
ax.set_aspect("equal");ax.grid(alpha=.12)
fig.subplots_adjust(left=.09,right=.98,bottom=.16,top=.87)

fig.savefig(Path.cwd()/(Path(__file__).stem+".png"),facecolor="white",transparent=False)
plt.close(fig)
