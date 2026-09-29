"""Original plots; Python 3.14, numpy/matplotlib. Writes one PNG in the current working directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False,metadata={"Software":"Matplotlib"})
    plt.close(fig)

t=np.linspace(0,24,1600);omega=1.6;D=1/(omega*omega-1)
x=D*(np.cos(t)-np.cos(omega*t));y=D*(np.sin(t)-np.sin(omega*t)/omega)
xr=.5*t*np.sin(t);yr=.5*(np.sin(t)-t*np.cos(t))
fig,axs=plt.subplots(1,3,figsize=(12,3.9),layout="constrained")
axs[0].plot(t,x,color="#165b91",lw=1.6,label="x / R");axs[0].plot(t,y,color="#bf5a13",lw=1.6,label="y / R")
axs[0].set(xlabel="Ride angle (Omega t)",ylabel="Relative position / R",title="Off resonance: omega / Omega = 1.6");axs[0].legend(fontsize=9)
axs[1].plot(x,y,color="#165b91",lw=1.2);axs[1].plot(0,0,"o",color="black",ms=4)
axs[1].set(xlabel="x / R",ylabel="y / R",title="Bounded relative trajectory",aspect="equal")
axs[2].plot(t,np.sqrt(xr*xr+yr*yr),color="#488523",lw=1.6,label="exact relative distance")
axs[2].plot(t,.5*t,"k--",alpha=.6,label="secular scale: Omega t / 2")
axs[2].set(xlabel="Ride angle (Omega t)",ylabel="Distance from cup center / R",title="Resonance: omega = Omega");axs[2].legend(fontsize=8)
for ax in axs:ax.grid(alpha=.2)
fig.suptitle("Initially centered marble at rest; cup axes remain parallel to inertial axes",fontsize=13)
save(fig)
