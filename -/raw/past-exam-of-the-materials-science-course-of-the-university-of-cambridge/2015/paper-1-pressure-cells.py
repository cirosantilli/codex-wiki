"""Original schematic/calculation. Save only a PNG basename in the working directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(11,4),layout="constrained")
for ax in axs:
 ax.axis("off");ax.set(xlim=(0,1),ylim=(0,1),aspect="equal")
ax=axs[0]
ax.add_patch(Rectangle((.32,.32),.36,.36,color="#dae4ed",ec="#555555"))
ax.add_patch(Rectangle((.43,.43),.14,.14,color="#d55e00"))
for pts in [[(.1,.15),(.3,.34),(.3,.66),(.1,.85)],[(.9,.15),(.7,.34),(.7,.66),(.9,.85)],[(.15,.1),(.34,.3),(.66,.3),(.85,.1)],[(.15,.9),(.34,.7),(.66,.7),(.85,.9)]]:
 ax.add_patch(Polygon(pts,color="#777777"))
for start,end in [((.02,.5),(.24,.5)),((.98,.5),(.76,.5)),((.5,.02),(.5,.24)),((.5,.98),(.5,.76))]:
 ax.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"->","lw":2})
ax.text(.5,.62,"Confining medium",ha="center",fontsize=9)
ax.text(.5,.5,"Sample",ha="center",va="center",fontsize=8,color="white")
ax.text(.5,-.04,"Four of six loading directions shown in section\nInternal heater / larger sample volume",ha="center",fontsize=9)
ax.set_title("Multi-anvil concept")
ax=axs[1]
for pts in [[(.02,.3),(.15,.12),(.43,.43),(.43,.57),(.15,.88),(.02,.7)],[(.98,.3),(.85,.12),(.57,.43),(.57,.57),(.85,.88),(.98,.7)]]:
 ax.add_patch(Polygon(pts,facecolor="#b9ddeb",edgecolor="#0072b2"))
ax.add_patch(Rectangle((.44,.25),.12,.5,color="#999999"))
ax.add_patch(Rectangle((.44,.46),.12,.08,color="#d55e00"))
ax.annotate("",xy=(.37,.5),xytext=(.04,.5),arrowprops={"arrowstyle":"->","lw":2})
ax.annotate("",xy=(.63,.5),xytext=(.96,.5),arrowprops={"arrowstyle":"->","lw":2})
ax.annotate("Small sample at opposed culets",xy=(.5,.5),xytext=(.5,.93),ha="center",arrowprops={"arrowstyle":"->"},fontsize=9)
ax.annotate("Gasket",xy=(.5,.3),xytext=(.73,.18),arrowprops={"arrowstyle":"->"},fontsize=9)
ax.text(.5,-.04,"Tiny loaded area; optical / X-ray access\nHeating and pressure require calibration",ha="center",fontsize=9)
ax.set_title("Diamond-anvil concept")
finish(fig,"paper-1-pressure-cells")
