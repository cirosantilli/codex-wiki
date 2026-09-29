"""Original solution figure; tested with Python 3.14.4.
Dependencies: NumPy 2.3.5 and Matplotlib 3.10.7 (root pyproject.toml).
Writes its PNG basename into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
u=np.linspace(0,3.8,18001)
f=np.exp(.5j*np.pi*u*u)
F=np.r_[0,np.cumsum((f[:-1]+f[1:])/2*np.diff(u))]
fig,ax=plt.subplots(figsize=(6.6,5.4),layout="constrained")
ax.plot(F.real,F.imag,color="#1565a8",lw=1.7)
ax.plot(-F.real,-F.imag,color="#1565a8",lw=1.7)
ax.plot([-.5,.5],[-.5,.5],color="#ca6720",lw=4,alpha=.45,ls="--",label="full open chord")
ax.annotate("",xy=(.5,.5),xytext=(0,0),arrowprops={"arrowstyle":"->","lw":2.4,"color":"#33865b"})
ax.scatter([-.5,0,.5],[-.5,0,.5],color="black",s=23,zorder=4)
ax.text(-.49,-.87,r"$P_-=(-1/2,-1/2)$",ha="center")
ax.text(.50,.86,r"$P_+=(1/2,1/2)$",ha="center")
ax.annotate("open half-plane chord",xy=(.24,.24),xytext=(-.66,.49),arrowprops={"arrowstyle":"->","color":"#33865b"},color="#33865b",fontsize=9)
ax.text(.05,-.12,"u = 0")
ax.set(xlim=(-.86,.86),ylim=(-.92,.96),xlabel=r"$C(u)$",ylabel=r"$S(u)$",aspect="equal")
ax.axhline(0,color=".75",lw=.7);ax.axvline(0,color=".75",lw=.7)
ax.legend(frameon=False,loc="lower right")
ax.set_title("Shadow boundary: half the field, one quarter of the intensity")
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135)
