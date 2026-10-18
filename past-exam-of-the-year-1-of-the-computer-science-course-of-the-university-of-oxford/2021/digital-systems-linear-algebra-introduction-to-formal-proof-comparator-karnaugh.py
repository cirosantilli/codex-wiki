"""Original solution figure. Python 3.14; NumPy 2.3; Matplotlib 3.10. Writes to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig,ax=plt.subplots(figsize=(6.5,5.2),layout="constrained")
gray=[0,1,3,2]
for i,a in enumerate(gray):
 for j,b in enumerate(gray):
  v=int(a>=b)
  ax.add_patch(plt.Rectangle((j,i),1,1,facecolor="#eef5fa" if v else "white",edgecolor="#999"))
  ax.text(j+.5,i+.5,str(v),ha="center",va="center",fontsize=19)
# Five essential size-four implicants; wraparound rectangles are split.
groups=[([(0,2,2,2)],"#a32638"), ([(0,2,4,1)],"#27638b"), ([(0,2,1,2),(3,2,1,2)],"#b66c00"), ([(0,1,2,2)],"#277646"), ([(0,0,1,4)],"#774b96")]
for k,(rects,color) in enumerate(groups):
 for x,y,w,h in rects:
  d=.045+k*.025
  ax.add_patch(FancyBboxPatch((x+d,y+d),w-2*d,h-2*d,boxstyle="round,pad=0",fill=False,ec=color,lw=2))
ax.set(xticks=np.arange(4)+.5,xticklabels=[format(x,"02b") for x in gray],yticks=np.arange(4)+.5,yticklabels=[format(x,"02b") for x in gray],xlabel="$b_1b_0$ (Gray order)",ylabel="$a_1a_0$ (Gray order)",xlim=(-.05,4.05),ylim=(4.05,-.05),title="Comparator: 1 exactly when a ≥ b")
ax.tick_params(length=0)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=110)
