"""Original s/p_x cosine bands with equal-coefficient orbital signs."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Ellipse

q=np.linspace(-np.pi,np.pi,900)
fig,axes=plt.subplots(2,2,figsize=(9.2,5.8),layout="constrained",gridspec_kw={"height_ratios":[2,1]})
for ax,energy,label in [(axes[0,0],-2*np.cos(q),"s band: negative nearest-neighbor hopping"),(axes[0,1],2*np.cos(q),"pₓ band: positive σ hopping")]:
    ax.plot(q/np.pi,energy,color="#2a729e",lw=2)
    ax.set(xlabel=r"$ka/\pi$",ylabel="Energy / hopping magnitude",xlim=(-1,1),ylim=(-2.35,2.35),title=label)
    ax.set_xticks([-1,0,1]);ax.grid(alpha=.18)
for col,ax in enumerate(axes[1]):
    ax.axhline(0,color="#777777",lw=.7)
    for j in [0,1,2]:
        if col==0:
            ax.add_patch(Circle((j,0),.28,facecolor="#99bfd8",edgecolor="#34779d",alpha=.85))
            ax.text(j,0,"+",ha="center",va="center",fontsize=13)
        else:
            for direction,color,sign in [(-1,"#d8a180","−"),(1,"#99bfd8","+")]:
                ax.add_patch(Ellipse((j+direction*.2,0),.38,.4,facecolor=color,edgecolor="#555555",lw=.8))
                ax.text(j+direction*.2,0,sign,ha="center",va="center",fontsize=12)
            ax.scatter([j],[0],s=7,color="#333333",zorder=4)
    ax.set(xlim=(-.5,2.5),ylim=(-.65,.65),xticks=[0,1,2],yticks=[],xlabel="Atomic site j")
    ax.set_aspect("equal")
    ax.set_title("At k = 0: facing signs match (bonding)" if col==0 else "At k = 0: facing signs oppose (antibonding)",fontsize=10)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
