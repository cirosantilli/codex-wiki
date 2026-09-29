"""Original illustrative figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the corresponding _media directory; the PNG is written to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig,(ax,charge)=plt.subplots(2,1,figsize=(9,5.8),sharex=True,gridspec_kw={"height_ratios":[3,1]},layout="constrained")
ax.axvspan(-2,-1,color="#e5e7eb"); ax.axvspan(-1,0,color="#fef3c7"); ax.axvspan(0,2.5,color="#dbeafe",alpha=.4)
x=np.linspace(0,4,600); ec=.8-.6*np.maximum(1-x/2.5,0)**2
ax.plot(x,ec,color="#2563eb",label=r"$E_c$");ax.plot(x,ec-1,color="#dc2626",label=r"$E_v$");ax.plot(x,ec-.5,"--",color="#777",label=r"$E_i$")
ax.hlines(0,0,4,color="black",linestyle=":");ax.text(3.95,.03,r"$\mu_s$",ha="right")
ax.hlines(-1.15,-2,-1,color="black",linestyle=":");ax.text(-1.95,-1.11,r"$\mu_g$ (biased gate)")
ax.plot([-1,0],[1.05,1.6],color="#2563eb");ax.plot([-1,0],[-2,-1.45],color="#dc2626")
ax.text(-1.5,1.85,"Metal",ha="center");ax.text(-.5,1.85,"Insulator",ha="center");ax.text(2,1.85,"p-type semiconductor",ha="center")
ax.annotate(r"Surface shift $e\psi_s=2e\phi_F$",xy=(0,.2),xytext=(.55,1.15),arrowprops={"arrowstyle":"->"})
ax.annotate("Inversion electrons",xy=(.06,.23),xytext=(.7,-1.65),arrowprops={"arrowstyle":"->"})
ax.set_ylim(-2.2,2.1);ax.set_ylabel("Electron energy (schematic)");ax.set_yticks([]);ax.legend(loc="upper right",ncol=3)
charge.axhline(0,color="black",lw=.8);charge.axvspan(-1,0,color="#fef3c7");charge.fill_between([0,2.5],0,-.45,color="#93c5fd")
charge.vlines(-1.03,0,1,color="#dc2626",lw=4);charge.vlines(.03,0,-.7,color="#2563eb",lw=3)
charge.text(-1.9,.5,"Positive gate charge",fontsize=9);charge.text(1.25,-.32,"Fixed negative acceptors",ha="center",fontsize=9)
charge.annotate("Depletion width",xy=(0,-.85),xytext=(2.5,-.85),arrowprops={"arrowstyle":"<->"},ha="right")
charge.set_ylim(-1.1,1.2);charge.set_yticks([]);charge.set_xlim(-2,4);charge.set_xlabel("Position across the stack (schematic)");charge.set_ylabel("Charge")
fig.suptitle("Conventional onset of strong inversion; energy and charge scales schematic")

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
