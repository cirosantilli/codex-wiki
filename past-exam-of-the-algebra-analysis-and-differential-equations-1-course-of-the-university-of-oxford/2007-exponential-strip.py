"""Original strip-to-annulus covering. Python3.14, NumPy, Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
fig,(ax,bx)=plt.subplots(1,2,figsize=(9,4),facecolor="white")
ax.axvspan(.25,.5,color="#d8eef7");ax.axvline(.25,color="#2166ac",ls="--");ax.axvline(.5,color="#2166ac",ls="--")
ax.scatter([.375,.375],[0,2*np.pi],color="#b2182b",s=30)
ax.text(.39,0,r"$z$",fontsize=12);ax.text(.39,2*np.pi,r"$z+2\pi i$",fontsize=12)
ax.set(xlim=(.05,.8),ylim=(-1,7.5),xticks=[.25,.5],xticklabels=[r"$1/4$",r"$1/2$"],
       yticks=[0,2*np.pi],yticklabels=["0",r"$2\pi$"],xlabel=r"$\operatorname{Re}z$",ylabel=r"$\operatorname{Im}z$",title="Vertical strip")
theta=np.linspace(0,2*np.pi,600);ri=np.exp(.25);ro=np.exp(.5)
bx.fill(ro*np.cos(theta),ro*np.sin(theta),color="#d8eef7")
bx.fill(ri*np.cos(theta),ri*np.sin(theta),color="white")
for r in [ri,ro]:bx.plot(r*np.cos(theta),r*np.sin(theta),color="#2166ac",ls="--")
bx.scatter([np.exp(.375)],[0],color="#b2182b",s=35);bx.text(.08,.1,r"$e^z=e^{z+2\pi i}$",fontsize=12)
bx.set(xlim=(-1.85,1.85),ylim=(-1.85,1.85),aspect="equal",xlabel=r"$\operatorname{Re}w$",
       ylabel=r"$\operatorname{Im}w$",title=r"Annulus: $e^{1/4}<|w|<e^{1/2}$")
for a in [ax,bx]:a.spines[["top","right"]].set_visible(False)
fig.suptitle("The exponential preserves angles locally and repeats every full turn")
fig.tight_layout();fig.savefig("2007-exponential-strip.png",dpi=150,facecolor="white")
