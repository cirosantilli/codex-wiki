"""Original schematic/calculation. Save only a PNG basename in the working directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

fig,ax=plt.subplots(figsize=(6.4,6.4),layout="constrained")
for c in np.arange(-.5,2,.5):
 x=np.linspace(0,1,500)
 for y in [x+c,-x+c]:
  mask=(y>=0)&(y<=1)
  ax.plot(x[mask],y[mask],"--",color="#a9a9a9",lw=.9,zorder=1)
groups=[
([(0,0),(1,0),(0,1),(1,1),(.5,.5)],"0","#0072b2"),
([(.5,0),(.5,1),(0,.5),(1,.5)],"1/2","#d55e00"),
([(.25,.25),(.75,.75)],"1/4","#009e73"),
([(.25,.75),(.75,.25)],"3/4","#cc79a7")]
for pts,label,color in groups:
 xy=np.array(pts)
 ax.scatter(*xy.T,s=260,color=color,edgecolors="white",zorder=3,label=rf"$z/a={label}$")
 for x,y in pts:ax.text(x,y,label,ha="center",va="center",color="white",fontsize=8,zorder=4)
ax.add_patch(Rectangle((0,0),1,1,fill=False,color="black",lw=1))
ax.plot(.125,.125,"*",ms=13,color="black",zorder=5)
ax.annotate(r"Inversion centre: $(1/8,1/8)$"+"\n"+r"height $z/a=1/8$",xy=(.125,.125),xytext=(.31,-.16),arrowprops={"arrowstyle":"->"},fontsize=9)
ax.set(xlim=(-.08,1.08),ylim=(-.23,1.08),xlabel=r"$x/a$",ylabel=r"$y/a$",title=r"Diamond: original $[001]$ projection",aspect="equal",xticks=[0,.25,.5,.75,1],yticks=[0,.25,.5,.75,1])
ax.legend(loc="upper center",bbox_to_anchor=(.5,-.12),ncol=2,fontsize=9)
finish(fig,"paper-1-diamond-projection")
