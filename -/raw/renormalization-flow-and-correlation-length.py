"""An analytic infrared-flow and correlation-length scaling example.
Tested on Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; no SciPy.
Run from _media to emit this script's basename as PNG.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

EPSILON = 0.2
THERMAL_EIGENVALUE = 1.5


def flow(ell, g0):
    return EPSILON / (1 + (EPSILON/g0 - 1)*np.exp(-EPSILON*np.asarray(ell)))


def correlation_length(t, amplitude=1):
    return amplitude*np.abs(np.asarray(t))**(-1/THERMAL_EIGENVALUE)


def checks():
    ell = np.linspace(0, 30, 301)
    h = 1e-4
    residuals = []
    for g0 in (.025, .05, .12, .3, .6):
        g = flow(ell, g0)
        derivative = (flow(ell+h, g0)-flow(ell-h, g0))/(2*h)
        residuals.append(float(np.max(np.abs(derivative-(EPSILON*g-g*g)))))
        assert np.all(g >= min(g0, EPSILON)-1e-14)
        assert np.all(g <= max(g0, EPSILON)+1e-14)
    assert max(residuals) < 2e-9
    assert np.isclose(flow(np.log(1024), .05), 4/35)
    assert np.isclose(flow(np.log(1024), .6), 6/25)
    t = np.geomspace(1e-6, 1e-2, 81)
    scaling_residual = 0.0
    for b in (2., 4., 10.):
        for amplitude in (1., 2.):
            lhs = correlation_length(t, amplitude)
            rhs = b*correlation_length(b**THERMAL_EIGENVALUE*t, amplitude)
            scaling_residual = max(scaling_residual, float(np.max(np.abs(rhs/lhs-1))))
    assert scaling_residual < 2e-14
    slope = float(np.polyfit(np.log(t), np.log(correlation_length(t)), 1)[0])
    assert abs(slope + 2/3) < 1e-13
    return {"flow_derivative_max_residual": max(residuals),
            "correlation_scaling_max_relative_residual": scaling_residual,
            "log_slope": slope, "eigenvalues": [-EPSILON, THERMAL_EIGENVALUE]}


def main():
    print(checks())
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), facecolor="white")
    fig.subplots_adjust(left=.075, right=.98, bottom=.23, top=.80, wspace=.34)
    ell = np.linspace(0, 30, 400)
    colors = ["#376b9f", "#4f8a68", "#9c7b36", "#9860a4", "#bd584c"]
    for g0, color in zip((.025, .05, .12, .3, .6), colors):
        axes[0].plot(ell, flow(ell, g0), color=color, lw=2, label=f"{g0:g}")
    axes[0].axhline(EPSILON, color="#242b37", ls="--", lw=1.3)
    axes[0].text(29, .215, r"$g_*=1/5$", ha="right", fontsize=11)
    axes[0].set(xlabel=r"Increasing log length $\ell=\log(L/a)$ →",
                ylabel="Dimensionless coupling g", xlim=(0, 30), ylim=(0, .63))
    axes[0].legend(title=r"Initial $g_0$", fontsize=9, title_fontsize=9,
                   loc="upper right", frameon=False, ncol=2)
    axes[0].set_title(r"$dg/d\ell=g/5-g^2$", pad=13, fontsize=13)
    t = np.geomspace(1e-6, 1e-2, 120)
    ax = axes[1]
    ax.loglog(t, correlation_length(t), lw=2, color="#376b9f", label=r"$\xi/a,\ C_+=1$")
    ax.loglog(t, correlation_length(t, 2), lw=2, color="#bd584c", label=r"$\xi/a,\ C_+=2$")
    selected = np.geomspace(1e-6, 1e-2, 9)
    ax.loglog(selected, correlation_length(selected, 2)/2, "o", ms=5,
              mfc="white", mec="#bd584c", mew=1.4, label=r"$\xi/(aC_+),\ C_+=2$")
    ax.set(xlabel=r"Positive thermal coordinate $t$", ylabel="Correlation length in lattice units",
           xlim=(7e-7, 1.4e-2), ylim=(12, 30000))
    ax.set_title(r"Chosen $y_t=3/2$: $\nu=2/3$", pad=13, fontsize=13)
    ax.legend(fontsize=9, loc="upper right", frameon=False)
    ax.text(.04, .10, "Normalize the amplitude:\nred circles collapse onto blue.",
            transform=ax.transAxes, fontsize=10, color="#434d5d")
    for axis in axes:
        axis.spines[["top", "right"]].set_visible(False)
        axis.grid(alpha=.14)
    fig.suptitle("A solvable model of infrared attraction and thermal escape", fontsize=14, y=.96, weight="bold")
    fig.text(.075, .075, "Analytic example with chosen coefficients; not measured data or a precision 3D Ising calculation.",
             fontsize=10, color="#434d5d")
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
