"""Oxford AC1 (2012), question 6: two stages of a conformal map.

Writes 2012-half-strip-map.png in the process CWD.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies: repository root pyproject.toml.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.8), facecolor="white")
    blue, orange, edge = "#186a97", "#be621a", "#48535b"
    y = np.linspace(.015, 3.1, 800)
    x = np.linspace(.015, np.pi-.015, 800)
    curves = [(a+1j*y, blue) for a in np.linspace(.35, np.pi-.35, 6)]
    curves += [(x+1j*b, orange) for b in [.18, .4, .7, 1.05, 1.5, 2.1, 2.8]]
    for z, colour in curves:
        w = np.exp(1j*z)
        image = -(w+1/w)
        for ax, values in zip(axes, [z, w, image]):
            ax.plot(values.real, values.imag, color=colour, lw=.85, alpha=.85)

    axes[0].set(xlim=(-.25, np.pi+.25), ylim=(-.08, 3.15), xlabel=r"$x$", ylabel=r"$y$")
    axes[0].set_xticks([0, np.pi/2, np.pi], ["0", r"$\pi/2$", r"$\pi$"])
    axes[0].plot([0, 0], [0, 3.15], "--", color=edge, lw=1)
    axes[0].plot([np.pi, np.pi], [0, 3.15], "--", color=edge, lw=1)
    axes[0].plot([0, np.pi], [0, 0], "--", color=edge, lw=1)
    axes[0].set_title(r"Half-strip $S$", fontsize=12)

    theta = np.linspace(0, np.pi, 500)
    axes[1].plot(np.cos(theta), np.sin(theta), "--", color=edge, lw=1)
    axes[1].plot([-1, 1], [0, 0], "--", color=edge, lw=1)
    axes[1].set(xlim=(-1.12, 1.12), ylim=(-.08, 1.15), xlabel=r"$\mathrm{Re}\,w$", ylabel=r"$\mathrm{Im}\,w$")
    axes[1].set_aspect("equal", adjustable="box")
    axes[1].set_title(r"$w=e^{iz}$: upper half-disc", fontsize=12)

    axes[2].axhline(0, ls="--", color=edge, lw=1)
    axes[2].set(xlim=(-5, 5), ylim=(-.1, 6), xlabel=r"$\mathrm{Re}\,\zeta$", ylabel=r"$\mathrm{Im}\,\zeta$")
    axes[2].set_title(r"$\zeta=-(w+w^{-1})$: upper half-plane", fontsize=11)
    for ax in axes:
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.12)
        ax.tick_params(labelsize=9)
    fig.suptitle(r"$S\ \longrightarrow\ D_+\ \longrightarrow\ H,\qquad\zeta=-2\cos z$", fontsize=15, y=.98)
    fig.text(.5, .015, "Matching colours trace the same curves. The half-strip and half-plane extend upward; dashed boundaries are excluded.", ha="center", fontsize=9)
    fig.tight_layout(rect=(0, .06, 1, .91), w_pad=2.1)
    fig.savefig("2012-half-strip-map.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
