"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,3.6),layout='constrained')
t=np.linspace(.005,2.2,450);heat=[]
for z in t:
 x=np.linspace(1e-8,min(1/z,80),2200);integrand=x**4*np.exp(-x)/(-np.expm1(-x))**2
 heat.append(3*z**3*np.trapezoid(integrand,x))
axs[0].plot(np.r_[0,t],np.r_[0,heat],label='Debye integral');tl=np.linspace(0,.17,100);axs[0].plot(tl,4*np.pi**4/5*tl**3,'--',label=r'Low-$T$ cubic limit');axs[0].axhline(1,color='0.5',ls=':',label='Dulong–Petit limit');axs[0].set(xlabel=r'$T/\theta_D$',ylabel=r'$C_m/(3Nk_B)$',ylim=(0,1.08),title='Lattice heat capacity');axs[0].legend(fontsize=8)
w=np.linspace(0,5,500);axs[1].plot(w,1/(1+w*w));axs[1].plot(1,.5,'o');axs[1].axhline(.5,color='0.6',ls=':');axs[1].axvline(1,color='0.6',ls=':');axs[1].set(xlabel=r'$\omega\tau$',ylabel=r'$|\sigma(\omega)|^2/\sigma_0^2$',ylim=(0,1.08),title=r'Drude half-maximum at $\omega\tau=1$')
for a in axs:a.grid(alpha=.15)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
