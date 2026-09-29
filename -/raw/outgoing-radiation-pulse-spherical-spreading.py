"""Draw outgoing-radiation-pulse-spherical-spreading.png in cwd.

Angularly averaged leading far-field pulse model, not a spherically symmetric
vector Maxwell solution or a measurement. Emission is P0*sin²(pi*s/tau)
for 0 <= s <= tau and zero outside that interval; L = c*tau.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
import numpy as np


def emission(q):
    return np.where((q >= 0) & (q <= 1), np.sin(np.pi * q) ** 2, 0.0)


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    blue, orange, green = "#1766a6", "#bc5710", "#23744a"
    fig = plt.figure(figsize=(10.6, 8.0), facecolor="white")
    fig.suptitle("An outgoing pulse spreads; its total energy stays the same", fontsize=17, y=0.98)
    fig.text(0.5, 0.927, r"Angularly averaged far-field model: $\overline{S}_r=P_{\rm emit}(t-r/c)/(4\pi r^2)$",
             ha="center", fontsize=13)

    for rectangle, time, color in [((0.10, 0.54, 0.33, 0.32), 3, blue),
                                    ((0.59, 0.54, 0.33, 0.32), 5, orange)]:
        ax = fig.add_axes(rectangle, facecolor="white")
        ax.add_patch(Wedge((0, 0), time, 0, 360, width=1, color=color, alpha=0.16))
        for radius in (time - 1, time):
            ax.add_patch(Circle((0, 0), radius, fill=False, color=color, lw=1.7))
        ax.plot(0, 0, "o", color="#333333", ms=5)
        ax.text(0, -0.65, "Source", ha="center", fontsize=10)
        ax.annotate("", (time, 0), (0, 0), arrowprops={"arrowstyle": "->", "color": color})
        ax.text(time / 2, 0.35, rf"$ct={time}L$", ha="center", color=color)
        ax.annotate("", (0, time), (0, time - 1),
                    arrowprops={"arrowstyle": "<->", "color": "#333333"})
        ax.text(0.3, time - 0.5, r"$L$", va="center")
        ax.set_title(rf"$t={time}\tau$: shell from ${time-1}L$ to ${time}L$", pad=8)
        ax.set(xlim=(-5.5, 5.5), ylim=(-5.5, 5.5), aspect="equal")
        ax.axis("off")
    fig.text(0.5, 0.52, r"Same length scale in both snapshots. Shell thickness $L=c\tau$; shading marks support only.",
             ha="center", fontsize=10.5)

    density = fig.add_axes((0.10, 0.14, 0.37, 0.29), facecolor="white")
    position = np.linspace(0, 6, 1801)
    for time, color in [(3, blue), (5, orange)]:
        profile = emission(time - position)
        density.plot(position, profile, color=color, lw=2.5, label=rf"$t={time}\tau$")
        density.fill_between(position, profile, color=color, alpha=0.12)
    density.set(xlim=(0, 6), ylim=(0, 1.18), xlabel=r"Radius $r/L$",
                ylabel=r"$(c/P_0)\,dU/dr$")
    density.set_title("Energy per radius translates outward", pad=12, fontsize=12)
    density.legend(loc="upper left", fontsize=11)
    density.grid(alpha=0.2)
    density.text(0.5, 0.68, r"Both areas $=1/2$", transform=density.transAxes, ha="center", fontsize=11)

    dilution = fig.add_axes((0.61, 0.14, 0.35, 0.29), facecolor="white")
    ratio = np.linspace(1, 4, 501)
    dilution.plot(ratio, 1 / ratio, color=green, lw=2.5, label=r"Field: $E(r)/E(r_0)=r_0/r$")
    dilution.plot(ratio, 1 / ratio ** 2, color=blue, lw=2.5, ls="--",
                  label=r"Flux: $S_r(r)/S_r(r_0)=(r_0/r)^2$")
    dilution.scatter([2, 2], [0.5, 0.25], color=[green, blue], zorder=3)
    dilution.annotate("1/2", (2, 0.5), xytext=(2.18, 0.53), color=green, fontsize=11)
    dilution.annotate("1/4", (2, 0.25), xytext=(2.18, 0.25), color=blue, fontsize=11)
    dilution.set(xlim=(1, 4), ylim=(0, 1.12), xlabel=r"Distance ratio $r/r_0$", ylabel="Ratio to reference value")
    dilution.set_title("Compare the same emitted instant", pad=12, fontsize=12)
    dilution.legend(loc="upper right", fontsize=9.5)
    dilution.grid(alpha=0.2)
    fig.text(0.285, 0.062, r"Shell energy $U=P_0\tau/2$ at either time", ha="center", fontsize=11)
    fig.text(0.5, 0.018, "Calculated model, not measured data. Fixed-direction ratios use corresponding arrival times in the radiation zone.",
             ha="center", fontsize=10.5)
    fig.savefig("outgoing-radiation-pulse-spherical-spreading.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
