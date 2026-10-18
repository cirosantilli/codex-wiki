from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
def segment(ax,a,b,label="",arrow=False,anti=False,dashed=False,offset=(0,.13)):
    a,b=np.array(a,dtype=float),np.array(b,dtype=float)
    ax.plot([a[0],b[0]],[a[1],b[1]],color="#174c75",lw=2,ls="--" if dashed else "-")
    if arrow:
        p,q=a+.40*(b-a),a+.60*(b-a)
        if anti:p,q=q,p
        ax.annotate("",xy=q,xytext=p,arrowprops=dict(arrowstyle="-|>",lw=1.4,color="#174c75",mutation_scale=12))
    if label:ax.text(*((a+b)/2+offset),label,ha="center",va="bottom",fontsize=13)
def wavy(ax,a,b,label=""):
    a,b=np.array(a,dtype=float),np.array(b,dtype=float);d=b-a;n=np.array([-d[1],d[0]])/np.linalg.norm(d)
    t=np.linspace(0,1,300);v=a[:,None]+d[:,None]*t+.045*n[:,None]*np.sin(16*np.pi*t)
    ax.plot(v[0],v[1],color="#b35b15",lw=1.8)
    if label:ax.text(*((a+b)/2+[0,.18]),label,ha="center",fontsize=13)

from matplotlib.patches import Circle
fig,(ax,bx)=plt.subplots(1,2,figsize=(11.8,4.7),layout="constrained",width_ratios=[1.15,1])
xs=[0,2.5,5]
for x,name in zip(xs,["empty","A occupied","B occupied"]):
    ax.add_patch(Circle((x,0),.64,fc="#e8f0f7",ec="#174c75",lw=2));ax.text(x,0,name.replace(" ","\n"),ha="center",va="center",fontsize=12)
for a,b,forward,backward in [(0,2.5,r"$f_1$",r"$f_4$"),(2.5,5,r"$f_2$",r"$f_3$")]:
    ax.annotate("",xy=(b-.65,.18),xytext=(a+.65,.18),arrowprops=dict(arrowstyle="-|>",lw=1.7,color="#174c75",connectionstyle="arc3,rad=-.35"))
    ax.annotate("",xy=(a+.65,-.18),xytext=(b-.65,-.18),arrowprops=dict(arrowstyle="-|>",lw=1.7,color="#b35b15",connectionstyle="arc3,rad=-.35"))
    ax.text((a+b)/2,.65,forward,ha="center",fontsize=14);ax.text((a+b)/2,-.85,backward,ha="center",fontsize=14)
ax.text(2.5,-1.48,"One charge at most.\nForward traffic can be nonzero while net current vanishes.",ha="center",fontsize=11)
ax.set(xlim=(-.8,5.8),ylim=(-2,1.5));ax.axis("off");ax.set_title("State-space graph",fontsize=14)
t=np.linspace(0,6,350);p=1/3-.5*np.exp(-t)+np.exp(-3*t)/6
bx.plot(t,p,color="#174c75",lw=2,label=r"$p_B(t)$")
bx.axhline(1/3,color="#b35b15",ls="--",label=r"stationary $1/3$")
bx.set(xlabel=r"$ft$ (all rates equal)",ylabel="Probability",ylim=(-.01,.37),title="Two jumps are needed to reach B")
bx.legend(frameon=False,loc="lower right");bx.grid(alpha=.2)
fig.suptitle("Single-contact molecule: jump topology and relaxation",fontsize=16)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=135,transparent=False)
