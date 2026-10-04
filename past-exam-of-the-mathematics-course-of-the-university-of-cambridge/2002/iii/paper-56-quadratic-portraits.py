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

fig,axs=plt.subplots(2,3,figsize=(10,6.2))
for i,ax in enumerate(axs.flat):
 if i==5:
  ax.axis("off")
  ax.text(.05,.7,"Filled blue: attractor\nOpen red: repelling equilibrium\nBlack x: saddle\nSolid blue loop: attracting cycle\nBlack curve: saddle basin boundary",va="top",fontsize=11)
  continue
 ax.set_xlim(0,1.75);ax.set_ylim(-.1,1.6);ax.set_xticks([]);ax.set_yticks([]);ax.set_xlabel(r"$u$");ax.set_ylabel(r"$v$")
 ax.axvline(0,color=DARK,lw=1)
 mark(ax,0,0,"saddle" if i==4 else "sink")
 if i==0:
  for u,v in [(.5,.8),(1.2,.5),(1.4,1.3)]:
   ax.annotate("",xy=(.08,.06),xytext=(u,v),arrowprops={"arrowstyle":"->","color":BLUE})
 else:
  if i<4:
   mark(ax,.45,.22,"saddle")
   v=np.linspace(.08,1.45,120);u=.45+.13*np.sin((v-.22)*2)
   ax.plot(u,v,color=DARK,lw=.9)
   ax.annotate("",xy=(.46,.35),xytext=(.5,.7),arrowprops={"arrowstyle":"->","color":DARK})
  mark(ax,.88,.79,"sink" if i==1 else "source")
  if i==2:cycle(ax,.88,.79,.48,.56,True,clockwise=False)
  if i==4:cycle(ax,.88,.79,1.05,1.08,True,clockwise=False)
  if i==3:
   ax.annotate("",xy=(.08,.05),xytext=(.27,.6),arrowprops={"arrowstyle":"->","color":BLUE})
 ax.set_title(["A: below saddle-node","B: upper sink","C: attracting cycle","D: after saddle loop",r"$\lambda>1,\ \mu>\mu_H>0$"][i],fontsize=10)
fig.suptitle("Topological sketches in the invariant half-plane u > 0",fontsize=12)
fig.tight_layout();save(fig)
