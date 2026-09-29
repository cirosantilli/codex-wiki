"""Original abstract ring maps; not relaxed atomic structures."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
fig,axs=plt.subplots(1,3,figsize=(12,4),layout="constrained")
maps=[("A  Stone-Wales: no atom loss",[(5,-.7,.6),(7,.7,.6),(7,-.7,-.6),(5,.7,-.6)],"four hexagons become 5-7-7-5"),
("B  Monovacancy: one C removed",[(5,-.7,0),(9,.7,0)],"common 5-9 reconstruction"),
("C  Divacancy: two C removed",[(5,-1.25,0),(8,0,0),(5,1.25,0)],"common 5-8-5 reconstruction")]
for ax,(title,rings,note) in zip(axs,maps):
 for n,x,y in rings:
  ax.add_patch(RegularPolygon((x,y),n,radius=.61,orientation=np.pi/2,facecolor={5:"#e0edd4",7:"#f4dfce",8:"#d5e2ef",9:"#e7d8ee"}[n],edgecolor="k",lw=1.3))
  ax.text(x,y,str(n),ha="center",va="center",fontsize=17)
 ax.set_aspect("equal");ax.set(xlim=(-2,2),ylim=(-1.6,1.6),title=title);ax.text(0,-1.4,note,ha="center",fontsize=9);ax.axis("off")
fig.suptitle("Ring inventory only: polygons are symbolic, not an atomic-coordinate embedding",fontsize=11)
fig.savefig("paper-2-carbon-defects.png",dpi=155,facecolor="white")

