from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(9,4.4));x=np.linspace(-2,4,400)
ax.fill_between(x,x*x,2*x+8,color="#c5dfeb",alpha=.8);ax.plot(x,x*x,color="#236a9b",lw=2,label=r"$y=x^2$");ax.plot(x,2*x+8,color="#b74c37",lw=2,label=r"$y=2x+8$");ax.scatter([-2,4],[4,16],color="#263743",s=25,zorder=4)
ax.axvline(1,color="#777777",ls="--",lw=.9);ax.text(1.1,2,"Centroid x = 1",fontsize=10);ax.set(xlim=(-2.6,4.6),ylim=(-.7,18),xlabel="x",ylabel="y",title="Parabola–line region");ax.grid(alpha=.15);ax.legend(fontsize=10,loc="upper left")
th=np.linspace(0,np.pi/2,250);xx=np.r_[0,np.cos(th),0];yy=np.r_[0,np.sin(th),0];bx.fill(xx,yy,color="#c5dfeb");bx.plot(np.cos(th),np.sin(th),color="#236a9b",lw=2);bx.plot([0,1],[0,0],color="#263743",lw=1.2);bx.plot([0,0],[0,1],color="#263743",lw=1.2)
bx.text(.25,.4,r"$0\leq r\leq1$"+"\n"+r"$0\leq\theta\leq\pi/2$",fontsize=13);bx.set(xlim=(-.08,1.15),ylim=(-.08,1.15),xlabel="x",ylabel="y",aspect="equal",title="First-quadrant unit disk");bx.set_xticks([0,.5,1]);bx.set_yticks([0,.5,1]);bx.grid(alpha=.15);fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
