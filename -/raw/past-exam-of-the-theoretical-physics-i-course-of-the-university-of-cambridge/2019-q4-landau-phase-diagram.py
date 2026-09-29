"""Original sextic Landau plots. Save the PNG in the working directory."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, (ax, phase) = plt.subplots(1, 2, figsize=(10, 4.4), layout="constrained")
    fig.patch.set_facecolor("white")
    m = np.linspace(-1.2, 1.2, 1001)
    for r, color, style, label in [
        (0, "#228833", "-", r"$r=0$: already ordered"),
        (3/16, "#8844aa", "-", r"$r=3/16$: coexistence"),
        (0.24, "#bb5566", "--", r"$r=0.24$: disordered"),
    ]:
        ax.plot(m, r*m*m - m**4/2 + m**6/3, color=color, ls=style, lw=2, label=label)
    ax.axhline(0, lw=0.7, color="#777777")
    ax.scatter([-np.sqrt(3)/2, 0, np.sqrt(3)/2], [0, 0, 0], color="#8844aa", s=25, zorder=4)
    ax.set(xlabel=r"Order parameter $m$", ylabel=r"Free energy $f$",
           title=r"$b=-1,\ c=1$", xlim=(-1.2, 1.2), ylim=(-0.19, 0.39))
    ax.legend(loc="upper center", fontsize=9, frameon=False)
    ax.grid(alpha=0.15)

    b = np.linspace(-1.55, 1.35, 800)
    boundary = np.where(b < 0, 3*b*b/16, 0)
    phase.fill_betweenx(b, -0.38, boundary, color="#e5f1e5")
    phase.fill_betweenx(b, boundary, 0.65, color="#edf1fb")
    neg = b[b <= 0]
    phase.plot(np.zeros(250), np.linspace(0, 1.35, 250), color="#174ea6", lw=2.5,
               label="Continuous transition")
    phase.plot(3*neg*neg/16, neg, color="#8844aa", lw=2.5,
               label="First-order transition")
    phase.plot(np.zeros_like(neg), neg, "--", color="#888888", lw=1.1)
    phase.plot(neg*neg/4, neg, "--", color="#888888", lw=1.1, label="Spinodal limits")
    phase.scatter([0], [0], color="#111111", s=32, zorder=5)
    phase.annotate("Tricritical point", xy=(0, 0), xytext=(-0.31, -0.28),
                   fontsize=9, arrowprops={"arrowstyle": "->", "color": "#444444"})
    phase.text(-0.31, 0.72, "Ordered\n" + r"$m=\pm m_0$", fontsize=10)
    phase.text(0.31, 0.72, "Disordered\n" + r"$m=0$", fontsize=10)
    phase.set(xlim=(-0.38, 0.65), ylim=(-1.55, 1.35), xlabel=r"$T-T_c$",
              ylabel=r"Quartic coefficient $b$", title=r"Equilibrium phases ($a=c=1$)")
    phase.legend(loc="lower left", fontsize=8, frameon=True, facecolor="white", framealpha=0.94)
    fig.savefig(Path.cwd() / "2019-q4-landau-phase-diagram.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
