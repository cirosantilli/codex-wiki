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

fig,ax=plt.subplots(figsize=(10.4,7.1),layout="constrained")
y=np.linspace(-1.45,1.45,100)
for q in [-1,0,1]:
    ax.plot(q-y/2,y,"--",lw=1.4,color="#b36b26",alpha=.75)
    ax.text(q-.73,1.49,f"Q = {q:+d}" if q else "Q = 0",ha="center",color="#8b440f",fontsize=11)
for st in [-1,0,1]:
    ax.axhline(st,color="#609597",lw=1.3,ls=":")
    ax.text(1.77,st+.06,f"S = {st:+d}" if st else "S = 0",ha="right",color="#267072",fontsize=11)
weights=[(-.5,1,r"$K^0=d\bar s$",(-.25,.14)),(.5,1,r"$K^+=u\bar s$",(.24,.14)),(-1,0,r"$\pi^-$",(-.25,.12)),(1,0,r"$\pi^+$",(.22,.12)),(-.5,-1,r"$K^-=s\bar u$",(-.25,-.26)),(.5,-1,r"$\bar K^0=s\bar d$",(.3,-.26))]
for x,st,label,off in weights:
    ax.scatter([x],[st],s=90,color="#174c75",zorder=4)
    ax.text(x+off[0],st+off[1],label,ha="center",fontsize=13)
ax.scatter([0],[0],s=150,color="#174c75",zorder=4)
ax.text(0,.22,r"$\pi^0,\;\eta,\;\eta'$",ha="center",fontsize=15,bbox=dict(facecolor="white",edgecolor="none",alpha=.96))
ax.text(0,-.32,"Three states at one weight",ha="center",fontsize=10,bbox=dict(facecolor="white",edgecolor="none",alpha=.96))
ax.set(xlim=(-1.8,1.8),ylim=(-1.6,1.8),xlabel=r"Third isospin component $I_3$",ylabel=r"Strangeness $S$")
ax.set_xticks([-1,-.5,0,.5,1]);ax.set_yticks([-1,0,1]);ax.spines[['top','right']].set_visible(False)
ax.set_title(r"Light pseudoscalar nonet: $Q=I_3+S/2$",fontsize=17,pad=20)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,transparent=False)
