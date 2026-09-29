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

fig,axs=plt.subplots(1,3,figsize=(11,3.3),layout="constrained")
t=np.linspace(0,5,400);x=np.geomspace(.01,100,500)
axs[0].plot(t,1-np.exp(-t),color="#0072b2")
axs[0].set(xlabel=r"$t/\tau$",ylabel=r"$E\varepsilon/\sigma_0$",title="Step-stress creep")
axs[1].plot(x,1/np.sqrt(1+x*x),color="#d55e00")
axs[1].set(xscale="log",xlabel=r"$\omega\tau$",ylabel=r"$E|\varepsilon|/\sigma_0$",title="Harmonic stress response")
axs[2].plot(x,np.rad2deg(np.arctan(x)),color="#009e73")
axs[2].set(xscale="log",xlabel=r"$\omega\tau$",ylabel="Strain lag (degrees)",title="Elastic to viscous limit",ylim=(0,90))
finish(fig,"paper-1-voigt-response")
