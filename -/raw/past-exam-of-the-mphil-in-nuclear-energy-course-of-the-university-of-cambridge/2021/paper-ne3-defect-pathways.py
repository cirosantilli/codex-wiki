"""Original lattice cartoon and defect-population flow diagram; not a Zr unit cell."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig,axs=plt.subplots(1,2,figsize=(11,4.8),dpi=150,gridspec_kw={"width_ratios":[1,1.5]})
ax=axs[0]
points=np.array([(x,y)for x in range(5)for y in range(5)if (x,y)!=(2,2)])
ax.scatter(points[:,0],points[:,1],s=90,color="#7e8e9b",edgecolor="white",zorder=2)
ax.scatter([2],[2],s=160,facecolor="white",edgecolor="#276b9b",linewidth=2,zorder=3)
ax.scatter([2.5],[3.5],s=115,color="#bd4b3e",edgecolor="white",zorder=3)
ax.annotate("",(2.5,3.5),(2.03,2.08),arrowprops={"arrowstyle":"->","color":"#bd4b3e","lw":1.8})
ax.annotate("vacancy",(2,2),(.05,1.2),arrowprops={"arrowstyle":"-","color":"#276b9b"},color="#276b9b",fontsize=12)
ax.annotate("self-interstitial",(2.5,3.5),(.05,4.8),arrowprops={"arrowstyle":"-","color":"#bd4b3e"},color="#bd4b3e",fontsize=12)
ax.set(xlim=(-.5,4.5),ylim=(-.4,5.3),aspect="equal",title="A separated vacancy–interstitial pair")
ax.axis("off")
ax.text(2,-.7,"Square-grid cartoon, not a zirconium unit cell.",ha="center",fontsize=9)
ax=axs[1];ax.set(xlim=(0,10),ylim=(0,7));ax.axis("off")
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="round,pad=.08",
                              facecolor=color,edgecolor="#63717d",lw=1))
    ax.text(x,y,text,ha="center",va="center",fontsize=10.5)
def arrow(start,end):
    ax.annotate("",end,start,arrowprops={"arrowstyle":"->","lw":1.4,"color":"#525f6a"})
box(5,6.2,5,.7,"surviving vacancies and interstitials","#e6edf3")
box(2.1,4.5,3.5,1,"recombination:\nrestore lattice occupancy","#e4efe4")
box(7.9,4.5,3.5,1,"sink absorption:\nboundaries, surfaces, lines","#e4efe4")
box(5,2.9,3.5,.8,"defect clustering","#f4ecdc")
box(2.3,1,3.7,1,"vacancy cavities\nif nuclei survive and grow","#f0e4df")
box(7.7,1,3.7,1,"vacancy or interstitial\ndislocation loops","#e7e4f0")
for a,b in [((3.5,5.8),(2.1,5.05)),((6.5,5.8),(7.9,5.05)),((5,5.8),(5,3.4)),
            ((4,2.45),(2.3,1.55)),((6,2.45),(7.7,1.55))]:arrow(a,b)
ax.set_title("Competing routes after displacement damage")
fig.suptitle("Defects can recombine, reach sinks, or form extended structures",fontsize=14)
fig.tight_layout(rect=(0,.025,1,.93))
fig.savefig(Path(__file__).with_suffix(".png").name,facecolor="white")
