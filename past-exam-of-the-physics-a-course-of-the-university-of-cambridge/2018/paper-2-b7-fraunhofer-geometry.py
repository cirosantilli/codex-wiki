"""Original solution figure; tested with Python 3.14.4.
Uses NumPy 2.3.5 and Matplotlib 3.10.7 from the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
fig, axes = plt.subplots(2, 1, figsize=(9.1, 5.2), layout="constrained")
for ax in axes:
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1.8, 2)
    ax.axis("off")
ax=axes[0]
ax.plot([0,0],[-1.1,-.55],color="k",lw=4)
ax.plot([0,0],[.55,1.1],color="k",lw=4)
ax.plot([8,8],[-1.2,1.5],color="0.4",lw=2)
ax.plot([-1,9],[0,0],color="0.6",ls="--")
for y in [-.5,0,.5]:
    ax.plot([0,8],[y,1.1],color="#1565a8",lw=1.2)
for y in [-.35,.35]: ax.annotate("", xy=(0,y),xytext=(-.9,y),arrowprops={"arrowstyle":"->","color":"#ca6720"})
ax.text(-.8,1.45,"Plane illumination")
ax.text(.15,-1.3,"Aperture (x, y)")
ax.text(8.15,1.12,"P = (X, Y, R)")
ax.annotate("",xy=(8,-.85),xytext=(0,-.85),arrowprops={"arrowstyle":"<->"})
ax.text(4,-1.25,"R",ha="center")
ax.text(1.4,1.55,r"Actual far field: $b^2/(\lambda R)\ll1$")
ax=axes[1]
ax.plot([-1,9.2],[0,0],color="0.6",ls="--")
for y in [-.5,0,.5]:
    ax.plot([-1,0,4,8],[y,y,1.0+y,1.0],color="#1565a8",lw=1.2)
    ax.annotate("",xy=(-.15,y),xytext=(-.85,y),arrowprops={"arrowstyle":"->","color":"#ca6720"})
ax.plot([0,0],[-1,-.55],color="k",lw=4)
ax.plot([0,0],[.55,1.2],color="k",lw=4)
ax.annotate("",xy=(4,1.6),xytext=(4,-1.2),arrowprops={"arrowstyle":"<->","color":"#33865b","lw":2})
ax.plot([8,8],[-1.2,1.6],color="0.4",lw=2)
ax.text(.2,-1.3,"Aperture")
ax.text(3.3,-1.65,"Converging lens")
ax.text(8.1,-1.3,"Focal plane")
ax.text(.5,1.6,"Collimated illumination; the lens maps angle to position")
ax.annotate("",xy=(8,-.85),xytext=(4,-.85),arrowprops={"arrowstyle":"<->"})
ax.text(6,-1.2,"f",ha="center")
ax.text(8.1,1.1,r"$X\simeq f\theta_x$")
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=135)
