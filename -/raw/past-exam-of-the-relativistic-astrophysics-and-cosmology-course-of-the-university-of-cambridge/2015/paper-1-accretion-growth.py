"""Original retained-mass Eddington growth curves; output basename to cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
G=6.67430e-11;c=299792458.;mp=1.67262192595e-27;sig=6.65e-29;yr=365.25*86400
tE=sig*c/(4*np.pi*G*mp)/yr
eta0=1-np.sqrt(8/9);bound=1e9/(1e9+tE*np.log(1e8))
t=np.linspace(0,1e9,500)
fig,ax=plt.subplots(figsize=(8,4.4),layout="constrained")
for eta,col,label in [(eta0,"#285e85",r"Schwarzschild $\eta=0.05719$"),(bound,"#b65b29",r"Bound $\eta=0.10758$"),(.2,"#598754",r"Example $\eta=0.2$")]:
    ts=tE*eta/(1-eta)
    ax.semilogy(t/1e9,10*np.exp(t/ts),color=col,lw=2,label=label)
ax.axhline(1e9,ls="--",color=".4",label=r"Target $10^9 M_\odot$")
ax.set(xlabel="Accretion interval (Gyr)",ylabel=r"Black-hole mass ($M_\odot$)",title=r"Continuous $L=L_{\rm Edd}$; constant efficiency; seed $10M_\odot$")
ax.grid(alpha=.2);ax.legend(fontsize=10)
fig.savefig("paper-1-accretion-growth.png",dpi=155,facecolor="white")
