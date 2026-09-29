from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#1765a3"; RED="#b33d35"; DARK="#303030"; GREEN="#398050"
def save(fig):
    fig.savefig(Path.cwd() / (Path(__file__).stem+".png"),dpi=150,facecolor="white",bbox_inches="tight")
    plt.close(fig)
def mark(ax,x,y,kind="sink"):
    if kind=="saddle":ax.plot(x,y,"x",color=DARK,ms=7,mew=1.5)
    else:ax.plot(x,y,"o",color=BLUE if kind=="sink" else RED,mfc=BLUE if kind=="sink" else "white",ms=6,mew=1.5)
def cycle(ax,cx,cy,w,h,stable=True,clockwise=True):
    color=BLUE if stable else RED
    ax.add_patch(Ellipse((cx,cy),w,h,fill=False,color=color,lw=1.5,ls="-" if stable else "--"))
    theta=np.pi/3
    px=cx+w/2*np.cos(theta);py=cy+h/2*np.sin(theta)
    sign=1 if clockwise else -1
    ax.annotate("",xy=(px+sign*.08*w,py-sign*.06*h),xytext=(px,py),arrowprops={"arrowstyle":"->","color":color,"lw":1.1})
def tidy(ax,xlabel,ylabel):
    ax.set_xlabel(xlabel);ax.set_ylabel(ylabel);ax.grid(alpha=.13)

fig,axs=plt.subplots(1,2,figsize=(10,4.3))
ax=axs[0];lam=.8;m=np.linspace(-.25,.45,600);splus=(1+np.sqrt(1+4*m))/2;sminus=(1-np.sqrt(1+4*m))/2
mh=lam*(lam-1)
for u,stable in [(splus,m<mh),(sminus,m>0)]:
 ax.plot(m,np.where(stable,u,np.nan),color=BLUE,lw=2)
 ax.plot(m,np.where(~stable,u,np.nan),color=RED,lw=1.5,ls="--")
x=np.linspace(-.34,.45,500)
ax.plot(x,np.where(x<0,0,np.nan),color=BLUE,lw=2)
ax.plot(x,np.where(x>0,0,np.nan),color=RED,lw=1.5,ls="--")
ax.axvline(-.25,color="#888888",lw=.8,ls=":");ax.axvline(0,color="#888888",lw=.8,ls=":")
ax.plot(mh,lam,"o",color=GREEN);ax.annotate("Hopf",xy=(mh,lam),xytext=(-.04,.64),arrowprops={"arrowstyle":"->","color":GREEN},color=GREEN)
tidy(ax,r"$\mu$",r"$u$");ax.set_title(r"Equilibria at $\lambda=0.8$");ax.set_xlim(-.34,.45)
ax=axs[1]
ax.axvline(-.25,color=DARK,lw=1.5,label="Saddle-node");ax.axvline(0,color="#777777",ls=":",lw=1.5,label="Transcritical")
ls=np.linspace(.5,1.35,300);ax.plot(ls*(ls-1),ls,color=RED,lw=1.7,label="Hopf")
ls=np.linspace(.5,.72,200);ax.plot(-.25+1.96*(ls-.5)**2,ls,color=GREEN,ls="--",lw=1.7,label="Saddle loop (schematic)")
ax.plot(-.25,.5,"ko",ms=5);ax.annotate("double zero",xy=(-.25,.5),xytext=(-.18,.31),arrowprops={"arrowstyle":"->"})
tidy(ax,r"$\mu$",r"$\lambda$");ax.set_title("Parameter diagram and local saddle-loop placement")
ax.set_xlim(-.33,.5);ax.set_ylim(.2,1.38);ax.legend(fontsize=8,loc="upper right")
fig.tight_layout();save(fig)
