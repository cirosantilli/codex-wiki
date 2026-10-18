"""Original tunnel/runner spacetime diagrams; Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Writes only the same-basename CWD PNG.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    beta = 0.6
    gamma = 1/np.sqrt(1-beta**2)
    times = np.linspace(-1, 1.15, 400)
    blue, orange, purple, gray = "#126782", "#b55d15", "#80529b", "#596672"
    fig, (lab, runner) = plt.subplots(1, 2, figsize=(11.8, 6.5))
    lab.plot(np.zeros_like(times), times, color=gray, lw=1.5, label="Entrance")
    lab.plot(np.ones_like(times), times, color=gray, lw=1.5, ls="--", label="Far end")
    lab.plot(beta*times, times, color=blue, lw=2, label="Runner")
    photon_time = np.linspace(0, 1/(1+beta), 200)
    lab.plot(1-photon_time, photon_time, color=orange, lw=2.5, label="Photon")
    lab.plot([0, 1], [-beta, 0], color=purple, lw=1.4, ls=":", label="Simultaneous in runner frame")
    lab.plot([0, 1], [0, 0], color="#cbd1d6", lw=0.8)
    lab.scatter([0, 1, beta/(1+beta), 0], [0, 0, 1/(1+beta), -beta], color=[blue, orange, orange, purple], s=35, zorder=4)
    for x, y, text in [(-0.25, 0.07, "Entry O"), (1.04, -0.13, "Emission E"),
                       (0.60, 0.72, "Detection D"), (-0.70, -0.80, "Clock event G")]:
        lab.text(x, y, text, fontsize=10, bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.8, "pad": 1})
    lab.set(xlim=(-0.75, 1.65), ylim=(-1, 1.15), aspect="equal", xlabel=r"$x/L$", ylabel=r"$ct/L$", title="Tunnel frame")
    runner.plot(-beta*times, times, color=gray, lw=1.5)
    runner.plot(1/gamma-beta*times, times, color=gray, lw=1.5, ls="--")
    runner.plot(np.zeros_like(times), times, color=blue, lw=2)
    emission_time = -gamma*beta
    detection_time = 1/(gamma*(1+beta))
    tprime = np.linspace(emission_time, detection_time, 200)
    runner.plot(gamma-(tprime-emission_time), tprime, color=orange, lw=2.5)
    gap = gamma*beta**2
    runner.plot([0, gamma], [emission_time, emission_time], color=purple, ls=":", lw=1.4)
    runner.scatter([0, gamma, 0, gap], [0, emission_time, detection_time, emission_time],
                   color=[blue, orange, orange, purple], s=35, zorder=4)
    for x, y, text in [(-0.27, 0.07, "Entry O"), (1.04, -0.97, "Emission E"),
                       (0.65, 0.57, "Detection D"), (0.30, -0.65, "G")]:
        runner.text(x, y, text, fontsize=10, bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.8, "pad": 1})
    runner.annotate("", (0, emission_time-0.10), (gap, emission_time-0.10),
                    arrowprops={"arrowstyle": "<->", "color": purple, "lw": 1.2})
    runner.text(gap/2, emission_time-0.24, r"$\gamma\beta^2L$", ha="center", color=purple, fontsize=11)
    runner.set(xlim=(-0.75, 1.65), ylim=(-1.08, 1.15), aspect="equal", xlabel=r"$x'/L$", ylabel=r"$ct'/L$", title="Runner frame")
    for ax in [lab, runner]:
        ax.grid(alpha=0.12)
    handles, labels = lab.get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 0.90), ncol=3, frameon=False, fontsize=10)
    fig.suptitle("Tunnel photon timing: entry and emission are not simultaneous in both frames", fontsize=16, y=0.97)
    fig.text(0.5, 0.13, r"Example: $\beta=0.6$, $\gamma=1.25$. The photon travels $\gamma L$ in the runner frame.", ha="center", fontsize=13)
    fig.text(0.5, 0.065, r"At G the entrance clock reads $-vL/c^2$; the entrance is still ahead of the runner when E occurs in that frame.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.02, r"Subtract that initial gap to obtain the same interception fraction: $f=\beta/(1+\beta)=0.375$.",
             ha="center", fontsize=11, color=gray)
    fig.subplots_adjust(left=0.065, right=0.975, bottom=0.23, top=0.77, wspace=0.22)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
