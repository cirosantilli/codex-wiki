"""Generate PNG in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
phi=(1+np.sqrt(5))/2
fig,axs=plt.subplots(1,3,figsize=(11,3.6),facecolor="white",layout="constrained")
a=np.linspace(0,np.pi,1000)
nom=np.ones_like(a);cau=1/np.sqrt(np.cos(a)**2+(np.sin(a)-np.cos(a))**2)
axs[0].plot(a*180/np.pi,nom,label=r"$|T_RN|/\mu$",color="#197c4d",lw=2)
axs[0].plot(a*180/np.pi,cau,label=r"$|Tn|/\mu$",color="#12679b",lw=2)
astar=np.arctan(phi);axs[0].scatter([astar*180/np.pi],[phi],color="#b23c41",zorder=5)
axs[0].set(xlabel=r"Reference normal angle $\alpha$ (degrees)",ylabel="Traction magnitude",title="Different area measures",xlim=(0,180))
axs[0].grid(alpha=.2);axs[0].legend(frameon=False,fontsize=9)
N=np.array([1,phi]);N=N/np.linalg.norm(N)
F=np.array([[1,1],[0,1]],float);t=np.array([-N[1],N[0]])
n=np.linalg.solve(F.T,N);n=n/np.linalg.norm(n)
for ax,tan,normal,title in[(axs[1],t,N,"Reference plane"),(axs[2],F@t,n,"Deformed plane")]:
 tan=tan/np.linalg.norm(tan)
 ax.plot([-1.3*tan[0],1.3*tan[0]],[-1.3*tan[1],1.3*tan[1]],color="#12679b",lw=2.5)
 ax.annotate("",xy=normal,xytext=(0,0),arrowprops=dict(arrowstyle="->",color="#b23c41",lw=2))
 ax.set(aspect="equal",xlim=(-1.5,1.5),ylim=(-1.4,1.5),xlabel="$x_1$"if ax is axs[1]else"$y_1$",ylabel="$x_2$"if ax is axs[1]else"$y_2$",title=title)
 ax.axhline(0,color="0.8",lw=.7);ax.axvline(0,color="0.8",lw=.7)
axs[1].text(-1.35,1.22,r"$N\parallel(1,\varphi)$",fontsize=11)
axs[2].text(-1.35,1.22,r"$n\parallel(\varphi,1)$",fontsize=11)
fig.savefig("2007-shear-tractions.png",dpi=160,facecolor="white")
