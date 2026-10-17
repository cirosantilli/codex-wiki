"""Original counterclockwise contours and enclosed poles for two residue calculations."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig,(semi,square)=plt.subplots(1,2,figsize=(9.2,4.7),layout="constrained")
angle=np.linspace(0,np.pi,400)
semi.plot(3*np.cos(angle),3*np.sin(angle),color="#245b9f",lw=2)
semi.plot([-3,3],[0,0],color="#245b9f",lw=2)
semi.annotate("",xy=(1,0),xytext=(0,0),arrowprops={"arrowstyle":"->","lw":1.5,"color":"#245b9f"})
semi.annotate("",xy=(3*np.cos(1.15),3*np.sin(1.15)),
              xytext=(3*np.cos(.9),3*np.sin(.9)),
              arrowprops={"arrowstyle":"->","lw":1.5,"color":"#245b9f"})
semi.plot([0,0],[1,2],"o",color="#a3472a",ms=6)
semi.text(.15,1,r"$i$ (double)",fontsize=10,va="center")
semi.text(.15,2,r"$2i$ (simple)",fontsize=10,va="center")
semi.set(aspect="equal",xlim=(-3.4,3.4),ylim=(-.45,3.5),xlabel=r"Re $z$",ylabel=r"Im $z$",
         title="Rational integral: upper semicircle")
R=2.5
square.plot([-R,R,R,-R,-R],[-R,-R,R,R,-R],color="#245b9f",lw=2)
for start,end in [((-.5,-R),(.5,-R)),((R,-.5),(R,.5)),((.5,R),(-.5,R)),((-R,.5),(-R,-.5))]:
    square.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"->","lw":1.5,"color":"#245b9f"})
square.plot([-2,-1,1,2],[0,0,0,0],"o",color="#245b9f",ms=5)
square.plot(0,0,"o",color="#a3472a",ms=7)
square.annotate("third-order pole",xy=(0,0),xytext=(-1.9,1.2),
                arrowprops={"arrowstyle":"->","lw":.8},fontsize=10)
square.text(0,-1.1,r"half-side $N+1/2$, here $N=2$",ha="center",fontsize=9)
square.set(aspect="equal",xlim=(-3.1,3.1),ylim=(-3.1,3.1),xlabel=r"Re $z$",ylabel=r"Im $z$",
           title="Cotangent summation: square contour")
for ax in [semi,square]:
    ax.axvline(0,color=".65",lw=.6,zorder=0)
    ax.axhline(0,color=".65",lw=.6,zorder=0)
    ax.grid(alpha=.12)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
