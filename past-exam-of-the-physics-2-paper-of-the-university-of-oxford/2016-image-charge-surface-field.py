from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(9.6,4.7),gridspec_kw={"width_ratios":[1,1.3]})
ax.set(xlim=(-1.5,1.5),ylim=(-2.6,2.6),xlabel=r"$x/d$",ylabel=r"$z/d$")
ax.axhspan(-2.6,0,color="#eceff1");ax.axhline(0,color="#263743",lw=2)
for z,label,col in [(1,"+Q","#b34335"),(2,"−2Q","#2a6795"),(-1,"−Q (image)","#2a6795"),(-2,"+2Q (image)","#b34335")]:
 ax.scatter(0,z,s=75,color=col,zorder=3);ax.text(.17,z,label,va="center",color=col,fontsize=11)
ax.text(-1.4,.12,"Conducting plane",fontsize=10);ax.set_title("Auxiliary image-charge construction",fontsize=12)
s=np.linspace(0,6,600);field=4/(s*s+4)**1.5-1/(s*s+1)**1.5;s0=np.sqrt((4-4**(2/3))/(4**(2/3)-1))
bx.plot(s,field,color="#23699c",lw=2.3,label="Exact signed field");bx.axhline(0,color="#555555",lw=.9);bx.scatter([s0],[0],color="#b34335",zorder=4);bx.annotate(r"$x/d=0.98686$",(s0,0),xytext=(1.5,-.18),arrowprops=dict(arrowstyle="->",color="#b34335"),fontsize=11)
far=np.linspace(3.5,6,120);bx.plot(far,3/far**3,color="#b34335",ls="--",label=r"Far tail $3(d/x)^3$")
bx.set(xlim=(0,6),ylim=(-.55,.14),xlabel=r"$x/d$",ylabel=r"$E_z/(2k_eQ/d^2)$",title="Normal field: sign reversal and dipole tail")
bx.legend(fontsize=10,loc="lower right");bx.grid(alpha=.2);fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
