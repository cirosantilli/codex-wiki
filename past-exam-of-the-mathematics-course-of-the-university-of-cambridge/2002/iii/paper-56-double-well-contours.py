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

fig,ax=plt.subplots(figsize=(6.2,4.2))
u=np.linspace(-2.1,2.1,600);v=np.linspace(-1.6,1.6,500)
U,V=np.meshgrid(u,v);H=.5*V**2-.5*U**2+.25*U**4
ax.contour(U,V,H,levels=[-.23,-.17,-.08],colors=BLUE,linewidths=.8)
ax.contour(U,V,H,levels=[.06,.2,.5,.9],colors="#888888",linewidths=.8)
ax.contour(U,V,H,levels=[0],colors=GREEN,linewidths=2)
for x in [-1,1]:mark(ax,x,0)
mark(ax,0,0,"saddle")
ax.annotate("",xy=(.8,.8*np.sqrt(1-.8**2/2)),xytext=(.65,.65*np.sqrt(1-.65**2/2)),arrowprops={"arrowstyle":"->","color":GREEN})
ax.text(.18,1.35,r"$H>0$: one outer contour")
ax.text(.2,-1.36,r"$H=0$: two saddle loops",color=GREEN)
ax.text(-1.05,.12,r"$H<0$",ha="center",color=BLUE)
ax.text(1.05,.12,r"$H<0$",ha="center",color=BLUE)
tidy(ax,r"$u$",r"$v$");ax.set_title(r"Double-well Hamiltonian contours ($\alpha=-1$)")
ax.set_aspect("equal")
save(fig)
