from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white", "font.family": "DejaVu Sans"})
def fermion(ax,a,b,label,anti=False,offset=(0,0.14)):
    a,b=np.array(a,dtype=float),np.array(b,dtype=float)
    ax.plot([a[0],b[0]],[a[1],b[1]],color="#174c75",lw=2)
    p,q=(a+.40*(b-a),a+.60*(b-a))
    if anti:p,q=q,p
    ax.annotate("",xy=q,xytext=p,arrowprops=dict(arrowstyle="-|>",color="#174c75",lw=1.5,mutation_scale=12))
    m=(a+b)/2+offset
    ax.text(*m,label,ha="center",va="bottom",color="#123b59")
def boson(ax,a,b,label):
    a,b=np.array(a,dtype=float),np.array(b,dtype=float)
    d=b-a; n=np.array([-d[1],d[0]])/np.linalg.norm(d)
    t=np.linspace(0,1,400);v=a[:,None]+d[:,None]*t+0.055*n[:,None]*np.sin(2*np.pi*9*t)
    ax.plot(v[0],v[1],color="#b35b15",lw=1.8)
    ax.text(*((a+b)/2+np.array([0,0.16])),label,ha="center",va="bottom",color="#8b440f")

fig,axs=plt.subplots(3,1,figsize=(11.5,10.4),layout="constrained",height_ratios=[1,1,1.35])
for ax,antiq,name,factor in [(axs[0],r"$\bar d$",r"$\pi^+\to\mu^+\nu_\mu$",r"$V_{ud}\simeq\cos\theta_C$"),(axs[1],r"$\bar s$",r"$K^+\to\mu^+\nu_\mu$",r"$V_{us}\simeq\sin\theta_C$")]:
    fermion(ax,(0,1),(2,0),r"$u$",offset=(-.2,.1))
    fermion(ax,(0,-1),(2,0),antiq,anti=True,offset=(-.2,-.48))
    boson(ax,(2,0),(4.3,0),r"$W^{+*}$")
    fermion(ax,(4.3,0),(6.7,1),r"$\mu^+$",anti=True)
    fermion(ax,(4.3,0),(6.7,-1),r"$\nu_\mu$",offset=(.1,-.45))
    ax.text(7.3,.65,factor,fontsize=13)
    ax.set_title(name,loc="left",fontsize=14)
    ax.set(xlim=(-.6,10.2),ylim=(-1.65,1.8));ax.axis("off")
ax=axs[2]
fermion(ax,(0,2.5),(8,2.5),r"$u$ spectator",offset=(-1,.12))
fermion(ax,(0,-.65),(2.7,-.65),r"$\bar s$",anti=True,offset=(0,-.45))
fermion(ax,(2.7,-.65),(8,-.65),r"$\bar u$",anti=True,offset=(1,-.45))
boson(ax,(2.7,-.65),(4.6,1.0),r"$W^{+*}$")
fermion(ax,(4.6,1),(8,1.25),r"$u$",offset=(.65,-.43))
fermion(ax,(4.6,1),(8,2.0),r"$\bar d$",anti=True,offset=(.65,.1))
ax.plot([8.35,8.5,8.5,8.35],[2.6,2.6,1.9,1.9],color="black")
ax.text(8.7,2.22,r"$\pi^+$",va="center",fontsize=14)
ax.plot([8.35,8.5,8.5,8.35],[1.35,1.35,-.75,-.75],color="black")
ax.text(8.7,.3,r"$\pi^0$"+"\n"+r"$u\bar u$ component",va="center",fontsize=12)
ax.text(.1,1.15,r"$K^+:u\bar s$",fontsize=13)
ax.text(4.6,-1.6,r"weak factor $V_{us}^{*}V_{ud}$; hadronization also matters",ha="center",fontsize=11)
ax.set_title(r"$K^+\to\pi^+\pi^0$: one spectator topology",loc="left",fontsize=14)
ax.set(xlim=(-.6,10.2),ylim=(-2,3.1));ax.axis("off")
fig.suptitle("Weak pion and kaon decays: fermion-flow arrows",fontsize=17)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,transparent=False)
