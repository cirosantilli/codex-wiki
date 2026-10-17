"""Original relic calculation from supplied constants; output basename cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
mass=38.;t0=2.35e-13;hc=2e-16;critical=5.
def ratio(p):return mass*6*(t0/hc)**3*p**1.5*np.exp(-p)/critical
p=np.linspace(20,45,700)
fig,ax=plt.subplots(figsize=(8,4.5),layout="constrained")
ax.semilogy(p,ratio(p),lw=2,color="#274e82",label=r"Sharp cutoff, conserved $aT$ and particle number")
ax.axhline(1,color=".4",ls="--",label="Critical-density fraction 1")
ax.plot(36,ratio(36),"o",color="#bc5429",ms=7)
ax.annotate(r"$P=36:\ \Omega_\chi=0.003706$",xy=(36,ratio(36)),xytext=(26,2e-4),arrowprops={"arrowstyle":"->","color":"#bc5429"},fontsize=11)
ax.set(xlabel=r"$P=mc^2/(k_BT_f)$",ylabel=r"$\rho_{\chi,0}/\rho_c$",title="Freeze-out temperature strongly controls the assumed relic abundance")
ax.legend(loc="upper right",fontsize=9);ax.grid(alpha=.2)
fig.savefig("paper-1-relic-sensitivity.png",dpi=150,facecolor="white")
