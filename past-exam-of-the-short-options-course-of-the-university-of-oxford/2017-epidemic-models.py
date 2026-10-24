"""Generate 2017-epidemic-models.png in the current directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig,axes=plt.subplots(1,3,figsize=(12,4.5),dpi=100,facecolor="white")
    x,y=1.03,.19;values=[]
    for step in range(301):
        values.append(y)
        x,y=x+.2-x*y,x*y
    axes[0].plot(np.arange(301),values,color="#2563eb",lw=1.5)
    axes[0].axhline(.2,color="#64748b",ls="--",lw=1)
    axes[0].set(title="Recruitment: repeated small waves",xlabel="Generation t",ylabel=r"Scaled infectives $\alpha I_t$")
    axes[0].set_ylim(.18,.22)

    reproduction=1.8;seed=.005;dt=.05;state=np.array([1,seed,0.]);path=[state.copy()]
    def rhs(a):
        u,v,w=a
        return np.array([-reproduction*u*v,(reproduction*u-1)*v,v])
    for _ in range(1000):
        k1=rhs(state);k2=rhs(state+dt*k1/2);k3=rhs(state+dt*k2/2);k4=rhs(state+dt*k3)
        state=state+dt*(k1+2*k2+2*k3+k4)/6
        path.append(state.copy())
    times=dt*np.arange(len(path));path=np.asarray(path)
    for index,label,color in [(0,"Susceptible u","#2563eb"),(1,"Infectious v","#b91c1c"),(2,"Removed w","#15803d")]:
        axes[1].plot(times,path[:,index],label=label,color=color,lw=1.7)
    axes[1].set(title=r"Closed SIR: $\mathcal{R}_0=1.8$",xlabel=r"Scaled time $\tau$",ylabel="Scaled counts")
    axes[1].legend(fontsize=8,loc="center right")

    ratios=np.linspace(1.01,1.3,120);seed=1e-8;exact=[]
    for ratio in ratios:
        low,high=0.,1+seed
        for _ in range(80):
            middle=(low+high)/2
            residual=seed-middle-np.expm1(-ratio*middle)
            if residual>0:low=middle
            else:high=middle
        exact.append((low+high)/2)
    axes[2].plot(ratios,exact,color="#111827",label="Exact final-size root",lw=1.8)
    axes[2].plot(ratios,2*(ratios-1)/ratios**2,color="#7e22ce",ls="--",label="Small-seed quadratic limit",lw=1.8)
    axes[2].set(title=r"Near threshold, $v_0=10^{-8}$",xlabel=r"$\mathcal{R}_0$",ylabel=r"Final removed count $w_\infty$")
    axes[2].legend(fontsize=8,loc="lower right")
    for ax in axes:
        ax.grid(alpha=.2);ax.spines[["top","right"]].set_visible(False)
        ax.title.set_fontsize(11)
    fig.suptitle("Generic epidemic models: replenishment, one-wave depletion and final size",fontsize=14,y=.96)
    fig.subplots_adjust(left=.06,right=.985,bottom=.16,top=.80,wspace=.32)
    fig.savefig("2017-epidemic-models.png",dpi=100,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
