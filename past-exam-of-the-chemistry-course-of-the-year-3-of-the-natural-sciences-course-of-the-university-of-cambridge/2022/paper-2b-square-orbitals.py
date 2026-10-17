"""Original analytic illustration. Tested with Python 3.14, NumPy and Matplotlib.
Run from the intended output directory; the PNG is written to the current directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "savefig.facecolor": "white"})

from matplotlib.patches import Circle
POS_SQ=np.array([[-1,0],[0,1],[1,0],[0,-1]])
POS_TR=np.array([[-.65,.65],[.65,.65],[1.05,-.65],[-1.05,-.65]])
def draw(ax,coef,pos,title,axis=False):
 for i,j in [(0,1),(1,2),(2,3),(3,0)]:
  ax.plot(*np.array([pos[i],pos[j]]).T,color=".72",lw=1.2,zorder=0)
 for k,(xy,c) in enumerate(zip(pos,coef)):
  if abs(c)>1e-8:
   ax.add_patch(Circle(xy,.26,facecolor=("#4c81ac" if c>0 else "#db8c57"),edgecolor=".25"))
   ax.text(*xy,"+" if c>0 else "−",ha="center",va="center",fontsize=15)
  else:ax.add_patch(Circle(xy,.075,facecolor="white",edgecolor=".5"))
  ax.text(xy[0],xy[1]-.39,str(k+1),ha="center",va="center",fontsize=10)
 ax.set(xlim=(-1.6,1.6),ylim=(-1.65,1.65),aspect="equal",title=title);ax.axis("off")
 if axis:
  ax.annotate("x",xy=(1.45,0),xytext=(.4,0),arrowprops={"arrowstyle":"->","lw":.6},ha="center",va="bottom",color=".3")
  ax.annotate("y",xy=(0,1.45),xytext=(0,.4),arrowprops={"arrowstyle":"->","lw":.6},ha="left",color=".3")

fig,axs=plt.subplots(1,4,figsize=(11.5,3.8),layout="constrained")
cs=[[1,1,1,1],[1,-1,1,-1],[-1,0,1,0],[0,1,0,-1]]
ts=[r"$A_{1g}$: coefficients $\pm1/2$",r"$B_{1g}$: coefficients $\pm1/2$",r"$E_{u,x}$: coefficients $\pm1/\sqrt{2}$",r"$E_{u,y}$: coefficients $\pm1/\sqrt{2}$"]
for a,c,t in zip(axs,cs,ts):draw(a,c,POS_SQ,t)
fig.suptitle("Colour and sign denote orbital phase; small hollow dots denote zero amplitude",fontsize=12)
fig.savefig("paper-2b-square-orbitals.png",dpi=165)
plt.close(fig)
