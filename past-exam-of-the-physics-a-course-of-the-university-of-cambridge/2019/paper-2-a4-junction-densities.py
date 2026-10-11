"""Original solution figure; tested with Python 3.14.

Uses NumPy and Matplotlib as declared in the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    x=np.linspace(-2.2,2.2,1500)
    # Smooth, illustrative carrier densities from a depletion-model potential.
    potential=np.where(x<0,-1+np.maximum(x+1,0)**2,1-np.maximum(1-x,0)**2)
    potential=np.clip(potential,-1,1)
    ni_over_N=1e-6
    n=ni_over_N*np.exp(np.log(1/ni_over_N)*potential)
    p=ni_over_N*np.exp(-np.log(1/ni_over_N)*potential)
    fig,(ax,charge)=plt.subplots(2,1,figsize=(8.3,6.2),sharex=True,layout="constrained",height_ratios=[1.45,1])
    ax.semilogy(x,n,label="Electrons n/N",color="#b55713",lw=2)
    ax.semilogy(x,p,label="Holes p/N",color="#0068a0",lw=2)
    ax.set(ylim=(2e-13,3),ylabel="Carrier density / dopant density N",title="Equilibrium abrupt p–n junction: illustrative symmetric case")
    ax.legend(loc="upper center",ncol=2,fontsize=9);ax.grid(alpha=.15)
    ax.text(-2.05,.15,"p-type bulk",fontsize=11);ax.text(1.15,.15,"n-type bulk",fontsize=11)
    charge.plot([-2.2,-1,-1,0,0,1,1,2.2],[0,0,-1,-1,1,1,0,0],color="#555555",lw=2)
    charge.fill_between([-1,0],-1,0,color="#0068a0",alpha=.18)
    charge.fill_between([0,1],0,1,color="#b55713",alpha=.18)
    charge.text(-.91,-.65,r"$-eN_A$: fixed acceptors",fontsize=9)
    charge.text(.1,.6,r"$+eN_D$: fixed donors",fontsize=9)
    charge.text(-2.1,.15,"Quasi-neutral",fontsize=10);charge.text(1.1,-.25,"Quasi-neutral",fontsize=10)
    charge.set(ylim=(-1.45,1.45),ylabel=r"Net charge density $\rho/(eN)$",xlabel="Position (arbitrary units)")
    charge.set_xticks([-1,0,1],[r"$-x_p$","Junction",r"$x_n$"])
    for a in (ax,charge):
        a.axvspan(-1,1,color="#eeeeee",alpha=.3,zorder=-10)
        a.axvline(-1,color="#999999",ls="--",lw=.8);a.axvline(1,color="#999999",ls="--",lw=.8)
    charge.text(.5,.03,"Depletion interval; N_A = N_D = N",transform=charge.transAxes,ha="center",fontsize=9)

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
