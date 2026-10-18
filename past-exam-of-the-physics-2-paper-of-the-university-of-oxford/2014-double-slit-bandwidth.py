"""Original Oxford CP2 2014 solution figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

fig,ax=plt.subplots(2,1,figsize=(9,6),layout="constrained")
b=1e-3;D=1.;lam=532e-9
y=np.linspace(-2,2,2500)*1e-3
ax[0].plot(y*1e3,np.cos(np.pi*b*y/(lam*D))**2,color="#146b9c",lw=1.8)
ax[0].set(xlim=(-2,2),title=r"532 nm: fringe spacing 0.532 mm (no slide)",ylabel=r"$I/(4I_s)$")
y=np.linspace(-16,16,11000)*1e-3;delta=b*y/D
slo=1/(540e-9);shi=1/(520e-9);width=shi-slo;centre=(shi+slo)/2
gamma=np.sinc(width*delta)
band=.5*(1+gamma*np.cos(2*np.pi*centre*delta))
ax[1].plot(y*1e3,band,color="#146b9c",lw=.9,label="Band-averaged intensity")
ax[1].plot(y*1e3,.5*(1+abs(gamma)),color="#d76c20",ls="--",lw=1.6,label="Visibility envelopes")
ax[1].plot(y*1e3,.5*(1-abs(gamma)),color="#d76c20",ls="--",lw=1.6)
yzero=D/(b*width)*1e3
for s in [-1,1]:ax[1].axvline(s*yzero,color=".4",ls=":",lw=1)
ax[1].set(xlim=(-16,16),title="520–540 nm, uniform spectrum in inverse wavelength",ylabel=r"$I/(4I_s)$")
ax[1].legend(loc="upper right",fontsize=9)
for a in ax:a.set(xlabel="Screen position y (mm)",ylim=(-.06,1.09));a.grid(alpha=.15)
fig.suptitle("Bandwidth washout: first visibility zero near order ±26.5",fontsize=14)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, facecolor="white", metadata={"Software":"Oxford CP2 original Matplotlib figure"})
plt.close(fig)
