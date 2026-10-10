"""Draw buffer-ratio-ph.png in the current working directory.

Henderson-Hasselbalch concentration approximation with stipulated pKa = 4.76.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Build from the repository root: make _media/buffer-ratio-ph.png
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    pka = 4.76
    ratio = np.geomspace(0.1, 10, 401)
    ph = pka + np.log10(ratio)
    marked_ratios = np.array([0.1, 1, 2, 10])
    marked_ph = pka + np.log10(marked_ratios)
    np.testing.assert_allclose(marked_ph, [3.76, 4.76, 5.061029995663981, 5.76],
                               rtol=0, atol=1e-14)
    np.testing.assert_allclose(pka + np.log10(10 * ratio) - ph, 1,
                               rtol=0, atol=1e-14)
    # Verify the activity-equilibrium identity used to obtain the approximation.
    ka = 10.0 ** -pka
    np.testing.assert_allclose(np.power(10.0, -ph) * ratio, ka, rtol=1e-14)
    # At fixed ratio, scaling both concentrations leaves the approximation unchanged.
    assert math.isclose(pka + math.log10(0.020 / 0.010),
                        pka + math.log10(0.0020 / 0.0010), abs_tol=1e-14)

    plt.rcParams.update({"font.size": 14, "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.8, 5.6), facecolor="white")
    fig.subplots_adjust(left=0.11, right=0.96, top=0.79, bottom=0.24)
    fig.suptitle("A buffer's pH depends on the partner ratio", fontsize=21, y=0.96)
    fig.text(0.5, 0.86, r"$\mathrm{pH}\approx4.76+\log_{10}([\mathrm{A}^-]/[\mathrm{HA}])$",
             ha="center", fontsize=16)
    ax.semilogx(ratio, ph, color="#3d7f51", lw=3)
    ax.axhline(pka, color="#888888", lw=1.2, ls="--")
    ax.scatter(marked_ratios, marked_ph, color="#3d7f51", s=55, zorder=4)
    labels = ["Ratio 0.1\npH 3.76", "Equal partners\npH 4.76",
              "Ratio 2\npH 5.06103", "Ratio 10\npH 5.76"]
    for r, p, label, offset, alignment in zip(
            marked_ratios, marked_ph, labels,
            [(12, 8), (-12, 18), (20, -48), (-12, -42)],
            ["left", "right", "left", "right"]):
        ax.annotate(label, xy=(r, p), xytext=offset, textcoords="offset points",
                    ha=alignment, fontsize=13,
                    arrowprops={"arrowstyle": "-", "color": "#777777"})
    ax.set(xlim=(0.085, 11.8), ylim=(3.55, 5.97), xticks=[0.1, 1, 2, 10],
           yticks=[3.76, 4.76, 5.76], ylabel="pH",
           xlabel=r"Conjugate-base / weak-acid concentration ratio $[\mathrm{A}^-]/[\mathrm{HA}]$")
    ax.set_xticklabels(["0.1", "1", "2", "10"])
    ax.minorticks_off()
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#dddddd", lw=0.7)
    fig.text(0.5, 0.10, "Stipulated pKa = 4.76; ideal dilute partners at equilibrium.",
             ha="center", fontsize=12, color="#444444")
    fig.text(0.5, 0.045, "Water ionization neglected; curve is a calculation, not measured data.",
             ha="center", fontsize=12, color="#444444")
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Verified ratio 2 → pH {marked_ph[2]:.12f}; ratio 1 → pH {pka:.2f}.")
    print("Verified decade change → +1 pH, Ka activity identity, and common-scale invariance.")


if __name__ == "__main__":
    main()
