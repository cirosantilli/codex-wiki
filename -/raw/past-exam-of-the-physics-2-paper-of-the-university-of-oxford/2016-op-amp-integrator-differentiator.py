from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,axes=plt.subplots(2,1,figsize=(9,6.5))
def component(ax,x0,x1,y,kind):
 mid=(x0+x1)/2
 if kind=="R":
  ax.plot([x0,mid-.55],[y,y],color="#20333e",lw=1.7);ax.plot([mid+.55,x1],[y,y],color="#20333e",lw=1.7);ax.add_patch(Rectangle((mid-.55,y-.17),1.1,.34,fill=False,lw=1.7));ax.text(mid,y+.32,"$R$",ha="center",fontsize=14)
 else:
  ax.plot([x0,mid-.1],[y,y],color="#20333e",lw=1.7);ax.plot([mid+.1,x1],[y,y],color="#20333e",lw=1.7);ax.plot([mid-.1,mid-.1],[y-.35,y+.35],color="#20333e",lw=1.7);ax.plot([mid+.1,mid+.1],[y-.35,y+.35],color="#20333e",lw=1.7);ax.text(mid,y+.45,"$C$",ha="center",fontsize=14)
for ax,diff in zip(axes,[False,True]):
 ax.set(xlim=(-.1,10),ylim=(.1,4.45));ax.axis("off")
 ax.add_patch(Polygon([[5,1],[5,3.2],[7,2.1]],facecolor="#e9f2f7",edgecolor="#234e70",lw=1.8))
 component(ax,.55,3,2.65,"C" if diff else "R");ax.plot([3,5],[2.65,2.65],color="#20333e",lw=1.7)
 ax.plot([3,3,4],[2.65,3.8,3.8],color="#20333e",lw=1.7);component(ax,4,7.3,3.8,"R" if diff else "C");ax.plot([7.3,8.3,8.3],[3.8,3.8,2.1],color="#20333e",lw=1.7)
 ax.plot([7,9.35],[2.1,2.1],color="#20333e",lw=1.7);ax.scatter([3,8.3],[2.65,2.1],s=16,color="#20333e")
 ax.plot([5,4.35,4.35],[1.55,1.55,.65],color="#20333e",lw=1.7)
 for width,y in [(.55,.65),(.36,.49),(.16,.33)]:ax.plot([4.35-width/2,4.35+width/2],[y,y],color="#20333e",lw=1.5)
 ax.text(5.15,2.65,"−",fontsize=16,va="center");ax.text(5.15,1.55,"+",fontsize=16,va="center")
 ax.text(.1,2.65,r"$V_{\rm in}$",ha="center",va="center",fontsize=14);ax.text(9.7,2.1,r"$V_{\rm out}$",ha="center",va="center",fontsize=14)
 ax.text(3.0,2.2,"Virtual ground",ha="center",fontsize=10)
 ax.set_title("Differentiator: capacitor input, resistor feedback" if diff else "Integrator: resistor input, capacitor feedback",fontsize=13)
fig.subplots_adjust(left=.03,right=.97,top=.94,bottom=.03,hspace=.3)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
