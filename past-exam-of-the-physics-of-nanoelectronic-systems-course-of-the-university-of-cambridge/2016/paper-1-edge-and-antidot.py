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
ax=axes[0];pos=np.array([[-1,-.65],[1,-.65],[1,.65],[-1,.65]])
for i,(x,y)in enumerate(pos):
    j=(i+1)%4;xx,yy=pos[j];vec=np.array([xx-x,yy-y]);unit=vec/np.linalg.norm(vec)
    a=np.array([x,y])+.25*unit;b=np.array([xx,yy])-.25*unit
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="->",mutation_scale=14,color=".45",lw=1.6))
    col="#ba492c"if i<2 else"#2466a5"
    ax.add_patch(Circle((x,y),.21,color=col))
    ax.text(x,y,str(i+1),color="white",ha="center",va="center",weight="bold")
    ax.text(x,y+(.35 if y>0 else-.35),r"$V_S$"if i<2 else r"$0$",ha="center",color=col)
ax.text(0,.14,r"$I_i=(5e^2/h)(V_i-V_{i-1})$",ha="center",fontsize=10)
ax.text(0,-.16,"1 injects; 3 drains; 2 and 4 float",ha="center",fontsize=9)
ax.set(xlim=(-1.5,1.5),ylim=(-1.3,1.3),title="Chiral connectivity, not physical mesa shape");ax.axis("off")
ax=axes[1];x=np.linspace(-85,135,1800);period=103.391692423
for per,off,col,label in [(period,1.2,".55",r"Single-electron $h/e$ period"),(period/2,0,"#ba492c",r"Two-spin charging model")]:
    peaks=sum(1/(1+((x-j*per)/3.5)**2)for j in range(-5,6))
    ax.plot(x,off+.55*peaks,color=col,lw=1.8,label=label)
ax.annotate("",xy=(period/2,.83),xytext=(0,.83),arrowprops=dict(arrowstyle="<->",color="#ba492c"))
ax.text(period/4,.9,"51.7 mT",ha="center",color="#ba492c",fontsize=9)
ax.set(xlim=(-85,135),ylim=(-.08,2.16),xlabel=r"Field shift $\Delta B$ / mT",ylabel="Schematic resistance + offsets",title="Fixed effective area 0.04 μm²",yticks=[])
ax.legend(loc="upper left",fontsize=8)

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
