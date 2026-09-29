"""Original chosen charge models, not experimental data or a copied figure.

Tested with Python 3.14, NumPy 2.3, SciPy 1.16 and Matplotlib 3.10.
Run in the mirrored _media directory; the white PNG is saved to cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson

# A chosen illustrative heavy-nucleus scale; neither model is a fit to a named isotope.
R, a = 6.5, 0.5
r = np.linspace(0, 20, 6001)
rho = 1/(1+np.exp((r-R)/a))
norm = simpson(r*r*rho,x=r)
x = np.linspace(0, 12, 900)
Fdiff = np.array([simpson(r*r*rho*np.sinc(qR*r/R/np.pi),x=r)/norm for qR in x])
Fsharp = np.ones_like(x)
Fsharp[1:] = 3*(np.sin(x[1:])-x[1:]*np.cos(x[1:]))/x[1:]**3
fig, axes = plt.subplots(1,2,figsize=(9.2,3.7),facecolor="white")
colors=["#27547b","#b64c27"]
axes[0].plot(r/R,(r<=R).astype(float),label="Sharp sphere",color=colors[0],lw=2)
axes[0].plot(r/R,rho,label="Diffuse surface",color=colors[1],lw=2)
axes[0].set(xlim=(0,1.55),ylim=(-.04,1.1),xlabel=r"Radius $r/R$",ylabel=r"Relative charge density $\rho/\rho_0$",title="Chosen density profiles")
axes[0].legend(frameon=False,fontsize=9)
axes[1].semilogy(x,np.maximum(Fsharp**2,1e-10),color=colors[0],lw=1.8,label="Sharp sphere")
axes[1].semilogy(x,np.maximum(Fdiff**2,1e-10),color=colors[1],lw=1.8,label="Diffuse surface")
axes[1].set(xlim=(0,12),ylim=(1e-7,1.2),xlabel=r"Momentum transfer $qR$",ylabel=r"Form-factor intensity $|F(q)|^2$",title="Shape information in diffraction")
for ax in axes:
    ax.set_facecolor("white")
    ax.spines[["top","right"]].set_visible(False)
    ax.grid(alpha=.17)
fig.text(.5,.02,r"Illustrative models: $R=c=6.5\,$fm, diffuse surface $a=0.5\,$fm; each form factor has $F(0)=1$.",ha="center",fontsize=9)
fig.tight_layout(rect=(0,.065,1,1),w_pad=2.0)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=145,facecolor="white")
plt.close(fig)
