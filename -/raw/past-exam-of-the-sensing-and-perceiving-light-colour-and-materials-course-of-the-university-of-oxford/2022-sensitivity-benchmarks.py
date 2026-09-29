from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,ax=plt.subplots(1,2,figsize=(9.3,3.5),layout="constrained")
N=np.geomspace(100,1e6,500)
for delta,label,col,style in [(np.sqrt(N),"Poisson benchmark: ΔN = √N","#00549f","-"),(.02*N,"Fixed fraction: ΔN = 0.02 N","#a43c30","--")]:
 ax[0].loglog(N,delta,label=label,color=col,lw=2,ls=style)
 ax[1].loglog(N,delta/N,label=label,color=col,lw=2,ls=style)
ax[0].set(xlabel="Mean background photon count N",ylabel="Increment benchmark ΔN",title="Different absolute-threshold scaling")
ax[1].set(xlabel="Mean background photon count N",ylabel="Fractional increment ΔN / N",title="Different contrast-threshold scaling")
for a in ax:a.grid(alpha=.15,which="both");a.legend(fontsize=8)
fig.savefig(Path.cwd()/"2022-sensitivity-benchmarks.png",dpi=110,transparent=False)
