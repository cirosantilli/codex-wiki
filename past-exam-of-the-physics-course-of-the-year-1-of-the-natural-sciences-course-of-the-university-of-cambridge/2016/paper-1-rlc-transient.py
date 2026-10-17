"""Original explanatory figure. Python 3.14; root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white"})

L=1.;C=5e-6;R=50.;V0=6.;gamma=R/(2*L);wd=np.sqrt(1/(L*C)-gamma**2);T=2*np.pi/wd
t=np.linspace(0,3*T,1200);q=C*V0*np.exp(-gamma*t)*(np.cos(wd*t)+gamma/wd*np.sin(wd*t));I=-V0/(L*wd)*np.exp(-gamma*t)*np.sin(wd*t)
Ec=q*q/(2*C);El=L*I*I/2
fig,axs=plt.subplots(3,1,figsize=(7.5,7),sharex=True,layout="constrained")
axs[0].plot(t*1000,q/C,color="#1565c0");axs[0].set(ylabel="Capacitor voltage (V)",title="Free RLC discharge: three damped periods")
axs[1].plot(t*1000,I*1000,color="#d84315");axs[1].set_ylabel("Printed-arrow current (mA)");axs[1].annotate("Initial discharge is negative",xy=(2,I[np.argmin(abs(t-.002))]*1000),xytext=(10,-9),arrowprops={"arrowstyle":"->","color":"#555"},fontsize=9)
axs[2].plot(t*1000,Ec*1e6,label="Capacitor",color="#1565c0");axs[2].plot(t*1000,El*1e6,label="Inductor",color="#d84315");axs[2].plot(t*1000,(Ec+El)*1e6,label="Total",color="#222",lw=2)
axs[2].set(xlabel="Time (ms)",ylabel=r"Stored energy ($\mu$J)",ylim=(0,95));axs[2].legend(ncol=3,fontsize=9)
for a in axs:
 a.axhline(0,color="#999",lw=.7);a.grid(alpha=.18)
 for n in [1,2,3]:a.axvline(n*T*1000,color="#bbb",ls=":",lw=.8)

fig.savefig(Path(__file__).stem + ".png", dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
