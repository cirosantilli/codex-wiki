from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

fig,ax=plt.subplots(figsize=(8.5,5),layout="constrained")
a=3.;b=2.;f=np.sqrt(a*a-b*b);A=np.array([-f,0.]);B=np.array([f,0.]);t=np.linspace(0,2*np.pi,800);ax.plot(a*np.cos(t),b*np.sin(t),color="#344f65",lw=2.5)
for tt,col in zip([.35,.7,1.1,1.55,2.,2.5,2.85],plt.cm.viridis(np.linspace(.08,.9,7))):
 P=np.array([a*np.cos(tt),b*np.sin(tt)]);ax.plot([A[0],P[0],B[0]],[0,P[1],0],color=col,lw=1.4,alpha=.85)
 mid=(P+B)/2;d=(B-P)/np.linalg.norm(B-P);ax.annotate("",xy=mid+.12*d,xytext=mid-.12*d,arrowprops={"arrowstyle":"-|>","color":col,"lw":1.4})
ax.plot([-f,f],[0,0],"o",color="#b34e3e",ms=7);ax.text(-f,-.33,"A",ha="center",fontsize=14);ax.text(f,-.33,"B",ha="center",fontsize=14)
ax.text(0,-1.1,"Every reflected route: AP + PB = 2a = 6\nHomogeneous-speed travel time: 6 / cₛ",ha="center",fontsize=12)
ax.set(xlabel="x",ylabel="y",xlim=(-3.3,3.3),ylim=(-2.25,2.35),aspect="equal",title="An ellipse reflects rays from one focus toward the other");ax.grid(alpha=.1)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
