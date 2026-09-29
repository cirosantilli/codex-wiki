"""Original Friedmann potential sketches; Python 3.14.4, root pyproject versions.

The caller supplies MPLCONFIGDIR when desired. Output is a PNG basename in CWD.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.linspace(0.24, 3.0, 1200)
    dust, radiation, vacuum = 1.0, 0.12, 0.22
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3), facecolor="white")
    minus = -dust / a - radiation / a**2 + vacuum * a**2
    plus = -dust / a - radiation / a**2 - vacuum * a**2
    axes[0].plot(a, minus, color="#166c88", linewidth=2.2)
    axes[0].axhline(0, color="#c76524", linestyle="--", label=r"Energy $E=-k$")
    roots = np.roots([vacuum, 0, 0, -dust, -radiation])
    turn = next(float(z.real) for z in roots if abs(z.imag) < 1e-9 and z.real > 0)
    axes[0].plot(turn, 0, "o", color="#c76524")
    axes[0].annotate(r"Maximum scale factor", (turn, 0), (0.85, 1.3), arrowprops={"arrowstyle": "->"})
    axes[0].annotate("Expansion", (0.98, -0.9), (0.38, -0.9), arrowprops={"arrowstyle": "->"})
    axes[0].annotate("Recollapse", (0.38, -1.65), (1.08, -1.65), arrowprops={"arrowstyle": "->"})
    axes[0].set_title("Negative vacuum density: one turning point")
    roots = np.roots([2 * vacuum, 0, 0, -dust, -2 * radiation])
    critical = next(float(z.real) for z in roots if abs(z.imag) < 1e-9 and z.real > 0)
    maximum = -dust / critical - radiation / critical**2 - vacuum * critical**2
    axes[1].plot(a, plus, color="#166c88", linewidth=2.2)
    for energy, color, style, label in [(maximum + 0.45, "#3a8155", "--", "Monotonic histories"), (maximum, "#9b4992", ":", "Static / asymptotic histories"), (maximum - 0.75, "#c76524", "--", "Recollapse / bounce")]:
        axes[1].axhline(energy, color=color, linestyle=style, label=label)
    axes[1].plot(critical, maximum, "o", color="#9b4992")
    lower = maximum - 0.75
    roots = np.roots([vacuum, 0, lower, dust, radiation])
    turning = sorted(z.real for z in roots if abs(z.imag) < 1e-9 and z.real > 0)
    for x in turning:
        axes[1].plot(x, lower, "o", color="#c76524")
    axes[1].text(0.26, lower - 0.8, "Inner branch:\nrecollapse", fontsize=9)
    axes[1].text(2.24, lower - 0.8, "Outer branch:\nbounce", fontsize=9)
    axes[1].set_title("Positive vacuum density: potential maximum")
    for ax in axes:
        ax.set(xlabel=r"Scale factor $a$", ylabel=r"Effective potential $V(a)$", xlim=(0.23, 3), ylim=(-5.0, 2.0))
        ax.grid(alpha=0.2)
        ax.legend(loc="lower left", fontsize=8, framealpha=1)
    fig.tight_layout()
    fig.savefig("paper-58-effective-potentials.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
