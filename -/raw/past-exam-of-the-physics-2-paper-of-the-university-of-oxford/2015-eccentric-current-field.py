from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

from matplotlib.patches import Circle
fig,ax=plt.subplots(figsize=(9,6),layout="constrained")
x=np.linspace(-4.2,4.2,165);y=np.linspace(-3.3,3.3,135);X,Y=np.meshgrid(x,y);r2=X*X+Y*Y;d2=(X-1)**2+Y*Y
with np.errstate(divide="ignore",invalid="ignore"):
 U=(-4*Y/r2+Y/d2)/3;V=(4*X/r2-(X-1)/d2)/3
mask=r2<4.025
U=np.ma.array(U,mask=mask);V=np.ma.array(V,mask=mask)
speed=np.sqrt(U*U+V*V)
s=ax.streamplot(x,y,U,V,density=1.5,color=speed,cmap="viridis",linewidth=1.15,arrowsize=1.1)
ax.add_patch(Circle((0,0),2,facecolor="#dce1e7",edgecolor="#384b5a",lw=2,zorder=4))
ax.add_patch(Circle((1,0),1,facecolor="white",edgecolor="#384b5a",lw=1.5,zorder=5))
ax.text(-.75,0,"Uniform current\nout of the page",ha="center",va="center",zorder=6,fontsize=12)
ax.text(1,0,"No\ncurrent",ha="center",va="center",zorder=6)
ax.plot(0,0,"o",color="#173f5f",zorder=6,ms=3);ax.plot(1,0,"o",color="#173f5f",zorder=6,ms=3)
ax.set(xlabel=r"$x/a$",ylabel=r"$y/a$",title="An eccentric cavity breaks the exterior field's rotational symmetry",xlim=(-4.2,4.2),ylim=(-3.3,3.3));ax.set_aspect("equal")
cb=fig.colorbar(s.lines,ax=ax,pad=.025,shrink=.85);cb.set_label(r"$|B|\,/\,[\mu_0 I/(2\pi a)]$")
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
