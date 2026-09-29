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
    k=np.linspace(0,4*np.pi,6000);f=np.cos(k)+10*np.sinc(k/np.pi)
    starts=[2.6276754329857965,5.307324799118129,8.067135580679963,10.90870750976562]
    fig,(ax,detail)=plt.subplots(2,1,figsize=(9,6),sharex=True,layout="constrained",height_ratios=[1,1.15])
    for a in (ax,detail):
        a.axhspan(-1,1,color="#dbece1",alpha=.6)
        for j,start in enumerate(starts,1):a.axvspan(start,j*np.pi,color="#339966",alpha=.18)
        a.plot(k,f,color="#0068a0",lw=1.6)
        a.axhline(1,color="#555555",ls="--",lw=1);a.axhline(-1,color="#555555",ls="--",lw=1)
        a.grid(alpha=.12);a.set_ylabel(r"$f(k)=\cos k+10\sin k/k$")
    ax.set(ylim=(-4,12),title="Repulsive delta comb: only |f(k)| ≤ 1 gives real Bloch wavevector")
    ax.plot(0,11,"o",color="#b55713");ax.text(.25,10.3,"f(0) = 11",fontsize=10)
    detail.set(ylim=(-1.7,1.7),xlim=(0,4*np.pi),xlabel="k, with a = 1")
    detail.set_xticks(np.arange(5)*np.pi,["0",r"$\pi$",r"$2\pi$",r"$3\pi$",r"$4\pi$"])
    detail.text(.03,.85,"Green vertical intervals: allowed bands\nHorizontal green strip: −1 ≤ f ≤ 1",transform=detail.transAxes,fontsize=10)

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
