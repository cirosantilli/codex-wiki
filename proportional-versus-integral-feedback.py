"""Compare ideal P and PI feedback, checking RK4 against exact solutions.

The disturbance is constant within each RK4 step; the grid splits at t=4.
PNG goes to cwd. Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def simulate(time, disturbance=0.0, switch=4.0):
    """State = (x_P, x_PI, z); fixed gains k=k_p=2, k_i=1."""
    state = np.zeros((len(time), 3))
    assert np.any(time == switch), "The grid must contain the disturbance switch."
    assert np.all((time[:-1] >= switch) | (time[1:] <= switch)), "A step crosses the switch."
    for i, h in enumerate(np.diff(time)):
        w = disturbance if time[i] >= switch else 0.0

        def rhs(value):
            xp, xpi, z = value
            return np.array([2 * (1 - xp) + w, 2 * (1 - xpi) + z + w, 1 - xpi])

        current = state[i]
        a = rhs(current)
        b = rhs(current + h * a / 2)
        c = rhs(current + h * b / 2)
        d = rhs(current + h * c)
        state[i + 1] = current + h * (a + 2 * b + 2 * c + d) / 6
    return state


def exact(time, disturbance=0.0, switch=4.0):
    elapsed = np.maximum(time - switch, 0.0)
    xp = -np.expm1(-2 * time) - disturbance / 2 * np.expm1(-2 * elapsed)
    xpi = 1 - (1 - time) * np.exp(-time) + disturbance * elapsed * np.exp(-elapsed)
    z = time * np.exp(-time) - disturbance * (1 - (1 + elapsed) * np.exp(-elapsed))
    return np.column_stack([xp, xpi, z])


def main():
    time = np.linspace(0, 14, 7001)
    nominal = simulate(time)
    disturbed = simulate(time, disturbance=0.2)
    nominal_error = np.max(np.abs(nominal - exact(time)))
    disturbed_error = np.max(np.abs(disturbed - exact(time, disturbance=0.2)))
    np.testing.assert_allclose(nominal, exact(time), atol=2e-11, rtol=0)
    np.testing.assert_allclose(disturbed, exact(time, disturbance=0.2), atol=2e-11, rtol=0)
    peak_index = np.argmax(nominal[:, 1])
    assert time[peak_index] == 2
    np.testing.assert_allclose(nominal[peak_index, 1], 1 + np.exp(-2), atol=2e-11, rtol=0)
    np.testing.assert_allclose(disturbed[-1], [1.1, 1, -0.2], atol=1.2e-4, rtol=0)
    print(f"RK4 exact-solution errors: nominal={nominal_error:.3g}, disturbed={disturbed_error:.3g}; "
          f"peak x_PI(2)={nominal[peak_index, 1]:.9f}; "
          f"at t=14: x_P={disturbed[-1, 0]:.9f}, x_PI={disturbed[-1, 1]:.9f}, "
          f"z={disturbed[-1, 2]:.9f}")

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), dpi=120, facecolor="white")
    for ax, values, title, end in zip(
        axes, [nominal, disturbed],
        [r"Reference arrival: $w=0$", r"Disturbance rejection: $w=0.2$ from $t=4$"], [7, 14]
    ):
        ax.axhline(1, color="#555555", ls="--", lw=1.2, label=r"Reference $r=1$")
        ax.plot(time, values[:, 0], color="#bd7024", lw=2.4, label=r"P: $u=2e$")
        ax.plot(time, values[:, 1], color="#207699", lw=2.4, label=r"PI: $u=2e+z$, $\dot{z}=e$")
        ax.set(title=title, xlabel="Dimensionless time t", ylabel="Dimensionless position x",
               xlim=(0, end), ylim=(0, 1.35))
        ax.legend(loc="lower right", frameon=True, facecolor="white", framealpha=1, fontsize=9)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(color="#e5e9eb", lw=0.7)
        ax.set_axisbelow(True)
    axes[0].scatter([2], [1 + np.exp(-2)], s=30, color="#207699", zorder=5)
    axes[0].annotate("PI peak: 1.135335 at t=2", xy=(2, 1 + np.exp(-2)), xytext=(2.5, 1.25),
                     fontsize=9, arrowprops={"arrowstyle": "->"})
    axes[0].text(0.27, 0.42, "Integral memory removes a persistent offset;\nit can also produce overshoot.",
                 fontsize=9, transform=axes[0].transAxes)
    axes[1].axvline(4, color="#999999", ls=":", lw=1.2)
    axes[1].hlines(1.1, 4, 14, color="#bd7024", ls=":", lw=1)
    axes[1].annotate("P: lasting offset +0.1", xy=(11, 1.1), xytext=(7.0, 1.25),
                     fontsize=9, arrowprops={"arrowstyle": "->", "color": "#bd7024"})
    axes[1].annotate("PI: returns to 1", xy=(12, disturbed[6000, 1]), xytext=(7.0, 0.79),
                     fontsize=9, arrowprops={"arrowstyle": "->", "color": "#207699"})
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.14, top=0.90, wspace=0.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
