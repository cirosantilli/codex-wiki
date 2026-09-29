"""Original slit/array Fourier analysis and demonstration layout."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Ellipse
fig,axs=plt.subplots(2,2,figsize=(10,7),layout="constrained")
ax=axs[0,0];v=np.linspace(-4,4,1600)
ax.plot(v,np.sinc(v)**2,color="#245d84",lw=2)
ax.set(xlabel=r"$a\sin\theta/\lambda$",ylabel=r"$I/I(0)$",title="Single slit: sinc-squared")
for n in [-1,1]:ax.plot(n,0,"o",color="#b2602c")
ax=axs[0,1]
for j in range(8):
    ax.add_patch(Rectangle((j-1/6,0),1/3,1,facecolor="#83b0cc",edgecolor="#245d84"))
ax.set(xlim=(-.7,7.7),ylim=(0,1.5),xlabel=r"$x/b$",ylabel="Aperture transmission",title=r"$\mathrm{rect}_a * \sum_j\delta(x-jb)$; $b/a=3$")
ax.text(3.5,1.2,"8 equal slits; spacing b; width a",ha="center",fontsize=9)
ax=axs[1,0];u=np.linspace(-4,4,4000)
array=np.abs(np.exp(-2j*np.pi*u[:,None]*np.arange(8)).mean(axis=1))**2
env=np.sinc(u/3)**2
ax.plot(u,env*array,color="#245d84",label="Finite grating")
ax.plot(u,env,"--",color="#b2602c",label="Slit envelope")
ax.set(xlabel=r"$b\sin\theta/\lambda$",ylabel=r"$I/(N^2 I_{\rm one}(0))$",title="Narrow orders inside broad envelope")
ax.annotate("Missing order m = 3",xy=(3,0),xytext=(.8,.35),arrowprops=dict(arrowstyle="->"),fontsize=9)
ax.legend(fontsize=8)
ax=axs[1,1];ax.set(xlim=(-.5,9),ylim=(-1.6,1.6));ax.axis("off")
ax.add_patch(Rectangle((0,-.28),1,.56,facecolor="#e8e8e8",edgecolor=".3"))
ax.text(.5,0,"Laser",ha="center",va="center",fontsize=9)
for y in [-.23,0,.23]:
    ax.annotate("",(2,y),(1,y),arrowprops=dict(arrowstyle="->",color="#245d84"))
ax.plot([2,2],[-1,-.1],color=".2",lw=3);ax.plot([2,2],[.1,1],color=".2",lw=3)
ax.add_patch(Ellipse((5,0),.2,2,facecolor="#dcebf5",edgecolor="#245d84"))
ax.plot([8,8],[-1.1,1.1],color=".2",lw=3)
for y0 in [-.06,.06]:ax.plot([2,5,8],[y0,y0+.45,.45],color="#b2602c",lw=1)
ax.plot(8,.45,"o",color="#b2602c",ms=4)
ax.text(8.1,.62,r"$x=f\theta$",fontsize=9)
ax.text(2,-1.3,"Slit",ha="center");ax.text(5,-1.3,"Lens",ha="center")
ax.text(8,-1.3,"Screen",ha="center")
ax.annotate("",(5,1.2),(8,1.2),arrowprops=dict(arrowstyle="<->"))
ax.text(6.5,1.32,"focal length f",ha="center",fontsize=9)
ax.set_title("Collimated illumination; screen at back focal plane")
for a in [axs[0,0],axs[1,0]]:a.grid(alpha=.15)
fig.savefig("paper-2-grating-fourier.png",dpi=150,facecolor="white")
