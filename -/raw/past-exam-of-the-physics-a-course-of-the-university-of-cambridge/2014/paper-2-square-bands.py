"""Original directional two-branch NFE sketches; not full corner diagonalization."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
A=2.350188510275442;gap=1.;q=np.linspace(0,1.25,600)
fig,axes=plt.subplots(1,2,figsize=(9,4.2),layout="constrained")
for ax,factor,title in zip(axes,[1,2],[r"[10]: $\mathbf{k}=(q,0)\pi/a$",r"[11]: $\mathbf{k}=(q,q)\pi/a$"]):
    E1=factor*A*q*q;E2=factor*A*(2-q)**2
    mean=(E1+E2)/2;split=np.sqrt(((E1-E2)/2)**2+(gap/2)**2)
    ax.plot(q,E1,":",color=".5");ax.plot(q,E2,":",color=".5")
    ax.plot(q,mean-split,color="#245d84",lw=2,label="Lower branch")
    ax.plot(q,mean+split,color="#b2602c",lw=2,label="Upper branch")
    ax.axvline(1,color=".5",ls="--")
    for ee,col in [(A+.5,"#b2602c"),(2*A-.5,"#245d84")]:ax.axhline(ee,color=col,ls="--",alpha=.6)
    ax.plot([1,1],[factor*A-.5,factor*A+.5],"o",color=".2")
    ax.text(.66,factor*A+.64,f"{factor*A-.5:.2f}, {factor*A+.5:.2f} eV",fontsize=9)
    ax.set(xlim=(0,1.25),ylim=(-.1,6.5),xlabel="q",ylabel="Energy (eV)",title=title)
    ax.grid(alpha=.15)
axes[0].legend(fontsize=9,loc="upper left")
fig.suptitle("Stipulated directional gap model: upper face energy below lower corner energy")
fig.savefig("paper-2-square-bands.png",dpi=150,facecolor="white")
