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

f=.15;L=1.;d=(6*f/np.pi)**(1/3);r=d/2
fig,axs=plt.subplots(1,3,figsize=(11,3.6),layout="constrained")
for ax in axs:
 ax.set_aspect("equal");ax.axis("off")
axs[0].add_patch(Rectangle((0,0),1,1,fill=False,ec="#777777"))
axs[0].add_patch(Circle((.5,.5),r,color="#cfe2f3",ec="#0072b2"))
axs[0].annotate("",xy=(0,-.09),xytext=(1,-.09),arrowprops={"arrowstyle":"<->"})
axs[0].text(.5,-.2,r"Representative pitch $L$",ha="center")
axs[0].text(.5,.5,rf"$d/L={d:.2f}$",ha="center")
axs[0].set(xlim=(-.1,1.1),ylim=(-.3,1.2),title="One sphere per volume L³")
ax=axs[1]
for x in [0,1]:ax.add_patch(Circle((x,.5),r,color="#cfe2f3",ec="#0072b2"))
gap=1-d;xc=.5
theta=np.linspace(0,np.pi,200)
ax.plot(xc+(gap/2)*np.cos(theta),.5+(gap/2)*np.sin(theta),color="#d55e00",lw=2)
ax.annotate("",xy=(r,.4),xytext=(1-r,.4),arrowprops={"arrowstyle":"<->"})
ax.text(.5,.2,r"Free gap $\ell=L-d$",ha="center")
ax.set(xlim=(-.4,1.4),ylim=(-.25,1.25),title="Simplified Orowan span")
ax=axs[2]
ax.add_patch(Circle((.5,.5),r,facecolor="#cfe2f3",ec="#0072b2"))
ax.plot([.5,.5],[.5-r,.5+r],"--",color="#d55e00",lw=2)
ax.annotate("",xy=(.62,.5),xytext=(.62,.32),arrowprops={"arrowstyle":"->","color":"#0072b2"})
ax.annotate("",xy=(.38,.32),xytext=(.38,.5),arrowprops={"arrowstyle":"->","color":"#0072b2"})
ax.text(.5,-.02,r"Trial wall area $\pi r^2$",ha="center")
ax.text(.5,-.15,r"Cost $\gamma_w A_w$ vs release $\Delta U$",ha="center")
ax.set(xlim=(0,1),ylim=(-.3,1.1),title="Conditional domain-wall comparison")
finish(fig,"paper-1-precipitate-estimates")
