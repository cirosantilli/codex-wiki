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

fig,ax=plt.subplots(figsize=(9.2,6.4),layout="constrained")
r=np.linspace(-3,3,500);top=np.full_like(r,3.)
ax.fill_between(r,0,np.minimum(np.abs(r),3),where=r<0,color="#dce9f6")
ax.fill_between(r,0,np.minimum(np.abs(r),3),where=r>0,color="#f7e4ce")
ax.fill_between(r,np.abs(r),top,color="#edf1e8")
ax.plot([-3,0],[3,0],color="#174c75",lw=2);ax.plot([0,3],[0,3],color="#b35b15",lw=2)
ax.text(0,2.05,"Disordered\n"+r"$\mathbf{m}=0$",ha="center",fontsize=16)
ax.text(-2.2,.65,"Axis 1 ordered\n"+r"$m_1=\pm\sqrt{-(t+r)/(4u)}$",ha="center",fontsize=12)
ax.text(2.15,.65,"Axis 2 ordered\n"+r"$m_2=\pm\sqrt{(r-t)/(4u)}$",ha="center",fontsize=12)
ax.text(-1.4,1.6,r"$r=-t$",rotation=-42,ha="center",color="#174c75",fontsize=14)
ax.text(1.4,1.6,r"$r=t$",rotation=42,ha="center",color="#9c4f14",fontsize=14)
ax.text(0,.18,"Both boundaries: continuous transitions",ha="center",fontsize=10)
ax.set(xlim=(-3,3),ylim=(0,3),xlabel="Quadratic anisotropy r",ylabel="Isotropic quadratic coefficient t > 0")
ax.spines[['top','right']].set_visible(False);ax.set_xticks([-3,-2,-1,0,1,2,3]);ax.set_yticks([0,1,2,3])
ax.set_title("Positive quartic coupling u: the specified upper half-plane",fontsize=15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=135,transparent=False)
