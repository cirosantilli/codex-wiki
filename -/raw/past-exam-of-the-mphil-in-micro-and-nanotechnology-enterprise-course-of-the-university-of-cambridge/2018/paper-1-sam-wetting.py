"""Original explanatory figure; Python 3.14, numpy and matplotlib.
Write the same-basename PNG to the current working directory for Make.
No source image or source data file is read.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, Arc
import numpy as np

def box(ax,x,y,w,h,text,fc="#e5edf5",size=9):
    ax.add_patch(Rectangle((x,y),w,h,fc=fc,ec="#253858",lw=1.2))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=size)

def arrow(ax,a,b,text=None):
    ax.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="->",lw=1.3,color="#253858"))
    if text:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2,text,fontsize=8,ha="center",va="bottom")

def finish(fig,name):
    fig.set_facecolor("white")
    fig.savefig(name,dpi=150,facecolor="white",bbox_inches="tight")
    plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(9,4.7),layout="constrained")
ax=axs[0];ax.set(xlim=(0,10),ylim=(0,10),title="Hydroxyl-terminated monolayer");ax.axis("off")
box(ax,.5,.5,9,1.1,"Gold surface",fc="#e5ba54",size=11)
for x in [1.6,3.1,4.6,6.1,7.6]:
    ax.add_patch(Circle((x,1.85),.17,fc="#c69012"));ax.text(x-.3,1.9,"S",fontsize=8)
    xx=x+np.array([0,.3,.1,.4,.2,.5,.3]);yy=np.linspace(2,6.3,7);ax.plot(xx,yy,color="#253858",lw=1.8)
    ax.text(x+.3,6.6,"OH",ha="center",color="#007f91",fontsize=10)
ax.text(5,8.5,"Polar groups face water",ha="center",fontsize=11);ax.text(5,.1,"Sulfur anchor; chains organize laterally",ha="center",fontsize=9)
ax=axs[1];ax.set(xlim=(-.3,3.5),ylim=(-.25,2.8),title="Angle measured through liquid");ax.set_aspect("equal");ax.axis("off")
# Circular cap with an acute right-hand contact angle.
R=1.1;cy=-.35;xc=1.1;dx=np.sqrt(R*R-cy*cy);right=xc+dx
ang=np.linspace(np.arcsin(-cy/R),np.pi-np.arcsin(-cy/R),200)
x=xc+R*np.cos(ang);y=cy+R*np.sin(ang)
ax.fill(np.r_[x,right],np.r_[y,0],color="#cde9ef");ax.plot(x,y,color="#007f91",lw=2);ax.plot([-.2,3.4],[0,0],color="#555555",lw=2)
theta=np.arccos(-cy/R)
ax.add_patch(Arc((right,0),.75,.75,theta1=180-np.degrees(theta),theta2=180,color="#a35012"));ax.text(right-.65,.16,r"$\theta_C$",color="#a35012")
arrow(ax,(right,0),(right-.75,0));arrow(ax,(right,0),(right+.85,0));arrow(ax,(right,0),(right-.55*np.cos(theta),.55*np.sin(theta)))
ax.text(right-.7,-.18,r"$\gamma_{SL}$",ha="center");ax.text(right+.65,-.18,r"$\gamma_{SV}$",ha="center");ax.text(right-.65,.65,r"$\gamma_{LV}$")
ax.text(.95,.35,"Liquid",ha="center");ax.text(.9,1.5,"Vapor",ha="center");ax.text(1.5,-.45,"Solid",ha="center")
ax.text(1.5,2.3,r"$\gamma_{SV}=\gamma_{SL}+\gamma_{LV}\cos\theta_C$",ha="center",fontsize=11)
finish(fig,"paper-1-sam-wetting.png")
