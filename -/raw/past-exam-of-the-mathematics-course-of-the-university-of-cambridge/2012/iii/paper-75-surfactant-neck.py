"""Original Paper 75 figure. Python 3.14, root matplotlib/numpy dependencies.
Requires caller-supplied MPLCONFIGDIR; writes basename PNG only to cwd.
"""
from pathlib import Path
import os
if not os.environ.get("MPLCONFIGDIR"):
    raise RuntimeError("Set MPLCONFIGDIR to a caller-owned cache directory")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10})
fig,ax=plt.subplots(figsize=(8.4,4.2),facecolor="white")
x=np.linspace(-3.2,3.2,500);h=1-.35*np.exp(-x*x)
ax.fill_between(x,-h,h,color="#d9edf8")
ax.plot(x,h,color="#277ca6",lw=2);ax.plot(x,-h,color="#277ca6",lw=2)
dots=np.r_[np.linspace(-3,-1.15,9),[-.65,.65],np.linspace(1.15,3,9)]
dh=1-.35*np.exp(-dots*dots)
ax.scatter(dots,dh,s=23,color="#225f9c");ax.scatter(dots,-dh,s=23,color="#225f9c")
for side in [-1,1]:
    ax.annotate("",xy=(side*2.1,.42),xytext=(side*.4,.25),arrowprops={"arrowstyle":"->","lw":2,"color":"#b83b2c"})
    ax.annotate("",xy=(side*.35,1.05),xytext=(side*2.1,1.22),arrowprops={"arrowstyle":"->","lw":2,"color":"#26844b"})
ax.text(0,1.62,"expanded neck\nless surfactant, higher tension",ha="center",fontsize=10)
ax.text(-2.55,1.82,"concentration rises\ntension falls",ha="center",fontsize=9)
ax.text(2.55,1.82,"concentration rises\ntension falls",ha="center",fontsize=9)
ax.text(0,-1.48,"red: draining fluid away from neck    green: opposing Marangoni stress",ha="center",fontsize=9)
ax.set_xlim(-3.4,3.4);ax.set_ylim(-1.8,2.35);ax.axis("off")
ax.set_title("Surfactant resists rupture at the same equilibrium surface tension")
fig.subplots_adjust(left=.03,right=.97,bottom=.07,top=.86)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
plt.close(fig)
