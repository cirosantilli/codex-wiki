"""Original free-electron Fermi circles relative to a square Brillouin zone."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle

fig,axes=plt.subplots(1,2,figsize=(8.2,4.5),layout="constrained")
for ax,valence in zip(axes,[1,2]):
    radius=np.sqrt(2*valence/np.pi)
    ax.add_patch(Circle((0,0),radius,facecolor="#c9dfeb",edgecolor="#287fa8",lw=2))
    ax.add_patch(Rectangle((-1,-1),2,2,facecolor="none",edgecolor="#555555",lw=1.8))
    ax.axhline(0,color="#888888",lw=.7);ax.axvline(0,color="#888888",lw=.7)
    ax.set(xlim=(-1.43,1.43),ylim=(-1.43,1.43),xticks=[-1,0,1],yticks=[-1,0,1],xlabel=r"$k_x/(\pi/a)$",ylabel=r"$k_y/(\pi/a)$",title=f"{valence} electron{'s' if valence==2 else ''} per cell")
    ax.text(0,1.28,r"$k_F/(\pi/a)=$"+f"{radius:.3f}",ha="center",fontsize=10)
    ax.set_aspect("equal");ax.grid(alpha=.12)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
