"""Exact original two-dimensional Gaussian diffusion example; PNG in CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    r = np.linspace(0, 5.5, 1001)
    times = [0., .25, 1.]
    colors = ["#222222", "#a64f00", "#006f86"]
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.0), dpi=120, facecolor="white")
    for t, color in zip(times, colors):
        s = 1+4*t
        axes[0].plot(r, np.exp(-r*r/s)/s, lw=2.3, color=color,
                     label=rf"$t={t:g}$: peak ${1/s:g}$")
    axes[0].set(xlabel=r"Radius $r=\sqrt{x^2+y^2}$", ylabel=r"$u(r,t)$",
                xlim=(0, 5.5), ylim=(-.035, 1.075))
    axes[0].set_title("Lower peak, wider profile", fontsize=14)
    axes[0].legend(fontsize=11, frameon=False)
    t = .25
    s = 1+4*t
    rate = 4*(r*r-s)/s**3*np.exp(-r*r/s)
    axes[1].plot(r, rate, color="#333333", lw=2)
    axes[1].fill_between(r, 0, rate, where=rate<=0, color="#2166ac", alpha=.3,
                         label="Inner region decreases")
    axes[1].fill_between(r, 0, rate, where=rate>=0, color="#b2182b", alpha=.3,
                         label="Outer region increases")
    axes[1].axhline(0, color="#777777", lw=.8)
    axes[1].axvline(np.sqrt(s), color="#777777", lw=1, ls="--")
    axes[1].text(np.sqrt(s)+.12, -.58, r"$r=\sqrt{2}$", fontsize=12)
    axes[1].set(xlabel=r"Radius $r$", ylabel=r"$u_t(r,t)=\Delta u(r,t)$",
                xlim=(0, 5.5), ylim=(-1.08, .24))
    axes[1].set_title(r"Instantaneous change at $t=1/4$", fontsize=14)
    axes[1].legend(loc="lower right", fontsize=10.5, frameon=False)
    for ax in axes:
        ax.grid(alpha=.22)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=11)
    fig.suptitle(r"Exact diffusion: $u(r,t)=(1+4t)^{-1}\exp[-r^2/(1+4t)]$",
                 fontsize=17, weight="bold", y=.97)
    fig.text(.5, .075, r"On the whole plane: $2\pi\int_0^\infty r\,u(r,t)\,dr=\pi$ at every time.",
             ha="center", fontsize=13)
    fig.text(.5, .025, "Analytic model in dimensionless coordinates with diffusivity 1; not measured data.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.075, right=.98, top=.80, bottom=.22, wspace=.30)
    fig.savefig(Path(__file__).stem+".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
