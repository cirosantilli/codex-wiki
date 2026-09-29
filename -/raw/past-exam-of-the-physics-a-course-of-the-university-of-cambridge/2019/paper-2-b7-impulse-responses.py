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
    t=np.linspace(0,13,1000)
    fig,ax=plt.subplots(figsize=(8.2,4.4),layout="constrained")
    for gamma,color in [(.22,"#0068a0"),(1.,"#b55713"),(2.,"#654c9e")]:
        if gamma<1:
            wd=np.sqrt(1-gamma*gamma);y=np.exp(-gamma*t)*np.sin(wd*t)/wd;label="Underdamped: γ/ω₀ = 0.22"
        elif gamma==1:y=t*np.exp(-t);label="Critical: γ/ω₀ = 1"
        else:
            s=np.sqrt(gamma*gamma-1);y=(np.exp((-gamma+s)*t)-np.exp((-gamma-s)*t))/(2*s);label="Overdamped: γ/ω₀ = 2"
        ax.plot(t,y,label=label,color=color,lw=2)
    ax.axhline(0,color="#777777",lw=.8)
    ax.set(xlabel=r"$\omega_0 t$",ylabel=r"$x/(v_0/\omega_0)$",xlim=(0,13),title="Same displacement zero and same initial velocity")
    ax.legend(fontsize=10);ax.grid(alpha=.18)

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
