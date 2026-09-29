"""Original explanatory diagram; Python 3.14, numpy, matplotlib.
Outputs its basename PNG to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge,Polygon
fig,axs=plt.subplots(2,2,figsize=(11,8.5),layout="constrained")
t=np.array([12.,-5.])/13;ang=np.degrees(np.arctan2(-5,12))
for row,north in enumerate([False,True]):
 ax=axs[row,0]
 for start,end,col in [(0,90,"#e5f0f5"),(ang,0,"#f6e8d7"),(90,360+ang,"#eeeeee")]:ax.add_patch(Wedge((0,0),1.7,start,end,color=col))
 ax.plot([0,1.7],[0,0],color="#333333",lw=2);ax.plot([0,0],[0,1.7],color="#333333",lw=2);ax.plot([0,1.7*t[0]],[0,1.7*t[1]],color="#333333",lw=2)
 if north:
  ax.plot([0,1.7],[-.04,-.04],color="#b04444",lw=1);ax.plot([-.04,-.04],[0,1.7],color="#b04444",lw=1)
 else:
  for a in [.35,.7,1.05,1.4]:
   ax.add_patch(Polygon([[a-.06,0],[a+.06,0],[a,-.13]],color="#333333"))
   ax.add_patch(Polygon([[0,a-.06],[0,a+.06],[.13,a]],color="#333333"))
 ax.text(.6,.7,"A",fontsize=15);ax.text(1.,-.17,"B",fontsize=14);ax.text(-.8,-.5,"C",fontsize=15)
 ax.text(.5,.10,"AB: ridge" if north else "AB: B above A",fontsize=9)
 ax.text(-.12,1.05,"AC: ridge" if north else "AC: A above C",rotation=90,ha="right",fontsize=9)
 ax.text(.75,-.56,"BC: transform",rotation=ang,fontsize=9)
 ax.plot(0,0,"ko",ms=4);ax.set(xlim=(-1.8,1.85),ylim=(-1.,1.85),xlabel="x: tangent toward 0° longitude",ylabel="y: tangent toward 90° E",title=("North: RRF" if north else "South: TTF"));ax.set_aspect("equal");ax.grid(alpha=.15)
 ax=axs[row,1];sgn=1 if north else -1;C=np.array([0.,0.]);A=sgn*np.array([48.,0.]);B=sgn*np.array([48.,-20.]);U=(B+C)/2 if north else B
 for p,q,label in [(C,A,"48"),(A,B,"20"),(B,C,"52")]:
  ax.annotate("",xy=q,xytext=p,arrowprops=dict(arrowstyle="->",color="#286b93",lw=1.8));mid=(p+q)/2;ax.text(mid[0]+1,mid[1]+1,label,color="#286b93",fontsize=10)
 for p,name,off in [(C,"C",(1,2)),(A,"A",(1,2)),(B,"B",(1,2))]:ax.plot(*p,"ko",ms=4);ax.text(p[0]+off[0],p[1]+off[1],name,fontsize=12)
 ax.axhline(U[1],color="#b04444",ls="--",lw=1,label="AB constraint");ax.axvline(U[0],color="#c67c22",ls="--",lw=1,label="AC constraint")
 xx=np.linspace(-62,62,100);ax.plot(xx,-5*xx/12,color="#777777",ls=":",lw=1.2,label="BC constraint")
 ax.plot(*U,"o",color="#b04444",ms=7);ax.text(U[0]-4,U[1]-5,"J",color="#b04444",fontsize=12)
 ax.set(xlim=(-8,62) if north else (-62,10),ylim=(-34,12) if north else (-12,34),xlabel="Velocity x / mm yr⁻¹",ylabel="Velocity y / mm yr⁻¹",title=f"Compatible J = ({U[0]:.0f}, {U[1]:.0f}) in C frame");ax.set_aspect("equal");ax.grid(alpha=.2)
 if north:ax.legend(fontsize=8,loc="lower left")
fig.suptitle("Original geometry and velocity-space construction; common fixed tangent axes at both poles")
fig.savefig("paper-1-polar-junctions.png",dpi=150,facecolor="white")
