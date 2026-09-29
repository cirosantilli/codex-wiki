"""Original radial conformal diagram; Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7.
Write the basename PNG to caller CWD; honor MPLCONFIGDIR. Angles are suppressed.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(8.8, 7.8), dpi=100, facecolor="white")
    fig.subplots_adjust(left=.12, right=.94, top=.88, bottom=.21)
    pi = np.pi
    ax.fill([0, pi, 0], [-pi, 0, pi], color="#edf5fa")
    ax.plot([0, pi], [pi, 0], color="#326f46", lw=2)
    ax.plot([0, pi], [-pi, 0], color="#326f46", lw=2)
    ax.plot([0, 0], [-pi, pi], color="#999999", lw=1.4)
    # Exact t->(T,R) transformation of a stationary Minkowski geodesic r=.8.
    t = np.concatenate((-np.geomspace(1000, 1, 250), np.linspace(-1,1,250), np.geomspace(1,1000,250)))
    p, q = np.arctan(t-.8), np.arctan(t+.8)
    T = np.concatenate(([-pi],p+q,[pi]))
    R = np.concatenate(([0],q-p,[0]))
    ax.plot(R,T,color="#2369a5",lw=2.2,label="Timelike inertial geodesic")
    # A complete radial light ray t=x: the radial chart reverses angle at r=0.
    null_T = np.linspace(-pi/2, pi/2, 400)
    ax.plot(np.abs(null_T),null_T,color="#c76622",lw=2.2,label="Null ray through the centre")
    ax.plot([0,pi],[0,0],color="#7d4a9d",lw=1.7,ls="--",label="Spacelike geodesic at t=0")
    for x,y in [(0,pi),(0,-pi),(pi,0)]:ax.plot(x,y,"o",color="#222222",ms=5)
    ax.text(.10,pi-.12,r"$i^+$",ha="left",va="top",fontsize=17)
    ax.text(.10,-pi+.12,r"$i^-$",ha="left",va="bottom",fontsize=17)
    ax.text(pi+.08,0,r"$i^0$",ha="left",va="center",fontsize=17)
    ax.text(1.80,1.65,r"$\mathcal{I}^+$",color="#326f46",fontsize=17)
    ax.text(1.80,-1.65,r"$\mathcal{I}^-$",color="#326f46",fontsize=17)
    ax.text(-.28,0,"Regular centre r=0",rotation=90,ha="center",va="center",color="#666666",fontsize=11)
    ax.set(xlim=(-.38,pi+.38),ylim=(-pi-.25,pi+.25),xlabel="R",ylabel="T",title=r"Minkowski region: $R\geq0,\ |T|+R<\pi$")
    ax.set_aspect("equal")
    ax.set_xticks([0,pi/2,pi],["0",r"$\pi/2$",r"$\pi$"])
    ax.set_yticks([-pi,-pi/2,0,pi/2,pi],[r"$-\pi$",r"$-\pi/2$","0",r"$\pi/2$",r"$\pi$"])
    ax.spines[["top","right"]].set_visible(False)
    fig.legend(loc="lower center",bbox_to_anchor=(.5,.015),frameon=False,fontsize=10)
    fig.suptitle("Finite conformal endpoints represent infinite physical parameter",fontsize=14,y=.96)
    fig.savefig(Path.cwd()/"paper-60-minkowski-compactification.png",facecolor="white",transparent=False)
    plt.close(fig)

if __name__ == "__main__":
    main()
