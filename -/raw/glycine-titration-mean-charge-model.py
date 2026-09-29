"""Draw ideal glycine titration and mean charge models (Python 3.14).

Run from _media. This is not a fit or an experimental data reconstruction.
The solid curve solves charge balance for 20 mL 0.100 M glycine plus one
equivalent HCl, titrated with 0.100 M NaOH. Volumes add, activity coefficients
are one, and Kw=1e-14 is stipulated at 25 C. The dashed curve neglects free
water ions. Each generator is self-contained and writes its own basename.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


PKA1, PKA2 = 2.35, 9.78
PI = (PKA1 + PKA2) / 2
KW, C0 = 1e-14, 0.100


def mean_charge(ph):
    h = 10.0 ** (-np.asarray(ph))
    k1, k2 = 10.0**-PKA1, 10.0**-PKA2
    return (h * h - k1 * k2) / (h * h + k1 * h + k1 * k2)


def charge_balance(ph, base_equivalents):
    h = 10.0 ** (-ph)
    ct = C0 / (1 + base_equivalents)
    return h - KW / h + ct * (base_equivalents + mean_charge(ph) - 1)


def titration_ph(base_equivalents):
    # The residual decreases monotonically as pH increases.
    lo = np.zeros_like(base_equivalents)
    hi = np.full_like(base_equivalents, 14.0)
    for _ in range(70):
        mid = (lo + hi) / 2
        positive = charge_balance(mid, base_equivalents) > 0
        lo = np.where(positive, mid, lo)
        hi = np.where(positive, hi, mid)
    return (lo + hi) / 2


def equivalents_at_ph(ph):
    h = 10.0**-ph
    q = (KW / h - h) / C0
    return (1 - mean_charge(ph) + q) / (1 - q)


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig, (ax, charge_ax) = plt.subplots(2, 1, figsize=(11, 8.5), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.09, right=0.965, top=0.86, bottom=0.11, hspace=0.48)
    fig.suptitle("Glycine titration and mean charge — calculated models", fontsize=18, y=0.969)
    fig.text(0.5, 0.916, "Stipulated pKa₁ = 2.35, pKa₂ = 9.78; pI = 6.065; ideal activities, 25 °C",
             ha="center", fontsize=12)
    base = np.unique(np.r_[np.linspace(0, 2.2, 1401), [0.5, 1, 1.5, 2]])
    ax.plot(base, titration_ph(base), color="#345b94", lw=2.8,
            label="Water ions + dilution + charge balance")
    ph = np.linspace(0, 14, 2001)
    ax.plot(1 - mean_charge(ph), ph, color="#777777", ls="--", lw=1.7,
            label="Glycine proton inventory only: b = 1 − z̄")
    for p, name, offset in ((PKA1, "pKa₁", (30, 12)), (PI, "pI", (32, -7)),
                            (PKA2, "pKa₂", (20, -28))):
        b = float(equivalents_at_ph(p))
        ax.scatter(b, p, s=35, color="#345b94", zorder=5)
        ax.annotate(f"{name} = {p:g}\nb = {b:.3f}", (b, p), xytext=offset,
                    textcoords="offset points", fontsize=10,
                    arrowprops={"arrowstyle": "-", "color": "#555555"},
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.set(xlim=(0, 2.2), ylim=(1, 13), xlabel="Added NaOH / initial glycine, b (mol/mol)", ylabel="Calculated pH")
    ax.set_xticks([0, 0.5, 1, 1.5, 2])
    ax.grid(alpha=0.18)
    ax.legend(loc="lower right", fontsize=10, frameon=True, framealpha=1)
    charge = mean_charge(ph)
    charge_ax.fill_between(ph, 0, charge, where=charge >= 0, color="#1764a1", alpha=0.14)
    charge_ax.fill_between(ph, 0, charge, where=charge <= 0, color="#c25823", alpha=0.14)
    charge_ax.plot(ph, charge, color="#303d4f", lw=2.8)
    charge_ax.axhline(0, color="#777777", lw=1)
    charge_ax.axvline(PI, color="#777777", lw=1.2, ls=":")
    charge_ax.scatter([PI], [0], color="#303d4f", zorder=5)
    charge_ax.text(PI, 0.25, "pI = 6.065\nmean charge zero", ha="center", fontsize=11,
                   bbox={"facecolor": "white", "edgecolor": "none"})
    charge_ax.text(1.1, -0.78, "positive mean charge\n→ negative electrode", color="#1764a1", fontsize=11)
    charge_ax.text(10.1, 0.64, "negative mean charge\n→ positive electrode", color="#a0441a", fontsize=11)
    charge_ax.set(xlim=(0, 14), ylim=(-1.1, 1.1), xlabel="pH", ylabel="Mean charge / e, z̄")
    charge_ax.grid(alpha=0.18)
    fig.text(0.5, 0.04, "Solid curve: 20 mL of 0.100 M glycine + 1 eq HCl; 0.100 M NaOH. No measured data.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
