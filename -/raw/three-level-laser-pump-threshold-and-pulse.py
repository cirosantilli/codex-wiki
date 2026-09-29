"""Original three-level population model, not a fit to ruby measurements.

Python 3.14 / numpy 2.3 / matplotlib 3.10. Matching PNG is written to the CWD.
The normalized equations count stored excitations and selected-mode photons.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def integrate(step=.0005, end=8., pump_end=4., coupling=100., loss=20., beta=1e-4):
    """RK4 on two constant-pump intervals; no step straddles the switch."""
    times = [0.]
    states = [np.zeros(2)]
    for start, stop, pump in [(0., pump_end, 3.), (pump_end, end, 0.)]:
        n = round((stop-start)/step)
        h = (stop-start)/n
        y = states[-1].copy()
        def rhs(z):
            u, s = z
            stimulated = coupling*(2*u-1)*s
            return np.array([pump*(1-u)-u-stimulated,
                             stimulated-loss*s+beta*u])
        for i in range(n):
            k1 = rhs(y)
            k2 = rhs(y+h*k1/2)
            k3 = rhs(y+h*k2/2)
            k4 = rhs(y+h*k3)
            y = y+h*(k1+2*k2+2*k3+k4)/6
            times.append(start+(i+1)*h)
            states.append(y.copy())
    return np.asarray(times), np.asarray(states)


def main():
    plt.rcParams.update({"font.size":11, "axes.spines.top":False,
                         "axes.spines.right":False})
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 6), facecolor="white")
    fig.subplots_adjust(left=.065, right=.94, bottom=.18, top=.77, wspace=.31)
    x = np.linspace(0, 3, 601)
    for r, col in [(.5,"#8c8c8c"), (1.,"#bc8b31"), (2.,"#3d7ca5"), (3.,"#4a8d5b")]:
        u = r/(r+1)*(1-np.exp(-(r+1)*x))
        axes[0].plot(x, u, color=col, lw=2, label=f"r = {r:g}")
    axes[0].axhline(.5, color=".55", linestyle=":", label="Inversion: u = 0.5")
    axes[0].axhline(.6, color="#a63f43", linestyle="--", label="Loss threshold: u = 0.6")
    axes[0].set(xlabel=r"Time $t/\tau$", ylabel="Excited-state fraction u", xlim=(0, 3), ylim=(0, .85),
                title="Negligible-light filling model")
    axes[0].legend(loc="lower right", fontsize=9)
    xx, ys = integrate()
    assert np.all(ys >= -1e-12) and ys[:, 0].max() <= 1+1e-12
    ax = axes[1]
    ax.plot(xx, ys[:, 0], color="#3d7ca5", lw=1.8, label="Excited fraction u")
    ax.axhline(.6, color="#a63f43", linestyle="--", lw=1, label="u threshold")
    ax.axvline(4, color=".45", linestyle=":", lw=1)
    ax.axvspan(0, 4, color="#f3d8a3", alpha=.28)
    ax.set(xlabel=r"Time $t/\tau$", ylabel="Excited-state fraction u", xlim=(0, 8), ylim=(0, .85),
           title="Coupled populations under a finite pump")
    photons = ax.twinx()
    photons.plot(xx, ys[:, 1], color="#b85136", lw=1.7, label="Photons per emitter s")
    photons.set_ylabel("Cavity photons per emitter s", color="#a44830")
    photons.tick_params(axis="y", colors="#a44830")
    photons.spines["top"].set_visible(False)
    photons.set_ylim(bottom=0)
    ax.text(1.8, .80, "Pump r = 3", ha="center", fontsize=10)
    ax.text(5.8, .80, "Pump off", ha="center", fontsize=10)
    handles, labels = ax.get_legend_handles_labels()
    h2, l2 = photons.get_legend_handles_labels()
    ax.legend(handles+h2, labels+l2, fontsize=9, loc="upper right", bbox_to_anchor=(1.02, .83))
    fig.suptitle("A laser pulse draws on stored excitation", y=.96, fontsize=18)
    fig.text(.5, .885, r"Original reduced model: $C=100$, $K=20$, $\beta=10^{-4}$; initial $u=s=0$",
             ha="center", fontsize=12)
    fig.text(.5, .825, "All rates are chosen dimensionless inputs; these are not measured ruby lifetimes or a historical pulse trace",
             ha="center", color=".3", fontsize=10)
    fig.text(.5, .055, "Pump energy fills the upper state. Stimulated exchange cancels from the total excitation budget u + s.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
