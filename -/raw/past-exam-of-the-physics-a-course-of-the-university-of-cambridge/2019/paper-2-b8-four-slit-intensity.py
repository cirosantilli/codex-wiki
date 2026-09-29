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
    x=np.linspace(-.05,.05,14000);L=.5;lam=.5e-6;a=10e-6;D=20e-6
    q=2*np.pi*x/(lam*np.sqrt(L*L+x*x))
    envelope=np.sinc(q*a/(2*np.pi))**2
    intensity=envelope*np.cos(q*D/2)**2*np.cos(q*D)**2
    fig,ax=plt.subplots(figsize=(9,4.3),layout="constrained")
    ax.plot(x*1000,intensity,color="#0068a0",lw=1.4,label="Four-slit intensity")
    ax.plot(x*1000,envelope,color="#777777",ls="--",lw=1,label="Single-slit envelope")
    for m in (-3,-2,-1,1,2,3):
        s=m*lam/D;pos=1000*L*s/np.sqrt(1-s*s)
        ax.axvline(pos,color="#bbbbbb",lw=.6,ls=":")
        if abs(m)==2:ax.text(pos,.12,f"m = {m}\nmissing",ha="center",fontsize=9)
        else:ax.text(pos,.53 if abs(m)==1 else .16,f"m = {m}",ha="center",fontsize=9)
    ax.set(xlabel="Screen position X (mm)",ylabel=r"$I(X)/I(0)$",xlim=(-50,50),ylim=(-.02,1.08),
           title="Four slits: 10 μm width, 20 μm spacing, λ = 500 nm, L = 0.5 m")
    ax.legend(loc="upper right",fontsize=9);ax.grid(alpha=.15)

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
