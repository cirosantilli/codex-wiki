"""Original Oxford CP2 2013 figure; Python 3.14, NumPy and Matplotlib root dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

from matplotlib.patches import Polygon,Rectangle
fig,ax=plt.subplots(figsize=(8.4,4.4),layout="constrained")
ax.add_patch(Polygon([[3.6,.4],[3.6,2.6],[5.8,1.5]],closed=True,fill=False,lw=2))
ax.plot([.4,1.1],[2,2],color="black",lw=1.8);ax.add_patch(Rectangle((1.1,1.82),1.05,.36,fill=False,lw=1.8));ax.plot([2.15,3.6],[2,2],color="black",lw=1.8)
ax.text(1.62,2.34,r"$R_i$",ha="center");ax.text(3.8,1.97,"−",ha="center",va="center",fontsize=18);ax.text(3.8,1.02,"+",ha="center",va="center",fontsize=16)
ax.plot([3.6,3.05,3.05],[1,1,.5],color="black",lw=1.8)
for yy,hw in [(.5,.25),(.39,.17),(.28,.08)]:ax.plot([3.05-hw,3.05+hw],[yy,yy],color="black",lw=1.4)
ax.plot([5.8,6.8],[1.5,1.5],color="black",lw=1.8);ax.plot([3,3,4.35],[2,3.3,3.3],color="black",lw=1.8)
ax.plot([4.35,4.35],[2.95,3.65],color="black",lw=2);ax.plot([4.52,4.52],[2.95,3.65],color="black",lw=2)
ax.plot([4.52,6.2,6.2],[3.3,3.3,1.5],color="black",lw=1.8)
ax.plot([3,6.2],[2,1.5],"ko",ms=5);ax.text(4.44,3.85,r"$C_f$",ha="center")
ax.text(.3,1.45,r"$V_i$ or input"+"\n"+r"charge $Q_{\rm in}$",ha="left",va="top");ax.text(6.9,1.5,r"$V_o$",va="center")
ax.text(3,1.75,"Virtual ground",ha="right",va="top",fontsize=10)
ax.text(4.65,.03,r"$\Delta V_o=-Q_{\rm in}/C_f$",ha="center",fontsize=14)
ax.set(xlim=(0,7.5),ylim=(-.25,4.2),aspect="equal",title="Charge integrator: replace feedback resistance by capacitance")
ax.axis("off")

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white",metadata={"Software":"Original CP2 solution figure"})
plt.close(fig)
