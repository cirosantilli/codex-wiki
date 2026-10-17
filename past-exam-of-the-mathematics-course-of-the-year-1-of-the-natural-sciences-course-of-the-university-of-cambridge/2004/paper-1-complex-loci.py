"""Original complex-plane circle, stretch, translation and rotation loci."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

theta=np.linspace(0,2*np.pi,900)
z=-1-1j+8*np.exp(1j*theta)
loci=[(z,-1-1j,"z: center (−1, −1), radius 8"),(2*z.real+1j*z.imag,-2-1j,"u: center (−2, −1), semiaxes 16 and 8"),(z+4+3j,3+2j,"v: center (3, 2), radius 8"),(1j*(z+4+3j),-2+3j,"w: center (−2, 3), radius 8")]
fig,axes=plt.subplots(2,2,figsize=(9.4,7.8),layout="constrained")
for ax,(curve,center,title),color in zip(axes.flat,loci,["#2975a1","#b05c2a","#528a3d","#885b9e"]):
    ax.plot(curve.real,curve.imag,color=color,lw=2)
    ax.scatter([center.real],[center.imag],color=color,s=24,zorder=4)
    ax.axhline(0,color="#555555",lw=.7);ax.axvline(0,color="#555555",lw=.7)
    padx=2.5;pady=2.5
    ax.set(xlim=(curve.real.min()-padx,curve.real.max()+padx),ylim=(curve.imag.min()-pady,curve.imag.max()+pady),xlabel="Real coordinate",ylabel="Imaginary coordinate",title=title)
    ax.set_aspect("equal");ax.grid(alpha=.16)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
