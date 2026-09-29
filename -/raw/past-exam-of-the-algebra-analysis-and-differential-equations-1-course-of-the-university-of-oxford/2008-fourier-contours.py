"""Python 3.14; NumPy and Matplotlib in ../pyproject.toml. Output in CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(8.4,3.7),facecolor="white")
for ax,sgn,title in zip(axs,[1,-1],[r"$\lambda>0$: close above",r"$\lambda<0$: close below"]):
 t=np.linspace(0,sgn*np.pi,500)
 z=2*np.exp(1j*t)
 ax.plot([-2,2],[0,0],color="C0",lw=2)
 ax.plot(z.real,z.imag,color="C0",lw=2)
 ax.annotate("",xy=(.45,0),xytext=(-.45,0),arrowprops=dict(arrowstyle="->",color="C0",lw=2))
 k=220
 ax.annotate("",xy=(z[k+25].real,z[k+25].imag),xytext=(z[k].real,z[k].imag),arrowprops=dict(arrowstyle="->",color="C0",lw=2))
 ax.scatter([0],[1],color="C3",s=28)
 ax.text(.09,1.05,"Pole at i",color="C3")
 ax.text(-1.1,sgn*1.1,"Exponential decays",fontsize=9)
 ax.set(xlim=(-2.35,2.35),ylim=(-2.3,2.3),title=title,xlabel="Real part",ylabel="Imaginary part")
 ax.set_aspect("equal");ax.spines[["top","right"]].set_visible(False)
fig.tight_layout();fig.savefig("2008-fourier-contours.png",dpi=150,facecolor="white")
