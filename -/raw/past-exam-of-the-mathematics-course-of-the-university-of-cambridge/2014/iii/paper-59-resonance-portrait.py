"""Original exam-solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only the same-basename PNG in the current working directory.
Uses MPLCONFIGDIR supplied by the caller.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white"})
fig,axes=plt.subplots(1,2,figsize=(10,4.6),layout="constrained")
phi=np.linspace(0,2*np.pi,1800);pot=2*np.sin((phi-np.pi)/2)**2
for en,col in [(.08,"#2166ac"),(.65,"#2166ac"),(1.6,"#2166ac"),(2.,"#b2182b"),(2.6,"#555555")]:
 v=np.sqrt(np.maximum(0,2*(en-pot)));v[pot>en]=np.nan
 axes[0].plot(phi,v,c=col,lw=1.5);axes[0].plot(phi,-v,c=col,lw=1.5)
axes[0].scatter([0,np.pi,2*np.pi],[0,0,0],c=["#b2182b","#2166ac","#b2182b"])
axes[0].set(xticks=[0,np.pi,2*np.pi],xticklabels=["0","π","2π"],xlabel="Resonant argument φ",ylabel="Angular speed φ̇/ω₀",title="Libration (blue), separatrix (red), circulation (grey)")
axes[0].grid(alpha=.2)
z=np.linspace(-.04,.04,400);e0=.2;ratio=1/3
ee=np.sqrt(e0*e0+ratio*np.log1p(z))
axes[1].plot(1+z,ee,c="#2166ac",lw=2)
for idx,delta in [(130,15),(280,-15)]:
 axes[1].annotate("",(1+z[idx+delta],ee[idx+delta]),(1+z[idx],ee[idx]),arrowprops={"arrowstyle":"->","color":"#b2182b"})
axes[1].scatter([1],[e0],c="black",s=18)
axes[1].set(xlabel="Semimajor axis a/a(0)",ylabel="Eccentricity e",title="Same invariant curve traversed in both directions\nq/(p+q) = 1/3; e(0) = 0.2")
axes[1].grid(alpha=.2)
fig.savefig(Path(__file__).stem+".png",dpi=100,facecolor="white",transparent=False)
