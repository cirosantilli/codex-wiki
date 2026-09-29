"""Original harmonic-gas cutoff illustration, dimensionless, output cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x=np.linspace(0,13,1000);p=x*x*np.exp(-x)/2;cut=5.
fig,ax=plt.subplots(figsize=(8,4),layout="constrained")
ax.plot(x,p,lw=2,color="#274e82",label=r"Before selection: $f(x)=x^2e^{-x}/2$")
ax.fill_between(x,p,where=x>=cut,color="#bc5429",alpha=.35,label="Atoms removed from high-energy tail")
ax.axvline(cut,color="#bc5429",ls="--")
ax.text(cut+.1,.23,r"Illustrative $\eta=5$",color="#8b351e")
ax.axvline(3,color=".5",ls=":",label=r"Initial mean energy $3k_BT$")
ax.set(xlabel=r"Initial atom energy $x=\epsilon/(k_BT)$",ylabel="Probability density",title="Energy-selective removal in a fixed harmonic trap")
ax.legend(fontsize=10);ax.grid(alpha=.15)
fig.savefig("paper-1-evaporation.png",dpi=150,facecolor="white")
