from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "savefig.facecolor": "white"})
fig,axs=plt.subplots(1,2,figsize=(10,4.4),layout="constrained")
delta0=1;Delta=.13;t=np.linspace(0,10*np.pi,2200);env=np.exp(-Delta**2*t*t/2)
x=-env*np.sin(t);y=-env*np.cos(t)
ax=axs[0];a=np.linspace(0,2*np.pi,400);ax.plot(np.cos(a),np.sin(a),color="0.7",lw=1)
ax.plot(x,y,color="#175c9e",lw=1.8)
for tt in [1,6,12,18]:
 i=np.searchsorted(t,tt);ax.annotate("",(x[i+8],y[i+8]),(x[i-8],y[i-8]),arrowprops={"arrowstyle":"->","color":"#175c9e"})
ax.plot(0,-1,"o",color="#bd492e");ax.text(.05,-.95,"T = 0",fontsize=10)
ax.axhline(0,color="0.8",lw=.6);ax.axvline(0,color="0.8",lw=.6)
ax.set(xlabel=r"$\langle r_x\rangle$",ylabel=r"$\langle r_y\rangle$",title="Free evolution: equatorial spiral",xlim=(-1.1,1.1),ylim=(-1.1,1.1));ax.set_aspect("equal")
ax=axs[1];periods=t/(2*np.pi);p=(1-env*np.cos(t))/2
ax.plot(periods,p,color="#175c9e",lw=1.7,label="Return population")
ax.plot(periods,(1+env)/2,"--",color="#bd492e",lw=1,label="Gaussian envelopes")
ax.plot(periods,(1-env)/2,"--",color="#bd492e",lw=1)
ax.axhline(.5,color="0.6",ls=":",lw=1);ax.set(xlabel=r"$\delta_0 T/(2\pi)$",ylabel=r"$\overline{\rho}_{11}$",title=r"Identical pulses, $\Delta=0.13\delta_0$",ylim=(-.03,1.03),xlim=(0,5))
ax.legend(loc="upper right",fontsize=9)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
