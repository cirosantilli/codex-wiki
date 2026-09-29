"""Original integral comparison and computed finite harmonic/logarithmic bounds."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(2,3,400)
indices=np.arange(1,51)
harmonic=np.cumsum(1/indices)
upper=harmonic-np.log(indices)
lower=harmonic-np.log(indices+1)
fig,(integrals,bounds)=plt.subplots(1,2,figsize=(9.4,4.3),layout="constrained")
integrals.fill_between(x,0,.5,color="#e9edf1",label=r"rectangle of area $1/n$")
integrals.plot(x,1/x,color="#245b9f",lw=2,label=r"$1/x$")
integrals.plot(x,1/(x-1),color="#b0522b",lw=2,label=r"$1/(x-1)$")
integrals.plot([2,3],[.5,.5],color="black",ls="--",lw=1.4,label=r"$1/n$, with $n=2$")
integrals.set(xlim=(1.97,3.03),ylim=(0,1.08),xlabel=r"$x$",ylabel="Height",
              title="Unit-interval comparison")
integrals.legend(loc="lower left",fontsize=9)
bounds.fill_between(indices,lower,upper,color="#e9edf1")
bounds.plot(indices,upper,color="#b0522b",lw=2,label=r"$H_N-\ln N$ (decreasing)")
bounds.plot(indices,lower,color="#245b9f",lw=2,label=r"$H_N-\ln(N+1)$ (increasing)")
bounds.axhline(.5772156649015329,color="0.3",ls=":",lw=1.2,label=r"common limit $\gamma$")
bounds.set(xlim=(1,50),ylim=(.28,1.04),xlabel=r"$N$",ylabel="Sequence value",
           title=r"Bounds with gap $\ln(1+1/N)$")
bounds.legend(loc="upper right",fontsize=9)
for ax in [integrals,bounds]:ax.grid(alpha=.13)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
