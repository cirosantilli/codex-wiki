"""Original qualitative UCST diagram; not fitted to chromatin measurements.

Run from the desired media directory. Python/matplotlib/numpy requirements
are declared in the repository's pyproject.toml.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def coexistence(c, critical_temperature, width):
    return critical_temperature * (1 - ((c - 1) / width) ** 2)


def main():
    plt.rcParams.update({"font.size": 12})
    fig, ax = plt.subplots(figsize=(8.8, 6.1), layout="constrained", facecolor="white")
    c = np.linspace(0.08, 1.92, 700)
    t = coexistence(c, 1.0, 0.92)
    ax.fill_between(c, 0, t, color="#dce9f7", alpha=0.9)
    ax.plot(c, t, color="#15589b", lw=2.6, label="0.15 M NaCl: illustrative binodal")
    c_low = np.linspace(0.3, 1.7, 600)
    ax.plot(c_low, coexistence(c_low, 0.72, 0.70), color="#b64720", ls="--", lw=2.4,
            label="0.10 M NaCl: weaker-attraction model")
    ax.plot(1, 1, "o", ms=7, color="#15589b")
    ax.annotate("Critical point $(c_c,T_c)$", (1, 1), xytext=(0.28, 1.11),
                arrowprops={"arrowstyle": "->", "color": "#15589b"})
    tie_t = 0.52
    a = 1 - 0.92 * np.sqrt(1 - tie_t)
    b = 1 + 0.92 * np.sqrt(1 - tie_t)
    assert 0 < a < 1 < b < 2
    assert np.isclose(coexistence(a, 1, .92), tie_t)
    ax.plot([a, b], [tie_t, tie_t], color="#333333", lw=1.5)
    ax.plot([a, b], [tie_t, tie_t], "o", color="#333333", ms=5)
    ax.annotate("$c_{sat}(T)$", (a, tie_t), xytext=(a - 0.23, tie_t + 0.12),
                arrowprops={"arrowstyle": "->", "color": "#333333"})
    ax.annotate("$c_{dense}(T)$", (b, tie_t), xytext=(b + 0.04, tie_t + 0.12),
                arrowprops={"arrowstyle": "->", "color": "#333333"})
    ax.text(1, .24, "Two coexisting liquids\n(dilute + chromatin-rich)", ha="center", va="center")
    ax.text(1.7, 1.10, "One homogeneous\nliquid", ha="center", va="center")
    ax.set(xlim=(0, 2.05), ylim=(0, 1.28),
           xlabel="Chromatin concentration / reference critical concentration",
           ylabel="Temperature / reference critical temperature",
           title="Qualitative phase diagram under an upper-critical assumption")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.14), frameon=False, fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
