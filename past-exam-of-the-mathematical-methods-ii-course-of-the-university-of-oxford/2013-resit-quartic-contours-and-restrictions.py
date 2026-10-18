from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

fig,(ax,bx)=plt.subplots(1,2,figsize=(10.4,5.2),layout="constrained")
x=np.linspace(-5,5,601);X,Y=np.meshgrid(x,x);Z=X**4+Y**4-16*X*Y
levels=[-30,-20,-8,0,16,64,160,400,800];cs=ax.contour(X,Y,Z,levels=levels,cmap="viridis",linewidths=1.3);ax.clabel(cs,fontsize=9,fmt="%d")
ax.plot([-2,2],[-2,2],"o",color="#b94d3b",ms=6);ax.plot(0,0,"x",color="#b94d3b",ms=8,mew=2);ax.axhline(0,color="gray",lw=.6,ls=":");ax.plot(x,x,color="gray",lw=.6,ls=":")
ax.set(xlabel="x",ylabel="y",xlim=(-5,5),ylim=(-5,5),aspect="equal",title=r"Contours of $x^4+y^4-16xy$")
u=np.linspace(-3,3,600);bx.plot(u,u**4,lw=2.5,color="#286c98",label="Restriction y = 0");bx.plot(u,2*u**4-16*u*u,lw=2.5,color="#9861a1",label="Restriction y = x")
bx.plot(0,0,"o",color="#286c98");bx.plot([-2,2],[-32,-32],"o",color="#9861a1");bx.axhline(0,color="gray",lw=.7);bx.annotate("Origin: minimum along y = 0,\nmaximum along y = x",xy=(0,0),xytext=(-2.75,75),arrowprops={"arrowstyle":"->"},fontsize=11)
bx.set(xlabel="x along the chosen line",ylabel="Restricted function value",xlim=(-3,3),ylim=(-40,105),title="One-dimensional turning points");bx.grid(alpha=.15);bx.legend(loc="upper right",fontsize=10)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
