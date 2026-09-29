"""Original illustrative figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the corresponding _media directory; the PNG is written to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

x=np.linspace(0,3,2300);eps=1+4/(1-x*x-.15j*x);N=np.sqrt(eps);R=np.abs((N-1)/(N+1))**2;alpha=2*x*N.imag
fig,(ax,bx)=plt.subplots(1,2,figsize=(9,3.8),layout="constrained")
ax.plot(x,eps.real,label=r"$\mathrm{Re}\,\epsilon_r$",color="#2563eb");ax.plot(x,eps.imag,label=r"$\mathrm{Im}\,\epsilon_r$",color="#dc2626");ax.axhline(1,color="black",lw=.6);ax.set(xlabel=r"$\omega/\omega_0$",ylabel="Relative permittivity",ylim=(-14,30));ax.legend()
l1=bx.plot(x,R,color="#2563eb",label="Reflectance R");cx=bx.twinx();l2=cx.plot(x,alpha,color="#dc2626",ls="--",label=r"Attenuation $\alpha c/\omega_0$");bx.set(xlabel=r"$\omega/\omega_0$",ylabel="Power reflectance",ylim=(0,1));cx.set_ylabel(r"$\alpha c/\omega_0$");bx.legend(l1+l2,[l.get_label() for l in l1+l2],fontsize=8)
for a in (ax,bx):a.axvline(1,color="#888",ls=":",lw=.8);a.grid(alpha=.15)
fig.suptitle(r"Illustrative bound electrons: $\omega_p/\omega_0=2$, $\gamma/\omega_0=0.15$")

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
