"""Positive-feedback binary-chain mean-field minima; continuous onset."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def minimum(temperature):
    if temperature >= 1:
        return 0.
    lo, hi = 1e-10, 1.
    for _ in range(70):
        mid = (lo+hi)/2
        if np.tanh(mid/temperature)-mid > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def main():
    temp = np.linspace(.05, 1.6, 601)
    extension = np.array([minimum(t) for t in temp])
    x = np.linspace(-.9999, .9999, 701)
    entropy_part = .5*((1+x)*np.log(1+x)+(1-x)*np.log(1-x))
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.4), layout="constrained")
    axes[0].plot(temp, extension, lw=2.2)
    axes[0].axvline(1, ls="--", color="0.5")
    axes[0].set(xlabel=r"$T/T_c$", ylabel=r"Stable $L/(Na)$, positive branch", title="Extension emerges continuously", ylim=(-.04, 1.04))
    for t in [.75, 1, 1.25]:
        axes[1].plot(x, -.5*x*x+t*entropy_part, label=f"T/Tc = {t}")
    axes[1].set(xlabel=r"$x=L/(Na)$", ylabel=r"$[F(x)-F(0)]/(Nk_BT_c)$", title="One minimum becomes two")
    axes[1].legend(frameon=False)
    for ax in axes:
        ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
