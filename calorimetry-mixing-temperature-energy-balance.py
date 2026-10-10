"""Original synthetic water-mixing balance; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; write the matching PNG basename into the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


def main():
    cw, mh, mc = 4180.0, 0.100, 0.200
    th, tc, ccal = 80.0, 20.0, 100.0
    ch, cc = mh * cw, mc * cw
    tf = (ch * th + (cc + ccal) * tc) / (ch + cc + ccal)
    qh, qc, qcal = ch * (th - tf), cc * (tf - tc), ccal * (tf - tc)
    assert np.isclose(qh, qc + qcal, atol=1e-9)
    capacities = np.linspace(0, 300, 301)
    finals = (ch * th + (cc + capacities) * tc) / (ch + cc + capacities)
    assert np.all(np.diff(finals) < 0)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14, "axes.labelsize": 12})
    fig, (flow, graph) = plt.subplots(1, 2, figsize=(11.8, 5.7),
                                     gridspec_kw={"width_ratios": [1.18, 1]}, layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Water mixing: an insulated vessel still absorbs energy", fontsize=17)
    flow.set(xlim=(0, 10), ylim=(0, 10))
    flow.axis("off")

    def box(x, y, width, height, text, color):
        flow.add_patch(FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.12",
                                     facecolor=color, edgecolor="#40464d", linewidth=1.2))
        flow.text(x + width / 2, y + height / 2, text, ha="center", va="center")

    box(0.25, 3.25, 3.55, 3.4,
        f"Hot water\n0.100 kg at 80 °C\n\nReleases {qh / 1000:.3f} kJ", "#fde1d9")
    box(6.4, 6.3, 3.3, 2.5, "Cold water\n0.200 kg at 20 °C", "#dfeff9")
    box(6.4, 1.6, 3.3, 2.5, "Vessel + immersed parts\n100 J/K at 20 °C", "#eee9f7")
    for end, value in [((6.2, 7.1), qc), ((6.2, 3.0), qcal)]:
        flow.annotate("", xy=end, xytext=(3.98, 5.1),
                      arrowprops={"arrowstyle": "->", "lw": 2.4, "color": "#b95525"})
        flow.text(5.0, (end[1] + 5.1) / 2 + (0.35 if end[1] > 5 else -0.5),
                  f"{value / 1000:.3f} kJ", ha="center", color="#913717",
                  bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    flow.text(5, 9.45, "Heat transfers inside the combined boundary", ha="center", fontsize=13)
    flow.text(5, 0.5, f"All finish at {tf:.3f} °C   •   No room losses", ha="center", fontsize=13)
    flow.text(5, -0.05, "Synthetic example; water specific heat = 4180 J/(kg K)",
              ha="center", fontsize=10.5)
    graph.plot(capacities, finals, color="#1e6b8b", lw=2.5)
    graph.scatter([ccal], [tf], color="#b95525", s=65, zorder=4)
    graph.axvline(ccal, color="#b95525", ls=":", lw=1.3)
    graph.annotate(f"100 J/K → {tf:.3f} °C", xy=(ccal, tf), xytext=(130, 39.3),
                   arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=12)
    graph.scatter([0], [40], color="#1e6b8b", s=40)
    graph.text(12, 40.1, "Ignoring vessel: 40 °C", fontsize=11)
    graph.set(title="Separate runs with different vessel capacities",
              xlabel="Vessel heat capacity (J/K)", ylabel="Final common temperature (°C)",
              xlim=(0, 300), ylim=(35.5, 40.8))
    graph.grid(alpha=0.22)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
