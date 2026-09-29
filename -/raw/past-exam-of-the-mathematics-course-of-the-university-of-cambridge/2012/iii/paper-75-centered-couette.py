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
fig,axes=plt.subplots(2,1,figsize=(8.4,5),facecolor="white")
xi=np.linspace(-3.2,3.2,500);eta=np.linspace(0,11.5,450)
XX,YY=np.meshgrid(xi,eta);H=1+XX*XX;z=YY/H;A=-3+4/H
psi=H*(-z+z*z/2+A*(z**3/3-z*z/2))
psi=np.ma.masked_where(YY>H,psi)
for ax,sign,description in zip(axes,[-1,1],["upper wall: +U","lower wall: -U"]):
    field=sign*psi;levels=sorted(sign*np.array([-3,-1.8,-1,-.8,-2/3,-.5,-.25,-.1]))
    ax.contour(XX,YY,field,levels=levels,colors="#2673a5",linewidths=1)
    ax.plot(xi,1+xi*xi,color="#333333",lw=2);ax.axhline(0,color="#333333",lw=2)
    ax.fill_between(xi,1+xi*xi,12,color="#dddddd")
    ax.set_xlim(-3.2,3.2);ax.set_ylim(-.1,10.7);ax.set_ylabel("gap distance / d")
    ax.set_title(description,fontsize=10)
    direction=1 if sign==-1 else -1
    ax.annotate("",xy=(direction*.7,.3),xytext=(-direction*.7,.3),arrowprops={"arrowstyle":"->","color":"#b44826","lw":2})
axes[0].invert_yaxis();axes[0].set_xticklabels([])
axes[1].set_xlabel(r"$\xi=x/\sqrt{2ad}$")
fig.suptitle("Centered force-free cylinder: equal gaps, opposite leading flows")
fig.subplots_adjust(left=.12,right=.97,bottom=.18,top=.82,hspace=.36)
fig.text(.5,.025,"Contact-region zooms; cylinder lies between the two gaps. V = 0 at leading order.",ha="center",fontsize=9)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
plt.close(fig)
