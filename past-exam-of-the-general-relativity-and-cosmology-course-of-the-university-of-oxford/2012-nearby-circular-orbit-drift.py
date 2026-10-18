from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

fig,(ax,bx)=plt.subplots(1,2,figsize=(10.2,4.8),layout="constrained")
v=np.linspace(-1,1,7);X,Y=np.meshgrid(v,v);ax.quiver(X,Y,2*X,-Y,color="#2a718f",angles="xy",scale_units="xy",scale=6,width=.007);ax.plot(0,0,"o",ms=5,color="#b74f42")
ax.axhline(0,color="gray",lw=.6);ax.axvline(0,color="gray",lw=.6);ax.set(xlabel="Radial separation",ylabel="Transverse separation",xlim=(-1.5,1.5),ylim=(-1.3,1.3),aspect="equal",title="Physical tidal acceleration: stretch / compress")
ax.text(0,-1.17,r"$a_{\rm rel}\propto(2\Delta_r,-\Delta_\perp)$",ha="center",fontsize=12)
t=np.linspace(0,8,500);dr=.001;R2=1+dr;dom=R2**(-1.5)-1;sep=np.sqrt(dr*dr+4*R2*np.sin(dom*t/2)**2)/dr;early=np.sqrt(1+(1.5*t)**2)
bx.plot(t,sep,lw=2.6,color="#2a718f",label="Two exact Newtonian circles");bx.plot(t,early,lw=1.8,ls="--",color="#b56a31",label="Early differential-drift estimate")
bx.set(xlabel=r"$\Omega t$",ylabel=r"$|\Delta|/|\delta R|$",xlim=(0,8),ylim=(0,13),title="Different radii produce along-track drift");bx.grid(alpha=.15);bx.legend(fontsize=9,loc="upper left")
fig.suptitle("Local weak-field model; orbit-radius difference shown is illustrative",fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
