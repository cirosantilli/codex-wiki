"""Original struck-stick geometry; Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Writes only the same-basename PNG in the CWD.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(11.8, 5.3))
    critical = 1 / (2 * np.pi)
    for ax, beta, heading in zip(axes, [0.10, critical, 0.22], ["Contact", "Grazing limit", "Clearance"]):
        for psi, color, width, label in [(0, "#b8bfc5", 2, "Initially"),
                                          (np.pi/4, "#b55d15", 2, r"$\psi=\pi/4$"),
                                          (np.pi/2, "#126782", 3, r"$\psi=\pi/2$")]:
            centre = np.array([2 * beta * psi, 0.0])
            direction = np.array([-np.sin(psi), np.cos(psi)])
            endpoints = np.array([centre - 0.5 * direction, centre + 0.5 * direction])
            ax.plot(endpoints[:, 0], endpoints[:, 1], color=color, lw=width, label=label)
            ax.scatter(*centre, color=color, s=20, zorder=4)
        ax.scatter([0], [0], color="#b3443c", s=75, marker="x", lw=2, zorder=6)
        ax.text(-0.12, -0.14, "Pole", color="#b3443c", ha="right", fontsize=11)
        ax.axhline(0, color="#d2d7dc", ls=":", lw=0.7, zorder=0)
        trailing = np.pi * beta - 0.5
        ax.scatter([trailing], [0], facecolors="white", edgecolors="#126782", s=55, lw=1.7, zorder=5)
        ax.text(0.38, 0.60, heading, ha="center", fontsize=14,
                color="#287d53" if beta > critical else "#b3443c")
        ax.text(0.38, 0.43, rf"$\beta={beta:.5f}$", ha="center", fontsize=12)
        ax.text(0.38, -0.61, rf"Trailing end: $x/l={trailing:.3f}$", ha="center", fontsize=11)
        ax.set(xlim=(-0.45, 1.20), ylim=(-0.78, 0.77), aspect="equal")
        ax.set_axis_off()
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 0.88), ncol=3, frameon=False)
    fig.suptitle("An end impulse: translation must outrun the first quarter-turn", fontsize=17, y=0.97)
    fig.text(0.5, 0.14, r"$V=J/m$,  $\Omega=J/(2\beta ml)$,  $x_{\mathrm{trail}}(\pi/2)=l(\pi\beta-1/2)$",
             ha="center", fontsize=14)
    fig.text(0.5, 0.065, r"Strict clearance: $\beta>1/(2\pi)$; equality just grazes the ideal point pole.",
             ha="center", fontsize=13)
    fig.text(0.5, 0.02, "Snapshots assume free motion up to contact; no post-collision trajectory is implied.",
             ha="center", fontsize=10, color="#596672")
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.22, top=0.79, wspace=0.12)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
