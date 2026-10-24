"""Generate PNG in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(9,4),facecolor="white",layout="constrained")
ax=axs[0]
ax.axhspan(0,2.4,color="#eef5fa")
ax.plot([-2.5,-1],[0,0],color="#197c4d",lw=4)
ax.plot([-1,1],[.02,.02],color="#b23c41",lw=4,zorder=4)
ax.plot([1,2.5],[0,0],color="#197c4d",lw=4)
for t,label in[(-1,"$-1$"),(0,"$0$"),(1,"$1$")]:
 ax.scatter([t],[0],color="black",s=20,zorder=5);ax.text(t,-.17,label,ha="center")
ax.text(0,1.3,r"$U=\pi^{-1}\arg\frac{Z-1}{Z+1}$",ha="center",fontsize=13)
ax.text(0,.3,"Value 1",ha="center",color="#b23c41")
ax.text(-1.9,.3,"Value 0",ha="center",color="#197c4d")
ax.text(1.9,.3,"Value 0",ha="center",color="#197c4d")
ax.set(xlim=(-2.6,2.6),ylim=(-.4,2.4),xlabel="$X$",ylabel="$Y$",title="Upper half-plane")
ax=axs[1]
x=np.linspace(.015,3,450);y=np.linspace(-2,2,500)
xx,yy=np.meshgrid(x,y);z=xx+1j*yy
Z=np.sqrt(1-1/z**2);Z=np.where(Z.imag<0,-Z,Z)
u=np.angle((Z-1)/(Z+1))/np.pi
im=ax.pcolormesh(xx,yy,u,shading="auto",vmin=0,vmax=1,cmap="Blues")
ax.plot([0,0],[-2,2],color="#197c4d",lw=4)
ax.plot([1,3],[0,0],color="#b23c41",lw=3)
ax.scatter([1],[0],color="#b23c41",s=25,zorder=5)
ax.text(1,-.23,"Slit tip",ha="center",fontsize=10)
ax.text(1.15,.17,"Value 1 on both banks",fontsize=9)
ax.set(xlim=(-.05,3),ylim=(-2,2),xlabel="$x$",ylabel="$y$",title=r"$z=(1-Z^2)^{-1/2}$")
fig.colorbar(im,ax=ax,label="Bounded harmonic solution $u$",shrink=.85)
fig.savefig("2007-slit-domain-map.png",dpi=160,facecolor="white")
