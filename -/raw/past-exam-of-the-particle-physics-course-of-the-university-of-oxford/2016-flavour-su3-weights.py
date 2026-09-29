from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans", "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4.8))
for a in [ax,bx]:
 a.axhline(0,color="#aab0b5",lw=.8);a.axvline(0,color="#aab0b5",lw=.8);a.set_xlabel(r"$I_3$");a.set_ylabel(r"$Y$");a.grid(alpha=.18)
pts={"u":(.5,1/3),"d":(-.5,1/3),"s":(0,-2/3)}
for k,(x,y) in pts.items():ax.scatter(x,y,s=65,color="#234e70",zorder=4);ax.text(x+.045,y+.035,"$"+k+"$",fontsize=16)
for l,r,label in [("d","u",r"$I_+\ /\ I_-$"),("s","u",r"$V_+\ /\ V_-$"),("s","d",r"$U_+\ /\ U_-$")]:
 p=np.array(pts[l]);q=np.array(pts[r]);d=q-p;ax.add_patch(FancyArrowPatch(p+.09*d,q-.09*d,arrowstyle="<->",mutation_scale=13,lw=1.6,color="#b64140"))
 mid=(p+q)/2;ax.text(mid[0]+(.08 if l=="s" and r=="u" else -.1 if l=="s" else 0),mid[1]+(.1 if l=="d" else 0),label,ha="center",fontsize=11,bbox=dict(facecolor="white",edgecolor="none",pad=1))
ax.set(xlim=(-.8,.8),ylim=(-.9,.65),xticks=[-.5,0,.5],yticks=[-2/3,0,1/3]);ax.set_title("Quark triplet: three distinct weights")
mes=[(-1,0,r"$\pi^-$"),(1,0,r"$\pi^+$"),(.5,1,r"$K^+$"),(-.5,1,r"$K^0$"),(-.5,-1,r"$K^-$"),(.5,-1,r"$\bar K^0$")]
polygon=np.array([(1,0),(.5,1),(-.5,1),(-1,0),(-.5,-1),(.5,-1),(1,0)]);bx.plot(*polygon.T,color="#aab0b5",lw=1.3)
for x,y,label in mes:
 bx.scatter(x,y,s=60,color="#234e70",zorder=4);bx.annotate(label,(x,y),xytext=(8 if x>=0 else -8,10 if y>=0 else -18),textcoords="offset points",ha="left" if x>=0 else "right",fontsize=14)
bx.scatter([0],[0],s=85,facecolor="white",edgecolor="#b64140",lw=2,zorder=5);bx.text(.06,-.22,r"$\pi^0,\ \eta_8$",fontsize=14);bx.text(0,.3,"Two states at the same weight",ha="center",fontsize=10)
bx.set(xlim=(-1.5,1.5),ylim=(-1.4,1.4),xticks=[-1,-.5,0,.5,1],yticks=[-1,0,1]);bx.set_title("Meson octet: six outer + two central states")
fig.subplots_adjust(left=.07,right=.97,bottom=.14,top=.88,wspace=.27)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
