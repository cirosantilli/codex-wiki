"""Original supplement to the sketch omitted from the linked 2015 S18 notes.

Exact internal standing-wave enhancement and a resonance-pole approximation.
The impenetrable end wall leaves zero transmitted probability flux.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def denominator(z, lam):
    return -np.expm1(2j*z)+1j*lam*z


def pole(n, lam):
    """Newton root seeded by the fixed-low-mode, small-lambda expansion."""
    z=n*np.pi*(1+lam/2+lam**2/4)-1j*(lam*n*np.pi/2)**2
    for _ in range(30):
        step=denominator(z,lam)/(-2j*np.exp(2j*z)+1j*lam)
        z-=step
        if abs(step)<1e-14:break
    return z


def intensity(x, lam):
    x=np.asarray(x,dtype=float)
    with np.errstate(divide="ignore",invalid="ignore"):
        value=(lam*x)**2/abs(denominator(x,lam))**2
    return np.where(x==0,lam**2/(2-lam)**2,value)


def main():
    plt.rcParams.update({"font.size":12,"figure.facecolor":"white","axes.facecolor":"white"})
    fig,axes=plt.subplots(1,2,figsize=(10,4.2),layout="constrained");lam=.05
    x=np.linspace(0,3.5*np.pi,24001)
    axes[0].semilogy(x/np.pi,intensity(x,lam),color="#0072B2",lw=1.5)
    for n in [1,2,3]:
        axes[0].axvline(n,color=".6",ls=":",lw=.8)
        axes[0].scatter([n],[1],color=".3",s=16,zorder=4)
        p=pole(n,lam);axes[0].annotate(str(n),(p.real/np.pi,intensity(p.real,lam)),xytext=(4,4),textcoords="offset points",fontsize=10)
    axes[0].set(xlabel=r"real $ka/\pi$",ylabel=r"internal amplitude factor $|A|^2$",xlim=(0,3.5),ylim=(2e-4,400),title=rf"Narrow cavity resonances, $\lambda={lam}$")
    p=pole(1,lam);gamma=-p.imag;u=np.linspace(-6,6,1201);xx=p.real+gamma*u
    residue_scale=(lam*p.real)**2/abs(-2j*np.exp(2j*p)+1j*lam)**2
    height=residue_scale/gamma**2
    axes[1].plot(u,intensity(xx,lam)/height,label="exact amplitude",color="#0072B2")
    axes[1].plot(u,1/(1+u*u),ls="--",label="simple-pole approximation",color="#D55E00")
    axes[1].set(xlabel=r"$(ka-\mathrm{Re}\,p_1)/(-\mathrm{Im}\,p_1)$",ylabel="enhancement / pole height estimate",xlim=(-6,6),ylim=(0,1.1),title="First peak on its natural width scale");axes[1].legend(fontsize=10)
    for ax in axes:ax.grid(alpha=.2)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white");plt.close(fig)


if __name__=="__main__":main()
