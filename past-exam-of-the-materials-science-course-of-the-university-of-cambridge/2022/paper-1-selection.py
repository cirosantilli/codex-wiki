import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":11,"savefig.facecolor":"white","figure.facecolor":"white"})
fig,ax=plt.subplots(figsize=(7.0,5.4))
rhos=np.array([7.8,2.8,.55,1.6]);strength=np.array([2000,600,40,1000])
labels=["Steel","Al alloy","Pine: compression limit","Illustrative composite\n(assumed, not product data)"]
for i,(rho,sig,label) in enumerate(zip(rhos,strength,labels)):
 ax.scatter(rho,sig,s=75,c="#7252a2" if i==3 else "#245e86",zorder=4)
 ax.annotate(label,(rho,sig),xytext=(-8 if i==0 else 7,8 if i!=3 else 34),ha="right" if i==0 else "left",textcoords="offset points",fontsize=9)
r=np.geomspace(.35,12,300)
ax.plot(r,(2000/7.8)*r,"--",color="#b46025",label="Fixed height: constant strength / density")
ax.plot(r,(40/.55**2)*r**2,":",color="#3b8253",label="Fixed width: constant sqrt(strength) / density")
ax.set_xscale("log");ax.set_yscale("log");ax.set(xlim=(.35,12),ylim=(12,5000),xlabel=r"Density (Mg m$^{-3}$)",ylabel="Limiting bending strength (MPa)",title="Strength-limited cantilever screening")
ax.grid(which="both",alpha=.17);ax.legend(loc="lower right",fontsize=8,frameon=False)
fig.tight_layout();fig.savefig("paper-1-selection.png",dpi=140)
