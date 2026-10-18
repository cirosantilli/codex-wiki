from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,ax=plt.subplots(figsize=(7.5,4.6));alpha=.5;ax.axvspan(-1,0,color="#dcecf3",alpha=.8)
ax.plot([-1.65,-1],[-.25,-.25],color="#236a9b",lw=2.4);u=np.linspace(-1,0,250);ax.plot(u,u+(1+alpha)/2,color="#236a9b",lw=2.4);ax.plot([0,1],[.25,.25],color="#236a9b",lw=2.4)
ax.plot([0,0],[.75,.25],color="#b24b38",lw=1.4,ls="--");ax.scatter([0,0],[.25,.75],facecolor="white",edgecolor="#236a9b",s=45,lw=1.6,zorder=4);ax.scatter([-.75],[0],color="#b24b38",s=35,zorder=4)
ax.axhline(0,color="#777777",lw=.8);ax.axvline(-1,color="#777777",lw=.8,ls=":");ax.axvline(0,color="#777777",lw=.8,ls=":");ax.annotate("Field changes sign",(-.75,0),xytext=(-1.48,.25),arrowprops=dict(arrowstyle="->",color="#b24b38"),fontsize=10)
ax.text(-.52,.92,r"Slab: $\sigma/(\rho d)=1/2$",ha="center",fontsize=11);ax.text(.15,.58,r"Jump $-\sigma/\epsilon_0$",color="#b24b38",fontsize=11);ax.text(-1.43,-.42,"Below slab",ha="center",fontsize=10);ax.text(.5,-.42,"Above sheet",ha="center",fontsize=10)
ax.set(xlim=(-1.65,1),ylim=(-.5,1.05),xlabel=r"$z/d$",ylabel=r"$\epsilon_0E_z/(\rho d)$",title="Normal electric field of the sheet–slab distribution");ax.grid(alpha=.13);fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
