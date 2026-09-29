"""Draw ph-logarithmic-scale.png in the current working directory.

Activity definition of pH; concentration labels assume an ideal dilute solution.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Build from the repository root: make _media/ph-logarithmic-scale.png
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    ph = np.linspace(2, 6, 401)
    activity = np.power(10.0, -ph)
    np.testing.assert_allclose(-np.log10(activity), ph, rtol=0, atol=1e-14)
    np.testing.assert_allclose(np.power(10.0, -np.arange(2, 7))[:-1]
                               / np.power(10.0, -np.arange(2, 7))[1:], 10)
    assert -math.log10(0.001) == 3
    assert -math.log10(0.001 / 10) == 4
    # Compare the neglect of water with the exact ideal strong-acid model.
    # Charge balance h = C + [OH-] and h[OH-] = Kw, in mol/L units.
    kw = 1e-14
    exact_ph = [-math.log10((c + math.sqrt(c * c + 4 * kw)) / 2)
                for c in (1e-3, 1e-4)]
    np.testing.assert_allclose(exact_ph, [3, 4], rtol=0, atol=5e-7)

    plt.rcParams.update({"font.size": 14, "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.8, 5.6), facecolor="white")
    fig.subplots_adjust(left=0.15, right=0.96, top=0.79, bottom=0.23)
    fig.suptitle("pH: equal steps mean factors of ten", fontsize=21, y=0.96)
    fig.text(0.5, 0.86, r"$\mathrm{pH}=-\log_{10}a_{\mathrm{H}^+}$"
             "     |     Activity is dimensionless", ha="center", fontsize=15)
    ax.semilogy(ph, activity, color="#286c9c", lw=3)
    for p in range(2, 7):
        ax.plot([p], [10.0 ** -p], "o", color="#286c9c", ms=7)
    ax.annotate("Ideal strong acid\n0.001 mol/L → pH 3", xy=(3, 1e-3),
                xytext=(2.1, 2.3e-4), fontsize=13,
                arrowprops={"arrowstyle": "->", "color": "#444444"})
    ax.annotate("Tenfold dilution\n0.0001 mol/L → pH 4", xy=(4, 1e-4),
                xytext=(4.35, 7e-4), fontsize=13,
                arrowprops={"arrowstyle": "->", "color": "#444444"})
    ax.set(xlim=(1.9, 6.1), ylim=(7e-7, 1.5e-2), xticks=range(2, 7),
           yticks=[10.0 ** -p for p in range(2, 7)], xlabel="pH",
           ylabel=r"Hydrogen-ion activity $a_{\mathrm{H}^+}$")
    ax.minorticks_off()
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#dddddd", lw=0.7)
    fig.text(0.5, 0.10, "Concentration labels: ideal dilute model; water ionization neglected.",
             ha="center", fontsize=12, color="#444444")
    fig.text(0.5, 0.045, "This plotted interval is not a limit on possible pH values.",
             ha="center", fontsize=12, color="#444444")
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified pH 3 → 4 for tenfold dilution; tenfold activity per pH step.")
    print(f"Including ideal water ionization at Kw=1e-14: pH {exact_ph[0]:.9f}, "
          f"{exact_ph[1]:.9f}; approximation errors < 5e-7 pH units.")


if __name__ == "__main__":
    main()
