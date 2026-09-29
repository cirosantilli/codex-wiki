from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(9.3,4.5),gridspec_kw={"width_ratios":[1,1.4]});ax.set(xlim=(0,5.2),ylim=(-.1,3.1));ax.axis("off")
ax.plot([1,1,2],[1.55,2.4,2.4],color="#263743",lw=1.7);ax.plot([3.2,4,4],[2.4,2.4,1.45],color="#263743",lw=1.7);ax.add_patch(Rectangle((2,2.22),1.2,.36,fill=False,edgecolor="#263743",lw=1.7));ax.text(2.6,2.79,r"$R_{\rm th}=5R/3$",ha="center",fontsize=12)
ax.plot([4,4,1,1],[1.25,.45,.45,.85],color="#263743",lw=1.7);ax.plot([3.55,4.45],[1.45,1.45],color="#263743",lw=1.8);ax.plot([3.55,4.45],[1.25,1.25],color="#263743",lw=1.8);ax.text(4.65,1.35,"C",va="center",fontsize=13)
ax.add_patch(Circle((1,1.2),.35,facecolor="white",edgecolor="#263743",lw=1.7));ax.text(1,1.34,"+",ha="center",va="center",fontsize=13);ax.text(1,1.04,"−",ha="center",va="center",fontsize=13);ax.text(.75,.05,r"$V_{\rm th}=2V/3$",fontsize=12)
ax.set_aspect("equal",adjustable="box");ax.set_title("Equivalent seen by the capacitor",fontsize=12)
u=np.linspace(0,4,500);i2=.4*np.exp(-u);i1=1/3-i2/3;cross=np.log(8/5)
bx.plot(u,i1,color="#b44e37",lw=2,label=r"$I_1$ through $2R$");bx.plot(u,i2,color="#236a9b",lw=2,label=r"$I_2$ through C");bx.axhline(1/3,color="#b44e37",lw=.8,ls=":");bx.scatter([cross],[.25],color="#263743",s=30,zorder=4);bx.annotate(r"$t/\tau=\log(8/5)$",(cross,.25),xytext=(1.1,.23),arrowprops=dict(arrowstyle="->",color="#263743"),fontsize=11)
bx.set(xlim=(0,4),ylim=(0,.44),xlabel=r"$t/\tau$",ylabel=r"$IR/V$",title=r"$\tau=5RC/3$");bx.grid(alpha=.16);bx.legend(fontsize=10,loc="upper right");fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
