"""Original transverse string normal modes with masses 3m,4m,3m."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

positions=np.arange(5)
# Array order is the physical order: fixed, x, z, y, fixed.
modes=[([0,2,3,2,0],r"$\omega=\Omega/\sqrt{6}$","x:y:z = 2:2:3"),([0,1,0,-1,0],r"$\omega=\Omega\sqrt{2/3}$","x:y:z = 1:−1:0"),([0,1,-1,1,0],r"$\omega=\Omega$","x:y:z = 1:1:−1")]
fig,axes=plt.subplots(3,1,figsize=(7.8,6.2),layout="constrained",sharex=True)
for ax,(disp,title,ratio) in zip(axes,modes):
    y=np.asarray(disp,dtype=float);y/=max(abs(y))
    ax.axhline(0,color="#777777",lw=.8,ls="--")
    ax.plot(positions,y,color="#2d75a3",lw=1.8)
    ax.scatter([0,4],[0,0],color="black",s=30,marker="s",zorder=4)
    ax.scatter(positions[1:4],y[1:4],s=[85,125,85],color="#b6572e",edgecolor="white",zorder=4)
    for pos,value,label in zip([1,2,3],y[1:4],["x (3m)","z (4m)","y (3m)"]):
        ax.annotate(label,(pos,value),xytext=(0,7 if value>=0 else -17),textcoords="offset points",ha="center",fontsize=9)
    ax.set(ylim=(-1.55,1.55),xlim=(-.2,4.2),yticks=[-1,0,1],ylabel="Displacement")
    ax.set_title(title+"; "+ratio,fontsize=11)
    ax.grid(axis="x",alpha=.15)
axes[-1].set_xlabel("Position along the string / a");axes[-1].set_xticks(range(5))
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
