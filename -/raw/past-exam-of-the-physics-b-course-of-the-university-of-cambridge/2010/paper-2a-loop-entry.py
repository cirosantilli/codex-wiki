"""Original entry-only falling-loop plots for ideal resistive/inductive limits.

Python 3.14; numpy 2.3.5; matplotlib 3.10.7 (root pyproject.toml).
Writes paper-2a-loop-entry.png to the current working directory.
The example heights are illustrative dimensionless parameters, not exam data.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 9, "figure.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    blue, orange = "#176493", "#b14d20"
    # Resistive example: beta_R=b/(g*tau^2)=3. The entry root is found by bisection.
    beta_r = 3.0
    left, right = 0.0, beta_r + 1.0
    for _ in range(70):
        middle = (left + right) / 2
        if middle + np.expm1(-middle) < beta_r:
            left = middle
        else:
            right = middle
    stop_r = (left + right) / 2
    s_r = np.linspace(0, stop_r, 900)
    velocity_r = -np.expm1(-s_r)
    penetration_r = s_r + np.expm1(-s_r)
    current_r = velocity_r
    # Inductive long-loop curve is valid for 0<s<2*pi if beta_L=b*omega^2/g>2.
    s_l = np.linspace(0, 2 * np.pi, 1300)
    penetration_l = 1 - np.cos(s_l)
    velocity_l = np.sin(s_l)
    current_l = penetration_l
    # Short-loop example beta_L=1 reaches full entry at pi/2: stop all its curves there.
    beta_l_short = 1.0
    stop_l_short = np.arccos(1 - beta_l_short)
    s_short = np.linspace(0, stop_l_short, 400)
    short_curves = [1 - np.cos(s_short), np.sin(s_short), 1 - np.cos(s_short)]

    fig, axes = plt.subplots(3, 2, figsize=(8.6, 6.3), sharex="col")
    fig.subplots_adjust(left=0.095, right=0.98, top=0.825, bottom=0.25, hspace=0.16, wspace=0.29)
    fig.suptitle("Falling loop: entry-only motion and induced current", y=0.975, fontsize=13)
    fig.text(0.29, 0.927, r"Resistive limit: $L=0$, $s=t/\tau$", ha="center", fontsize=11)
    fig.text(0.29, 0.889, r"$\tau=mR/K^2$; example $b/(g\tau^2)=3$", ha="center", fontsize=9)
    fig.text(0.29, 0.852, "All curves stop at full entry.", ha="center", fontsize=9, color="0.3")
    fig.text(0.765, 0.927, r"Inductive limit: $R=0$, $s=\omega t$", ha="center", fontsize=11)
    fig.text(0.765, 0.889, r"$\omega=K/\sqrt{mL}$; $\beta=b\omega^2/g$", ha="center", fontsize=9)
    fig.text(0.765, 0.852, r"Blue: $\beta>2$; dashed orange: $\beta=1$", ha="center", fontsize=9)

    rlabels = [r"$x/(g\tau^2)$", r"$v/(g\tau)$", r"$KI/(mg)$"]
    llabels = [r"$x\omega^2/g$", r"$v\omega/g$", r"$KI/(mg)$"]
    for row, (yr, yl, ys) in enumerate(zip(
            [penetration_r, velocity_r, current_r],
            [penetration_l, velocity_l, current_l], short_curves)):
        ar, al = axes[row]
        ar.plot(s_r, yr, color=blue, lw=1.9)
        ar.plot(stop_r, yr[-1], "o", color=blue, ms=4)
        ar.axvline(stop_r, color="0.55", ls=":", lw=0.9)
        ar.axvspan(stop_r, 4.35, facecolor="0.95")
        ar.set(xlim=(0, 4.35), ylabel=rlabels[row])
        al.plot(s_l, yl, color=blue, lw=1.9)
        al.plot(s_short, ys, "--", color=orange, lw=2.1)
        al.plot(stop_l_short, ys[-1], "o", color=orange, ms=4)
        al.axvline(stop_l_short, color=orange, ls=":", lw=0.8, alpha=0.8)
        al.axvline(np.pi, color="0.7", ls=":", lw=0.8)
        al.set(xlim=(0, 2 * np.pi), ylabel=llabels[row])
        al.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
                      ["0", "π/2", "π", "3π/2", "2π"])
        for ax in [ar, al]:
            ax.axhline(0, color="0.7", lw=0.7)
            ax.grid(axis="y", alpha=0.12)
    axes[0, 0].set_ylim(-0.08, 3.3)
    axes[0, 0].axhline(beta_r, color="0.6", ls="--", lw=0.8)
    axes[0, 0].text(0.15, 3.08, r"$x=b$", fontsize=8)
    for ax in axes[1:, 0]:
        ax.set_ylim(-0.05, 1.13)
        ax.axhline(1, color="0.6", ls="--", lw=0.7)
    axes[0, 1].set_ylim(-0.08, 2.3)
    axes[1, 1].set_ylim(-1.16, 1.16)
    axes[2, 1].set_ylim(-0.08, 2.3)
    axes[0, 1].text(np.pi + 0.12, 2.1, "Reversal", fontsize=8, color=blue)
    for ax in axes[-1]:
        ax.set_xlabel(r"Dimensionless time $s$")
    fig.text(0.5, 0.145, r"$K=B_0a$; $x$ and $v$ are downward; positive $I$ gives an upward magnetic force.",
             ha="center", fontsize=9)
    fig.text(0.5, 0.102, r"Valid only for $0<x<b$. At full entry: net magnetic force vanishes and $\ddot{x}=g$.",
             ha="center", fontsize=9)
    fig.text(0.5, 0.059, r"Then $I=0$ in the $L=0$ limit; $I$ stays constant in the $R=0$ limit. These stages are not plotted.",
             ha="center", fontsize=9)
    fig.text(0.5, 0.018, r"For $0<\beta<2$, stop at $s=\arccos(1-\beta)$; $\beta=2$ is the ideal boundary/grazing case.",
             ha="center", fontsize=9)
    fig.savefig("paper-2a-loop-entry.png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
