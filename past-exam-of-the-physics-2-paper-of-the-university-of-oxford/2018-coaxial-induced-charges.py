"""Original solution illustration; output the matching PNG into the cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
plt.rcParams.update({"font.size":12,"figure.facecolor":"white"})

fig,ax=plt.subplots(figsize=(7.8,6.4),layout="constrained")
R,b,a=.43,1.25,2.1
for radius,color,width in [(a,"#424a50",10),(b,"#929ca2",9)]:ax.add_patch(patches.Circle((0,0),radius,fill=False,ec=color,lw=width))
ax.add_patch(patches.Circle((0,0),R,facecolor="#f2d2b0",edgecolor="#9c552d",lw=1.8));ax.text(0,0,r"$+Q$",ha="center",va="center",fontsize=15)
for angle in np.linspace(0,2*np.pi,8,endpoint=False):
    unit=np.array([np.cos(angle),np.sin(angle)])
    for lo,hi,col in [(R+.08,b-.16,"#a55d34"),(b+.17,a-.18,"#276b85")]:
        p=lo*unit;q=hi*unit;ax.annotate("",xy=q,xytext=p,arrowprops={"arrowstyle":"->","color":col,"lw":1.4})
for ang in np.deg2rad([22.5,112.5,202.5,292.5]):
    u=np.array([np.cos(ang),np.sin(ang)])
    for radius,sign,col in [(b-.12,"−","#a55d34"),(b+.12,"+","#276b85"),(a-.12,"−","#276b85")]:
        ax.text(*(radius*u),sign,color=col,ha="center",va="center",fontsize=15)
ax.annotate("Inner wall: −Q\nOuter wall: +Q\nNet inner-conductor charge: 0",xy=(1.25,0),xytext=(2.55,.7),fontsize=11,arrowprops={"arrowstyle":"->"})
ax.annotate("Outer conductor grounded\nInside wall: −Q",xy=(0,-a),xytext=(-2.5,-2.7),fontsize=11,arrowprops={"arrowstyle":"->"})
ax.text(0,2.5,r"$E_r=Q/(2\pi\epsilon_0lr)$ for $b<r<a$",ha="center")
ax.text(-2.5,2.8,"Transverse schematic; end effects omitted",fontsize=11)
ax.set(xlim=(-2.65,5.3),ylim=(-3.1,3.1));ax.set_aspect("equal");ax.axis("off")

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
