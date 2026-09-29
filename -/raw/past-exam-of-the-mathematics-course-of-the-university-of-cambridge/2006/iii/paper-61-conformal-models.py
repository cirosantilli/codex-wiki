"""Original conformal diagrams; output opaque basename PNG to caller CWD.

Repository dependencies: Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Caller controls MPLBACKEND and MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def main():
    pi = np.pi
    fig, (ds, ads) = plt.subplots(1, 2, figsize=(12.6, 6.4), dpi=100,
                                 gridspec_kw={"width_ratios": [1.7, 1]}, facecolor="white")
    fig.subplots_adjust(left=0.065, right=0.925, top=0.86, bottom=0.16, wspace=0.30)
    ds.set(xlim=(-pi, pi), ylim=(-pi/2, pi/2), xlabel=r"$\chi$", ylabel=r"$\eta$")
    ds.set_aspect("equal", adjustable="box")
    ds.set_anchor("N")
    ds.set_title("de Sitter: finite conformal-time cylinder", fontsize=12, pad=23)
    for y in [-pi/2, pi/2]:
        ds.plot([-pi, pi], [y, y], color="0.35", lw=2.7)
    for x in [-pi, pi]:
        ds.plot([x, x], [-pi/2, pi/2], color="0.5", lw=1.1, ls="--")
    ds.add_patch(Polygon([(-pi/2, 0), (0, pi/2), (pi/2, 0), (0, -pi/2)],
                         facecolor="#f2e9fa", edgecolor="none", label="Static patch"))
    eta = np.linspace(-pi/2, pi/2, 401)
    for sign in [-1, 1]:
        ds.plot(sign*(pi/2-eta), eta, color="#8e44ad", ls="--", lw=1.7,
                label="Future event horizon" if sign == 1 else None)
        ds.plot(sign*(eta+pi/2), eta, color="#2980b9", ls=":", lw=1.9,
                label="Past observer horizon" if sign == 1 else None)
    ds.plot(eta+pi/3, eta, color="#d62728", lw=2, label="Null geodesic")
    ds.plot([0, 0], [-pi/2, pi/2], color="black", lw=1.3, label="Observer")
    ds.set_xticks([-pi,-pi/2,0,pi/2,pi], [r"$-\pi$",r"$-\pi/2$","0",r"$\pi/2$",r"$\pi$"])
    ds.set_yticks([-pi/2,0,pi/2], [r"$-\pi/2$","0",r"$\pi/2$"])
    ds.text(0.02, 1.035, r"$\mathcal{I}^{+}$: spacelike", transform=ds.transAxes, fontsize=10)
    ds.text(0.02, -0.145, r"$\mathcal{I}^{-}$: spacelike", transform=ds.transAxes, fontsize=10)
    ds.legend(loc="upper center", bbox_to_anchor=(0.52,-0.23), ncol=2, fontsize=9,
              frameon=False, columnspacing=1.1)
    ds.text(0.5, -0.53, "Left and right spatial edges are identified.",
            transform=ds.transAxes, ha="center", fontsize=10)

    ads.set(xlim=(-pi/2, pi/2), ylim=(-pi, pi), xlabel=r"$\psi$", ylabel=r"$t$")
    ads.set_aspect("equal", adjustable="box")
    ads.set_anchor("N")
    ads.set_title("anti-de Sitter: covering strip", fontsize=12, pad=23)
    for x in [-pi/2, pi/2]:
        ads.plot([x,x],[-pi,pi],color="0.35",lw=2.7)
    ads.spines["top"].set_visible(False)
    ads.spines["bottom"].set_visible(False)
    psi=np.linspace(-pi/2,pi/2,401)
    ads.plot(psi,psi,color="#d62728",lw=2,label="Null geodesic")
    ads.plot([0,0],[-pi,pi],color="black",lw=1,ls=":")
    E=1.45
    s=np.linspace(-pi,pi,1201)
    r=np.arcsinh(np.sqrt(E*E-1)*np.sin(s))
    t=np.unwrap(np.arctan2(E*np.sin(s),np.cos(s)))
    ads.plot(np.arctan(np.sinh(r)),t,color="#2e8b57",lw=1.8,label="Timelike geodesic")
    ads.text(-pi/2-0.27,0,"Timelike boundary",rotation=90,ha="center",va="center",fontsize=10)
    ads.text(pi/2+0.16,0,"Timelike boundary",rotation=90,ha="center",va="center",fontsize=10)
    for sign in [-1,1]:
        ads.annotate("",xy=(1.05,sign*(pi+0.18)),xytext=(1.05,sign*(pi-0.20)),
                     arrowprops={"arrowstyle":"->","color":"0.25","lw":1.3},annotation_clip=False)
    ads.set_xticks([-pi/2,0,pi/2],[r"$-\pi/2$","0",r"$\pi/2$"])
    ads.set_yticks([-pi,-pi/2,0,pi/2,pi],[r"$-\pi$",r"$-\pi/2$","0",r"$\pi/2$",r"$\pi$"])
    ads.legend(loc="upper center",bbox_to_anchor=(0.5,-0.16),fontsize=9,frameon=False)
    fig.text(0.775,0.035,"Finite time window shown; covering time extends over R.",ha="center",fontsize=9)
    for ax in [ds,ads]:
        ax.tick_params(labelsize=10)
        ax.set_facecolor("white")
    fig.savefig(Path.cwd()/"paper-61-conformal-models.png",dpi=100,facecolor="white",transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
