from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(9.5,4.7));a,c,b=.1,.2,.4;V1=1000.;V2=2000/3
r=np.linspace(a,b,500);r1=np.linspace(a,c,250);r2=np.linspace(c,b,250)
vold=V1*(1/r-1/b)/(1/a-1/b);vleft=V2+(V1-V2)*(1/r1-1/c)/(1/a-1/c);vright=V2*(1/r2-1/b)/(1/c-1/b)
ax.plot(r,vold,color="#23699c",lw=2,label="Two spheres");ax.plot(r1,vleft,color="#bd5138",lw=2,label="Optimized third sphere");ax.plot(r2,vright,color="#bd5138",lw=2);ax.scatter([c],[V2],color="#bd5138",zorder=4)
ax.set(xlabel="Radius r (m)",ylabel="Potential V (V)",title="Continuous potentials");ax.legend(fontsize=10);ax.grid(alpha=.2)
eold=V1*a*b/(b-a)/r**2;eleft=(V1-V2)*a*c/(c-a)/r1**2;eright=V2*b*c/(b-c)/r2**2
bx.plot(r,eold/1000,color="#23699c",lw=2,label="Two spheres");bx.plot(r1,eleft/1000,color="#bd5138",lw=2,label="Optimized third sphere");bx.plot(r2,eright/1000,color="#bd5138",lw=2);bx.plot([c,c],[eleft[-1]/1000,eright[0]/1000],ls=":",color="#bd5138")
bx.scatter([a,c],[eleft[0]/1000,eright[0]/1000],color="#bd5138",zorder=4);bx.scatter([a],[eold[0]/1000],color="#23699c",zorder=4);bx.scatter([c],[eleft[-1]/1000],facecolor="white",edgecolor="#bd5138",zorder=4)
bx.annotate(r"Equal maxima at $a^+$ and $c^+$",(.2,20/3),xytext=(.17,9.8),arrowprops=dict(arrowstyle="->",color="#bd5138"),fontsize=10)
bx.set(xlabel="Radius r (m)",ylabel="Gap electric field (kV/m)",title="One-sided fields and their maxima",ylim=(0,14.5));bx.grid(alpha=.2)
for aa in [ax,bx]:aa.set_xlim(a,b);aa.set_xticks([a,c,b]);aa.axvline(c,color="#999999",ls="--",lw=.7)
fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
