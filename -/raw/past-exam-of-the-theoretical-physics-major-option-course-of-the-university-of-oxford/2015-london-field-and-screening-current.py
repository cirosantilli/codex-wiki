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

fig,axs=plt.subplots(1,2,figsize=(11,4.6),layout="constrained")
x=np.linspace(-1.2,5,500);inside=x>=0;B=np.where(inside,np.exp(-x),1.)
axs[0].axvspan(-1.2,0,color="#f4eee4");axs[0].axvspan(0,5,color="#eaf1f7")
axs[0].plot(x,B,color="#174c75",lw=2.4);axs[0].axvline(0,color="gray",ls=":")
axs[0].text(-.65,.15,"outside",ha="center");axs[0].text(2.7,.8,"superconductor",ha="center")
axs[0].set(xlabel=r"Depth $x/\lambda_L$",ylabel=r"$B_z(x)/B_z(0)$",title="Magnetic field",xlim=(-1.2,5),ylim=(0,1.12))
z=np.linspace(0,5,400);axs[1].plot(z,np.exp(-z),color="#b35b15",lw=2.4)
axs[1].text(2.7,.78,r"$j_y=-\partial_x B_z$"+"\n"+r"$\mathbf{E}=0$",ha="center",fontsize=14)
axs[1].set(xlabel=r"Depth $x/\lambda_L$",ylabel=r"$j_y(x)\lambda_L/B_z(0)$",title="Persistent screening current",xlim=(0,5),ylim=(0,1.12))
for ax in axs:ax.grid(alpha=.2);ax.spines[['top','right']].set_visible(False)
fig.suptitle(r"London screening: $\lambda_L^{-2}=2e^2v^2$ for $|\varphi|=v$",fontsize=16)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=135,transparent=False)
