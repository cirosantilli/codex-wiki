"""Original circuit and synthetic thermal response; Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Run from _media; write an opaque PNG to the current directory.
All parameters are invented for teaching, not fitted physiological data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def pulse_response(t, gain, tau=4.0, start=2.0, stop=10.0):
    """Exact solution of tau*x' = d - (1+gain)*x for a unit pulse."""
    rate = (1.0 + gain) / tau
    elapsed = np.clip(t - start, 0, stop - start)
    return -np.expm1(-rate * elapsed) / (1.0 + gain) * np.exp(
        -rate * np.maximum(t - stop, 0)
    )


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10.4, 8.0), facecolor="white")
    gs = fig.add_gridspec(3, 1, height_ratios=[2.5, 0.8, 1.5], hspace=0.5)
    ax = fig.add_subplot(gs[0])
    ax.set(xlim=(0, 10), ylim=(0, 5))
    ax.axis("off")

    def box(x, y, w, h, text, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                   facecolor=color, edgecolor="#334155"))
        ax.text(x+w/2, y+h/2, text, ha="center", va="center", fontsize=11)

    def arrow(points, color="#334155", dashed=False):
        for a, b in zip(points[:-2], points[1:-1]):
            ax.plot([a[0], b[0]], [a[1], b[1]], color=color,
                    linestyle="--" if dashed else "-", linewidth=1.7)
        ax.add_patch(FancyArrowPatch(points[-2], points[-1], arrowstyle="-|>",
                                     mutation_scale=13, linewidth=1.7, color=color,
                                     linestyle="--" if dashed else "-"))

    box(.25, 2.45, 2.0, 1.0, "Sensor\nInternal temperature", "#dbeafe")
    box(3.75, 2.45, 2.3, 1.0, "Integrator\nHypothalamic network", "#e0e7ff")
    box(7.55, 2.45, 2.2, 1.0, "Effectors\nSweat / skin blood flow", "#dcfce7")
    box(3.75, .2, 2.3, .9, "Regulated variable\nCore temperature", "#fef3c7")
    arrow([(2.35, 2.95), (3.65, 2.95)])
    arrow([(6.15, 2.95), (7.45, 2.95)])
    ax.text(3.0, 3.16, "information", ha="center", fontsize=10)
    ax.text(6.8, 3.16, "command", ha="center", fontsize=10)
    arrow([(8.65, 2.35), (8.65, .65), (6.15, .65)])
    ax.text(7.6, 1.65, "Cooling counters\nwarming", ha="center", fontsize=10)
    arrow([(3.65, .65), (1.25, .65), (1.25, 2.35)])
    ax.text(2.35, 1.65, "Sensed again", ha="center", fontsize=10)
    ax.text(4.9, 4.75, "Current reference", ha="center")
    arrow([(4.9, 4.5), (4.9, 3.55)])
    ax.text(8.6, 4.75, "Skin-temperature input", ha="center", color="#7c3aed")
    arrow([(8.6, 4.5), (8.6, 3.9), (6.7, 3.9), (6.05, 3.55)],
          color="#7c3aed", dashed=True)
    ax.text(8.4, 4.12, "Can anticipate a core change", ha="center", fontsize=9,
            color="#7c3aed")
    ax.text(4.9, 1.95, "Added heat load", ha="center", color="#b45309")
    arrow([(4.9, 1.7), (4.9, 1.2)], color="#b45309")
    ax.set_title("Qualitative thermoregulation circuit", loc="left", fontweight="bold")

    t = np.linspace(0, 18, 1801)
    load = ((t >= 2) & (t < 10)).astype(float)
    disturbance = fig.add_subplot(gs[1])
    disturbance.step(t, load, where="post", color="#b45309", linewidth=2)
    disturbance.set(ylabel="Heat load d", ylim=(-.05, 1.2), xlim=(0, 18))
    disturbance.set_title("SYNTHETIC PLOTS — invented parameters; no measured data",
                          loc="left", fontsize=12, fontweight="bold")
    response = fig.add_subplot(gs[2], sharex=disturbance)
    response.plot(t, pulse_response(t, 0), color="#64748b", linewidth=2.4,
                  label="Passive loss only (k = 0)")
    response.plot(t, pulse_response(t, 3), color="#0369a1", linewidth=2.4,
                  label="Negative feedback (k = 3)")
    response.axhline(0, color="#94a3b8", linewidth=.8)
    response.set(ylabel="Displacement x", xlabel="Time (arbitrary units)",
                 ylim=(-.02, .96))
    response.legend(loc="upper right", fontsize=10, frameon=False)
    for a in (disturbance, response):
        a.axvspan(2, 10, color="#fef3c7", alpha=.45)
        a.grid(alpha=.15)
    fig.subplots_adjust(left=.12, right=.97, top=.94, bottom=.12)
    fig.text(.12, .025, "Lower model: 4 dx/dt = d − x − kx. All plotted quantities are scaled and synthetic.",
             fontsize=10, color="#475569")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
