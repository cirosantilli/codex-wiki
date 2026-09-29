"""Original sharp-freeze-out calculation; saves basename in cwd. Python 3.14."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
mass=1900.;theta0=2.35e-13;hc=2e-16;critical=5.
def omega(p):
    return mass*6*(theta0/hc)**3*p**1.5*np.exp(-p)/critical
p=np.linspace(29,43,600)
fig,ax=plt.subplots(figsize=(8,4.2),layout="constrained")
ax.semilogy(p,omega(p),color="#245e84",lw=2,label=r"Conserved $aT$, sharp chemical freeze-out")
ax.axhline(.2,color="#8b5b35",ls="--",label="Stipulated dark-matter fraction 0.2")
ax.scatter([36],[omega(36)],s=50,color="#b84e2b",zorder=5)
ax.annotate(r"$P=36:\ \Omega_\chi=0.1853$",xy=(36,omega(36)),xytext=(30,0.009),arrowprops=dict(arrowstyle="->",color="#b84e2b"),fontsize=11)
ax.set(xlabel=r"$P=mc^2/(k_BT_f)$",ylabel=r"$\Omega_\chi=\epsilon_{\chi,0}/\epsilon_c$",title=r"Relic abundance for $mc^2=1900\ \mathrm{GeV}$")
ax.grid(alpha=.2);ax.legend(fontsize=9)
fig.savefig("paper-1-relic-sensitivity.png",dpi=155,facecolor="white")
