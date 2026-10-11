"""Original contour diagram; Python 3.14, NumPy 2.3 and Matplotlib 3.10.
Run in the mirrored _media directory; save the white PNG to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(7.0,4.6),facecolor="white")
blue="#245b80";red="#b94425";R=3.1;eps=.24
ax.axhline(0,color="#8b939f",lw=.8);ax.axvline(0,color="#a8afb9",lw=.7)
ax.plot([-1,1],[0,0],color=red,lw=4,alpha=1,zorder=2)
for lo,hi in [(-R,-1-eps),(-1+eps,1-eps),(1+eps,R)]:
    yy=.035 if lo==-1+eps else 0
    ax.plot([lo,hi],[yy,yy],color=blue,lw=1.8,zorder=3)
    mid=(lo+hi)/2
    ax.annotate("",(mid+.22,yy),(mid-.22,yy),arrowprops={"arrowstyle":"-|>","lw":1.5,"color":blue})
for center in (-1,1):
    theta=np.linspace(np.pi,0,160)
    ax.plot(center+eps*np.cos(theta),eps*np.sin(theta),color=blue,lw=1.8)
    a1,a2=2.2,1.4
    ax.annotate("",(center+eps*np.cos(a2),eps*np.sin(a2)),(center+eps*np.cos(a1),eps*np.sin(a1)),arrowprops={"arrowstyle":"-|>","lw":1.3,"color":blue})
    ax.plot(center,0,"o",color=red,ms=5,zorder=5)
    ax.text(center,-.18,str(center),ha="center",va="top",fontsize=11)
theta=np.linspace(0,np.pi,500)
ax.plot(R*np.cos(theta),R*np.sin(theta),color=blue,lw=1.8)
for angle in (.6,2.2):
    ax.annotate("",(R*np.cos(angle+.14),R*np.sin(angle+.14)),(R*np.cos(angle),R*np.sin(angle)),arrowprops={"arrowstyle":"-|>","lw":1.6,"color":blue})
for yy,label in [(1,r"$i$"),(2,r"$2i$")]:
    ax.plot(0,yy,"x",color="#172c43",mew=2,ms=7)
    ax.text(.16,yy,label,va="center",fontsize=12)
ax.text(-R,-.16,r"$-R$",ha="center",va="top",fontsize=11)
ax.text(R,-.16,r"$R$",ha="center",va="top",fontsize=11)
ax.text(0,-.48,"branch cut: [−1, 1]",ha="center",color=red,fontsize=11)
ax.annotate("upper bank",(-.3,.04),(-1.8,.9),arrowprops={"arrowstyle":"->","color":"#596777"},fontsize=10)
ax.text(2.7,2.05,"large arc",ha="center",color=blue,fontsize=11)
ax.text(3.48,.01,r"$\mathrm{Re}\,z$",va="center",fontsize=11)
ax.text(.08,3.40,r"$\mathrm{Im}\,z$",fontsize=11)
ax.set(xlim=(-3.65,3.8),ylim=(-.65,3.55),aspect="equal",title="A closed upper-half-plane contour with endpoint indentations")
ax.axis("off")
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
plt.close(fig)
