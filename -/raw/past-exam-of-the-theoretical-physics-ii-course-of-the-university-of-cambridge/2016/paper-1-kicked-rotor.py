"""Original explanatory figure. Render with the repository Makefile into mirrored _media."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(10,3.5),layout="constrained")
theta=np.arange(4096)*2*np.pi/4096
m=np.fft.fftfreq(len(theta),1/len(theta))
for z,color in [(2,"#0072b2"),(6,"#d55e00")]:
    coeff=np.fft.fft(np.exp(1j*z*np.cos(theta)))/len(theta)
    order=np.argsort(m)
    axs[0].plot(m[order],abs(coeff[order])**2,"o-",ms=3,label=rf"$N\eta={z}$",color=color)
axs[0].set(xlim=(-12,12),xlabel=r"Angular-momentum index $m$",ylabel=r"$P_m=J_m(N\eta)^2$",title="Resonant momentum spreading")
axs[0].legend()
N=np.arange(11)
axs[1].plot(N,N**2,"o-",color="#0072b2",label=r"Coherent resonance: $N^2$")
axs[1].plot(N,N,"--",color="#999999",label=r"Incoherent comparison: $N$")
axs[1].set(xlabel="Number of kicks N",ylabel=r"$4I\langle K\rangle/(\hbar^2\eta^2)$",title="Kinetic energy")
axs[1].legend()
finish(fig,"paper-1-kicked-rotor")
