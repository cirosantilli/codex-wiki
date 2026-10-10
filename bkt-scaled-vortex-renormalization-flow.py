"""Original leading-order BKT model, not data. Python 3.14 / mpl 3.10.7 / NumPy 2.3.5.

Run from _media. Integrate X'=Y^2, Y'=XY by RK4, check against closed forms
and the invariant X^2-Y^2. The small plotted domain is the near-critical model.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def rhs(z):
    x, y = z
    return np.array([y * y, x * y])


def trajectory(x0, y0=.06, end=30, step=.005):
    ell = np.linspace(0, end, round(end / step) + 1)
    z = np.empty((len(ell), 2))
    z[0] = [x0, y0]
    for i, h in enumerate(np.diff(ell)):
        a = rhs(z[i])
        b = rhs(z[i] + h * a / 2)
        c = rhs(z[i] + h * b / 2)
        d = rhs(z[i] + h * c)
        z[i + 1] = z[i] + h * (a + 2 * b + 2 * c + d) / 6
    invariant = z[:, 0] ** 2 - z[:, 1] ** 2
    np.testing.assert_allclose(invariant, invariant[0], atol=2e-12, rtol=0)
    return ell, z, float(np.max(np.abs(invariant - invariant[0])))


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (ax, stiff) = plt.subplots(1, 2, figsize=(9.6, 4.7), layout="constrained")
    xx, yy = np.meshgrid(np.linspace(-.15, .16, 24), np.linspace(.006, .18, 20))
    vx, vy = yy ** 2, xx * yy
    speed = np.hypot(vx, vy)
    ax.quiver(xx, yy, vx / speed, vy / speed, color="#c2c9ce", pivot="mid", scale=32, width=.0026)
    checks = []
    for x0, label, color in [(-.10, "Bound side", "#287b57"), (-.06, "Critical separatrix", "#6e4aa2"), (-.03, "Unbinding side", "#c35438")]:
        ell, z, drift = trajectory(x0)
        if x0 == -.06:
            exact_x = -.06 / (1 + .06 * ell)
            exact_y = -exact_x
        elif x0 == -.10:
            c = np.sqrt(x0 * x0 - .06 ** 2)
            arg = c * ell + np.arcsinh(c / .06)
            exact_x, exact_y = -c / np.tanh(arg), c / np.sinh(arg)
        else:
            c = np.sqrt(.06 ** 2 - x0 * x0)
            arg = c * ell + np.arctan(x0 / c)
            exact_x, exact_y = c * np.tan(arg), c / np.cos(arg)
        error = float(np.max(np.abs(z - np.column_stack([exact_x, exact_y]))))
        assert error < 1e-10
        checks.append({"X0":x0, "Y0":.06, "max_invariant_drift":drift, "max_closed_form_error":error})
        ax.plot(z[:, 0], z[:, 1], color=color, lw=2.5, label=label)
        ax.scatter(*z[0], s=30, color=color, zorder=5)
        j = len(z) // 2
        ax.annotate("", xy=z[j + 150], xytext=z[j], arrowprops={"arrowstyle":"->", "color":color, "lw":2})
        stiff.plot(ell, (2 - z[:, 0]) / np.pi, color=color, lw=2.3, label=label)
    ax.plot([-.18, 0], [.18, 0], ls="--", color="#6e4aa2", alpha=.65, zorder=0)
    ax.axhline(0, color="#444444", lw=1.5)
    ax.text(-.146, .007, "Fixed line: Y = 0", fontsize=9)
    ax.set(xlim=(-.15, .16), ylim=(-.005, .18), xlabel=r"$X=2-\pi K$", ylabel=r"$Y=4\pi y$", title="Flow toward longer distances")
    ax.legend(loc="upper left", fontsize=9, framealpha=.95)
    stiff.axhline(2 / np.pi, color="#666666", ls="--", label=r"$K_c=2/\pi$")
    stiff.set(xlim=(0, 30), xlabel=r"$\ell=\log(L/a)$", ylabel=r"$K(\ell)=(2-X(\ell))/\pi$", title="Finite-scale stiffness")
    stiff.legend(loc="lower left", fontsize=9)
    stiff.grid(alpha=.18)
    fig.suptitle("Leading near-critical model: $X'=Y^2$, $Y'=XY$; $X^2-Y^2$ is constant", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(checks)


if __name__ == "__main__":
    main()
