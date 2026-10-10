"""Synthetic species fractions at externally imposed pH, not a pure HA sample.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
Counterions and the external pH-setting reservoir are omitted from the schematic.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    ka = 1e-5
    ph = np.linspace(2, 8, 401)
    h = 10.0**(-ph)
    fraction_a = ka / (ka + h)
    fraction_ha = h / (ka + h)
    np.testing.assert_allclose(fraction_a + fraction_ha, 1, atol=2e-16)
    np.testing.assert_allclose(h * fraction_a / fraction_ha, ka, rtol=3e-15)
    # Independent ratio from the Henderson-Hasselbalch rearrangement.
    np.testing.assert_allclose(fraction_a / fraction_ha, 10.0**(ph - 5), rtol=3e-15)
    exact_a = np.array([1/11, 1/2, 10/11])
    samples = ka / (ka + 10.0**(-np.array([4, 5, 6])))
    np.testing.assert_allclose(samples, exact_a, rtol=2e-15)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig = plt.figure(figsize=(9.6, 5.8), layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[1, 3])
    reaction = fig.add_subplot(grid[0, :])
    reaction.set_axis_off()
    reaction.text(0.5, 0.72,
                  r"$\mathrm{HA(aq)+H_2O(l)\ \rightleftharpoons\ H_3O^+(aq)+A^-(aq)}$",
                  fontsize=19, ha="center")
    reaction.text(0.5, 0.24, "HA / A⁻ differ by one proton; water accepts that proton",
                  ha="center", fontsize=12)
    curves = fig.add_subplot(grid[1, 0])
    curves.plot(ph, fraction_ha, color="#8042a0", lw=2.5, label="HA")
    curves.plot(ph, fraction_a, color="#007f8b", lw=2.5, label="A⁻")
    curves.axvline(5, ls=":", color="#777777")
    curves.plot([5, 5], [0.5, 0.5], "o", color="#222222")
    curves.set(xlabel="Externally imposed pH", ylabel="Fraction of total acid",
               xlim=(2, 8), ylim=(0, 1.05), title="Equal fractions at pH = pKa = 5")
    curves.legend()
    curves.grid(alpha=0.2)
    bars = fig.add_subplot(grid[1, 1])
    x = np.arange(3)
    bars.bar(x, 1 - exact_a, color="#8042a0", width=0.55, label="HA")
    bars.bar(x, exact_a, bottom=1 - exact_a, color="#007f8b", width=0.55, label="A⁻")
    for xi, ai in zip(x, exact_a, strict=True):
        bars.text(xi, (1-ai)/2, f"{100*(1-ai):.1f}%", color="white",
                  ha="center", va="center", fontsize=10)
        bars.text(xi, 1-ai+ai/2, f"{100*ai:.1f}%", color="white",
                  ha="center", va="center", fontsize=10)
    bars.set(xticks=x, xticklabels=["pH 4", "pH 5", "pH 6"], ylim=(0, 1.05),
             ylabel="Fraction of total acid", title="Same total acid, different partition")
    bars.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2)
    fig.suptitle("Equilibrium species of a synthetic monoprotic acid", fontsize=16)
    fig.supxlabel("Ideal activities; fixed temperature. External pH control and counterions omitted.",
                  fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
