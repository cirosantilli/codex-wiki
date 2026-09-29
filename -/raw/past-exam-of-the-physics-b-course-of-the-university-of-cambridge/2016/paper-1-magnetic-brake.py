"""Original teaching diagram. Tested with Python 3.14, numpy, matplotlib.
Run in the desired output directory; PNG is written as a basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle
fig=plt.figure(figsize=(10,6),layout="constrained");gs=fig.add_gridspec(2,3,height_ratios=[1.4,1])
def arrow(ax,a,b,col):ax.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="->",color=col,lw=2))
for j,(name,x0,sense) in enumerate([("Entry: counterclockwise",-.5,1),("Fully inside: zero current",.15,0),("Exit: clockwise",.85,-1)]):
 ax=fig.add_subplot(gs[0,j]);ax.axvspan(0,1.35,color="#e3edf6");ax.text(.66,1.32,"B into page",ha="center",fontsize=9)
 ax.add_patch(Rectangle((x0,0),1,1,fill=False,lw=2,color="black"))
 if sense:
  sides=[((x0+.22,0),(x0+.72,0)),((x0+1,.25),(x0+1,.75)),((x0+.72,1),(x0+.22,1)),((x0,.75),(x0,.25))]
  for a,b in sides:arrow(ax,a,b,"#326a97") if sense==1 else arrow(ax,b,a,"#326a97")
  inside_x=x0+1 if sense==1 else x0
  arrow(ax,(inside_x,.5),(inside_x-.4,.5),"#ba3737")
  mid=.25 if sense==1 else 1.1
  arrow(ax,(mid,1),(mid,1-.3*sense),"#ba3737");arrow(ax,(mid,0),(mid,.3*sense),"#ba3737")
  ax.text(x0+.5,-.68,"net drag opposite motion",ha="center",fontsize=8)
 else:ax.text(x0+.5,.5,"i = 0\nF = 0 on all sides",ha="center",va="center",fontsize=8)
 arrow(ax,(-.5,-.4),(.2,-.4),"#333333");ax.text(.3,-.42,"v",fontsize=11)
 ax.set(xlim=(-.85,2.15),ylim=(-.85,1.6),aspect="equal",title=name);ax.axis("off")
b=fig.add_subplot(gs[1,:]);times=[-.2,0,0,1,1,1.35,1.35,2.35,2.35,2.6];forces=[0,0,-1,-1,0,0,-1,-1,0,0]
b.plot(times,forces,color="#ba3737",lw=2);b.axhline(0,color="#555555",lw=.8)
b.set(xlabel="Time / (a/v)",ylabel="Force / (B² a² v/R)",ylim=(-1.3,.25),title="Two equal drag impulses; the full-overlap gap is illustrative")
b.text(.5,-.5,"entry",ha="center");b.text(1.85,-.5,"exit",ha="center")
fig.savefig("paper-1-magnetic-brake.png",dpi=150,facecolor="white")
