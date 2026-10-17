"""Original first-quadrant region bounded by a circle and rectangular hyperbola."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

lo=np.sin(np.pi/12);hi=np.cos(np.pi/12)
x=np.linspace(lo,hi,800);angle=np.linspace(0,np.pi/2,700)
fig,ax=plt.subplots(figsize=(6,5.4),layout="constrained")
ax.fill_between(x,1/(4*x),np.sqrt(1-x*x),color="#bdd9e8",alpha=.85,label="Integration region")
ax.plot(np.cos(angle),np.sin(angle),color="#287da5",lw=2,label=r"$x^2+y^2=1$")
hx=np.linspace(.2,1.1,600);ax.plot(hx,1/(4*hx),color="#ad6730",lw=2,label=r"$xy=1/4$")
for theta in [np.pi/12,5*np.pi/12]:
    endpoint=np.array([np.cos(theta),np.sin(theta)])
    ax.plot([0,endpoint[0]],[0,endpoint[1]],color="#777777",ls="--",lw=.9)
    ax.scatter([endpoint[0]],[endpoint[1]],color="#555555",s=27,zorder=5)
ax.text(.78,.12,r"$\theta=\pi/12$",fontsize=11)
ax.text(.10,.87,r"$\theta=5\pi/12$",rotation=75,fontsize=11)
ax.text(.57,.64,"R",fontsize=15,ha="center")
ax.set(xlim=(0,1.14),ylim=(0,1.14),xlabel="x",ylabel="y",title="Inside the circle and above the hyperbola")
ax.set_aspect("equal");ax.grid(alpha=.12);ax.legend(loc="upper right",fontsize=9)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
