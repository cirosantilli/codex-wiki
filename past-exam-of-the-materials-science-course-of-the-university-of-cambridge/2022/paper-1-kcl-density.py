import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":11,"savefig.facecolor":"white","figure.facecolor":"white"})
Avogadro = 6.02214076e23  # exact SI mol^-1
P=np.array([1.20,2.00,2.55,2.56,3.14,3.81]);a=np.array([6.179,6.109,6.076,3.659,3.638,3.618])*1e-10
Z=np.array([4,4,4,1,1,1]);rho=Z*.0745513/(Avogadro*a**3)
fig,ax=plt.subplots(figsize=(6.4,4.7))
for sl,label,col in [(slice(0,3),"Rock-salt structure (Z = 4)","#245e86"),(slice(3,6),"CsCl structure (Z = 1)","#be6231")]:
 ax.plot(P[sl],rho[sl],"o-",color=col,label=label)
ax.axvline(2.555,color="0.5",linestyle="--",linewidth=1)
ax.annotate("Density jump at structural transition",(2.555,2370),xytext=(1.30,2440),arrowprops={"arrowstyle":"->"},fontsize=9)
ax.set(xlabel="Pressure (GPa)",ylabel=r"Density (kg m$^{-3}$)",title="KCl: cell mass divided by cell volume",xlim=(1,4),ylim=(2020,2680));ax.legend(frameon=False,loc="lower right",fontsize=9);ax.grid(alpha=.15)
fig.tight_layout();fig.savefig("paper-1-kcl-density.png",dpi=140)
