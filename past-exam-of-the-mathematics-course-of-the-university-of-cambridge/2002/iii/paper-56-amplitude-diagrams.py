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

fig,axs=plt.subplots(1,2,figsize=(9.8,4.1))
ax=axs[0];m=np.linspace(-1.3,0,300)
for sign in [-1,1]:ax.plot(m,sign*np.sqrt(-m),color=RED,ls="--",lw=1.6)
ax.plot([-1.3,0],[0,0],color=BLUE,lw=2);ax.plot([0,1.2],[0,0],color=RED,ls="--",lw=1.6)
tidy(ax,r"$C_1\mu/C_2$",r"$a$");ax.set_title("Cubic subcritical pitchfork: no saturation");ax.set_xlim(-1.3,1.2)
ax=axs[1];C=1.;a=np.linspace(-1.55,1.55,1200);eta=a-C*a*a+a**4;gp=1-2*C*a+4*a**3
st=a*gp>0
ax.plot(np.where(st,eta,np.nan),a,color=BLUE,lw=2)
ax.plot(np.where(~st,eta,np.nan),a,color=RED,ls="--",lw=1.6)
ax.plot([-1.3,0],[0,0],color=BLUE,lw=2);ax.plot([0,2],[0,0],color=RED,ls="--",lw=1.6)
tidy(ax,r"$\eta=C_1\mu$",r"$a$");ax.set_title(r"Asymmetric quintic example ($C_2=1$)")
ax.set_xlim(-1.3,2);ax.set_ylim(-1.5,1.4)
fig.suptitle("Solid = stable; dashed = unstable",fontsize=11)
fig.tight_layout();save(fig)
