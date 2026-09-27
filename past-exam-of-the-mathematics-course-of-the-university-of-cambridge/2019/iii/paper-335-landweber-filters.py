"""Landweber damping and inverse coefficients; write PNG in cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    sigma=np.geomspace(1e-4, 1, 700)
    fig,axes=plt.subplots(1,2,figsize=(10,4.3),dpi=100,facecolor="white")
    for n,color in [(1,"#1766aa"),(10,"#d87922"),(100,"#38966b"),(1000,"#9c55a1")]:
        with np.errstate(divide="ignore"):
            filt=-np.expm1(n*np.log1p(-sigma*sigma))
        axes[0].semilogx(sigma,filt,color=color,lw=2.2,label=f"n = {n}")
        axes[1].loglog(sigma,filt/sigma,color=color,lw=2.2,label=f"n = {n}")
    axes[1].loglog(sigma,1/sigma,color="0.5",ls="--",lw=1.3,label=r"Unregularized $1/\sigma$")
    axes[0].set(xlim=(1e-4,1),ylim=(-.03,1.05),ylabel=r"Damping factor $f_n(\sigma)$",
                title="More iterations retain smaller singular values")
    axes[1].set(xlim=(1e-4,1),ylim=(1e-4,1e4),ylabel=r"Data multiplier $f_n(\sigma)/\sigma$",
                title="Finite stopping controls noise amplification")
    for ax in axes:
        ax.set_xlabel(r"Singular value $\sigma$")
        ax.grid(alpha=.2,which="both")
        ax.legend(frameon=False,fontsize=9,loc="upper left")
    fig.suptitle(r"Landweber iteration: zero start, unit step, $\|A\|\leq1$",fontsize=12)
    fig.tight_layout(rect=(0,0,1,.93))
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white",transparent=False,dpi=100)
    plt.close(fig)


if __name__=="__main__":
    main()
