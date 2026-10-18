"""Original solution figure. Python 3.14; NumPy 2.3; Matplotlib 3.10. Writes to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig,ax=plt.subplots(figsize=(6.2,3.6),layout="constrained")
gray=[0,1,3,2]
for i,a in enumerate([0,1]):
 for j,bc in enumerate(gray):
  b,c=bc//2,bc%2; v=int(a+b+c<=1)
  ax.add_patch(plt.Rectangle((j,i),1,1,facecolor="#eef5fa" if v else "white",edgecolor="#999"))
  ax.text(j+.5,i+.5,str(v),ha="center",va="center",fontsize=20)
# Pair a=0, bc=00/01: not a and not b.
ax.add_patch(FancyBboxPatch((.12,.13),1.76,.72,boxstyle="round,pad=0",fill=False,ec="#a32638",lw=2))
# Pair across periodic left/right boundary: not a and not c.
for j in [0,3]:
 ax.add_patch(FancyBboxPatch((j+.06,.06),.88,.88,boxstyle="round,pad=0",fill=False,ec="#b66c00",lw=2,linestyle="--"))
# Vertical pair: not b and not c.
ax.add_patch(FancyBboxPatch((.23,.20),.54,1.60,boxstyle="round,pad=0",fill=False,ec="#277646",lw=2))
ax.set(xticks=np.arange(4)+.5,xticklabels=[format(x,"02b") for x in gray],yticks=[.5,1.5],yticklabels=["0","1"],xlabel="$bc$ (Gray order)",ylabel="$a$",xlim=(-.05,4.05),ylim=(2.05,-.05),title="Minority: one-cells paired around 000")
ax.tick_params(length=0)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=110)
