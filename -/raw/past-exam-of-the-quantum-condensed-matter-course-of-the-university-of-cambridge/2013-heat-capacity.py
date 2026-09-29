"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,3.6),layout='constrained');t=np.linspace(.006,2,400);cv=[]
for u in t:
 x=np.linspace(1e-8,min(1/u,80),2000);cv.append(3*u**3*np.trapezoid(x**4*np.exp(-x)/(-np.expm1(-x))**2,x))
axs[0].plot(np.r_[0,t],np.r_[0,cv]);axs[0].axhline(1,color='0.6',ls=':',label='Classical lattice limit');axs[0].set(xlabel=r'$T/\theta_D$',ylabel=r'$C_{ph}/(3Nk_B)$',ylim=(0,1.08),title='Lattice heat capacity in either type of solid');axs[0].legend(fontsize=8)
x=np.linspace(0,9,200);axs[1].plot(x,.006*x,label='Insulator: lattice term');axs[1].plot(x,.05+.006*x,label='Normal metal: electronic + lattice');axs[1].plot(0,.05,'o');axs[1].annotate(r'Electronic intercept $\gamma$',(0,.05),(2,.032),fontsize=9,arrowprops=dict(arrowstyle='->'));axs[1].set(xlabel=r'$T^2$ (model units)',ylabel=r'$C/T$ (model units)',title='Illustrative low-temperature intercept test');axs[1].legend(fontsize=8)
for a in axs:a.grid(alpha=.15)
fig.suptitle('Original curves; the right-panel coefficients are illustrative, not measured material data')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
