"""Original tangent-displacement patterns for an arc-spring ring with μ=2."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

angles=np.array([0,2*np.pi/3,4*np.pi/3])
points=np.column_stack([np.cos(angles),np.sin(angles)])
tangents=np.column_stack([-np.sin(angles),np.cos(angles)])
phi=np.linspace(0,2*np.pi,600)
modes=[[1,1,1],[1,-1,0],[1,1,-1]]
titles=[r"Rigid rotation: $\omega^2=0$",r"Antisymmetric: $\omega^2=3k/m$",r"Symmetric: $\omega^2=2k/m$"]
fig,axes=plt.subplots(1,3,figsize=(10.2,3.9),layout="constrained")
for ax,mode,title in zip(axes,modes,titles):
    ax.plot(np.cos(phi),np.sin(phi),color="#a3a3a3",lw=1.7)
    for i,(position,tangent,amplitude) in enumerate(zip(points,tangents,mode)):
        color="#287fa8" if i<2 else "#b5682e"
        ax.scatter([position[0]],[position[1]],s=95 if i<2 else 155,color=color,zorder=5)
        label=[r"$m_1=m$",r"$m_2=m$",r"$m_3=2m$"][i]
        lp=position+np.array([.12,-.08]) if i==0 else 1.28*position
        ax.text(*lp,label,ha="left" if i==0 else "center",va="center",fontsize=10)
        if amplitude:
            ax.annotate("",xy=position+.42*amplitude*tangent,xytext=position,arrowprops=dict(arrowstyle="-|>",color=color,lw=2.1,mutation_scale=15))
        else:ax.text(position[0]+.15,position[1]+.2,"Fixed",fontsize=10)
    ax.set(title=title,xlim=(-1.6,1.7),ylim=(-1.55,1.55));ax.set_aspect("equal");ax.axis("off")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
