"""Plot the CP1 free-flight velocity solutions; save one PNG in the current directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    theta = np.pi / 4
    t = np.linspace(0, 4, 1201)
    s, c = np.sin(theta), np.cos(theta)

    def height(tau):
        return (s + 1) * (-np.expm1(-tau)) - tau

    lo, hi = 1e-7, 4.0
    for _ in range(70):
        mid = (lo + hi) / 2
        if height(mid) > 0:
            lo = mid
        else:
            hi = mid
    drag_landing = (lo + hi) / 2
    cases = [
        ("(i) No drag", c + 0 * t, s - t, 2 * s, (-3.5, 1)),
        ("(ii) Linear drag", c * np.exp(-t), (s + 1) * np.exp(-t) - 1,
         drag_landing, (-1.3, 1)),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4), layout="constrained")
    fig.patch.set_facecolor("white")
    for ax, (title, vx, vy, landing, limits) in zip(axes, cases):
        physical = t <= landing
        for velocity, color, label in [(vx, "#2166ac", r"$v_x/v_0$"),
                                       (vy, "#c65d12", r"$v_y/v_0$")]:
            ax.plot(t[physical], velocity[physical], color=color, lw=2.3, label=label)
            ax.plot(t[~physical], velocity[~physical], color=color, lw=1.5, ls="--")
        ax.axvline(landing, color="0.6", lw=1, ls=":")
        ax.text(landing + 0.06, limits[0] + 0.15, "ground contact", rotation=90,
                color="0.38", fontsize=9, va="bottom")
        ax.axhline(0, color="0.6", lw=0.7)
        ax.set(xlim=(0, 4), ylim=limits, xlabel=r"$T=gt/v_0$",
               ylabel="Velocity component / launch speed", title=title)
        ax.set_facecolor("white")
        ax.grid(alpha=0.15)
        ax.legend(loc="upper right", framealpha=1)
    axes[1].axhline(-1, color="0.55", ls=":", lw=1)
    axes[1].text(2.55, -0.91, "terminal value", color="0.35", fontsize=9)
    fig.suptitle(r"Launch at $45^\circ$; right panel: $\alpha v_0/(mg)=1$", fontsize=12)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, dpi=120, facecolor="white", metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
