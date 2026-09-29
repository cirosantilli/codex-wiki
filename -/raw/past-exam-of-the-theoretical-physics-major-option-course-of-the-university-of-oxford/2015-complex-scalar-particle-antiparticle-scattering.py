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

fig,axs=plt.subplots(1,2,figsize=(11.3,5.2),layout="constrained")
ax=axs[0]
segment(ax,(0,1),(2,0),r"$1:\varphi$",arrow=True,offset=(-.1,.16));segment(ax,(0,-1),(2,0),r"$2:\bar\varphi$",arrow=True,anti=True,offset=(-.1,-.45))
segment(ax,(2,0),(4,0),r"$\phi$",dashed=True)
segment(ax,(4,0),(6,1),r"$3:\varphi$",arrow=True,offset=(.1,.16));segment(ax,(4,0),(6,-1),r"$4:\bar\varphi$",arrow=True,anti=True,offset=(.1,-.45))
ax.set_title(r"s channel: $(p_1+p_2)^2=s$",fontsize=14)
ax=axs[1]
segment(ax,(0,1),(3,1),r"$1:\varphi$",arrow=True);segment(ax,(3,1),(6,1),r"$3:\varphi$",arrow=True)
segment(ax,(0,-1),(3,-1),r"$2:\bar\varphi$",arrow=True,anti=True,offset=(0,-.5));segment(ax,(3,-1),(6,-1),r"$4:\bar\varphi$",arrow=True,anti=True,offset=(0,-.5))
segment(ax,(3,1),(3,-1),r"$\phi$",dashed=True,offset=(.4,0))
ax.set_title(r"t channel: $(p_1-p_3)^2=t$",fontsize=14)
for ax in axs:
 ax.set(xlim=(-.4,6.5),ylim=(-2,2));ax.axis("off")
fig.suptitle("Neutral-scalar exchange preserves the complex charge arrows",fontsize=16)
fig.text(.5,.04,"Fixed final charge labels allow s and t exchange, not a third u-channel graph.",ha="center",fontsize=12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=135,transparent=False)
