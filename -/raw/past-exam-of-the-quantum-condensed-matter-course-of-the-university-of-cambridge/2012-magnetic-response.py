"""Original illustrative figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the corresponding _media directory; the PNG is written to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

h=np.linspace(-1.5,1.5,700);fig,(ax,bx)=plt.subplots(1,2,figsize=(8.8,3.6),layout="constrained")
ax.plot(h,.35*h,label="Paramagnet",color="#2563eb");ax.plot(h,-.15*h,label="Diamagnet",color="#dc2626");ax.set(xlabel="Applied field H (arbitrary units)",ylabel="Magnetization M",title="Weak-field linear response");ax.legend()
up=np.tanh(3*(h-.35));down=np.tanh(3*(h+.35));bx.plot(h,up,color="#2563eb",label="Increasing H");bx.plot(h,down,color="#dc2626",label="Decreasing H");bx.set(xlabel="Applied field H (arbitrary units)",ylabel="Magnetization M (normalized)",title="Schematic ferromagnetic loop");bx.legend(fontsize=8,loc="lower right")
bx.annotate("Remanence",xy=(0,np.tanh(1.05)),xytext=(-1.4,.9),arrowprops={"arrowstyle":"->"},fontsize=9)
bx.plot([-.35,.35],[0,0],"o",color="black",ms=3)
for a in (ax,bx):a.axhline(0,color="black",lw=.6);a.axvline(0,color="black",lw=.6);a.grid(alpha=.15)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
