"""Original explanatory figure. Python 3.14; root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white"})

x=np.geomspace(.025,30,1500);zeta=.06;H=1/(1-x*x+2j*zeta*x)
fig,(ax,bx)=plt.subplots(2,1,figsize=(7,6),sharex=True,layout="constrained")
ax.loglog(x,abs(H),lw=2,label=r"Absolute mass: $|x|/a_s$",color="#1565c0");ax.loglog(x,abs(H-1),lw=2,label=r"Recorded relative: $|x-y_2|/a_s$",color="#d84315");ax.axhline(1,color="#999",ls=":");ax.set(ylabel="Amplitude ratio",title=r"Specified absolute-velocity damping, $\zeta=0.06$");ax.legend(fontsize=9)
bx.semilogx(x,-np.angle(H),color="#1565c0",lw=2);bx.set(xlabel=r"Driving frequency / $\sqrt{k/m}$",ylabel="Mass phase lag (rad)",yticks=[0,np.pi/2,np.pi],yticklabels=["0",r"$\pi/2$",r"$\pi$"])
for a in (ax,bx):a.axvline(1,color="#999",ls=":");a.grid(alpha=.2,which="both")

fig.savefig(Path(__file__).stem + ".png", dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
