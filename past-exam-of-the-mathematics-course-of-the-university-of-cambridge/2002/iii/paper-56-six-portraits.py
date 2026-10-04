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

fig,axs=plt.subplots(2,3,figsize=(10,6.4))
labels=["I: sink only","II: attracting cycle","III: two sinks","IV: two outer cycles","V: two inner repellers","VI: outer attractor"]
for i,ax in enumerate(axs.flat):
 ax.axhline(0,color="#bbbbbb",lw=.5);ax.axvline(0,color="#bbbbbb",lw=.5)
 ax.set_xlim(-2.3,2.3);ax.set_ylim(-1.55,1.55);ax.set_aspect("equal")
 if i<2:
  mark(ax,0,0,"sink" if i==0 else "source")
  if i==0:
   for angle in np.arange(0,2*np.pi,np.pi/4):
    ax.annotate("",xy=(.35*np.cos(angle),.35*np.sin(angle)),xytext=(1.1*np.cos(angle),1.1*np.sin(angle)),arrowprops={"arrowstyle":"->","color":BLUE,"lw":1})
  else:cycle(ax,0,0,3.4,2.2,True)
 else:
  mark(ax,0,0,"saddle");mark(ax,-1,0,"source" if i==5 else "sink");mark(ax,1,0,"source" if i==5 else "sink")
  if i<=3:
   end=1.45 if i==2 else .63
   z=np.linspace(-end,end,100);ax.plot(-.85*z,z,color=DARK,lw=.9)
   for s in [-1,1]:ax.annotate("",xy=(-.085*s,.1*s),xytext=(-.34*s,.4*s),arrowprops={"arrowstyle":"->","color":DARK,"lw":1})
  else:
   t=np.linspace(0,1,120)
   for s in [-1,1]:
    if i==4:x=s*.62*t;y=-s*.31*t
    else:x=s*t;y=-s*.5*np.sin(np.pi*t)
    ax.plot(x,y,color=DARK,lw=.9)
    ax.annotate("",xy=(x[25],y[25]),xytext=(x[52],y[52]),arrowprops={"arrowstyle":"->","color":DARK,"lw":1})
  if i==2:
   for s in [-1,1]:ax.annotate("",xy=(.9*s,.05*s),xytext=(.25*s,.15*s),arrowprops={"arrowstyle":"->","color":BLUE})
  if i==3:cycle(ax,0,0,3.05,1.35,False)
  if i==4:
   cycle(ax,-1,0,1.1,.85,False);cycle(ax,1,0,1.1,.85,False)
  if i>=3:cycle(ax,0,0,4.,2.65,True)
 ax.set_title(labels[i],fontsize=10);ax.set_xlabel(r"$x$");ax.set_ylabel(r"$y$");ax.set_xticks([]);ax.set_yticks([])
fig.suptitle("Topological phase sketches; blue solid = attracting, red dashed = repelling",fontsize=11)
fig.tight_layout()
save(fig)
