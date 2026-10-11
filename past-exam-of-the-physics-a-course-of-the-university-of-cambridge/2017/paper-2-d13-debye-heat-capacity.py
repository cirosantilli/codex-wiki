"""Original solution figure; tested with Python 3.14.4.
Dependencies: NumPy 2.3.5 and Matplotlib 3.10.7 (root pyproject.toml).
Writes its PNG basename into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
g,w=np.polynomial.legendre.leggauss(180)
def cv(t):
 upper=min(1/t,70);x=(g+1)*upper/2
 f=x**4*np.exp(-x)/(-np.expm1(-x))**2
 return 3*t**3*np.dot(w*upper/2,f)
t=np.geomspace(.001,2.5,650);val=np.array([cv(z) for z in t])
fig,ax=plt.subplots(1,2,figsize=(9,3.6),layout="constrained")
ax[0].plot(t,val,color="#1565a8",lw=1.8)
ax[0].axhline(1,color=".5",ls="--",lw=1)
ax[0].set(xlim=(0,2.5),ylim=(0,1.08),xlabel=r"$T/\Theta_D$",ylabel=r"$C_V/(3Nk_B)$",title="Approach to the Dulong–Petit limit")
mask=t<.2
ax[1].loglog(t[mask],val[mask],color="#1565a8",lw=1.8,label="Debye integral")
ax[1].loglog(t[mask],4*np.pi**4/5*t[mask]**3,color="#ca6720",ls="--",lw=1.5,label=r"low-temperature $T^3$ law")
ax[1].set(xlabel=r"$T/\Theta_D$",ylabel=r"$C_V/(3Nk_B)$",title="Low-temperature cubic behaviour")
ax[1].legend(frameon=False,fontsize=9)
for a in ax:a.grid(alpha=.15)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135)
