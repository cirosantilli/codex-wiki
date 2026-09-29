"""Original meridional geometry of a sphere intersecting a plane; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

rho=np.sqrt(7)
t=np.linspace(0,2*np.pi,700)
fig,ax=plt.subplots(figsize=(6.4,5.0),layout="constrained")
ax.plot(4*np.cos(t),4*np.sin(t),color="#276fa4",lw=2,label="Sphere section (radius 4)")
ax.axhline(3,color="#a6572e",lw=1.5,label="Cutting plane")
ax.plot([-rho,rho],[3,3],color="#a6572e",lw=3)
ax.plot([0,rho],[0,3],color="#286d9b",lw=1.8)
ax.plot([0,0],[0,3],color="#555555",ls="--",lw=1.5)
ax.add_patch(Rectangle((0,2.72),0.28,0.28,fill=False,color="#555555",lw=1))
ax.scatter([0,0,rho,-rho],[0,3,3,3],color="#333333",s=24,zorder=4)
ax.annotate("C = (1, 2, 3)",(0,0),(-2.3,-0.65),fontsize=10,arrowprops={"arrowstyle":"->","lw":0.8})
ax.annotate("H = (2, 4, 5)",(0,3),(-2.5,3.48),fontsize=10,arrowprops={"arrowstyle":"->","lw":0.8})
ax.text(-0.6,1.45,"d = 3",rotation=90,fontsize=11)
ax.text(1.25,3.17,r"$\rho=\sqrt{7}$",fontsize=11)
ax.text(1.45,1.3,"r = 4",rotation=48,fontsize=11)
ax.set(xlim=(-4.6,4.6),ylim=(-4.4,4.4),xlabel="Direction within the cutting plane",ylabel="Distance along the plane normal",title="A perpendicular section gives the intersection-circle radius")
ax.set_aspect("equal");ax.grid(alpha=0.15)
ax.legend(loc="lower left",fontsize=8)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
