"""Original slit-torus schematic; tested Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Write an opaque same-basename PNG to CWD, independently of script location.
"""
from pathlib import Path
import os
os.environ["MPLCONFIGDIR"]="/tmp/2017-iii-paper-132-matplotlib"
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
fig,ax=plt.subplots(figsize=(9,3.4),dpi=100,facecolor="white");delta=.42
for x,y,side in [(0,.12,1),(1.65,.39,delta)]:
 ax.add_patch(Rectangle((x,y),side,side,facecolor="#f4f6f8",edgecolor="#555555",lw=1.5))
 for xx,yy,dx,dy in [(x+.35*side,y,.25*side,0),(x+.35*side,y+side,.25*side,0),(x,y+.35*side,0,.25*side),(x+side,y+.35*side,0,.25*side)]:
  ax.annotate("",xy=(xx+dx,yy+dy),xytext=(xx,yy),arrowprops={"arrowstyle":"->","color":"#555555"})
 mid=x+side/2;a,b=mid-delta**2/2,mid+delta**2/2;sy=y+side/2
 ax.plot([a,b],[sy,sy],color="#b45834",lw=3,zorder=3);ax.scatter([a,b],[sy,sy],color="#b45834",s=18,zorder=4)
 ax.text(mid,sy-.08,r"slit $\delta^2$",ha="center",fontsize=10,color="#b45834")
 ax.annotate("",xy=(x+side,y-.075),xytext=(x,y-.075),arrowprops={"arrowstyle":"<->","color":"#333333"})
 ax.text(mid,y-.16,"period 1" if side==1 else r"period $\delta$",ha="center",fontsize=11)
ax.text(.5,1.22,"Unit square torus",ha="center",fontsize=12);ax.text(1.86,.92,"Small square torus",ha="center",fontsize=12)
ax.plot([1.65,2.07],[.73,.73],color="#285b85",lw=2)
ax.annotate("",xy=(1.98,.73),xytext=(1.83,.73),arrowprops={"arrowstyle":"->","color":"#285b85","lw":2})
ax.text(2.14,.73,r"$\gamma$",ha="left",va="center",fontsize=14,color="#285b85")
ax.add_patch(FancyArrowPatch((.61,.66),(1.76,.67),connectionstyle="arc3,rad=-.3",arrowstyle="<->",mutation_scale=12,lw=1.2,linestyle="--",color="#b45834"))
ax.text(1.23,.98,"Cross-glue equal slit banks",ha="center",fontsize=10,color="#b45834")
ax.text(1.12,-.23,r"$q_\delta=\omega_\delta^2/(1+\delta^2)$ has area one; the displayed $\delta$ is illustrative.",ha="center",fontsize=10)
ax.set(xlim=(-.13,2.42),ylim=(-.34,1.39),aspect="equal");ax.axis("off")
fig.subplots_adjust(left=.02,right=.98,bottom=.025,top=.99)
fig.savefig(Path.cwd()/(Path(__file__).stem+".png"),dpi=100,facecolor="white",transparent=False)
