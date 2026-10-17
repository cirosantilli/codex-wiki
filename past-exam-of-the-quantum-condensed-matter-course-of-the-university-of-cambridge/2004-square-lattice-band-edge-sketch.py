"""Original directional two-wave gap sketches under the stated isotropic-gap model."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

hbar=1.054571817e-34;mass=9.1093837139e-31;charge=1.602176634e-19;a=.3e-9
ex=hbar*hbar*np.pi**2/(2*mass*a*a)/charge
eg=4.0;upper_min=ex+eg/2;lower_max=2*ex-eg/2
q=np.linspace(.7,1.3,700)
fig=plt.figure(figsize=(9.2,6.6),layout="constrained")
grid=fig.add_gridspec(2,2,height_ratios=[3.2,1.25])
axes=[fig.add_subplot(grid[0,0]),fig.add_subplot(grid[0,1])]
for ax,edge,title in zip(axes,[ex,2*ex],["[10] face boundary","[11] corner boundary (two-wave sketch)"]):
    e0=edge*q*q;e1=edge*(q-2)**2
    center=(e0+e1)/2;split=np.sqrt(((e0-e1)/2)**2+(eg/2)**2)
    ax.plot(q,center-split,color="#287fa8",lw=2,label="Lower branch")
    ax.plot(q,center+split,color="#ac6632",lw=2,label="Upper branch")
    ax.axvline(1,color="#777777",ls=":",lw=.9)
    ax.axhspan(upper_min,lower_max,color="#b78b3e",alpha=.24)
    ax.annotate("",xy=(1,edge+eg/2),xytext=(1,edge-eg/2),arrowprops=dict(arrowstyle="<->",color="#555555"))
    ax.text(1.018,edge,"4 eV",va="center",fontsize=10)
    ax.set(xlim=(.7,1.3),ylim=(0,15.5),xlabel=r"$k/k_{\mathrm{boundary}}$",ylabel="Energy (eV)",title=title)
    ax.grid(alpha=.14)
axes[0].legend(loc="upper left",fontsize=9)
ax=fig.add_subplot(grid[1,:])
ax.axvspan(upper_min,lower_max,color="#b78b3e",alpha=.24)
ax.vlines([upper_min,lower_max],.15,.9,color=["#ac6632","#287fa8"],lw=1.8)
ax.text(upper_min,.95,f"X upper edge: {upper_min:.2f} eV",ha="center",va="bottom",fontsize=10)
ax.text(lower_max,.95,f"Corner lower edge: {lower_max:.2f} eV",ha="center",va="bottom",fontsize=10)
ax.text((upper_min+lower_max)/2,.48,"Fermi level lies within the overlap\n(exact value is not specified)",ha="center",va="center",fontsize=10)
ax.set(xlim=(6.00,6.52),ylim=(0,1.2),yticks=[],xlabel="Energy near the overlap (eV)",title=f"Different momenta overlap by {lower_max-upper_min:.2f} eV in this model")
ax.grid(axis="x",alpha=.12)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
