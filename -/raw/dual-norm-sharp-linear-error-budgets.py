"""Show exact deterministic output-error budgets; output matching PNG in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    rates = np.array([2.,np.sqrt(5),3.])
    eps = np.linspace(0,.2,201)
    colors = ["#397d37","#28738f","#ba6429"]
    labels = [r"$\|\delta x\|_1\leq\varepsilon$",r"$\|\delta x\|_2\leq\varepsilon$",r"$\|\delta x\|_\infty\leq\varepsilon$"]
    fig,axes = plt.subplots(1,2,figsize=(11.3,5.2),dpi=120)
    fig.patch.set_facecolor("white")
    for rate,color,label in zip(rates,colors,labels):
        axes[0].plot(eps,rate*eps,color=color,lw=2.3,label=label)
        axes[0].scatter([.1],[rate*.1],color=color,s=35,zorder=4)
    axes[0].axvline(.1,color="#aaaaaa",ls="--",lw=1)
    axes[0].set(xlabel=r"Input norm budget $\varepsilon$",ylabel=r"Maximum $|\delta p|$",xlim=(0,.2),ylim=(0,.63))
    axes[0].set_title("Sharp error magnitudes",fontsize=15)
    axes[0].grid(color="#e5e5e5",lw=.6)
    axes[0].legend(frameon=False,fontsize=12,loc="upper left")
    for row,(rate,color,label) in enumerate(zip(rates,colors,labels)):
        y = 2-row
        bound = rate*.1
        axes[1].plot([-bound,bound],[y,y],color=color,lw=4,solid_capstyle="round")
        axes[1].scatter([-bound,bound],[y,y],color=color,s=50,zorder=4)
        axes[1].text(0,y+.2,label,ha="center",fontsize=12)
        text = f"±{bound:.3f}" if row==1 else f"±{bound:.1f}"
        axes[1].text(.345,y,text,ha="left",va="center",fontsize=12,color=color)
    axes[1].axvline(0,color="#aaaaaa",ls="--",lw=1)
    axes[1].set(xlim=(-.4,.49),ylim=(-.4,2.5),xlabel=r"Possible output error $\delta p$",yticks=[])
    axes[1].set_xticks([-.3,-.2,0,.2,.3])
    axes[1].set_title(r"Feasible intervals at $\varepsilon=0.1$",fontsize=15)
    axes[1].spines[["left","top","right"]].set_visible(False)
    axes[0].spines[["top","right"]].set_visible(False)
    fig.suptitle(r"Dual norm error bounds for $p(x)=2x_1-x_2$",fontsize=18,weight="bold")
    fig.text(.5,.035,"Different norm constraints describe different allowed perturbation sets.",ha="center",fontsize=12)
    fig.subplots_adjust(left=.085,right=.97,top=.79,bottom=.17,wspace=.31)
    fig.savefig(Path(__file__).stem+".png",facecolor="white",transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
