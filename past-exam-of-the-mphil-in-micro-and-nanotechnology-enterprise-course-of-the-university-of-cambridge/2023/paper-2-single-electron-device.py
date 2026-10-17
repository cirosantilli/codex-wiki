"""Original explanatory diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import os
import numpy as np
os.environ.setdefault("MPLCONFIGDIR", "/tmp/cambridge-nano2-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, RegularPolygon, FancyArrowPatch, Wedge
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "savefig.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(10,4),layout="constrained")
ax=axs[0];ax.plot([0,5],[2,2],"k",lw=1.3)
for x,label in [(1.15,r"$R_s\parallel C_s$"),(3.85,r"$R_d\parallel C_d$")]:
    ax.add_patch(Rectangle((x-.5,1.7),1,.6,fc="white",ec="black"))
    ax.text(x,2,label,ha="center",va="center",fontsize=10)
ax.add_patch(Circle((2.5,2),.27,fc="#c4dce9",ec="black"));ax.text(2.5,2.5,"Charge island",ha="center")
ax.text(-.1,2.4,r"Source: $V_s=V_{sd}$");ax.text(3.6,2.4,r"Drain: $V_d=0$")
ax.plot([2.5,2.5],[0.4,1.1],"k");ax.plot([2.5,2.5],[1.3,1.73],"k")
ax.plot([2.2,2.8],[1.1,1.1],"k");ax.plot([2.2,2.8],[1.3,1.3],"k")
ax.text(2.9,1.17,r"$C_g$");ax.text(2.5,.08,r"Gate: $V_g$ (no tunnel connection)",ha="center")
ax.set(xlim=(-.3,5.3),ylim=(-.2,3));ax.axis("off");ax.set_title("Two tunnel junctions and one capacitive gate")
ax=axs[1]
for E,label in [(.75,"(1,1)"),(1.5,"(2,1)"),(2.25,"(1,2)"),(2.75,"(3,1)")]:
    ax.hlines(E,0,1,color="#246c99");ax.text(1.05,E,label,va="center")
for E in [.75,1.5]:
    ax.annotate("",(.35,E+.25),(.35,E+.02),arrowprops=dict(arrowstyle="->",color="#b23a37"))
    ax.annotate("",(.65,E+.02),(.65,E+.25),arrowprops=dict(arrowstyle="->",color="#b23a37"))
ax.set(xlim=(-.15,1.55),ylim=(.4,3.2),xticks=[],ylabel="Single-electron energy (meV)",title="Rectangular-box orbital ladder")
ax.text(.02,.97,"Each orbital accommodates two spins.\nCharging energy is separate.",transform=ax.transAxes,fontsize=9,va="top")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145)
