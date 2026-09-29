"""Render 2017-exponential-endpoint-integral.png into the current directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    # x=1-s^2 removes the endpoint square root; quadrature nodes avoid s=1.
    nodes, weights = np.polynomial.legendre.leggauss(128)
    ss = (nodes + 1) / 2
    xx = 1 - ss**2
    tt = np.linspace(-3, 2, 301)
    tx = tt[:, None] * xx
    ff = (np.expm1(tx) / xx) @ weights
    dd = np.exp(tx) @ weights
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.4, 4.5), dpi=100, facecolor="white")
    left.plot(tt, ff, color="#2563eb", linewidth=2, label=r"$F(t)$")
    left.plot(tt, 2 * tt, color="#c2410c", linestyle="--", linewidth=1.5,
              label=r"Tangent at zero: $2t$")
    left.scatter([0], [0], color="#111827", s=25, zorder=4)
    left.set(xlabel=r"Parameter $t$", ylabel="Integral value", title="Convexity and the tangent bound")
    left.legend(frameon=False, fontsize=10, loc="upper left")
    right.plot(tt, dd, color="#15803d", linewidth=2, label=r"$F'(t)$")
    right.axhline(2, color="#c2410c", linestyle="--", linewidth=1.5, label="Reference value 2")
    right.fill_between(tt, dd, 2, where=tt < 0, color="#fed7aa", alpha=0.55)
    right.fill_between(tt, dd, 2, where=tt > 0, color="#bbf7d0", alpha=0.55)
    right.scatter([0], [2], color="#111827", s=25, zorder=4)
    right.set(xlabel=r"Parameter $t$", ylabel="Derivative", title=r"$F'(t)<2$ for $t<0$; $F'(t)>2$ for $t>0$")
    right.legend(frameon=False, fontsize=10, loc="upper left")
    for ax in (left, right):
        ax.axvline(0, color="#cbd5e1", linewidth=0.8, zorder=0)
        ax.grid(alpha=0.2)
    fig.suptitle(r"$F(t)=\int_0^1 (e^{tx}-1)/(x\sqrt{1-x})\,dx$", fontsize=15)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.15, top=0.76, wspace=0.29)
    fig.savefig("2017-exponential-endpoint-integral.png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
