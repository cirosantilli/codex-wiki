"""Original cycloid for equal-height endpoints; markers are uniform in time."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

theta=np.linspace(0,np.pi,1001)
x=(theta-.5*np.sin(2*theta))/np.pi
y=np.sin(theta)**2/np.pi
ticks=np.linspace(0,np.pi,9)
fig,ax=plt.subplots(figsize=(8.1,4.2),layout="constrained")
ax.plot(x,y,color="#245b9f",lw=2.5)
ax.plot((ticks-.5*np.sin(2*ticks))/np.pi,np.sin(ticks)**2/np.pi,"o",
        color="#245b9f",ms=5)
ax.axhline(0,color=".5",lw=.9)
ax.plot([.5,.67],[1/np.pi,1/np.pi],color=".5",ls=":",lw=.9)
ax.annotate("",xy=(.6,0),xytext=(.6,1/np.pi),
            arrowprops={"arrowstyle":"<->","lw":1.1,"color":"#a3472a"})
ax.text(.62,.16,r"$h/l=1/\pi$",color="#a3472a",va="center",fontsize=11)
ax.annotate("start",xy=(0,0),xytext=(.025,-.025),fontsize=10)
ax.annotate("target",xy=(1,0),xytext=(.88,-.025),fontsize=10)
ax.set(xlim=(-.03,1.03),ylim=(.39,-.05),aspect="equal",xlabel=r"$x/l$",
       ylabel=r"Downward depth $y/l$",title="One cycloid arch between equal-height endpoints")
ax.text(.02,.36,"Markers: equal intervals of travel time.",fontsize=9)
ax.grid(alpha=.13)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
