"""Original analytic illustration. Tested with Python 3.14, NumPy and Matplotlib.
Run from the intended output directory; the PNG is written to the current directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "savefig.facecolor": "white"})

q=np.linspace(-3.2,3.2,1801)
rho=np.exp(-q*q)/np.sqrt(np.pi)
fig,ax=plt.subplots(figsize=(8.2,3.7),layout="constrained")
ax.plot(q,rho,color="#173e62",lw=2,label=r"$|\phi_0(q)|^2=\pi^{-1/2}e^{-q^2}$")
for m in (q<=-1,q>=1):ax.fill_between(q,0,rho,where=m,color="#d57338",alpha=.75)
for t in (-1,1):ax.axvline(t,color=".35",ls="--",lw=1)
ax.text(0,.25,"classically allowed\ninterval",ha="center")
ax.text(-2,.12,"forbidden",ha="center",color="#99431b")
ax.text(2,.12,"forbidden",ha="center",color="#99431b")
ax.set(xlabel="Reduced displacement q",ylabel="Probability density",ylim=(0,.64),title="Both tails together contain 15.73% probability")
ax.legend(loc="upper right",frameon=False)
fig.savefig("paper-2b-oscillator-tails.png",dpi=165)
plt.close(fig)
