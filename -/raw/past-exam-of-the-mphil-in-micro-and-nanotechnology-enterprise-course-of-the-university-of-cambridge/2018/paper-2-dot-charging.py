"""Original dot geometry and ideal classical charging calculations."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,axs=plt.subplots(2,2,figsize=(11,8),layout="constrained")
ax=axs[0,0];ax.set(xlim=(-3,3),ylim=(-2,2.5),title="A  Surface-gate dot in a buried 2DEG")
ax.add_patch(Rectangle((-2.7,-1.7),5.4,3.7,facecolor="#dce3ed"))
for x,y,w,h in [(-1.7,.6,3.4,.45),(-1.7,-1.05,3.4,.45)]:
 ax.add_patch(Rectangle((x,y),w,h,color="#6c7888"))
ax.add_patch(Rectangle((-.7,-.45),1.4,.9,facecolor="white",ec="k"));ax.text(0,0,"island",ha="center")
for x in [-1.05,1.05]:ax.add_patch(Rectangle((x-.1,-.45),.2,.9,color="#bca58a"))
ax.text(-2.2,0,"source",ha="center",fontsize=9);ax.text(2.2,0,"drain",ha="center",fontsize=9)
ax.text(0,1.3,"depletion gates / plunger control",ha="center");ax.text(0,-1.5,"GaAs/AlGaAs; contacts to reservoirs",ha="center",fontsize=9);ax.axis("off")
ax=axs[0,1];q=np.linspace(-.4,3.4,900);energies=[]
for N in range(4):
 u=.5*(N-q)**2;energies.append(u);ax.plot(q,u,lw=1,label=f"N={N}")
ax.plot(q,np.min(energies,axis=0),"k",lw=2,label="equilibrium envelope")
ax.set(xlabel=r"$q=Q_{\rm ext}/e$",ylabel=r"$U/(e^2/C)$",ylim=(0,1.6),title="B  Charging parabolas");ax.legend(fontsize=8,ncol=2)
ax=axs[1,0];N=np.floor(q+.5);ax.step(q,-N,where="post",label="electron charge / e")
ax.plot(q,q-N,label="residual net charge / e")
ax.set(xlabel=r"$Q_{\rm ext}/e$",ylabel="charge / e",title="C  Two different charge conventions");ax.legend(fontsize=9)
ax=axs[1,1];Q,V=np.meshgrid(np.linspace(-.5,3.5,600),np.linspace(-1.5,1.5,500))
nearest=np.floor(Q+.5);boundary=1-2*np.abs(Q-nearest)
allowed=np.abs(V)>=boundary
ax.pcolormesh(Q,V,allowed,cmap="Blues",shading="auto",vmin=0,vmax=1)
for n in range(4):
 for sign in [-1,1]:
  x=np.linspace(n-.5,n+.5,101);ax.plot(x,sign*(1-2*np.abs(x-n)),color="k",lw=.7)
ax.set(xlabel=r"$Q_{\rm ext}/e$",ylabel=r"$eV_{\rm SD}/(e^2/C)$",title="D  Ideal symmetric Coulomb diamonds")
ax.text(.05,.05,"white: blocked",transform=ax.transAxes,bbox={"fc":"white","ec":"none"})
fig.savefig("paper-2-dot-charging.png",dpi=150,facecolor="white")

