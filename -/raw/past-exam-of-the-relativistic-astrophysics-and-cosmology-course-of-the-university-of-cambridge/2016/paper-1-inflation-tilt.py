"""Original explanatory calculation. Save the PNG basename in the working directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

k=np.geomspace(.001,1000,500)
eps=.01
fig,ax=plt.subplots(figsize=(8,3.8),layout="constrained")
ax.plot(k,k**(-2*eps),"k--",label=r"Tensor: $n_T=-2\epsilon_H=-0.02$")
for eps2,color in [(.04,"#0072b2"),(0,"#d55e00"),(-.04,"#009e73")]:
 slope=-2*eps-eps2
 ax.plot(k,k**slope,color=color,label=rf"Scalar: $\epsilon_2={eps2:+.2f}$, $n_s-1={slope:+.2f}$")
ax.axvline(1,ls=":",color="#999999")
ax.set(xscale="log",xlabel=r"$k/k_*$",ylabel="Power / power at pivot",title=r"Illustrative local slow-roll slopes at $\epsilon_H=0.01$")
ax.legend(fontsize=9)
fig.text(.5,-.02,r"$\epsilon_2=d\ln\epsilon_H/dN$; the curves illustrate local slopes, not a fitted CMB data set.",ha="center",fontsize=9)
finish(fig,"paper-1-inflation-tilt")
