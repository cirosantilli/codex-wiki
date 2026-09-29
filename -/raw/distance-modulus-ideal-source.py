"""Original distance/extinction toy diagram; writes its PNG basename to cwd.

Run from _media. Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig, (overview, inference) = plt.subplots(1, 2, figsize=(10.8, 4.9),
                                            layout="constrained", facecolor="white")
    fig.suptitle(r"One ideal source, fixed absolute magnitude $M=0$", fontsize=16)
    distance = np.geomspace(5, 1500, 400)
    magnitude = 5 * np.log10(distance / 10)
    blue, orange = "#175c9d", "#b95712"
    overview.plot(distance, magnitude, color=blue, lw=2.5, label=r"$A=0$ (transparent)")
    overview.plot(distance, magnitude + 1, color=orange, lw=2.3,
                  label=r"$A=1$ (fixed offset)")
    overview.set(xscale="log", xlim=(5, 1500), ylim=(-2.3, 12.5),
                 xlabel="True distance d (parsecs; logarithmic axis)",
                 ylabel="Apparent magnitude m (larger = fainter)",
                 title=r"$m=5\log_{10}(d/10\,\mathrm{pc})+A$")
    overview.set_xticks([10, 100, 1000], labels=["10", "100", "1000"])
    overview.set_yticks([0, 5, 10])
    overview.grid(alpha=0.23)
    overview.legend(loc="upper left", fontsize=10)
    for d, m in [(10, 0), (100, 5), (1000, 10)]:
        overview.scatter([d], [m], color=blue, zorder=3)
        overview.annotate(f"({d} pc, m={m})", (d, m), xytext=(6, -20),
                          textcoords="offset points", fontsize=9,
                          ha="right" if d == 1000 else "left")

    zoom = np.geomspace(70, 220, 200)
    inference.plot(zoom, 5 * np.log10(zoom / 10), color=blue, lw=2.5)
    inference.plot(zoom, 5 * np.log10(zoom / 10) + 1, color=orange, lw=2.3)
    true_distance = 100
    inferred_distance = true_distance * 10 ** (1 / 5)
    observed_magnitude = 6
    inference.set(xscale="log", xlim=(70, 220), ylim=(4.5, 7.6),
                  xlabel="Distance (parsecs; logarithmic axis)",
                  ylabel="Apparent magnitude m", title="Ignoring extinction overestimates distance")
    inference.set_xticks([100, inferred_distance, 200], labels=["100", "158.49", "200"])
    inference.set_yticks([5, 6, 7])
    inference.grid(alpha=0.23)
    inference.hlines(observed_magnitude, 72, 210, color="#555555", linestyle=":")
    inference.scatter([true_distance], [observed_magnitude], color=orange, zorder=4)
    inference.scatter([inferred_distance], [observed_magnitude], color=blue, zorder=4)
    inference.annotate("True: 100 pc\nwith A=1", (true_distance, observed_magnitude),
                       xytext=(78, 7.05), fontsize=10,
                       arrowprops={"arrowstyle": "->", "color": orange})
    inference.annotate("Inferred: 158.49 pc\nassuming A=0", (inferred_distance, observed_magnitude),
                       xytext=(125, 4.67), fontsize=10,
                       arrowprops={"arrowstyle": "->", "color": blue})
    inference.annotate("", (inferred_distance, 6.12), (true_distance, 6.12),
                       arrowprops={"arrowstyle": "<->", "color": "#333333"})
    inference.text(126, 6.25, r"$\times 10^{1/5}\approx1.58489$", ha="center", fontsize=10)
    fig.supxlabel("Illustrative toy values; unchanged emission, same passband; A=1 is not a dust-distance law",
                  fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
