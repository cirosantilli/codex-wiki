from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,ax=plt.subplots(figsize=(6.3,4.3));ax.plot([0,2,2],[0,0,1],color="#236a9b",lw=2.4)
for a,b in [((.75,0),(1.15,0)),((2,.3),(2,.65))]:ax.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="-|>",color="#236a9b",lw=2))
ax.scatter([0,2,2],[0,0,1],color="#a74736",s=35,zorder=4)
for x,y,text,dx,dy in [(0,0,"(0, 0)",-.07,-.13),(2,0,"(2, 0)",.07,-.13),(2,1,"(2, 1)",.07,.08)]:ax.text(x+dx,y+dy,text,ha="center",fontsize=11)
ax.text(1,.13,r"$\int_0^2 10x^4\,dx=64$",ha="center",fontsize=12);ax.text(1.25,.65,r"$\int_0^1-12y^2\,dy=-4$",ha="center",fontsize=12)
ax.set(xlim=(-.35,2.55),ylim=(-.35,1.35),xlabel="x",ylabel="y",title="A convenient oriented path: total integral 60")
ax.set_xticks([0,1,2]);ax.set_yticks([0,.5,1]);ax.grid(alpha=.18);fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
