"""Original schematic/calculation. Save only a PNG basename in the working directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

rng=np.random.default_rng(2015)
fig,axs=plt.subplots(1,3,figsize=(10.5,3.6),layout="constrained")
for ax in axs:
 ax.set(xlim=(0,1),ylim=(0,1),aspect="equal")
 ax.set_xticks([]);ax.set_yticks([])
 ax.add_patch(Rectangle((0,0),1,1,facecolor="#eef0f3",edgecolor="black"))
# Qualitative microstructure motifs; no measured dimensions or processing recipe.
for x0,x1,slope in [(0,.47,.5),(.47,1,-.6)]:
 for y0 in np.arange(-.6,1.6,.08):
  x=np.linspace(x0,x1,100);y=y0+slope*(x-x0);mask=(y>=0)&(y<=1)
  axs[0].plot(x[mask],y[mask],color="#455a64",lw=2)
axs[0].axvline(.47,color="#777777",lw=1)
for j,ax in enumerate(axs[1:]):
 for k in range(13):
  x,y=rng.uniform(.03,.8,2);length=rng.uniform(.18,.4);angle=rng.choice([.35,1.0,2.4])
  q=np.array([np.cos(angle),np.sin(angle)])*length
  p=np.array([x,y]);end=np.clip(p+q,.02,.98)
  ax.plot([p[0],end[0]],[p[1],end[1]],color="#566573",lw=4 if j==0 else 2)
 if j==1:
  p=rng.uniform(.04,.96,(85,2))
  ax.scatter(p[:,0],p[:,1],s=5,color="#d55e00")
axs[0].set_title("Pearlite colonies")
axs[1].set_title("Martensitic plate pattern")
axs[2].set_title("Carbides in transformed matrix")
fig.suptitle("Original qualitative steel sketches: not micrographs or a fabrication design",fontsize=11)
fig.text(.5,-.025,"Lamellae, plates and particles are schematic; no scale, phase fraction or kinetic rate is implied.",ha="center",fontsize=9)
finish(fig,"paper-1-steel-microstructures")
