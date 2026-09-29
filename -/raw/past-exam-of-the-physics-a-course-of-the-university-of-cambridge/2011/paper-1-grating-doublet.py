"""Original pedagogical figure; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from the destination directory: output is the script's basename PNG in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})
fig,axs=plt.subplots(2,1,figsize=(8.3,5.3),sharex=True,sharey=True,layout='constrained')
x=np.linspace(458.9,460.6,9000)
for ax,N in zip(axs,[1000,300]):
 total=np.zeros_like(x)
 for lam in [459.5,460.]:
  # m=3 and p*sin(theta)=3*x; reduce the phase by its integer order.
  z=3*x/lam-3;profile=(np.sinc(N*z)/np.sinc(z))**2;total+=profile
  ax.plot(x,profile,'--',lw=1,alpha=.8,label=f'{lam:.1f} nm')
 ax.plot(x,total,c='#176493',lw=1.7,label='Incoherent sum')
 ax.set(ylabel='Intensity / one-line peak',ylim=(0,1.25),title=f'{N*5/1000:.1f} mm beam: N={N}, Rayleigh scale ≈ {460/(3*N):.3f} nm')
 ax.axvline(459.75,c='0.8',ls=':',lw=.7)
axs[0].legend(fontsize=8,loc='upper right');axs[-1].set_xlabel(r'Equivalent wavelength $p\sin\theta/3$ (nm)')
fig.savefig("paper-1-grating-doublet.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
