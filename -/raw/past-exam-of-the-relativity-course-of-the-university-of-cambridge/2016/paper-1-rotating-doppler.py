"""Original analytic teaching diagram; Python 3.14, numpy, matplotlib.
Run from the desired output directory; writes its basename PNG to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from matplotlib.patches import Circle
fig,ax=plt.subplots(figsize=(8,4.8),layout="constrained")
d=2.5;phi=np.arccos(1/d)
ax.add_patch(Circle((0,0),1,fill=False,color="#555555",lw=1.5))
ax.plot(0,0,"o",color="black",ms=4);ax.plot(d,0,"o",color="black",ms=6)
ax.text(d+.06,0,"stationary receiver",fontsize=10,va="center")
for theta,label,col,sign in [(phi,"receding emission: minimum", "#aa5c31",1),(-phi,"approaching emission: maximum","#326a97",-1)]:
 x,y=np.cos(theta),np.sin(theta);v=np.array([-y,x]);n=np.array([d-x,-y]);n/=np.linalg.norm(n)
 assert abs(abs(np.dot(v,n))-1)<1e-12
 ax.plot([x,d],[y,0],color=col,lw=1.5);ax.plot(x,y,"o",color=col,ms=7)
 ax.annotate("",xy=np.array([x,y])+.45*v,xytext=(x,y),arrowprops=dict(arrowstyle="->",lw=2,color=col))
 ax.plot([0,x],[0,y],ls=":",color="#888888")
 ax.text(-1.25,sign*1.23,label,color=col,fontsize=10)
ax.text(-.55,-.12,"radius r",fontsize=10);ax.text(1.1,.15,"d > r",fontsize=10)
ax.annotate("counterclockwise rotation",xy=(-.9,.4),xytext=(-1.6,.85),fontsize=9,arrowprops=dict(arrowstyle="->",color="#555555"))
ax.set(xlim=(-1.8,3.8),ylim=(-1.45,1.45),aspect="equal",title="Tangent rays align with the source velocity at emission")
ax.axis("off")
fig.savefig("paper-1-rotating-doppler.png",dpi=155,facecolor="white")
