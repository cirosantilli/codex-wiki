from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4.8),gridspec_kw={"width_ratios":[1,1.35]})
x=np.array([0,1,3,4]);y=np.array([0,-.7,0,.35]);ax.axhline(0,color="#999999",ls="--",lw=.8);ax.plot(x,y,color="#234e70",lw=2.2);ax.scatter(x[1:3],y[1:3],s=115,color="#ba5239",zorder=4);ax.scatter([0,4],[0,.35],s=35,color="#234e70")
ax.text(0,.16,"Fixed",ha="center",fontsize=10);ax.text(1,-1.02,r"$y_1=-2h_0$",ha="center",fontsize=12);ax.text(3,.2,r"$y_2=0$",ha="center",fontsize=12);ax.text(4,.55,r"$h=h_0$",ha="center",fontsize=12)
for left,right,label in [(0,1,"L"),(1,3,"2L"),(3,4,"L")]:ax.annotate("",xy=(right,-1.18),xytext=(left,-1.18),arrowprops=dict(arrowstyle="<->",lw=1,color="#777777"));ax.text((left+right)/2,-1.36,label,ha="center",fontsize=11)
ax.set(xlim=(-.3,4.35),ylim=(-1.65,1.25),title=r"Particular response at $\omega=\sqrt{3}\omega_0$");ax.axis("off")
for lo,hi in [(0,np.sqrt(2)-.012),(np.sqrt(2)+.012,2-.012),(2+.012,2.7)]:
 r=np.linspace(lo,hi,350);s=r*r;d=(2-s)*(4-s)
 bx.plot(r,2/d,color="#236a9b",lw=1.8,label=r"$A_1/h_0$" if lo==0 else None);bx.plot(r,2*(3-s)/d,color="#ba5239",lw=1.8,label=r"$A_2/h_0$" if lo==0 else None)
for r in [np.sqrt(2),2]:bx.axvline(r,color="#777777",ls="--",lw=1)
bx.axhline(0,color="#999999",lw=.7);bx.scatter([np.sqrt(3)],[0],color="#ba5239",s=35,zorder=4);bx.annotate("Antiresonance",(np.sqrt(3),0),xytext=(1.75,1.8),arrowprops=dict(arrowstyle="->",color="#ba5239"),fontsize=10)
bx.set(xlim=(0,2.7),ylim=(-4,4),xlabel=r"$\omega/\omega_0$",ylabel="Signed amplitude / endpoint amplitude",title="Poles at the two natural frequencies");bx.grid(alpha=.18);bx.legend(loc="lower left",fontsize=11);fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
