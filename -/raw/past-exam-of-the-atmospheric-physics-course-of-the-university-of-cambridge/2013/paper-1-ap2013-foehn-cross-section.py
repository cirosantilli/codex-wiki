"""Original annotated schematic of the classical rainout foehn pathway.
Python3.14/NumPy2.3/Matplotlib3.10. Output PNG basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Ellipse
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
fig,ax=plt.subplots(figsize=(9,4.2),layout="constrained")
ax.add_patch(Polygon([(-3.6,0),(0,1.8),(3.6,0)],facecolor="#d1c2a7",edgecolor="#72634d",lw=1.4))
ax.plot([-3.3,-.1],[.45,2.27],color="#1b6791",lw=2)
ax.annotate("",(-1.6,1.42),(-2.2,1.08),arrowprops={"arrowstyle":"->","lw":2,"color":"#1b6791"})
ax.annotate("",(3.3,.45),(-.1,2.27),arrowprops={"arrowstyle":"->","lw":2.3,"color":"#b04c2e"})
ax.hlines(.95,-3.5,-2.40,color="0.5",ls="--",lw=1)
ax.text(-3.5,1.04,"Condensation level",fontsize=10)
ax.text(-3.45,.22,"Moist source air",color="#1b6791")
ax.text(-3.35,.56,r"Dry cooling: $\Gamma_d$",color="#1b6791",rotation=29)
ax.text(-3.4,1.75,"Saturated cooling\n"+r"$\Gamma_m<\Gamma_d$",color="#1b6791",fontsize=10)
for x,z,w in [(-1.12,2.05,.75),(-.72,2.18,.78),(-.35,2.13,.7)]:ax.add_patch(Ellipse((x,z),w,.32,facecolor="#dce6ed",edgecolor="0.55",zorder=3))
for x in [-1.35,-1.10,-.85]:ax.plot([x,x-.08],[1.85,1.61],color="#246c9c",lw=1.3)
ax.text(-1.15,2.55,"Condensation and condensate loss",ha="center",fontsize=10)
ax.text(1.9,1.93,"Unsaturated descent\nCompressional warming\n"+r"$\Gamma_d$",color="#b04c2e",ha="center",fontsize=10)
ax.text(2.1,.20,"Warmer, drier lee air",color="#b04c2e",ha="center")
ax.text(-2.65,-.17,"Windward",ha="center");ax.text(2.65,-.17,"Leeward",ha="center")
ax.set(xlim=(-3.7,3.7),ylim=(-.32,2.9));ax.axis("off")
fig.suptitle("Classical parcel path; dry drawdown and mixing are additional possible foehn mechanisms")
fig.savefig("paper-1-ap2013-foehn-cross-section.png",dpi=140,facecolor="white",bbox_inches="tight")
