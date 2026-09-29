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

fig,ax=plt.subplots(figsize=(6.6,4.8))
k=np.linspace(-.45,1.5,700);l=np.linspace(-1.25,1.1,700)
K,L=np.meshgrid(k,l);fold=.752256*(-L);hom=.8*(-L);hop=-L
reg=np.where(L>=0,np.where(K<0,0,1),np.where(K<fold,2,np.where(K<hom,3,np.where(K<hop,4,5))))
from matplotlib.colors import ListedColormap
ax.pcolormesh(K,L,reg,cmap=ListedColormap(["#e7eff8","#f1e9fa","#e5f3e8","#fff2d1","#fce5df","#e2f2f5"]),shading="nearest",alpha=.9)
ax.axhline(0,color=DARK,lw=1.5,label="Pitchfork")
ax.plot([0,0],[0,1.1],color=RED,lw=1.7)
a=np.linspace(0,1.25,200)
ax.plot(a,-a,color=RED,lw=1.7,label="Hopf")
ax.plot(.8*a,-a,color=GREEN,lw=1.7,ls="--",label="Homoclinic (leading)")
ax.plot(.752256*a,-a,color="#a77c1c",lw=1.7,ls=":",label="Cycle fold (leading)")
for x,y,s in [(-.25,.6,"I"),(.6,.6,"II"),(.15,-.85,"III"),(.66,-.85,"IV"),(.77,-.85,"V"),(1.22,-.85,"VI")]:
 ax.text(x,y,s,ha="center",va="center",weight="bold",fontsize=12)
ax.plot(0,0,"ko",ms=5)
tidy(ax,r"$\kappa$",r"$\lambda$")
ax.set_xlim(-.45,1.5);ax.set_ylim(-1.25,1.1)
ax.set_title("Symmetric double-zero unfolding (local schematic)")
ax.legend(loc="upper right",fontsize=8,framealpha=.95)
save(fig)
