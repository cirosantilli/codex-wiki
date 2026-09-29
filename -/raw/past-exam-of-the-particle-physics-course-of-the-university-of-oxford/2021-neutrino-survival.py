from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
fig, axes=plt.subplots(2,1,figsize=(8,6.0),layout="constrained",sharex=True)
E=np.linspace(1,10,8000)
P=.5+.5*np.cos(7.9/E)**2
axes[0].plot(E,P,color="#1769aa",lw=1.8,label="79 km reactor (vacuum)")
maxima=np.array([7.9/(2*np.pi),7.9/np.pi]);minima=np.array([7.9/(2.5*np.pi),7.9/(1.5*np.pi),7.9/(.5*np.pi)])
axes[0].scatter(maxima,np.ones(2),color="#1769aa",s=28,zorder=3)
axes[0].scatter(minima,.5*np.ones(3),color="#ba4a00",s=28,zorder=3)
for e in maxima: axes[0].annotate(f"{e:.3f}",(e,1),xytext=(8,7),textcoords="offset points",fontsize=9)
for j,e in enumerate(minima): axes[0].annotate(f"{e:.3f}",(e,.5),xytext=(5,-13 if j!=1 else 8),textcoords="offset points",fontsize=9)
axes[0].set_title(r"$\theta=22.5^\circ$: reactor extrema in $1<E<10$ MeV")
axes[0].legend(loc="upper right",fontsize=9)
# The physical solar oscillations are far too fine to resolve on this grid.
# Show their exact envelope and mark a small illustrative inset, never alias them.
axes[1].fill_between(E,.5,1,color="#bbdefb",alpha=.7,label="solar vacuum oscillation envelope")
axes[1].axhline(.75,color="#1769aa",lw=2,label="unresolved vacuum average: 0.75")
axes[1].axhline(np.sin(np.pi/8)**2,color="#ba4a00",ls="--",lw=1.6,label="high-density adiabatic limit: 0.146")
axes[1].text(5.7,.88,"Physical solar oscillations are unresolved.\nSpacing illustrated in inset is enlarged.",ha="center",fontsize=9)
ins=axes[1].inset_axes([.035,.70,.28,.25])
e=np.linspace(1,2,1400)
ins.plot(e,.5+.5*np.cos(80/e)**2,color="#1769aa",lw=.8)
ins.set_xticks([]);ins.set_yticks([.5,1]);ins.tick_params(labelsize=7)
axes[1].legend(loc="lower right",fontsize=8)
for ax in axes:
    ax.set_xlim(.95,10.05);ax.set_ylim(.05,1.1);ax.set_ylabel(r"$P_{ee}$");ax.grid(alpha=.2)
axes[1].set_xlabel("Neutrino energy E (MeV)")
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
