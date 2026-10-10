"""Original lumped calorimeter model; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes an opaque PNG in the current directory. No measured data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    capacity, addenda, conductance = 8e-7, 2e-7, 5e-8
    power, duration, bath = 2e-9, 100.0, 2.0
    total = capacity + addenda
    tau = total / conductance
    t = np.linspace(0, 200, 2001)
    excess_end = power / conductance * (-np.expm1(-duration / tau))
    excess = np.where(t <= duration,
                      power / conductance * (-np.expm1(-t / tau)),
                      excess_end * np.exp(-(t - duration) / tau))
    stored = total * excess_end
    loss = power * duration - stored
    assert np.isclose(tau, 20.0)
    assert np.isclose(stored + loss, power * duration)
    assert np.isclose(excess[1200] / excess[1000], np.exp(-1))

    fig, (ax, response) = plt.subplots(1, 2, figsize=(10.5, 4.8),
                                       gridspec_kw={"width_ratios": [1, 1.35]})
    fig.suptitle("A tiny heater pulse measures sample + addenda", fontsize=15)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    def box(x, y, w, h, label, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015",
                                   edgecolor="#334155", facecolor=color))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center")
    box(.09, .46, .82, .39,
        "Sample: Cₛ = 8 × 10⁻⁷ J/K\n\nPlatform + heater + thermometer\nAddenda: Cₐ = 2 × 10⁻⁷ J/K",
        "#e0f2fe")
    box(.09, .08, .82, .14, "Controlled bath: Tᵦ = 2.000 K", "#e2e8f0")
    ax.annotate("", xy=(.5, .235), xytext=(.5, .445),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#2563eb"})
    ax.text(.55, .335, "G = 5 × 10⁻⁸ W/K", va="center", fontsize=10)
    ax.annotate("P = 2 × 10⁻⁹ W", xy=(.5, .87), xytext=(.5, .94),
                ha="center", arrowprops={"arrowstyle": "->", "color": "#b45309", "lw": 2})
    ax.text(.5, .005, "One common temperature; ideal internal contact", ha="center", fontsize=9)

    response.axvspan(0, duration, color="#fef3c7", alpha=.7)
    response.axhline(.04, color="#64748b", linestyle=":", label="P/G = 0.040 K")
    response.plot(t, excess, color="#0369a1", linewidth=2.4, label="Model thermometer response")
    response.axvline(duration, color="#64748b", linestyle="--", linewidth=1)
    response.plot([100, 120], [excess_end, excess_end / np.e], "o", color="#0369a1")
    response.annotate("One time constant: 20 s\nexcess falls by 1/e", xy=(120, excess_end / np.e),
                      xytext=(130, .025), fontsize=10,
                      arrowprops={"arrowstyle": "->", "color": "#334155"})
    response.text(50, .006, "Heater on", ha="center", color="#92400e")
    response.text(155, .006, "Heater off", ha="center", color="#334155")
    response.set(xlabel="Time t (s)", ylabel="Temperature excess T − Tᵦ (K)",
                 xlim=(0, 200), ylim=(0, .048))
    response.legend(loc="upper right", fontsize=9, frameon=False)
    response.grid(alpha=.18)
    fig.text(.5, .025,
             "Constructed model, not experimental data  •  Cₛ = Gτ − Cₐ  •  "
             "A 100 s pulse loses 80.1% of its input to the bath",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, .065, 1, .94))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=150, facecolor="white")
    plt.close(fig)
    print(f"tau={tau:g} s; end_excess={excess_end:.10g} K; "
          f"stored={stored:.10g} J; loss={loss:.10g} J")


if __name__ == "__main__":
    main()
