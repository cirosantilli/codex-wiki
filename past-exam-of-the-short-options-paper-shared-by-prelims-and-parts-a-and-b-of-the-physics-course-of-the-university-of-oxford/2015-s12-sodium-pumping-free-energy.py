from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

e=1.602176634e-19;k=1.380649e-23;T=300.;C=1e-16;n0=1e4
f=np.linspace(0,.9999,1000);elect=n0*f*e/C;chem=-k*T/e*np.log1p(-f)
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4.8),layout="constrained")
ax.plot(f,elect,color="#246c94",lw=2,label="Electrical");ax.plot(f,chem,color="#d17a23",lw=2,label="Chemical");ax.plot(f,elect+chem,color="#79539a",lw=2,ls="--",label="Total")
ax.plot(.5,5000*e/C,"o",color="#246c94");ax.annotate("8.01 eV electrical\nat half depletion",xy=(.5,5000*e/C),xytext=(.08,11.7),arrowprops={"arrowstyle":"->"},fontsize=11)
ax.set(xlabel=r"Exported fraction $n/n_0$",ylabel="Export cost per ion (eV)",xlim=(0,1.01),ylim=(0,17.5),title="Electrical cost dominates most of the range");ax.legend(loc="lower right");ax.grid(alpha=.16)
bx.plot(f,1000*chem,color="#d17a23",lw=2.4);bx.plot(.5,1000*k*T/e*np.log(2),"o",color="#d17a23")
bx.annotate("17.9 meV\nat half depletion",xy=(.5,1000*k*T/e*np.log(2)),xytext=(.04,75),arrowprops={"arrowstyle":"->"},fontsize=11)
bx.axvline(1,color="gray",ls=":");bx.annotate("Logarithmic divergence\nin the continuum model",xy=(.996,140),xytext=(.12,180),arrowprops={"arrowstyle":"->"},fontsize=11)
bx.set(xlabel=r"Exported fraction $n/n_0$",ylabel="Chemical cost per ion (meV)",xlim=(0,1.015),ylim=(0,250),title="Chemical term enlarged");bx.grid(alpha=.16)
fig.suptitle(r"Ideal fixed-capacitance vesicle: $n_0=10^4$, $C=10^{-16}$ F, $T=300$ K",fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
