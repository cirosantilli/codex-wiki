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

fig,axes=plt.subplots(1,2,figsize=(8.7,3.7),constrained_layout=True)
L=2.;r=2.4595148248
for ax,bfield in zip(axes,[False,True]):
    for x in [0,L]:
        ax.add_patch(Rectangle((x-.055,.12),.11,1.5,color=".4"))
        ax.add_patch(Rectangle((x-.055,-1.65),.11,1.53,color=".4"))
    ax.text(0,-1.38,"Injector",ha="center",fontsize=9)
    ax.text(L,-1.38,"Collector",ha="center",fontsize=9)
    for angle in np.linspace(-.045,.045,7):
        t=np.linspace(0,2.5,500)
        if not bfield:x=t*np.cos(angle);y=t*np.sin(angle)
        else:
            x=r*(np.sin(angle+t/r)-np.sin(angle));y=r*(np.cos(angle)-np.cos(angle+t/r))
        keep=x<=L
        ax.plot(x[keep],y[keep],color="#2466a5",lw=1,alpha=.7)
    if not bfield:
        ax.add_patch(Circle((1.,.05),.15,facecolor="#f0ba76",edgecolor="#ba492c",alpha=.8))
        ax.annotate("Movable tip potential",xy=(1.,.2),xytext=(.95,.95),ha="center",arrowprops=dict(arrowstyle="->",color="#ba492c"),color="#ba492c",fontsize=9)
    ax.set(xlim=(-.28,2.3),ylim=(-1.6,1.5),xlabel="Position / μm",ylabel="Position / μm",aspect="equal",title="Zero-field direct beam"if not bfield else r"$B=30$ mT, $r_c=2.46$ μm")
fig.suptitle("Illustrative aligned openings at 2 μm separation; widths schematic",fontsize=11)

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
