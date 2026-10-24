"""Python 3.14; NumPy and Matplotlib in ../pyproject.toml. PNG output in CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
a=.5
angle=np.linspace(0,2*np.pi,700)
z=np.exp(1j*np.linspace(np.pi/2,3*np.pi/2,500))
fz=(z-a)/(1-a*z)
theta=np.arctan((1-a*a)/(2*a))
fig,axs=plt.subplots(1,2,figsize=(8.4,4.1),facecolor="white")
for ax in axs:
 ax.plot(np.cos(angle),np.sin(angle),color=".65",lw=1)
 ax.axhline(0,color=".85",lw=.7);ax.axvline(0,color=".85",lw=.7)
 ax.set_aspect("equal");ax.set(xlim=(-1.22,1.2),ylim=(-1.2,1.22),xlabel="Real part",ylabel="Imaginary part")
 ax.spines[["top","right"]].set_visible(False)
axs[0].plot(z.real,z.imag,color="C0",lw=3)
axs[0].scatter([a],[0],color="C3",s=35,zorder=5)
axs[0].text(a+.05,.08,r"$a=1/r$")
axs[0].text(.05,1.05,r"$i$");axs[0].text(.05,-1.13,r"$-i$")
axs[0].set_title("Original disk: start away from center")
axs[1].plot(fz.real,fz.imag,color="C0",lw=3)
axs[1].scatter([0],[0],color="C3",s=35,zorder=5)
axs[1].text(.05,.08,r"$f(a)=0$")
ep=fz[0]
axs[1].plot([0,ep.real],[0,ep.imag],color="C1",lw=1)
axs[1].plot([0,ep.real],[0,-ep.imag],color="C1",lw=1)
arc=np.linspace(np.pi-theta,np.pi+theta,120)
axs[1].plot(.33*np.cos(arc),.33*np.sin(arc),color="C1")
axs[1].text(-.53,-.04,r"$2\theta$",color="C1")
axs[1].text(ep.real+.03,ep.imag+.09,r"$f(i)$")
axs[1].text(ep.real+.03,-ep.imag-.18,r"$f(-i)$")
axs[1].set_title(r"Mapped arc has angle $2\theta$")
fig.suptitle(r"Disk automorphism $f(z)=(z-a)/(1-az)$",y=1.01)
fig.tight_layout()
fig.savefig("2009-semicircle-map.png",dpi=150,facecolor="white",bbox_inches="tight")
