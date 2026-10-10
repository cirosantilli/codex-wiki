"""Original LS-model ratio inversion and field-drift diagnostic.

Writes its matching PNG to the CWD. Python 3.14, matplotlib 3.10, numpy 2.3.
The bracketing protocol is an explanatory proposal, not historical data.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def infer_anomaly(r):
    return (r-2)/(r+1)


def main():
    plt.rcParams.update({"font.size":11, "axes.spines.top":False,
                         "axes.spines.right":False})
    a0 = .0012
    ratio0 = (2+a0)/(1-a0)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.7), facecolor="white")
    fig.subplots_adjust(left=.08, right=.97, bottom=.20, top=.76, wspace=.31)
    x = np.linspace(1.99, 2.012, 401)
    r = (2+x)/(4-x)
    axes[0].plot(x, r, color="#265b9a", lw=2)
    axes[0].scatter([2, 2.0024], [2, ratio0], c=[".45", "#c47a23"], zorder=4, s=44)
    axes[0].axhline(2, color=".7", lw=.8)
    axes[0].axvline(2, color=".7", lw=.8)
    axes[0].annotate("Chosen spin ratio 2.0024\nfrequency ratio 2.0036043", (2.0024, ratio0),
                     (1.994, 2.012), arrowprops={"arrowstyle":"->", "color":".35"}, fontsize=10)
    axes[0].text(.07, .09, r"$R=(2+x)/(4-x)$"+"\n"+r"$x=(4R-2)/(R+1)$",
                 transform=axes[0].transAxes, fontsize=12)
    axes[0].set(xlabel=r"Spin-to-orbital ratio $x=g_s/g_L$", ylabel=r"Electronic frequency ratio $R$",
                 title="Different moments have different weights", xlim=(1.99, 2.012))
    axes[0].set_xticks([1.99, 1.995, 2, 2.005, 2.01],
                       ["1.990", "1.995", "2.000", "2.005", "2.010"])
    axes[0].ticklabel_format(axis="y", useOffset=False)

    b_tau = np.linspace(-.002, .002, 401)
    unpaired = infer_anomaly(ratio0/(1-b_tau))
    bracket = np.full_like(b_tau, a0)
    curved = np.full_like(b_tau, infer_anomaly(ratio0/(1+.0002)))
    axes[1].plot(b_tau*1000, unpaired*1000, color="#b5523c", label="Unpaired reading")
    axes[1].plot(b_tau*1000, bracket*1000, color="#265b9a", lw=2, label="Symmetric bracket, linear field")
    axes[1].plot(b_tau*1000, curved*1000, "--", color="#51844d", label=r"Bracket, $c\tau^2=0.0002$")
    bad = infer_anomaly(ratio0/(1-.001))
    axes[1].scatter([1], [bad*1000], color="#b5523c", zorder=4)
    axes[1].annotate(f"Unpaired: {bad:.8f}", (1, bad*1000), (-.8, 2.35),
                     arrowprops={"arrowstyle":"->", "color":".35"}, fontsize=10)
    axes[1].set(xlabel=r"Linear field drift $1000b\tau$", ylabel=r"Inferred anomaly $1000a_e$",
                 title="A small field change can imitate the anomaly", xlim=(-2, 2), ylim=(-.25, 2.7))
    axes[1].legend(loc="lower right", fontsize=9)
    fig.suptitle("Frequency ratios remove a scale only when it is shared", y=.97, fontsize=17)
    fig.text(.5, .885, r"Original model: $g_L=1$, $g_s=2.0024$, true $a_e=0.0012$; $C(t)=C_0(1+bt+ct^2)$",
             ha="center", fontsize=12)
    fig.text(.5, .825, "No nuclear spin or atomic corrections; the proposed bracket is not a historical measurement record",
             ha="center", color=".3", fontsize=10)
    fig.text(.5, .055, r"The bracket cancels linear drift. Quadratic curvature, different sampled fields and additive offsets survive.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
