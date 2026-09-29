"""Original Oxford CP2 2014 solution figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

from matplotlib.patches import Circle
x1=np.sqrt(3)/2;x2=np.sqrt(15)/2
fig,(geo,field)=plt.subplots(1,2,figsize=(10.4,4.4),gridspec_kw={"width_ratios":[1,1.35]},layout="constrained")
geo.add_patch(Circle((0,-.5),2,fill=False,lw=2,color="#b86a16"))
geo.add_patch(Circle((0,.5),1,fill=False,lw=2,color="#146b9c"))
geo.axhline(0,color=".35",lw=.9);geo.axvline(0,color=".35",lw=.9)
geo.plot([0,0],[.5,-.5],"ko",ms=4)
geo.text(-.15,.5,r"$-q$",ha="right",va="center",color="#146b9c")
geo.text(-.15,-.5,r"$+q$",ha="right",va="center",color="#b86a16")
geo.plot([x1,x2],[0,0],"o",color="#a8283b",ms=5)
geo.annotate(r"$x_1$",(x1,0),xytext=(x1,-.65),ha="center",arrowprops={"arrowstyle":"-","color":".4"})
geo.annotate(r"$x_2$",(x2,0),xytext=(x2,.55),ha="center",arrowprops={"arrowstyle":"-","color":".4"})
geo.set(xlim=(-2.35,2.5),ylim=(-2.75,1.85),aspect="equal",xlabel=r"$x/a$",ylabel=r"$y/a$",title="Fixed uniform surface charges")
u=np.linspace(x1,x2,400);v=np.linspace(x2,6,600)
field.plot([0,x1],[0,0],lw=2.5,color="#146b9c")
field.plot(u,1/(u*u+.25),lw=2.5,color="#146b9c")
field.plot(v,1/(v*v+.25)**1.5,lw=2.5,color="#146b9c")
for x,ys in [(x1,[0,1]),(x2,[.25,.125])]:
    field.plot([x,x],ys,color=".5",ls=":",lw=1.1)
    field.plot([x,x],ys,"o",mfc="white",mec="#146b9c",ms=6,mew=1.5)
field.annotate(r"$1$",(x1,1),xytext=(1.12,1.01),color="#146b9c")
field.annotate(r"$1/4$",(x2,.25),xytext=(2.35,.36),arrowprops={"arrowstyle":"-","color":".5"})
field.annotate(r"$1/8$",(x2,.125),xytext=(2.7,.15),arrowprops={"arrowstyle":"-","color":".5"})
field.set(xlim=(0,6),ylim=(-.04,1.13),xlabel=r"$x/a$",ylabel=r"$|\mathbf{E}|/(k_e q/a^2)$",title="One-sided limits at shell crossings")
field.set_xticks([0,x1,x2,4,6],["0",r"$\sqrt{3}/2$",r"$\sqrt{15}/2$","4","6"])
field.grid(alpha=.18)
field.text(3.55,.68,"Far field: dipole\n"+r"$|\mathbf{E}|\propto x^{-3}$",fontsize=11)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, facecolor="white", metadata={"Software":"Oxford CP2 original Matplotlib figure"})
plt.close(fig)
