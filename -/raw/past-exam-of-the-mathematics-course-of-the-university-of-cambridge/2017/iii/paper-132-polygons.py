"""Original diagram; tested Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Write an opaque same-basename PNG to CWD, independently of script location.
"""
from pathlib import Path
import os
os.environ["MPLCONFIGDIR"]="/tmp/2017-iii-paper-132-matplotlib"
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(9,3.5),dpi=100,facecolor="white")
colors=["#285b85","#c77931","#47865f","#9c5b8b","#777777"]
for ax,n,title in zip(axes,[4,5],["Octagon: one double zero","Decagon: two simple zeros"]):
 angles=np.arange(2*n)*np.pi/n+np.pi/2
 points=np.c_[np.cos(angles),np.sin(angles)]
 for i in range(2*n):
  p,q=points[i],points[(i+1)%(2*n)];color=colors[i%n]
  ax.plot([p[0],q[0]],[p[1],q[1]],color=color,lw=2)
  u,v=(.3,.7) if i<n else (.7,.3)
  ax.annotate("",xy=p+v*(q-p),xytext=p+u*(q-p),arrowprops={"arrowstyle":"->","color":color,"lw":1.5})
  ax.text(*(1.11*(p+q)/2),chr(97+i%n),ha="center",va="center",color=color,fontsize=11)
 ax.scatter(points[:,0],points[:,1],c=["#b45834" if n%2==0 or i%2==0 else "#286590" for i in range(2*n)],s=32,zorder=4)
 for i,p in enumerate(points):ax.text(*(1.18*p),str(i),ha="center",va="center",fontsize=9)
 ax.set(title=title,xlim=(-1.33,1.33),ylim=(-1.28,1.35),aspect="equal");ax.axis("off")
fig.subplots_adjust(left=.035,right=.965,bottom=.04,top=.9,wspace=.22)
fig.savefig(Path.cwd()/(Path(__file__).stem+".png"),dpi=100,facecolor="white",transparent=False)
