"""Original 2012 Oxford Short Options figure; Python 3.14, NumPy and Matplotlib root dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

x=np.linspace(0,12,5000);form=np.ones_like(x);form[1:]=3*(np.sin(x[1:])-x[1:]*np.cos(x[1:]))/x[1:]**3
roots=[]
for n in [1,2,3]:
    lo=n*np.pi;hi=(n+.5)*np.pi
    for _ in range(70):
        mid=(lo+hi)/2
        if np.tan(mid)-mid>0:hi=mid
        else:lo=mid
    roots.append((lo+hi)/2)
fig,ax=plt.subplots(figsize=(8.8,4.4),layout="constrained")
ax.plot(x,form,color="#146b9c",lw=2.2,label=r"$f(q)/f(0)=3(\sin x-x\cos x)/x^3$")
ax.axhline(0,color=".6",lw=.8)
for j,r in enumerate(roots):
    ax.plot(r,0,"o",color="#d76c20",ms=6,label="Exact zeros" if j==0 else None)
    ax.axvline((j+1.5)*np.pi,color=".65",ls=":",lw=1,label=r"Approximate $(n+1/2)\pi$" if j==0 else None)
    ax.text(r,-.135,f"{r:.3f}",ha="center",fontsize=10)
ax.set(xlim=(0,12),ylim=(-.17,1.07),xlabel=r"$x=qr_0=2kr_0\sin(\theta/2)$",ylabel="Normalized scattering amplitude",title="Spherical step potential: finite forward amplitude and diffraction zeros")
ax.legend(loc="upper right");ax.grid(alpha=.17)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white",metadata={"Software":"Original Oxford Short Options figure"})
plt.close(fig)
