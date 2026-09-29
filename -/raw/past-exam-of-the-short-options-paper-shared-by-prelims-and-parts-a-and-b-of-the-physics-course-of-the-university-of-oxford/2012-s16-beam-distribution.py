"""Original 2012 Oxford Short Options figure; Python 3.14, NumPy and Matplotlib root dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

V=4.8;sb=.18;ratio=.001
v=np.linspace(-3.5,6.1,3500);fp=np.exp(-v*v/2)/np.sqrt(2*np.pi);fb=ratio*np.exp(-(v-V)**2/(2*sb*sb))/(np.sqrt(2*np.pi)*sb)
fig,ax=plt.subplots(1,2,figsize=(10,4.3),layout="constrained")
ax[0].semilogy(v,fp+fb,color="#146b9c",lw=2.1,label="Total")
ax[0].semilogy(v,fp,color=".45",lw=1.4,ls="--",label="Plasma alone")
ax[0].semilogy(v,fb,color="#d76c20",lw=1.4,ls=":",label="Beam alone")
ax[0].set(xlim=(-3.5,6.1),ylim=(1e-8,1),title="Broad plasma + narrow beam",ylabel=r"$f(v)/(n_p/\sigma_p)$")
u=np.linspace(4.05,5.4,1000);p=np.exp(-u*u/2)/np.sqrt(2*np.pi);b=ratio*np.exp(-(u-V)**2/(2*sb*sb))/(np.sqrt(2*np.pi)*sb)
ax[1].plot(u,p+b,color="#146b9c",lw=2.1,label="Total near beam")
ax[1].plot(u,p,color=".45",ls="--",lw=1.3)
ax[1].axvline(V-sb,color="#27835b",ls="--",lw=1.4,label=r"$V-\sigma_b$")
ax[1].axvline(V,color=".55",ls=":",lw=1.1,label=r"$V$")
ax[1].set(xlim=(4.05,5.4),ylim=(0,.0025),title="Maximum positive beam slope",ylabel=r"$f(v)/(n_p/\sigma_p)$")
for a in ax:a.set_xlabel(r"$v/\sigma_p$");a.grid(alpha=.15);a.legend()
fig.suptitle(r"Illustration: $V/\sigma_p=4.8$, $\sigma_b/\sigma_p=0.18$, $n_b/n_p=10^{-3}$",fontsize=13)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white",metadata={"Software":"Original Oxford Short Options figure"})
plt.close(fig)
