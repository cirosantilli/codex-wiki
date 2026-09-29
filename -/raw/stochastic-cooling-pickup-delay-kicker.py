"""Original functional cooling diagram and stipulated variance model.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5. Run from _media.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
fig = plt.figure(figsize=(10, 7.5), layout="constrained")
gs = fig.add_gridspec(2, 1, height_ratios=[1.2, 1])
ax = fig.add_subplot(gs[0]); ax.set(xlim=(0, 10), ylim=(0, 5)); ax.axis("off")
ax.set_title("Stochastic cooling: sample signal, timed correction", weight="bold", pad=10)
def box(x, y, w, h, text, color):
    ax.add_patch(FancyBboxPatch((x,y), w,h,boxstyle="round,pad=0.04",ec=color,fc="white",lw=2))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center")
def arrow(a,b,color="#244d73",style="->"):
    ax.annotate("",b,a,arrowprops=dict(arrowstyle=style,color=color,lw=2))
box(.35,2.45,2,1,"Pick-up\nbeam fluctuation", "#196b96")
box(7.6,2.45,2,1,"Kicker\ncorrecting field", "#196b96")
arrow((2.45,2.95),(7.5,2.95)); ax.text(5,3.17,"beam flight time",ha="center",color="#244d73")
box(3.45,.45,3.1,1.15,"Delay + amplifier\ngain and phase", "#b46916")
arrow((1.35,2.35),(1.35,1.02),"#b46916"); arrow((1.35,1.02),(3.35,1.02),"#b46916")
arrow((6.65,1.02),(8.6,1.02),"#b46916"); arrow((8.6,1.02),(8.6,2.35),"#b46916")
ax.text(5,.12,"Signal arrives with the sampled beam, at the corrective phase",ha="center",fontsize=10)
ax.plot([8.6,8.6,1.35,1.35],[3.55,4.25,4.25,3.55],color="#244d73",lw=1.8)
arrow((6.1,4.25),(4.6,4.25))
ax.text(5,4.46,"Return around ring: mixing changes sample membership",ha="center",fontsize=10)
ax.text(5,3.75,"Functional paths only; no individual-particle tracking",ha="center",fontsize=10,color="#555555")
bx=fig.add_subplot(gs[1]); g=np.linspace(0,2.05,411); v=(1-g)**2+.25*g*g
bx.plot(g,v,color="#196b96",lw=2.5,label=r"$V_{next}=(1-g)^2+0.25g^2$")
bx.axhline(1,color="#555555",ls="--",lw=1,label="initial variance V = 1")
bx.axvspan(1.6,2.05,color="#f9e2cf",alpha=.75)
bx.scatter([.8,1.8],[.2,1.45],color=["#196b96","#b46916"],zorder=4)
bx.annotate("best one-step gain\ng = 0.8, Vnext = 0.20",(.8,.2),(.22,.72),arrowprops=dict(arrowstyle="->"),fontsize=10)
bx.annotate("g = 1.8 heats\nVnext = 1.45",(1.8,1.45),(1.3,2.2),arrowprops=dict(arrowstyle="->"),fontsize=10)
bx.set(xlabel="Dimensionless feedback gain g",ylabel="Next-step variance",xlim=(0,2.05),ylim=(0,2.65),title="Stipulated scalar toy model: V = 1, noise variance = 0.25")
bx.legend(loc="upper left",fontsize=9); bx.spines[["top","right"]].set_visible(False)
fig.savefig(Path(__file__).stem+".png",dpi=120,facecolor="white")
