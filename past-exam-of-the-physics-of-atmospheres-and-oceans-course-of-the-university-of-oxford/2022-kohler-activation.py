"""Original solution illustration. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; this script writes only its PNG basename there.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white",
                     "axes.facecolor": "white", "savefig.facecolor": "white"})

x=np.linspace(.53,4.1,650)
y=1.5/x-.5/x**3
ambient=.6
roots=np.sort(np.roots([ambient,-1.5,0,.5])); left,right=roots[1:]
fig,ax=plt.subplots(figsize=(7.6,4.4),layout="constrained")
ax.plot(x,y,lw=2.5,color="#316e9d",label="Dilute equilibrium curve")
ax.axhline(ambient,color="#be4d26",ls="--",label="Ambient: 0.6 critical supersaturation")
ax.axhline(0,color="0.7",lw=1)
ax.vlines(1,-.5,1,color="0.6",ls=":")
ax.scatter([1],[1],color="#316e9d",zorder=3)
ax.scatter([left],[ambient],s=60,color="#247d55",zorder=4)
ax.scatter([right],[ambient],s=60,facecolors="white",edgecolors="#be4d26",linewidths=2,zorder=4)
ax.annotate(r"Critical: $(r_c,S_c)$",(1,1),xytext=(1.32,1.13),arrowprops={"arrowstyle":"->"})
ax.annotate("Stable wet radius",(left,ambient),xytext=(.65,-.2),arrowprops={"arrowstyle":"->"})
ax.annotate("Unstable threshold",(right,ambient),xytext=(2.65,.88),arrowprops={"arrowstyle":"->"})
for start,finish in [(.55,.64),(.9,.74),(1.8,1.25),(2.7,3.6)]:
 ax.annotate("",(finish,.17),xytext=(start,.17),arrowprops={"arrowstyle":"->","color":"#247d55","lw":2})
ax.text(2.72,.02,"Growth direction",fontsize=9,color="#247d55")
ax.text(.55,-.46,"Small-radius extrapolation leaves the dilute regime",fontsize=9)
ax.set(xlim=(.5,4.1),ylim=(-.55,1.3),xlabel=r"Droplet radius $r/r_c$",
 ylabel=r"Equilibrium supersaturation $(S_{eq}-1)/(S_c-1)$",title="Köhler activation and subcritical equilibria")
ax.legend(loc="upper right",bbox_to_anchor=(1,1),fontsize=9,frameon=False)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            dpi=120, facecolor="white", transparent=False,
            metadata={"Software": "Matplotlib"})
plt.close(fig)
