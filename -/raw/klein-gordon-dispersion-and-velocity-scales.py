#!/usr/bin/env python3
"""Original dimensionless Klein-Gordon curves; matching PNG is saved to CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (dispersion, speeds) = plt.subplots(1, 2, figsize=(9.2, 4.0))
    q = np.linspace(0, 4, 801)
    omega = np.sqrt(1 + q**2)
    q0, omega_c = 1.0, np.sqrt(2)
    vp, vg = omega_c / q0, q0 / omega_c
    dispersion.plot(q, omega, color="#2166ac", lw=2.3, label=r"$\Omega=\sqrt{1+q^2}$")
    secant_q = np.linspace(0, 2.35, 100)
    dispersion.plot(secant_q, vp * secant_q, color="#934aa1", ls=":", lw=2, label=r"Secant slope $v_p/c=\sqrt{2}$")
    tangent_q = np.linspace(0, 3.4, 100)
    dispersion.plot(tangent_q, omega_c + vg * (tangent_q - q0), color="#337755", ls="--", lw=2, label=r"Tangent slope $v_g/c=1/\sqrt{2}$")
    dispersion.scatter([q0], [omega_c], c="black", s=28, zorder=5)
    dispersion.annotate(r"$q_0=1$", (q0, omega_c), xytext=(1.65, 1.12), arrowprops={"arrowstyle": "->", "color": "black"})
    dispersion.set(xlim=(0, 4), ylim=(0, 4.4), xlabel=r"Wavenumber $q=ck/\omega_0$", ylabel=r"Frequency $\Omega=\omega/\omega_0$", title="Ratio and local slope")
    dispersion.legend(loc="upper left", fontsize=9, frameon=True, facecolor="white", edgecolor="white", framealpha=1)
    q_positive = np.linspace(0.15, 4, 1000)
    positive_omega = np.sqrt(1 + q_positive**2)
    speeds.plot(q_positive, positive_omega / q_positive, color="#934aa1", lw=2.2, label=r"Phase $v_p/c$")
    speeds.plot(q_positive, q_positive / positive_omega, color="#337755", lw=2.2, label=r"Group $v_g/c$")
    speeds.axhline(1, color="#444444", ls="--", lw=1.6, label=r"Maximal front speed $v_f/c=1$")
    speeds.scatter([1, 1], [vp, vg], c=["#934aa1", "#337755"], s=28, zorder=5)
    speeds.text(0.39, 0.52, r"$v_p v_g=c^2$", transform=speeds.transAxes, fontsize=14)
    speeds.annotate(r"$v_p\to\infty$ as $q\to0^+$", xy=(0.35, 3.03), xytext=(0.72, 2.25), fontsize=10, arrowprops={"arrowstyle": "->"})
    speeds.set(xlim=(0, 4), ylim=(0, 3.4), xlabel=r"Wavenumber $q=ck/\omega_0>0$", ylabel="Velocity / c", title="Three distinct velocity meanings")
    speeds.legend(loc="upper right", fontsize=9, frameon=False)
    for ax in (dispersion, speeds):
        ax.grid(alpha=0.16)
        ax.set_facecolor("white")
    fig.suptitle("Stipulated Klein–Gordon medium", fontsize=14)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
