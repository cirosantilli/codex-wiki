import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":11,"savefig.facecolor":"white","figure.facecolor":"white"})
fig,ax=plt.subplots(figsize=(6.2,6.4))
ax.plot([0,1,1,0,0],[0,0,1,1,0],color="0.4")
for x,y in [(0,0),(1,0),(0,1),(1,1),(.5,.5)]:
 ax.scatter(x,y,s=160,c="#2c6da4",zorder=4,clip_on=False)
 ax.annotate("Ti: z="+("1/2" if x==.5 else "0,1"),(x,y),xytext=(8,-18 if y==1 else 10),textcoords="offset points",fontsize=9)
for x,y,z in [(.3,.3,"0"),(.7,.7,"0"),(.8,.2,"1/2"),(.2,.8,"1/2")]:
 ax.scatter(x,y,s=90,c="#d45544",zorder=4)
 ax.annotate("O: z="+z,(x,y),xytext=(6,8),textcoords="offset points",fontsize=9)
ax.set(xlim=(-.10,1.20),ylim=(-.1,1.13),xlabel=r"$x/a$  [100]",ylabel=r"$y/a$  [010]",title=r"Rutile [001] projection, $u=0.30$")
ax.set_aspect("equal");ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1]);ax.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig("paper-1-rutile.png",dpi=140)
