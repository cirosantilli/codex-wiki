"""Original explanatory figure. Render with the repository Makefile into mirrored _media."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(10,3.7),layout="constrained")
ax=axs[0]
ax.axis("off")
for y,label in [(.78,"Virtual double occupancy"),(.20,"One boson per site")]:
    ax.text(.5,y+.12,label,ha="center",transform=ax.transAxes)
    ax.plot([.15,.85],[y,y],color="#999999",transform=ax.transAxes)
ax.text(.5,.82,r"$\Delta=\pm2,\quad E=U$",ha="center",transform=ax.transAxes)
ax.text(.5,.08,r"$\Delta=0,\quad E=0$",ha="center",transform=ax.transAxes)
for x,dx in [(.27,.13),(.73,-.13)]:
    ax.annotate("",xy=(x+dx,.76),xytext=(x,.23),xycoords="axes fraction",arrowprops={"arrowstyle":"<->","color":"#0072b2","lw":1.8})
ax.text(.5,.48,r"Virtual hopping $t$",ha="center",transform=ax.transAxes)
ax.text(.5,-.04,r"Illustrative charging energy: $E(\Delta)=U\Delta^2/4$, $U>0$",ha="center",transform=ax.transAxes,fontsize=9)
x=np.linspace(0,.25,401)
axs[1].plot(x,.5*(1-np.sqrt(1+16*x*x)),color="#0072b2",label="Exact triplet ground shift")
axs[1].plot(x,-4*x*x,"--",color="#d55e00",label=r"Second order: $-4t^2/U$")
axs[1].axhline(0,color="#009e73",label="Singlet: zero shift")
axs[1].set(xlabel=r"$t/U$",ylabel=r"Energy shift / $U$",title="Bosonic spin-sector shifts")
axs[1].legend(loc="lower left",fontsize=9)
finish(fig,"paper-1-bosonic-exchange")
