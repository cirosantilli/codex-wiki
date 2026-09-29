"""Original hydrogenic radial-scale comparison; outputs basename in cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
alpha=1/137.036;hc=197.3;mp=938.272
def bohr(m):return hc/(alpha*(m*mp/(m+mp)))
ae,amu=bohr(.511),bohr(106)
r=np.geomspace(.1,2e6,1200)
fig,axs=plt.subplots(1,2,figsize=(10,4.3),layout="constrained")
for a,name,color in [(ae,"Electronic hydrogen","#1c5b94"),(amu,"Muonic hydrogen","#b44824")]:
 x=r/a;density=4*x**3*np.exp(-2*x)
 axs[0].plot(r,density,label=name,color=color,lw=2)
axs[0].set(xscale="log",xlabel="Radius r (fm)",ylabel=r"Probability per unit $\ln r$",title="Normalized 1s point-charge model")
axs[0].legend(fontsize=10);axs[0].grid(alpha=.2)
ax=axs[1];ax.axis("off")
ax.text(.5,.95,"Reduced mass fixes the length scale",ha="center",va="top",fontsize=12,weight="bold",transform=ax.transAxes)
ax.text(.08,.73,rf"Electronic hydrogen: $a={ae:,.0f}$ fm",fontsize=12,transform=ax.transAxes)
ax.text(.08,.58,rf"Muonic hydrogen: $a={amu:.1f}$ fm",fontsize=12,transform=ax.transAxes)
ax.text(.08,.42,rf"Radius ratio: $a_e/a_\mu={ae/amu:.1f}$",fontsize=12,transform=ax.transAxes)
ax.text(.08,.17,"Finite proton mass is retained.\nFinite charge radius, relativity and QED\ncorrections are omitted from these curves.",fontsize=11,transform=ax.transAxes)
fig.savefig("paper-1-muonic-scales.png",dpi=150,facecolor="white")
