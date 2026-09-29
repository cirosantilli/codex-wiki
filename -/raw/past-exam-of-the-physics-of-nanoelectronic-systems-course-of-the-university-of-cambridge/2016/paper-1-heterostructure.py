"""Original explanatory model/schematic; no source figure or data copied.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes its same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle,FancyArrowPatch
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})

fig,axes=plt.subplots(1,2,figsize=(8.7,3.8),constrained_layout=True)
ax=axes[0]
layers=[(0,.25,"Surface gate / cap","#b8b8b8"),(.25,.38,"Doped AlGaAs: donors","#c9dced"),(.63,.3,"Undoped AlGaAs spacer","#e5eef5"),(.93,.1,"Confined electron layer","#e9ae4e"),(1.03,.7,"Undoped GaAs","#e4eadf")]
for y,h,label,col in layers:
    ax.add_patch(Rectangle((0,y),2.8,h,facecolor=col,edgecolor="white"))
    ax.text(1.4,y+h/2,label,ha="center",va="center",fontsize=9)
ax.annotate("",xy=(3.1,1.65),xytext=(3.1,.1),arrowprops=dict(arrowstyle="->",color=".35"))
ax.text(3.3,.9,"Depth",rotation=90,va="center",color=".35")
ax.set(xlim=(-.1,3.65),ylim=(1.8,-.1),title="Layer function (not to scale)");ax.axis("off")
ax=axes[1]
z1=np.linspace(-1,0,300);z2=np.linspace(0,1.4,500)
ec1=.9+.3*(-z1);ec2=.95*(1-np.exp(-z2/1.0))
ax.plot(z1,ec1,lw=2,color="#2466a5");ax.plot([0,0],[ec1[-1],ec2[0]],lw=2,color="#2466a5");ax.plot(z2,ec2,lw=2,color="#2466a5",label="Conduction edge")
ax.axhline(.32,color=".3",ls="--",label="Chemical potential")
ax.plot([.03,.39],[.14,.14],color="#ba492c",lw=2,label="Occupied subband")
ax.plot([.03,.66],[.43,.43],color=".65",lw=1,ls=":")
psi=.15*np.exp(-((z2-.16)/.1)**2)
ax.fill_between(z2,0,psi,color="#e9ae4e",alpha=.65)
ax.text(-.55,.55,"AlGaAs",ha="center");ax.text(.95,.55,"GaAs",ha="center")
ax.set(xlim=(-1,1.4),ylim=(-.04,1.28),xlabel="Coordinate normal to interface (schematic)",ylabel="Energy (arbitrary units)",title="Offset and band bending confine electrons",xticks=[0],xticklabels=["Interface"],yticks=[])
ax.legend(fontsize=8,loc="upper right")

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
