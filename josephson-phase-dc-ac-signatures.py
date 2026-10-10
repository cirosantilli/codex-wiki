"""Original ideal-junction signatures; Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5.

Run from _media. These analytic curves are stipulated models, not measurements.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.2), layout="constrained")
    fig.patch.set_facecolor("white")
    phase = np.linspace(-np.pi, np.pi, 801)
    axes[0].plot(phase / np.pi, np.sin(phase), color="#315f94", lw=2.5)
    axes[0].scatter([1/6, 1/2], [0.5, 1], color="#bd8234", zorder=3)
    axes[0].set(xlabel=r"Phase difference $\phi/\pi$", ylabel=r"Pair current $I_s/I_c$", title=r"A. $I_s=I_c\sin\phi$", xlim=(-1, 1), ylim=(-1.2, 1.2))
    axes[0].axhline(0, color="#aab7b8", lw=0.7)
    axes[1].plot([0, 0], [-1, 1], color="#315f94", lw=4)
    axes[1].scatter([0, 0], [-1, 1], color="#315f94", zorder=3)
    axes[1].set(xlabel=r"Junction voltage $V$", ylabel=r"Static pair current $I_s/I_c$", title="B. Zero-voltage DC branch", xlim=(-1, 1), ylim=(-1.2, 1.2), xticks=[0])
    axes[1].text(0.14, 0.02, "Phase adjusts\nto imposed current", va="center", fontsize=10)
    axes[1].text(0.02, -0.3, r"$|I_s|\leq I_c$", transform=axes[1].transAxes, fontsize=10)
    h, e = 6.62607015e-34, 1.602176634e-19
    voltage = 10e-6
    freq = 2 * e * voltage / h
    t_ns = np.linspace(0, 0.8, 1601)
    axes[2].plot(t_ns, np.sin(2*np.pi*freq*t_ns*1e-9), color="#276c50", lw=2)
    axes[2].axhline(0, color="#aab7b8", lw=0.7)
    axes[2].set(xlabel="Time (ns)", ylabel=r"Pair current $I_s/I_c$", title="C. Fixed V = 10 μV", xlim=(0, 0.8), ylim=(-1.2, 1.2))
    axes[2].text(0.5, -0.3, f"f = {freq/1e9:.6f} GHz; mean pair current = 0", transform=axes[2].transAxes, ha="center", fontsize=9)
    fig.suptitle("Ideal sinusoidal Josephson junction: model curves, not data", weight="bold", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
