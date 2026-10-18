"""Original linearized power-law orbit illustrations; Python 3.14,
NumPy 2.3.5, Matplotlib 3.10.7. Writes only a same-basename CWD PNG.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(11.8, 5.2))
    reference = np.linspace(0, 2*np.pi, 500)
    for ax, power, title in zip(axes, [2.0, 7.0, -1.75],
                                ["Two radial cycles per turn", "Three radial cycles per turn", "One radial cycle in two turns"]):
        ratio = np.sqrt(power + 2)
        angle = np.linspace(0, 4*np.pi if power < -1 else 2*np.pi, 2401)
        radius = 1 + 0.08*np.cos(ratio*angle)
        ax.plot(np.cos(reference), np.sin(reference), color="#c6cdd3", lw=1, ls="--")
        if power < -1:
            mid = len(angle)//2
            ax.plot(radius[:mid+1]*np.cos(angle[:mid+1]), radius[:mid+1]*np.sin(angle[:mid+1]),
                    color="#126782", lw=2.2, label="First revolution")
            ax.plot(radius[mid:]*np.cos(angle[mid:]), radius[mid:]*np.sin(angle[mid:]),
                    color="#b55d15", lw=2.2, label="Second revolution")
            ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.13), frameon=False, fontsize=10)
        else:
            ax.plot(radius*np.cos(angle), radius*np.sin(angle), color="#126782", lw=2.2)
        for phi in ([0.6, 2*np.pi+0.6] if power < -1 else [0.65, 3.4]):
            p0 = (1+0.08*np.cos(ratio*phi))*np.array([np.cos(phi), np.sin(phi)])
            p1 = (1+0.08*np.cos(ratio*(phi+0.13)))*np.array([np.cos(phi+0.13), np.sin(phi+0.13)])
            ax.annotate("", p1, p0, arrowprops={"arrowstyle": "->", "color": "#b55d15" if phi>2*np.pi else "#126782", "lw": 1.5})
        ax.scatter([0], [0], s=22, color="#233746")
        ax.text(0, -0.18, "Force centre", ha="center", fontsize=10, color="#596672")
        ax.set(xlim=(-1.25, 1.25), ylim=(-1.25, 1.25), aspect="equal")
        ax.set_axis_off()
        shown = "-7/4" if power < -1 else str(int(power))
        ax.set_title(rf"$k={shown}$; $\omega_r/\Omega={ratio:g}$"+"\n"+title, fontsize=12)
    fig.suptitle("Near-circular orbits in a power-law potential", fontsize=17, y=0.97)
    fig.text(0.5, 0.15, r"$V(r)=\beta r^k$,  $r/r_0=1+0.08\cos(\sqrt{k+2}\,\phi)$", ha="center", fontsize=14)
    fig.text(0.5, 0.075, "These are leading small-amplitude sketches. The harmonic case tends to a centred ellipse.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.025, "For k = 7 and k = -7/4, linearized closure does not imply exact finite-amplitude closure.",
             ha="center", fontsize=11, color="#596672")
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.30, top=0.77, wspace=0.17)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
