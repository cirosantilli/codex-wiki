"""Original Mach-angle curve; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes mach-angle-versus-speed-ratio.png to the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    mach = np.linspace(1, 6, 1200)
    angle = np.degrees(np.arcsin(1 / mach))
    ax.plot(mach, angle, color="#285b89", lw=2.6)
    ax.plot(1, 90, "o", ms=7, mfc="white", mec="#285b89", mew=1.8)
    ax.text(1.12, 84, r"$90^\circ$ limit as $M\to1^+$", fontsize=11)
    ax.plot([2, 2], [0, 30], "--", color="#c64632", lw=1.3)
    ax.plot([1, 2], [30, 30], "--", color="#c64632", lw=1.3)
    ax.plot(2, 30, "o", color="#c64632", ms=8)
    ax.annotate(r"$M=2\quad\Rightarrow\quad\mu=30^\circ$",
                (2, 30), (3.1, 52), color="#a63223",
                arrowprops={"arrowstyle": "->", "color": "#a63223"})
    ax.text(3.0, 71,
            r"$U=680\ \mathrm{m\,s^{-1}}$" + "\n" +
            r"$c=340\ \mathrm{m\,s^{-1}}$" + "\n" +
            "Chosen uniform-gas example",
            fontsize=11, bbox={"boxstyle": "round,pad=0.5",
                              "facecolor": "#f3f6f9", "edgecolor": "#c8d1db"})
    ax.set_xlim(0.95, 6.05)
    ax.set_ylim(0, 96)
    ax.set_xticks([1, 2, 3, 4, 5, 6])
    ax.set_yticks([0, 15, 30, 45, 60, 75, 90])
    ax.set_xlabel(r"Mach number $M=U/c$ (gas-relative speed)")
    ax.set_ylabel(r"Mach half-angle $\mu$ (degrees)")
    ax.grid(alpha=0.22)
    ax.set_title(r"A faster source makes a narrower sound cone: "
                 r"$\mu=\arcsin(1/M)$", fontsize=14, pad=14)
    fig.text(0.5, 0.075,
             "Weak linear waves, steady source, uniform isotropic 3D medium; M > 1.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.029,
             "Model prediction; not a finite-deflection shock angle or measured boom strength.",
             ha="center", fontsize=10, color="#525b65")
    fig.subplots_adjust(left=0.12, right=0.975, top=0.875, bottom=0.23)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
