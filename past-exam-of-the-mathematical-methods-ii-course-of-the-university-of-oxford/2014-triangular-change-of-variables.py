from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

from matplotlib.patches import Polygon
fig,(ax,bx)=plt.subplots(1,2,figsize=(9.5,4.7),layout="constrained")
for axis,verts,names in [(ax,[(0,0),(0,1),(.5,.5)],("x","y")),(bx,[(0,0),(1,1),(1,0)],("r = x + y","s = y − x"))]:
 axis.add_patch(Polygon(verts,facecolor="#dfeef5",edgecolor="#315e7a",lw=2));axis.set(xlabel=names[0],ylabel=names[1],xlim=(-.1,1.16),ylim=(-.12,1.15),aspect="equal");axis.grid(alpha=.12)
 for x,y in verts:axis.plot(x,y,"o",color="#315e7a",ms=5)
ax.text(.03,.84,"x = 0",fontsize=11);ax.text(.32,.18,"y = x",rotation=45,fontsize=11);ax.text(.28,.75,"x + y = 1",rotation=-45,fontsize=11);ax.set_title("Original region: 0 ≤ x ≤ 1/2")
bx.text(.48,.09,"s = 0",fontsize=11);bx.text(1.025,.5,"r = 1",rotation=90,fontsize=11);bx.text(.3,.5,"s = r",rotation=45,fontsize=11);bx.set_title("Transformed region: 0 ≤ s ≤ r ≤ 1")
fig.suptitle("Linear coordinate map; absolute inverse Jacobian = 1/2",fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
