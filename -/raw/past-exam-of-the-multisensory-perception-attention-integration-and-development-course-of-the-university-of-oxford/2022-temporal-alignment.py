from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,ax=plt.subplots(1,2,figsize=(9.4,3.6),layout="constrained")
d=np.linspace(0,100,301);delay=1000*d*(1/343-1/299792458)
ax[0].plot(d,delay,color="#00549f",lw=2)
ax[0].scatter([10,100],[1000*x*(1/343-1/299792458) for x in [10,100]],color="#00549f")
ax[0].annotate("10 m: 29.15 ms",(10,29.15),xytext=(20,60),arrowprops={"arrowstyle":"->"})
ax[0].set(xlabel="Source distance (m)",ylabel="Auditory minus visual travel time (ms)",title="Propagation delay grows with distance",xlim=(0,105),ylim=(0,320))
delta=np.linspace(-250,250,1001)
Phi=lambda z:np.array([.5*(1+math.erf(float(v)/math.sqrt(2))) for v in z])
for b,h,s,label,color,ls in [(0,60,30,"b = 0, h = 60, s = 30 ms","#00549f","-"),(-45,60,30,"b = −45, h = 60, s = 30 ms","#b01935","-"),(0,100,30,"b = 0, h = 100, s = 30 ms","#36803e","--")]:
 p=Phi((h-delta-b)/s)-Phi((-h-delta-b)/s)
 ax[1].plot(delta,p,label=label,color=color,lw=2,ls=ls)
ax[1].set(xlabel="Physical auditory minus visual onset (ms)",ylabel="Probability of reporting simultaneous",title="Offset and acceptance bounds differ",ylim=(-.02,1.04),xlim=(-250,250));ax[1].legend(fontsize=8,loc="upper left")
for a in ax:a.grid(alpha=.18)
fig.savefig(Path.cwd()/"2022-temporal-alignment.png",dpi=110,transparent=False)
