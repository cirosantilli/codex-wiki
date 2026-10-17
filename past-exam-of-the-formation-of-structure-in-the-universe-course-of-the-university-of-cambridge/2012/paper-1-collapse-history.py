"""Original cycloid and separate virialization prescription. Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
fig,ax=plt.subplots(figsize=(8,4.3),layout="constrained")
eta=np.linspace(0,2*np.pi,1000)
time=(eta-np.sin(eta))/np.pi
radius=(1-np.cos(eta))/2
ax.plot(time,radius,"--",lw=2,color="#1767a2",
        label="formal pressureless cycloid")
ax.axvline(1,color=".6",ls=":",lw=.8)
ax.plot(1,1,"o",color="#1767a2")
ax.annotate("turnaround\n"+r"$t_m,\ R_m$",(1,1),(.43,1.1),
            arrowprops={"arrowstyle":"->"},fontsize=10)
ax.plot(2,0,"o",mfc="white",mec="#1767a2",ms=6)
ax.annotate("formal point collapse",(2,0),(1.1,.13),
            arrowprops={"arrowstyle":"->"},fontsize=9)
ax.plot([2,2.62],[.5,.5],color="#32794a",lw=2.5,
        label="assigned virialized halo")
ax.plot(2,.5,"o",color="#32794a",ms=6)
ax.plot([2,2],[0,.5],":",color=".6",lw=1)
ax.annotate(r"$t_f=2t_m$"+"\n"+r"$R_v=R_m/2$",(2,.5),(2.14,.77),
            arrowprops={"arrowstyle":"->","color":"#32794a"},color="#32794a")
ax.axhline(.5,xmax=2/2.68,color=".75",lw=.8,ls=":")
ax.text(.08,.03,"Relaxation is not supplied by the cold cycloid.",
        transform=ax.transAxes,fontsize=9,color=".35")
ax.set(xlim=(0,2.68),ylim=(-.06,1.23),
       xlabel=r"$t/t_m$",ylabel=r"$R/R_m$",
       title="Spherical collapse and the virialization prescription")
ax.legend(loc="upper right",frameon=False,fontsize=9)
ax.grid(alpha=.13)
fig.savefig("paper-1-collapse-history.png",dpi=155,facecolor="white")
