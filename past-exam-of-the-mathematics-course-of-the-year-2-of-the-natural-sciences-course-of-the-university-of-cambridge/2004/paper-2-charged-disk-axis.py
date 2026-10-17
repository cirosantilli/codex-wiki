"""Original axial potential and one-sided normal fields of a uniform disk."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

s=np.linspace(-4,4,1401)
fig,axes=plt.subplots(1,2,figsize=(9.2,4.3),layout="constrained")
ax=axes[0];ax.plot(s,np.sqrt(1+s*s)-abs(s),color="#287fa8",lw=2,label="Exact axis potential")
near=s[abs(s)<.85];ax.plot(near,1-abs(near)+near**2/2,color="#b5682e",ls="--",lw=1.5,label="Near-center expansion")
for region in [s[s<-1.2],s[s>1.2]]:
    ax.plot(region,1/(2*abs(region))-1/(8*abs(region)**3),color="#638d40",ls=":",lw=2,label="Far-field expansion" if region[0]>0 else None)
ax.set(ylabel=r"$\psi/(\sigma a/2\epsilon_0)$",ylim=(0,1.08),title="Continuous potential with a cusp")
ax.legend(fontsize=9)
ax=axes[1]
for region in [s[s<0],s[s>0]]:
    field=np.sign(region)-region/np.sqrt(1+region**2)
    ax.plot(region,field,color="#89538d",lw=2)
ax.scatter([0,0],[-1,1],s=42,facecolors="white",edgecolors="#89538d",zorder=5)
ax.annotate("Jump = σ/ε₀",xy=(0,.95),xytext=(1.1,.75),arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=11)
ax.set(ylabel=r"$E_z/(\sigma/2\epsilon_0)$",ylim=(-1.15,1.15),title="One-sided field values at the sheet")
for ax in axes:
    ax.axvline(0,color="#777777",lw=.8);ax.axhline(0,color="#777777",lw=.8)
    ax.set(xlim=(-4,4),xlabel="Height z/a");ax.grid(alpha=.15)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
