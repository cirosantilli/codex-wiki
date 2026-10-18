"""Original solution illustration; output the matching PNG into the cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
plt.rcParams.update({"font.size":12,"figure.facecolor":"white"})

fig,ax=plt.subplots(figsize=(11,4.5),layout="constrained")
ax.axhline(0,color="#b4b4b4",ls="--",lw=.8)
ax.add_patch(patches.Circle((.25,0),.17,color="#e0ad50"));ax.text(.25,-.6,"Source",ha="center")
ax.plot([1.2,1.2],[-.55,-.07],color="#333333",lw=4);ax.plot([1.2,1.2],[.07,.55],color="#333333",lw=4)
ax.text(1.2,.85,"Narrow slit",ha="center")
ax.add_patch(patches.Ellipse((3,0),.15,1.3,facecolor="#c8e0eb",edgecolor="#286d88"))
ax.text(3,-.9,"Collimating lens",ha="center")
for y in [-.4,0,.4]:ax.plot([1.2,3,5],[0,y,y],color="#286d88",lw=1.2)
ax.plot([5,5],[-.8,.8],color="#545454",lw=4)
for y in np.linspace(-.75,.75,14):ax.plot([4.94,5.06],[y,y+.06],color="white",lw=.7)
ax.text(5,-1.2,"Grating\n(normal incidence)",ha="center")
th=np.deg2rad(25);direction=np.array([np.cos(th),np.sin(th)]);perp=np.array([-direction[1],direction[0]])
pc=np.array([7.8,1.3]);focus=pc+1.2*direction
for y in [-.4,0,.4]:
    start=np.array([5.,y]);hit=start+np.dot(pc-start,direction)*direction
    ax.plot([start[0],hit[0],focus[0]],[start[1],hit[1],focus[1]],color="#b96331",lw=1.3)
a=pc-.7*perp;b=pc+.7*perp;ax.plot([a[0],b[0]],[a[1],b[1]],color="#286d88",lw=4)
ax.scatter([focus[0]],[focus[1]],s=22,color="#a3304c")
ax.text(7.5,2.55,"Rotatable telescope",ha="center")
ax.annotate("Image at crosshair / detector",xy=focus,xytext=(8.2,3.1),fontsize=10,ha="center",arrowprops={"arrowstyle":"->","color":"#555555"})
ax.add_patch(patches.Arc((5,0),1.5,1.5,theta1=0,theta2=25,color="#555555"));ax.text(5.83,.15,r"$\theta$")
ax.set(xlim=(-.1,10.2),ylim=(-1.5,3.4));ax.set_aspect("equal");ax.axis("off")

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
