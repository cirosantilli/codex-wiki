"""Original indented half-disk and shifted rectangular contour diagrams."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,2,figsize=(9.0,4.0),layout="constrained")
left,right=axes
R,epsilon=2.7,0.38
outer=np.linspace(0,np.pi,400);inner=np.linspace(np.pi,0,150)
left.plot(R*np.cos(outer),R*np.sin(outer),color="#2c72a0",lw=2)
left.plot(epsilon*np.cos(inner),epsilon*np.sin(inner),color="#b5572c",lw=2)
left.plot([-R,-epsilon],[0,0],color="#2c72a0",lw=2);left.plot([epsilon,R],[0,0],color="#2c72a0",lw=2)
left.annotate("",(0.25,R-0.02),(0.65,R-0.08),arrowprops={"arrowstyle":"->","color":"#2c72a0"})
left.annotate("",(epsilon*np.cos(.8),epsilon*np.sin(.8)),(epsilon*np.cos(1.3),epsilon*np.sin(1.3)),arrowprops={"arrowstyle":"->","color":"#b5572c"})
left.annotate("",(-1.3,0),(-2.0,0),arrowprops={"arrowstyle":"->","color":"#2c72a0"})
left.annotate("",(2.0,0),(1.3,0),arrowprops={"arrowstyle":"->","color":"#2c72a0"})
left.scatter([0],[0],facecolor="white",edgecolor="#a84626",s=40,zorder=4)
left.text(0,-0.24,"Excluded pole",ha="center",fontsize=9)
left.text(0,0.65,"Clockwise indentation",ha="center",fontsize=9,color="#a84626")
left.set(xlim=(-3,3),ylim=(-0.5,3),xlabel="Re z",ylabel="Im z",title="No enclosed poles")
left.set_aspect("equal")
xs=[-2,2,2,-2,-2];ys=[0,0,1,1,0]
right.plot(xs,ys,color="#2c72a0",lw=2)
for start,end in [((-0.5,0),(0.5,0)),((2,0.25),(2,0.75)),((0.5,1),(-0.5,1)),((-2,0.75),(-2,0.25))]:
    right.annotate("",end,start,arrowprops={"arrowstyle":"->","color":"#2c72a0"})
right.scatter([0],[0.5],color="#ae4d28",s=42,zorder=4)
right.scatter([0,0],[-.5,1.5],color="#999999",s=24,zorder=4)
right.text(0.14,0.5,"i/2",fontsize=11,va="center")
right.text(0.14,-.5,"−i/2",fontsize=9,va="center",color="#666666")
right.text(0.14,1.5,"3i/2",fontsize=9,va="center",color="#666666")
right.set(xlim=(-2.5,2.5),ylim=(-.8,1.8),xlabel="Re z",ylabel="Im z",title="Height-one rectangle encloses one pole")
right.set_aspect("equal")
for ax in axes:ax.axvline(0,color="#555555",lw=.7,alpha=.5);ax.grid(alpha=.16)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
