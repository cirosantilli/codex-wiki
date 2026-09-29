"""Original analytic teaching diagram; tested with Python 3.14, numpy, matplotlib.
Run from the intended output directory; PNG output is a basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(10,4),layout="constrained")
x=np.linspace(-.3,3.3,900)
for N in range(4):
 axs[0].plot(x,(N-x)**2,label=f"N={N}")
low=np.min(np.array([(N-x)**2 for N in range(4)]),axis=0);axs[0].plot(x,low,"k",lw=2.5,label="stable charge")
for t in [.5,1.5,2.5]:axs[0].axvline(t,color="#999999",ls=":",lw=.8)
axs[0].set(ylim=(-.05,2.5),xlabel="Induced gate charge / e",ylabel="Electrostatic energy / E_C",title="Charging-only limit: charge crossings")
axs[0].legend(fontsize=8,ncol=2);axs[0].grid(alpha=.2)
# Explicit illustrative ratio hbar omega0 = e^2/C, not source-supplied parameters.
levels=[]
for q in range(5):levels.extend([q+1]*(2*(q+1)))
N=np.arange(1,15);add=np.array([1+levels[i]-levels[i-1] for i in N])
axs[1].bar(N,add,color=["#b35c25" if n in [2,6,12] else "#286b93" for n in N])
axs[1].axhline(1,color="k",ls="--",lw=1,label="capacitive contribution")
axs[1].set(xlabel="Occupied electron count N",ylabel="mu(N+1) - mu(N), units e²/C",title="Illustrative harmonic-shell addition energy",xticks=[2,4,6,8,10,12,14],ylim=(0,2.4))
axs[1].legend(fontsize=8);axs[1].grid(axis="y",alpha=.2)
fig.suptitle("Original constant-interaction examples; right panel uses hbar omega0 = e²/C")
fig.savefig("paper-1-dot-charging.png",dpi=155,facecolor="white")
