"""Original Bogoliubov and split-ring profiles; output PNG to cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(11,4.6),layout="constrained")
q=np.linspace(0,3,700);e=np.sqrt(q*q*(q*q+2))
ax=axs[0];ax.plot(q,e,color="#274e82",lw=2,label="Bogoliubov")
ax.plot(q,np.sqrt(2)*q,"--",color="#288969",label=r"Sound: $\sqrt{2}q$")
ax.plot(q,q*q+1,":",color="#bc5429",label=r"Particle limit: $q^2+1$")
ax.set(xlabel=r"$q=|k|\xi$",ylabel=r"$E/\mu$",title="Gapless phonons cross into particle excitations")
ax.legend(fontsize=10);ax.grid(alpha=.18)
ax=axs[1];theta=np.array([0,np.pi,np.pi,2*np.pi])
ax.plot(theta,[4/3,4/3,2/3,2/3],color="#274e82",lw=2,label=r"Density $\rho/\rho_0$")
ax.plot(theta,[2/3,2/3,4/3,4/3],color="#bc5429",lw=2,ls="--",label=r"Speed $v/[n\hbar/(mR)]$")
ax.axvline(np.pi,color=".5",ls=":")
ax.set(xticks=[0,np.pi,2*np.pi],xticklabels=["0",r"$\pi$",r"$2\pi$"],ylim=(.45,1.85),xlabel=r"Unwrapped ring angle $\theta$",ylabel="Normalized bulk density or speed",title=r"Raised left half: $V_0=2\mu_0/3$")
ax.text(np.pi/2,1.58,"Right: denser, slower",ha="center",fontsize=10)
ax.text(3*np.pi/2,1.58,"Left: depleted, faster",ha="center",fontsize=10)
ax.legend(loc="lower left",fontsize=10);ax.grid(alpha=.18)
fig.savefig("paper-1-bogoliubov-ring.png",dpi=150,facecolor="white")
