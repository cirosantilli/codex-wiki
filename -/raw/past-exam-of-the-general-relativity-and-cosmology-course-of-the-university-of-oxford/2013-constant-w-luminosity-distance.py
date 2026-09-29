"""Original exact single-fluid distance curves for Oxford 2013 GR Q4.

The displayed quantity is H0 D_L / c. Writes matching PNG into CWD.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def dimensionless_distance(z, w):
    alpha = (1+3*w)/2
    if abs(alpha) < 1e-12:
        return (1+z)*np.log1p(z)
    return (1+z)*(-np.expm1(-alpha*np.log1p(z)))/alpha


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
    z = np.linspace(0, 2, 801)
    cases = [(-1, "#0072B2", r"$w=-1$"), (-1/3, "#009E73", r"$w=-1/3$ (coasting)"),
             (0, "#D55E00", r"$w=0$ (dust)"), (1/3, "#CC79A7", r"$w=1/3$ (radiation)")]
    for w, color, label in cases:
        axes[0].plot(z, dimensionless_distance(z, w), color=color, label=label)
    axes[0].set(xlabel=r"redshift $z$", ylabel=r"$H_0 D_L/c$", xlim=(0, 2), ylim=(0, 6.2),
                title="Exact distances in flat single-fluid models")
    axes[0].legend(loc="upper left", fontsize=10)
    small = np.linspace(0, .5, 401)
    for w, color, label in [cases[0], cases[2]]:
        axes[1].plot(small, dimensionless_distance(small, w), color=color, label=label+" exact")
        approx = small+(1-3*w)*small**2/4
        axes[1].plot(small, approx, linestyle="--", color=color, label=label+" quadratic")
    axes[1].set(xlabel=r"redshift $z$", ylabel=r"$H_0 D_L/c$", xlim=(0, .5), ylim=(0, .8),
                title="Low-redshift quadratic approximation")
    axes[1].legend(loc="upper left", fontsize=9)
    for ax in axes:
        ax.grid(alpha=.2)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
