"""Original explanatory figure. Python 3.14; root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white"})

from matplotlib.patches import Rectangle
fig,(ax,bx)=plt.subplots(1,2,figsize=(9,3.6),gridspec_kw={"width_ratios":[1,1.4]},layout="constrained")
ax.set(xlim=(-.3,4.5),ylim=(-.5,3.0));ax.axis("off")
ax.plot([0,1.1],[2,2],color="#263238",lw=2);ax.add_patch(Rectangle((1.1,1.78),1,.44,fill=False,lw=2));ax.plot([2.1,3.6],[2,2],color="#263238",lw=2)
ax.plot([2.8,2.8],[2,1.2],color="#263238",lw=2)
for y in [1.2,.98]:ax.plot([2.4,3.2],[y,y],color="#263238",lw=2)
ax.plot([2.8,2.8],[.98,0],color="#263238",lw=2);ax.plot([0,3.6],[0,0],color="#263238",lw=2)
ax.scatter([0,0,3.6,3.6],[0,2,0,2],color="#1565c0",zorder=4)
ax.text(1.6,2.4,r"$R=330\,\Omega$",ha="center");ax.text(3.05,.6,r"$C=22\,\mu F$")
ax.text(0,2.7,r"$V_{\rm in}$",ha="center");ax.text(3.7,2.35,r"$V_{\rm out}$",ha="center");ax.text(1.8,-.38,"Common return",ha="center")
ax.set_title("Series resistor, shunt capacitor")
f=np.geomspace(.1,1e5,700);gain=1/np.sqrt(1+(2*np.pi*f*330*22e-6)**2)
bx.loglog(f,gain,color="#1565c0",lw=2)
for f0 in [1,20000]:
 g=1/np.sqrt(1+(2*np.pi*f0*330*22e-6)**2);bx.scatter([f0],[g],color="#d84315");bx.annotate(f"{f0:g} Hz: {g:.4g}",(f0,g),xytext=(7,8),textcoords="offset points",fontsize=9)
bx.axhline(1/500,color="#999",ls=":",label="1/500 amplitude")
bx.set(xlabel="Frequency (Hz)",ylabel="Amplitude gain",title="Unloaded voltage response",ylim=(3e-4,1.5));bx.grid(alpha=.2,which="both");bx.legend(loc="lower left",fontsize=8)

fig.savefig(Path(__file__).stem + ".png", dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
