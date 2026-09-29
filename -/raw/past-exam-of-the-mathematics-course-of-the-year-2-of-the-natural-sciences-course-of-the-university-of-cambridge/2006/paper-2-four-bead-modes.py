"""Original normal-mode diagrams with tangential arrows, without copied exam artwork."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

angles=np.arange(4)*np.pi/2
positions=np.column_stack([np.cos(angles),np.sin(angles)])
tangents=np.column_stack([-np.sin(angles),np.cos(angles)])
modes=[np.ones(4),np.array([1,0,-1,0]),np.array([0,1,0,-1]),np.array([1,-1,1,-1])]
labels=[r"$\omega=0$",r"$\omega=\sqrt{2k/m}$",r"$\omega=\sqrt{2k/m}$",r"$\omega=2\sqrt{k/m}$"]
fig,axes=plt.subplots(1,4,figsize=(10.0,3.1),layout="constrained")
circle=np.linspace(0,2*np.pi,400)
for ax,mode,label in zip(axes,modes,labels):
    ax.plot(np.cos(circle),np.sin(circle),color=".6",lw=1.3)
    for j,(point,tangent,amplitude) in enumerate(zip(positions,tangents,mode)):
        ax.plot(*point,"o",ms=7,mec="#245b9f",mfc="#245b9f" if amplitude else "white",zorder=3)
        ax.text(*(point*1.18),str(j),ha="center",va="center",fontsize=9)
        if amplitude:
            tip=point+.48*amplitude*tangent
            ax.annotate("",xy=tip,xytext=point,
                        arrowprops={"arrowstyle":"->","color":"#a3472a","lw":1.7})
    ax.set(aspect="equal",xlim=(-1.5,1.5),ylim=(-1.5,1.5),title=label)
    ax.axis("off")
fig.suptitle("Signed tangential displacements of the four ring modes",fontsize=12)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
