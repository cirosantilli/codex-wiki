from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,axes=plt.subplots(1,2,figsize=(10,4.8))
def arrowline(ax,a,b,color,style="-"):
 ax.plot([a[0],b[0]],[a[1],b[1]],color=color,lw=1.6,ls=style)
 if style=="-":
  p=np.array(a);q=np.array(b);mid=p+.6*(q-p);delta=.07*(q-p);ax.annotate("",xy=mid+delta,xytext=mid-delta,arrowprops=dict(arrowstyle="->",color=color,lw=1.5))
for ax,virtual in zip(axes,[False,True]):
 f=2.;u=1. if virtual else 6.;h=.6 if virtual else 1.2;v=f*u/(u-f);hp=-v/u*h
 ax.axhline(0,color="#777777",lw=.8);ax.annotate("",xy=(0,2),xytext=(0,-1.2),arrowprops=dict(arrowstyle="<->",lw=2,color="#234e70"));ax.text(.12,1.72,"Lens",fontsize=10,color="#234e70")
 ax.annotate("",xy=(-u,h),xytext=(-u,0),arrowprops=dict(arrowstyle="-|>",lw=2,color="black"));ax.text(-u if virtual else -u-.15,-.4 if virtual else h+.17,"Object",ha="center" if virtual else "right",fontsize=10)
 for x in [-f,f]:ax.scatter(x,0,color="#234e70",s=18);ax.text(x,-.24,"F",ha="center",fontsize=11)
 arrowline(ax,(-u,h),(0,h),"#bb4a35");arrowline(ax,(-u,h),(0,0),"#277c65")
 end=3.0 if virtual else v
 arrowline(ax,(0,h),(end,h*(1-end/f)),"#bb4a35");arrowline(ax,(0,0),(end,-h*end/u),"#277c65")
 if virtual:
  arrowline(ax,(0,h),(v,hp),"#bb4a35","--");arrowline(ax,(0,0),(v,hp),"#277c65","--");ax.plot([v,v],[0,hp],color="black",ls="--",lw=1.7);ax.text(v-.12,hp+.18,"Virtual image",ha="right",fontsize=10);ax.set(xlim=(-3.8,3.4),ylim=(-2,2.2));ax.set_title(r"$u<f$: virtual, upright")
 else:
  ax.annotate("",xy=(v,hp),xytext=(v,0),arrowprops=dict(arrowstyle="-|>",lw=2,color="black"));ax.text(v-.05,hp-.22,"Real image",ha="center",fontsize=10);ax.set(xlim=(-7.7,4.0),ylim=(-1.3,2.2));ax.set_title(r"$u>f$: real, inverted")
 ax.set_xticks([]);ax.set_yticks([])
 for spine in ax.spines.values():spine.set_visible(False)
fig.text(.5,.055,"Solid lines: actual rays. Dashed lines: backward extensions. Paraxial schematic; height scale enlarged.",ha="center",fontsize=10)
fig.subplots_adjust(left=.02,right=.98,top=.9,bottom=.13,wspace=.15)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
