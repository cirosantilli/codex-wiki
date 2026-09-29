import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":11,"savefig.facecolor":"white","figure.facecolor":"white"})
fig,ax=plt.subplots(figsize=(6.4,6.4))
ax.plot([0,1,1,0,0],[0,0,1,1,0],color="0.4")
for x,y in [(0,0),(1,0),(0,1),(1,1),(.5,.5),(.5,0),(.5,1),(0,.5),(1,.5)]:
 z="1/2" if (x==.5) != (y==.5) else "0,1"
 ax.scatter(x,y,s=140,c="#2c6da4",zorder=4,clip_on=False)
 ax.annotate(z,(x,y),xytext=(6,8),textcoords="offset points",fontsize=9)
for x in [.25,.75]:
 for y in [.25,.75]:
  ax.scatter(x,y,s=95,c="#d45544",zorder=4)
  ax.annotate("1/4, 3/4",(x,y),xytext=(0,-20),ha="center",textcoords="offset points",fontsize=9)
ax.scatter([],[],s=140,c="#2c6da4",label="Ce; labels are z/a")
ax.scatter([],[],s=95,c="#d45544",label="O; two heights per position")
ax.legend(loc="lower center",bbox_to_anchor=(.5,-.29),frameon=False)
ax.set(xlim=(-.12,1.18),ylim=(-.08,1.15),xlabel=r"$x/a$",ylabel=r"$y/a$",title="Fluorite [001] projection")
ax.set_aspect("equal");ax.set_xticks([0,.25,.5,.75,1]);ax.set_yticks([0,.25,.5,.75,1]);ax.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig("paper-1-fluorite.png",dpi=140)
