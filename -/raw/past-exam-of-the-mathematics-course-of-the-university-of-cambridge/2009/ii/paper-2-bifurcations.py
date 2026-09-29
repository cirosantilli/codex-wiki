"""Original diagrams; Python 3.14, root NumPy/Matplotlib dependencies.

Output only the PNG basename in caller CWD. Preserve caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    mu = np.linspace(-2.2, 2.2, 1801)
    fig, axes = plt.subplots(2, 2, figsize=(11, 8), layout="constrained")
    for row, system in enumerate([1, 2]):
        for col, a in enumerate([1, -1]):
            ax = axes[row, col]
            for inner in [False, True]:
                square = a + (-1 if inner else 1) * np.abs(mu)
                for sign in [-1, 1]:
                    x = sign * np.sqrt(np.maximum(square, 0))
                    derivative = -4 * x * (x*x-a)
                    if system == 2:
                        derivative *= x
                    for stable in [True, False]:
                        mask = (square > 0) & ((derivative < 0) == stable)
                        ax.plot(mu, np.where(mask, x, np.nan),
                                "-" if stable else "--",
                                color="#165ca5" if stable else "#c66b16", lw=2)
            if system == 2:
                for stable in [True, False]:
                    mask = ((mu*mu-1 < 0) == stable)
                    ax.plot(mu, np.where(mask, 0, np.nan),
                            "-" if stable else "--",
                            color="#165ca5" if stable else "#c66b16", lw=2)
            for critical in [-1, 1]:
                ax.scatter(critical, 0, color="#a32424", s=30, zorder=5)
                label = "SN" if system == 1 else ("subcritical PF" if a > 0 else "supercritical PF")
                ax.annotate(label, (critical, 0), xytext=(4, 10),
                            textcoords="offset points", fontsize=8)
            if a > 0:
                for critical in [-1, 1]:
                    ax.scatter(0, critical, color="#a32424", s=30, zorder=5)
                    ax.annotate("TC", (0, critical), xytext=(6, 4),
                                textcoords="offset points", fontsize=9)
            ax.set(xlim=(-2.2, 2.2), ylim=(-2, 2), xlabel=r"$\mu$",
                   ylabel=r"fixed point $x$", title=f"System ({'i' if system == 1 else 'ii'}), a = {a}")
            ax.axvline(0, color="#aaa", lw=.5)
            ax.axhline(0, color="#aaa", lw=.5, zorder=0)
            ax.grid(alpha=.12)
    fig.suptitle("Solid: stable    Dashed: unstable    SN: saddle-node    PF: pitchfork    TC: transcritical", fontsize=11)
    fig.savefig("paper-2-bifurcations.png", dpi=115, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
