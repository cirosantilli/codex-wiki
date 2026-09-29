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

fig,axs=plt.subplots(2,2,figsize=(10.1,7.7),layout="constrained")
configs=[(3,0,r"$hhh$",r"$-4\lambda v h^3$"),(4,0,r"$hhhh$",r"$-\lambda h^4$"),(3,2,r"$AAh$",r"$g^2v h A_\mu A^\mu$"),(4,2,r"$AAhh$",r"$\frac{1}{2}g^2h^2 A_\mu A^\mu$")]
for ax,(n,nA,name,term) in zip(axs.flat,configs):
    angles=np.array([90,210,330] if n==3 else [45,135,225,315])*np.pi/180
    for i,theta in enumerate(angles):
        end=1.35*np.array([np.cos(theta),np.sin(theta)])
        if i<nA:wavy(ax,(0,0),end);label='A'
        else:segment(ax,(0,0),end,dashed=True);label='h'
        pos=end*1.19;ax.text(*pos,r'$'+label+r'$',ha="center",va="center",fontsize=15)
    ax.scatter([0],[0],color="black",s=24,zorder=3)
    ax.text(0,-1.9,term,ha="center",fontsize=13)
    ax.set(xlim=(-2.1,2.1),ylim=(-2.2,2));ax.axis("off");ax.set_title(name,fontsize=16)
fig.suptitle("Broken-phase physical vertices: scalar h and massive vector A",fontsize=16)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=135,transparent=False)
