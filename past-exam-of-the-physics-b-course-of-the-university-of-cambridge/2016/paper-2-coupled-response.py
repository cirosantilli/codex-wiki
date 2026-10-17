"""Original explanatory figure; Python 3.14 and root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","axes.facecolor":"white"})

w=np.linspace(.05,2.2,2400);kappa=.6;b=.04
Hplus=1/(1-w*w+1j*b*w);Hminus=1/(1+2*kappa-w*w+1j*b*w)
x1=.5*(Hplus+Hminus);x2=.5*(Hplus-Hminus)
fig,ax=plt.subplots(figsize=(7.4,4.4),layout="constrained")
ax.semilogy(w,abs(x1),label="Directly driven mass",color="#1565c0",lw=2);ax.semilogy(w,abs(x2),label="Undriven partner",color="#d84315",lw=2)
for f in [1,np.sqrt(1+2*kappa)]:ax.axvline(f,color="#999",ls=":",lw=1)
fanti=np.sqrt(1+kappa);ax.axvline(fanti,color="#bbb",ls="--",lw=.8)
ax.annotate("Cancellation near the\nantiresonance",(fanti,abs(np.interp(fanti,w,abs(x1)))),xytext=(1.55,.2),arrowprops={"arrowstyle":"->"},fontsize=9)
ax.set(xlabel=r"Driving frequency / $\sqrt{k/m}$",ylabel=r"Displacement amplitude / $(F/k)$",title=r"Two coupled masses: $\kappa/k=0.6$, $b/\sqrt{mk}=0.04$",xlim=(.05,2.2),ylim=(.02,25));ax.legend(fontsize=9);ax.grid(alpha=.18,which="both")

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
