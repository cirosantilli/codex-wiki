"""Synthetic ideal aqueous HA model; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
No material data or measured observations are represented.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


KA = 1e-5
KW = 1e-14


def equilibrium(c):
    """Solve charge balance for dimensionless h = [H3O+]/(1 mol/L)."""
    lo, hi = np.sqrt(KW), c + np.sqrt(KW)
    for _ in range(90):
        h = (lo + hi) / 2
        if h - KW / h - c * KA / (h + KA) > 0:
            hi = h
        else:
            lo = h
    h = (lo + hi) / 2
    return h, c * KA / (h + KA), c * h / (h + KA), KW / h


def main():
    c = np.logspace(-2, -10, 401)
    states = np.array([equilibrium(value) for value in c])
    h, a, ha, oh = states.T
    np.testing.assert_allclose(a + ha, c, rtol=2e-15)
    np.testing.assert_allclose(a + oh, h, rtol=2e-14)
    np.testing.assert_allclose(h * a / ha, KA, rtol=3e-15)
    np.testing.assert_allclose(h * oh, KW, rtol=2e-15)
    # Independent polynomial-root solution, scaled to avoid tiny coefficients.
    for ci, hi in zip(c[::5], h[::5], strict=True):
        scale = max(np.sqrt(KA * ci), np.sqrt(KW))
        roots = np.roots([1, KA / scale, -(KW + KA * ci) / scale**2,
                          -KA * KW / scale**3])
        positive = [r.real * scale for r in roots
                    if abs(r.imag) < 1e-12 and r.real > 0]
        assert len(positive) == 1
        np.testing.assert_allclose(positive[0], hi, rtol=2e-12)
    assert np.all(np.diff(a / c) > 0)
    assert np.all(np.diff(-np.log10(h)) > 0)
    assert np.all(h >= np.sqrt(KW))

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.9), layout="constrained")
    fig.suptitle("Dilution: more dissociation, less hydronium", fontsize=16)
    axes[0].semilogx(c, 100 * a / c, color="#007f8b", lw=2.5,
                    label="Full ideal balance")
    axes[0].axhline(100 * KA / (KA + np.sqrt(KW)), color="#666666", ls=":",
                   label="Infinite-dilution limit: 99.01%")
    axes[0].set(ylabel=r"Dissociated acid, $100[A^-]/C_T$ (%)", ylim=(0, 105))
    no_water = 2 * KA * c / (KA + np.sqrt(KA**2 + 4 * KA * c))
    axes[1].semilogx(c, -np.log10(h), lw=2.5, color="#007f8b",
                    label="Full ideal balance")
    axes[1].semilogx(c, -np.log10(no_water), ls="--", color="#aa5a00",
                    label="Quadratic: neglect water")
    axes[1].semilogx(c, -np.log10(np.sqrt(KA * c)), ls=":", color="#8042a0",
                    label="Square root: also neglect depletion")
    axes[1].axhline(7, color="#666666", lw=1)
    axes[1].text(2e-10, 7.15, "Neutral water", ha="right", fontsize=10)
    axes[1].set(ylabel="Calculated pH", ylim=(3, 10.3))
    for ax in axes:
        ax.set(xlabel=r"Total acid $C_T$ (mol L$^{-1}$)", xlim=(1e-2, 1e-10))
        ax.set_xticks([1e-2, 1e-4, 1e-6, 1e-8, 1e-10])
        ax.grid(alpha=0.2)
        ax.legend(fontsize=8.5, loc="best")
    fig.supxlabel(r"Dilution increases to the right  →   |   Synthetic $K_a=10^{-5}$, $K_w=10^{-14}$; fixed temperature",
                  fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
