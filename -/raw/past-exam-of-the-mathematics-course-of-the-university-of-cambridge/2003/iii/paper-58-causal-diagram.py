"""Original de Sitter causal diagrams; Python 3.14.4, root dependencies.

Output is a PNG basename in the caller's CWD; supplied MPLCONFIGDIR is honored.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def compact(xi, eta):
    u, v = np.arctan(xi - eta), np.arctan(xi + eta)
    return (u + v) / 2, (v - u) / 2


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.1), facecolor="white")
    ax = axes[0]
    xi = np.tan(np.linspace(-np.pi / 2 + 1e-5, np.pi / 2 - 1e-5, 1600))
    upper_x, upper_y = compact(xi, np.pi / 2)
    lower_x, lower_y = compact(xi, -np.pi / 2)
    ax.fill_between(upper_x, lower_y, upper_y, color="#e8f0f3")
    for eta, color, label in [(np.pi / 2, "#166c88", r"Future infinity $\mathcal{I}^+$"), (-np.pi / 2, "#166c88", r"Past infinity $\mathcal{I}^-$")]:
        x, y = compact(xi, eta)
        ax.plot(x, y, color=color, linewidth=2)
        ax.text(0, np.arctan(eta) + np.sign(eta) * 0.12, label, ha="center", fontsize=10)
    ax.plot([-np.pi / 2, np.pi / 2], [0, 0], "--", color="#777777")
    ax.text(-1.4, 0.08, r"Cauchy slice $\eta=0$", fontsize=9)
    eta = np.linspace(-np.pi / 2 + 1e-5, np.pi / 2 - 1e-5, 600)
    x, y = compact(np.zeros_like(eta), eta)
    ax.plot(x, y, color="#333333", linewidth=1.7)
    for side in [-1, 1]:
        x, y = compact(side * (np.pi / 2 - eta), eta)
        ax.plot(x, y, color="#c76524", linewidth=1.5, label="Observer event horizons" if side == 1 else None)
    ax.text(0.04, 0.37, r"Observer $\xi=0$", fontsize=9)
    ax.plot([-np.pi / 2, np.pi / 2], [0, 0], "o", color="#333333", markersize=4)
    ax.set_title(r"Unwrapped space: $\xi\in\mathbb{R}$")
    ax.set(xlim=(-1.85, 1.85), ylim=(-1.4, 1.4), xlabel=r"$X=(\arctan u+\arctan v)/2$", ylabel=r"$Y=(\arctan v-\arctan u)/2$")
    ax.set_aspect("equal")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.22), frameon=False, fontsize=9)
    ax = axes[1]
    ax.fill_between([-np.pi, np.pi], -np.pi / 2, np.pi / 2, color="#e8f0f3")
    for eta, label in [(np.pi / 2, r"$\mathcal{I}^+$"), (-np.pi / 2, r"$\mathcal{I}^-$")]:
        ax.plot([-np.pi, np.pi], [eta, eta], color="#166c88", linewidth=2)
        ax.text(0, eta + np.sign(eta) * 0.18, label, ha="center")
    for side in [-np.pi, np.pi]:
        ax.plot([side, side], [-np.pi / 2, np.pi / 2], ":", color="#777777")
    ax.plot([-np.pi, np.pi], [0, 0], "--", color="#777777")
    eta = np.linspace(-np.pi / 2, np.pi / 2, 600)
    for sign in [-1, 1]:
        ax.plot(sign * eta, eta, color="#c76524", linewidth=1.5)
    ax.text(0, -0.3, "Spatial edges identified", ha="center", fontsize=9)
    ax.text(0, 0.85, "Null rays at 45 degrees", ha="center", fontsize=9)
    ax.set_title(r"Ordinary de Sitter: $\xi\sim\xi+2\pi$")
    ax.set(xlim=(-3.45, 3.45), ylim=(-1.95, 1.95), xlabel=r"Periodic coordinate $\xi$", ylabel=r"Conformal time $\eta$")
    ax.set_aspect("equal")
    fig.tight_layout()
    fig.savefig("paper-58-causal-diagram.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
