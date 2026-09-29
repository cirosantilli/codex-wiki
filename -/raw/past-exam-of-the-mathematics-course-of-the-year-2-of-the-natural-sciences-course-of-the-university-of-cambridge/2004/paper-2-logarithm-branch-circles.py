"""Original branch-cut crossing geometry for the two logarithm integrals."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

phi=np.linspace(0,2*np.pi,600)
fig,axes=plt.subplots(1,2,figsize=(8.7,4.6),layout="constrained")
for ax,beta,title,label in zip(axes,[0,np.pi/2],[r"Positive-real cut: $I=2\pi i$",r"Positive-imaginary cut: $I=-2\pi R$"],[r"$z_0=1$",r"$z_0=iR$"]):
    ax.axhline(0,color="#777777",lw=.8);ax.axvline(0,color="#777777",lw=.8)
    ax.plot(np.cos(phi),np.sin(phi),color="#287fa8",lw=2)
    direction=np.exp(1j*beta)
    ax.plot([0,1.48*direction.real],[0,1.48*direction.imag],color="#b35730",lw=2,ls="--")
    ax.scatter([direction.real],[direction.imag],s=45,color="#b35730",zorder=5)
    offset=np.array([.14,-.25]) if beta==0 else np.array([.12,.12])
    ax.text(direction.real+offset[0],direction.imag+offset[1],label,fontsize=12)
    ax.text(1.3*direction.real+.08,1.3*direction.imag+.05,"Cut",color="#b35730",fontsize=11)
    begin,end=.55,.85
    ax.annotate("",xy=(np.cos(end),np.sin(end)),xytext=(np.cos(begin),np.sin(begin)),arrowprops=dict(arrowstyle="-|>",color="#287fa8",lw=2,mutation_scale=16))
    ax.set(title=title,xlim=(-1.45,1.65),ylim=(-1.45,1.65),xlabel="Real coordinate (scaled)",ylabel="Imaginary coordinate (scaled)",xticks=[-1,0,1],yticks=[-1,0,1])
    ax.set_aspect("equal");ax.grid(alpha=.12)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
