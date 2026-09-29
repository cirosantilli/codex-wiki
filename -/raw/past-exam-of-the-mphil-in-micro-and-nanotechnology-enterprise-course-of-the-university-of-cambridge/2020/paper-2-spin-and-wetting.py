"""Original model sketches; Python 3.14, NumPy and Matplotlib. Output to cwd."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
plt.rcParams.update({"font.size":11})
fig,axs=plt.subplots(2,2,figsize=(11,8),layout="constrained")
ax=axs[0,0];h=np.linspace(-2.2,2.2,1000)
ax.plot(h,1+0.18*((h>.55)&(h<1.3)),label="increasing field")
ax.plot(h,1+0.18*((h<-.55)&(h>-1.3)),ls="--",label="decreasing field")
ax.set(xlabel="field (chosen units)",ylabel=r"$R/R_P$",title="A  Ideal positive spin-valve signal",ylim=(.97,1.24))
ax.text(.73,1.20,"antiparallel");ax.text(-.4,1.03,"parallel");ax.legend(loc="upper left",fontsize=9)
ax=axs[0,1];x=np.linspace(0,4,200)
ax.plot(x,np.exp(-x),label=r"$\mu_\uparrow-\mu_\downarrow$")
ax.axvline(1.8,color="gray",ls=":");ax.text(1.85,.63,"open-circuit\ndetector")
ax.set(xlabel=r"$x/\lambda_s$",ylabel="normalized spin imbalance",title="B  Diffusion beyond the charge path")
ax.annotate("injection",xy=(0,1),xytext=(.7,.9),arrowprops={"arrowstyle":"->"})
ax=axs[1,0];ax.set_aspect("equal");ax.set(xlim=(-1.8,1.6),ylim=(-.5,1.8),title="C  Right contact line: horizontal forces")
ax.plot([-1.7,1.5],[0,0],"k",lw=2)
for end,label,xy in [((1.25,0),r"$\gamma_{SV}$",(.65,-.24)),((-1.25,0),r"$\gamma_{SL}$",(-1.25,-.24)),((-.65,1.13),r"$\gamma_{LV}$",(-.95,1.16))]:
 ax.annotate("",xy=end,xytext=(0,0),arrowprops={"arrowstyle":"->","lw":2});ax.text(*xy,label)
ax.add_patch(Arc((0,0),.8,.8,theta1=120,theta2=180));ax.text(-.49,.18,r"$\theta$")
ax.text(-1.45,.65,"liquid");ax.text(.6,.55,"vapor");ax.text(-.2,-.45,"solid");ax.axis("off")
ax=axs[1,1];th=np.linspace(0,180,500)
for f in [1,.75,.5,.25]:
 star=np.degrees(np.arccos(np.clip(f*(1+np.cos(np.radians(th)))-1,-1,1)))
 ax.plot(th,star,label=f"f = {f:g}")
ax.axhline(90,color="gray",ls=":");ax.axvline(np.degrees(np.arccos(1/3)),color="gray",ls=":")
ax.set(xlabel=r"smooth angle $\theta$ (degrees)",ylabel=r"apparent angle $\theta^*$ (degrees)",title="D  Suspended Cassie-state prediction",xlim=(0,180),ylim=(0,180))
ax.legend(fontsize=9)
fig.savefig("paper-2-spin-and-wetting.png",dpi=155,facecolor="white")

