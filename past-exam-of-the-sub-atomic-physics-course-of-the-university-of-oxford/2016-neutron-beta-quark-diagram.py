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

fig,ax=plt.subplots(figsize=(10.3,5.4),layout="constrained")
fermion(ax,(0,3.3),(8,3.3),r"$u$ spectator")
fermion(ax,(0,2.55),(8,2.55),r"$d$ spectator")
fermion(ax,(0,1.8),(3,1.8),r"$d$")
fermion(ax,(3,1.8),(8,1.8),r"$u$")
boson(ax,(3,1.8),(5,0.35),r"$W^{-*}$")
fermion(ax,(5,.35),(8,.65),r"$e^-$",offset=(.15,.12))
fermion(ax,(5,.35),(8,-.6),r"$\bar\nu_e$",anti=True,offset=(.1,-.35))
ax.scatter([3,5],[1.8,.35],s=24,color="black",zorder=4)
ax.text(-.1,4.05,r"$n: udd$",ha="left",weight="bold",fontsize=15)
ax.text(7.6,4.05,r"$p: uud$",ha="right",weight="bold",fontsize=15)
ax.annotate("time / external momentum",xy=(6,-1.2),xytext=(2,-1.2),ha="center",arrowprops=dict(arrowstyle="->",color="black"),fontsize=11)
ax.text(4,-1.8,"Blue arrows show fermion flow; the antineutrino arrow opposes its momentum.\nThe W is virtual; this diagram does not imply an on-shell W in neutron decay.",ha="center",va="top",fontsize=11)
ax.set(xlim=(-.4,8.6),ylim=(-2.5,4.5));ax.axis("off")
fig.suptitle("Neutron beta decay: one flavor conversion, two spectators",fontsize=16)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,transparent=False)
