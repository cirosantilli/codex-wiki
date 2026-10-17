"""Original schematic/calculation. Save only a PNG basename in the working directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(10,3.5),layout="constrained")
w=np.linspace(380,780,800);Gamma=520.
for angle,c in [(45,"#0072b2"),(20,"#d55e00")]:
 intensity=np.sin(np.deg2rad(2*angle))**2*np.sin(np.pi*Gamma/w)**2
 axs[0].plot(w,intensity,color=c,label=rf"$\alpha={angle}^\circ$")
axs[0].axvline(520,color="grey",ls=":")
axs[0].set(xlabel="Wavelength (nm)",ylabel=r"$I/I_P$",title="Spectral cancellation at 520 nm")
axs[0].legend()
a=np.linspace(0,360,1000)
axs[1].plot(a,np.sin(np.deg2rad(2*a))**2,color="#009e73")
axs[1].set(xlabel="Azimuth (degrees)",ylabel=r"Brightness factor $\sin^2(2\alpha)$",title="Four extinction positions per revolution",xticks=[0,90,180,270,360])
finish(fig,"paper-1-crossed-polars")
