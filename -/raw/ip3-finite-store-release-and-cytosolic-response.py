"""Original finite-store toy model; writes matching opaque PNG to the CWD.

Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7. All constants are stipulated.
S, X, Q are amol; time is seconds; V is pL; amol/pL equals micromolar.
S'=-k*S, X'=k*S-h*X, Q'=h*X. The sink does not refill the store.
The separately held background is excluded from the excess mass balance.
This imposed effective permeability is not an IP3 receptor gating model.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

S0 = 1.0
V_C = 1.0
K_RELEASE = 0.4
H_CLEARANCE = 0.8
C_BACKGROUND = 0.1


def amounts(t):
    t = np.asarray(t, dtype=float)
    store = S0 * np.exp(-K_RELEASE * t)
    mobile = K_RELEASE * S0 / (H_CLEARANCE - K_RELEASE) * (
        np.exp(-K_RELEASE * t) - np.exp(-H_CLEARANCE * t))
    cleared = S0 - store - mobile
    return store, mobile, cleared


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    t = np.linspace(0, 16, 801)
    store, mobile, cleared = amounts(t)
    np.testing.assert_allclose(store + mobile + cleared, S0, atol=1e-14)
    assert np.min(np.stack([store, mobile, cleared])) >= -1e-14
    peak_t = np.log(H_CLEARANCE / K_RELEASE) / (H_CLEARANCE - K_RELEASE)
    _, peak_x, _ = amounts(peak_t)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), dpi=130, facecolor="white")
    axes[0].plot(t, K_RELEASE * store, color="#357d66", lw=2.8)
    axes[0].set(ylabel="Store-release rate (amol/s)", ylim=(0, 0.43),
                title="Release declines as the store empties")
    axes[0].annotate("Imposed release pathway stays active", xy=(5, 0.054),
                     xytext=(4.2, 0.30), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": "#374650"})
    axes[1].plot(t, C_BACKGROUND + mobile / V_C, color="#24689b", lw=2.8)
    axes[1].axhline(C_BACKGROUND, color="#747b82", ls="--", lw=1.2,
                   label=r"Chosen background: 0.1 $\mu$M")
    axes[1].plot(peak_t, C_BACKGROUND + peak_x / V_C, "o", color="#24689b")
    axes[1].annotate(r"Peak: 1.73 s, 0.35 $\mu$M", xy=(peak_t, 0.35),
                     xytext=(4.0, 0.32), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": "#374650"})
    axes[1].set(ylabel=r"Free cytosolic calcium ($\mu$M)", ylim=(0, 0.43),
                title="Concentration rises, peaks, then clears")
    axes[1].legend(loc="lower right", fontsize=9, frameon=False)
    for ax in axes:
        ax.set(xlabel="Time (s)", xlim=(0, 16))
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Finite store and clearance: stipulated analytic model", fontsize=15)
    fig.text(0.5, 0.065,
             r"$S_0=1$ amol, $V_c=1$ pL, $k=0.4$ s$^{-1}$, $h=0.8$ s$^{-1}$; $S+X+Q=S_0$",
             ha="center", fontsize=10)
    fig.text(0.5, 0.02, "No refill, influx, binding or reverse transfer; curves are not experimental measurements.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.23, top=0.81, wspace=0.34)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
