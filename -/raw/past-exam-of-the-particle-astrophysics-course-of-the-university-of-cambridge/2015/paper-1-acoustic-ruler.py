"""Original acoustic-ruler geometry; saves basename in current directory. Python 3.14."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
fig, axes = plt.subplots(1,2,figsize=(9,3.8),layout="constrained")
for ax in axes:
    ax.set_aspect("equal"); ax.set_xlim(-.5,5); ax.set_ylim(-1.8,1.8); ax.axis("off")
ax=axes[0]
ax.plot(0,0,"o",color="#3d4752")
for y in [-.8,.8]:
    ax.plot([0,4],[0,y],color=".6"); ax.plot(4,y,"o",color="#1d648a",ms=8)
ax.annotate("",(4,-.8),(4,.8),arrowprops=dict(arrowstyle="<->",lw=2,color="#be6426"))
ax.text(4.15,0,r"$r_d$",va="center",color="#be6426")
ax.add_patch(Arc((0,0),2,2,theta1=-11.31,theta2=11.31,color="#1d648a",lw=2))
ax.text(1.05,.12,r"$\Delta\theta$",color="#1d648a")
ax.text(1.8,-1.3,r"$D_M=r_d/\Delta\theta$",fontsize=13)
ax.text(0,.4,"Observer",ha="center",fontsize=9)
ax.set_title("Transverse: angular separation")
ax=axes[1]
ax.plot([0,4.5],[0,0],color=".6"); ax.plot(0,0,"o",color="#3d4752")
ax.scatter([2.7,4.3],[0,0],s=65,color="#1d648a")
ax.annotate("",(2.7,.5),(4.3,.5),arrowprops=dict(arrowstyle="<->",lw=2,color="#be6426"))
ax.text(3.5,.75,r"$r_d$",ha="center",color="#be6426")
ax.text(2.7,-.35,r"$z$",ha="center"); ax.text(4.3,-.35,r"$z+\Delta z$",ha="center")
ax.text(1.3,-1.3,r"$H(z)r_d=c\Delta z$",fontsize=13)
ax.set_title("Radial: redshift separation")
fig.suptitle("The same comoving ruler tests distance and expansion rate")
fig.savefig("paper-1-acoustic-ruler.png",dpi=155,facecolor="white")
