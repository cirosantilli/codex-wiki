"""Original Oxford CP2 2013 figure; Python 3.14, NumPy and Matplotlib root dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

z=np.linspace(0,.65,500);ratio=np.ones_like(z);ratio[1:]=np.arctanh(z[1:])/z[1:]
t=np.linspace(0,2,900);eta=.15;zz=eta*np.sin(2*np.pi*t);c=np.ones_like(t);mask=abs(zz)>1e-12;c[mask]=np.arctanh(zz[mask])/zz[mask];energy=1/c
fig,ax=plt.subplots(1,2,figsize=(9.8,4.2),layout="constrained")
ax[0].plot(z,ratio,color="#146b9c",lw=2.2,label="Local-strip integral")
ax[0].plot(z,1+z*z/3,color="#d76c20",lw=1.8,ls="--",label="Quadratic approximation")
ax[0].set(xlabel=r"$|\delta|/a$",ylabel=r"$C/C_0$",title="Tilt raises capacitance");ax[0].legend()
ax[1].plot(t,energy,color="#146b9c",lw=2.2,label=r"Fixed $Q$, $\delta_0/a=0.15$")
ax[1].plot(t,1-zz*zz/3,color="#d76c20",ls="--",lw=1.6,label="Quadratic approximation")
ax[1].set(xlabel="Mechanical cycles",ylabel=r"$U/U_0$",title="Energy oscillates twice as fast");ax[1].legend(loc="lower left",fontsize=9)
for a in ax:a.grid(alpha=.18)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white",metadata={"Software":"Original CP2 solution figure"})
plt.close(fig)
