from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

x=np.linspace(0,1,450);initial=np.sin(np.pi*x)-np.sin(3*np.pi*x)/3
fig,axs=plt.subplots(2,3,figsize=(10.2,5.6),layout="constrained",sharex=True,sharey=True)
for ax,tau in zip(axs.flat,[0,.25,.5,.75,1,2]):
 y=np.sin(np.pi*x)*np.cos(np.pi*tau)-np.sin(3*np.pi*x)*np.cos(3*np.pi*tau)/3
 ax.plot(x,initial,color="#aaaaaa",ls="--",lw=1,label="Initial profile");ax.plot(x,y,color="#775394",lw=2.5,label="Current profile");ax.axhline(0,color="#777777",lw=.6)
 ax.set(title=f"t = {tau:g} L/c",xlim=(0,1),ylim=(-1.5,1.5));ax.grid(alpha=.12)
for ax in axs[1]:ax.set_xlabel("x/L")
for ax in axs[:,0]:ax.set_ylabel("Displacement")
axs[0,0].legend(fontsize=9,loc="lower center")
fig.suptitle("Two string harmonics: half-period sign reversal and full-period recurrence",fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
