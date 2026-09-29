"""Original force directions in a local Northern Hemisphere model.
Python3.14/NumPy2.3/Matplotlib3.10. Write a PNG basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
fig,axes=plt.subplots(1,2,figsize=(9,4),layout="constrained")
for ax,r in zip(axes,[0.,.5]):
    f=1.;pressure=np.array([0.,-1.])
    u=np.linalg.solve(np.array([[r,-f],[f,r]]),pressure)
    cor=np.array([f*u[1],-f*u[0]])
    drag=-r*u
    for y in [-1.2,0,1.2]:ax.axhline(y,color="0.88",lw=1)
    ax.text(.91,1.20,"Higher pressure",ha="right",va="bottom",fontsize=9,color="0.4")
    ax.text(.91,-1.20,"Lower pressure",ha="right",va="top",fontsize=9,color="0.4")
    for vec,label,color,offset in [(pressure,"Pressure force", "#b22d24",(.08,-.04)),(cor,"Coriolis", "#258041",(-.02,.08))]:
        ax.annotate("",vec,(0,0),arrowprops={"arrowstyle":"->","lw":2.5,"color":color})
        ax.text(*(vec+offset),label,color=color,ha="right" if vec[0]<0 else "left",fontsize=10)
    if r:
        ax.annotate("",drag,(0,0),arrowprops={"arrowstyle":"->","lw":2.5,"color":"#be7a08"})
        ax.text(*(drag+np.array([.05,.03])),"Drag",color="#be7a08",fontsize=10)
    ax.annotate("",u,(0,0),arrowprops={"arrowstyle":"->","lw":2.5,"ls":"--","color":"#17477e"})
    ax.text(u[0]-.05,u[1]-.18,"Wind direction",ha="center",color="#17477e",fontsize=10)
    ax.plot(0,0,"o",color="0.15",ms=3)
    ax.set(xlim=(-1.65,1.4),ylim=(-1.6,1.7),xlabel="East",ylabel="North",xticks=[],yticks=[],title="Frictionless geostrophic balance" if not r else r"Illustrative linear drag: $r/f=0.5$")
    ax.set_aspect("equal")
fig.suptitle("Solid arrows: accelerations in common units; dashed arrow: wind direction")
fig.savefig("paper-1-ap2013-geostrophic-force-vectors.png",dpi=140,facecolor="white",bbox_inches="tight")
