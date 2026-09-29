"""Original synthetic DIS comparison; no measured data or fitted constants.

Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Run from _media; outputs basename.png.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    mass, x, q0_squared, lambda_squared = 0.938, 0.3, 2.0, 1.0
    q_squared = np.linspace(2.0, 5.0, 301)
    suppression = ((1 + q0_squared / lambda_squared) / (1 + q_squared / lambda_squared)) ** 4
    fig, (ax, kin) = plt.subplots(1, 2, figsize=(10, 6), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.085, right=0.98, top=0.78, bottom=0.30, wspace=0.35)
    fig.suptitle("What a fixed-$x$ scaling test compares", fontsize=17, y=0.975)
    fig.text(0.5, 0.895, "ORIGINAL MODEL CURVES • NOT MEASURED DATA • $x=0.3$", ha="center", fontsize=12)
    ax.plot(q_squared, np.ones_like(q_squared), lw=2.5, color="#176eac", label="Ideal scaling: $S=1$")
    ax.plot(q_squared, suppression, lw=2.5, color="#b64c10", label="Elastic-form-factor shape $A$")
    ax.set(xlim=(2, 5), ylim=(0, 1.15), xlabel="$Q^2$ (GeV$^2$)", ylabel="Normalized response shape")
    ax.set_title("Shape comparison", fontsize=12)
    ax.legend(loc="center right", frameon=False, fontsize=10)
    ax.annotate("$A(5)=1/16$", xy=(5, 1/16), xytext=(3.9, 0.25),
                arrowprops={"arrowstyle": "->", "color": "#b64c10"}, color="#b64c10")
    ax.grid(alpha=0.2)
    for energy, color in [(10.0, "#7d3a8a"), (15.0, "#176eac"), (20.0, "#358047")]:
        outgoing = energy - q_squared / (2 * mass * x)
        sine_squared = q_squared / (4 * energy * outgoing)
        assert np.all(outgoing > 0) and np.all((0 <= sine_squared) & (sine_squared <= 1))
        kin.plot(q_squared, outgoing, lw=2, color=color, label=f"$E={energy:g}$ GeV")
    w_squared = mass ** 2 + q_squared * (1 / x - 1)
    assert np.min(w_squared) > 4
    kin.set(xlim=(2, 5), ylim=(0, 18), xlabel="$Q^2$ (GeV$^2$)", ylabel="Outgoing $E'$ (GeV)")
    kin.set_title("Physical electron settings", fontsize=12)
    kin.legend(frameon=False, fontsize=10)
    kin.grid(alpha=0.2)
    fig.text(0.5, 0.135, "$S=F_2(x,Q^2)/F_2(x,Q_0^2)$    $A=[(1+Q_0^2/\\Lambda^2)/(1+Q^2/\\Lambda^2)]^4$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.075, "$Q_0^2=2$ GeV$^2$, $\\Lambda^2=1$ GeV$^2$ chosen for illustration. Elastic events themselves have $x=1$.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.025, "The flat line is an idealization; QCD permits scaling violations. No cross-section normalization is implied.",
             ha="center", fontsize=10, color="#56616a")
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
