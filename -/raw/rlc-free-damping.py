"""Free series-RLC charge and energy; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from the desired output directory; writes rlc-free-damping.png there.
The dimensionless variables are tau=omega0*t, x=q/q0, a=alpha/omega0.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def response(tau, a):
    """Return x, dx/dtau, d²x/dtau² for x(0)=1, x'(0)=0."""
    tau = np.asarray(tau)
    if a < 1:
        b = np.sqrt(1 - a*a)
        x = np.exp(-a*tau) * (np.cos(b*tau) + a/b*np.sin(b*tau))
        v = -np.exp(-a*tau) * np.sin(b*tau)/b
        acc = np.exp(-a*tau) * (a/b*np.sin(b*tau) - np.cos(b*tau))
    elif a == 1:
        x = (1 + tau)*np.exp(-tau)
        v = -tau*np.exp(-tau)
        acc = (tau - 1)*np.exp(-tau)
    else:
        b = np.sqrt(a*a - 1)
        slow, fast = -a+b, -a-b
        # Two decaying exponentials avoid growing cosh/sinh intermediates.
        x = ((a+b)*np.exp(slow*tau) - (a-b)*np.exp(fast*tau))/(2*b)
        v = (np.exp(fast*tau) - np.exp(slow*tau))/(2*b)
        acc = (fast*np.exp(fast*tau) - slow*np.exp(slow*tau))/(2*b)
    return x, v, acc


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    tau = np.linspace(0, 12, 1801)
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2), layout="constrained")
    curves = [(0.5, "#2369ad", "Underdamped"),
              (1.0, "#c46b17", "Critical"), (2.0, "#39804a", "Overdamped")]
    for a, color, label in curves:
        x, v, _ = response(tau, a)
        legend = rf"{label}: $\alpha/\omega_0={a:g}$"
        axes[0].plot(tau, x, color=color, lw=2.3, label=legend)
        axes[1].plot(tau, x*x + v*v, color=color, lw=2.3)
    axes[0].axhline(0, color="#777777", lw=0.8)
    axes[0].set(title="Charge: oscillation or direct return", ylabel=r"$q/q_0$",
                ylim=(-0.23, 1.05))
    axes[0].legend(fontsize=9, frameon=False)
    axes[1].set(title="Stored energy always decreases", ylabel=r"$E/E(0)$",
                ylim=(-0.02, 1.05))
    axes[1].text(0.97, 0.91, r"$E/E(0)=x^2+(dx/d\tau)^2$" + "\n" +
                 r"$d[E/E(0)]/d\tau=-4(\alpha/\omega_0)(dx/d\tau)^2$",
                 transform=axes[1].transAxes, ha="right", va="top", fontsize=10)
    for ax in axes:
        ax.set(xlim=(0, 12), xlabel=r"Dimensionless time $\tau=\omega_0t$")
        ax.grid(alpha=0.18)
    fig.suptitle(r"Free series RLC response: $q(0)=q_0$, $i(0)=0$", fontsize=14)
    fig.savefig("rlc-free-damping.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
