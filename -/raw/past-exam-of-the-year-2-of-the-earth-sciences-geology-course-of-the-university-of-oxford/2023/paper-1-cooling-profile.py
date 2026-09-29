"""Dirichlet cooling followed by insulated equilibration, all variables dimensionless."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x=np.linspace(0,1,701)
n=np.arange(1,402,2)
fig,ax=plt.subplots(1,2,figsize=(8.5,4.1),layout="constrained")
for tau in [.01,.04,.10]:
 values=np.sum((4/(np.pi*n)*np.exp(-np.pi**2*n*n*tau))[:,None]*np.sin(np.pi*n[:,None]*x),axis=0)
 ax[0].plot(x,values,label=fr"$\kappa t/L^2={tau:.2f}$")
ax[0].set(xlabel=r"$x/L$",ylabel=r"$T/T_0$",title="10(c): cooling in the bath",ylim=(0,1.04))
ax[0].legend(fontsize=8)
tau=np.linspace(0,.4,501)
mean=np.sum((8/(np.pi**2*n*n))[:,None]*np.exp(-np.pi**2*n[:,None]**2*tau),axis=0)
ax[1].plot(tau,mean,color="#276792")
ax[1].set(xlabel=r"Bath time $\kappa t_f/L^2$",ylabel=r"Final insulated $T_f/T_0$",title="10(e): remaining mean temperature",ylim=(0,1.04))
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=100,facecolor="white",transparent=False)
