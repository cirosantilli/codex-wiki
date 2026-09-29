"""Original figure. Tested Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Run from the desired image directory; writes an opaque white PNG to CWD.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Polygon
fig,ax=plt.subplots(figsize=(9,5.2),dpi=100,facecolor="white")
alpha=np.deg2rad(22);ex=np.array([np.cos(alpha),-np.sin(alpha)]);ez=np.array([np.sin(alpha),np.cos(alpha)])
def pt(x,z):return x*ex+z*ez
def arrow(a,b,label,offset=(0,0),color="black"):
 ax.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="->",lw=1.8,color=color));mid=(a+b)/2+np.array(offset);ax.text(*mid,label,color=color,fontsize=11)
ax.add_patch(Polygon([pt(-.4,0),pt(5,0),pt(5,1.25),pt(-.4,1.25)],facecolor="#e3f2fd",edgecolor="none"))
ax.plot(*np.array([pt(-.6,0),pt(5.2,0)]).T,color="black",lw=3)
ax.plot(*np.array([pt(-.4,1.25),pt(5,1.25)]).T,color="#427a9c",lw=2)
arrow(pt(.0,.0),pt(1.2,0),"$x$",(0,-.3));arrow(pt(0,0),pt(0,1.9),"$z$",(-.25,0))
arrow(pt(3.6,1.48),pt(2.0,1.48),"wind traction $-S$",(0,.16),"#ad3c28")
arrow(pt(4.55,1.9),pt(4.55,1.25),"$-p_{atm}$",(.18,0))
p=pt(1.35,.75);arrow(p,p+np.array([0,-1.2]),r"$\rho\mathbf{g}$",(.12,-.12),"#7b4ab4")
arrow(pt(2.0,0),pt(1.1,0),"wall on fluid",(-.7,-.40),"#ad3c28")
arrow(pt(.4,0),pt(.4,.55),"wall normal",(-.55,.12),"#805500")
Z=np.linspace(0,1,80);U=.8*Z-.5*Z**2
curve=np.array([pt(3.25+1.3*u,1.25*z) for z,u in zip(Z,U)])
ax.plot(*curve.T,color="#17613d",lw=2);ax.plot(*np.array([pt(3.25,0),pt(3.25,1.25)]).T,color="gray",ls=":")
for z in [.2,.4,.6,.8,1]:arrow(pt(3.25,1.25*z),pt(3.25+1.3*(.8*z-.5*z*z),1.25*z),"",color="#17613d")
ax.text(*pt(3.25,.55),"$u(z)$",fontsize=12);ax.text(*pt(-.35,1.3),"$z=h$",ha="right");ax.text(*pt(-.3,-.2),"rigid plane",ha="right")
ax.plot([0,1.2],[0,0],color="gray",lw=1);ax.text(.75,-.16,r"$\alpha$")
ax.set_aspect("equal");ax.set_xlim(-1.5,6.25);ax.set_ylim(-2.25,2.7);ax.axis("off")
fig.tight_layout();fig.savefig("paper-1-inclined-film.png",facecolor="white",transparent=False)
