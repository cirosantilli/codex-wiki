"""Generate lie-affine-noncommutation.png in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media. Products act on column vectors, rightmost factor first.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def scale(a):
    return np.array([[np.exp(a), 0.], [0., 1.]])


def translate(b):
    return np.array([[1., b], [0., 1.]])


def main():
    d = np.array([[1., 0.], [0., 0.]])
    t = np.array([[0., 1.], [0., 0.]])
    assert np.array_equal(d @ t - t @ d, t)
    point = np.array([1., 1.])
    a = np.log(2.)
    first = (scale(a) @ translate(1.) @ point)[0]
    second = (translate(1.) @ scale(a) @ point)[0]
    assert np.isclose(first, 4.) and np.isclose(second, 3.)
    for a, b in [(np.log(2), 1.), (.1, .1), (-.2, .3)]:
        product = scale(a) @ translate(b) @ scale(-a) @ translate(-b)
        assert np.allclose(product, translate(np.expm1(a) * b))
    displacement = .1 * np.expm1(.1)
    assert np.isclose(displacement, .010517091807564762, atol=1e-15)
    eps_checks = np.array([.1, .05, .01])
    ratios = np.expm1(eps_checks) / eps_checks
    assert np.all(np.diff(np.abs(ratios - 1)) < 0)

    blue, orange, gray = "#276ba3", "#bf6224", "#667887"
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.7), dpi=120,
                             facecolor="white",
                             gridspec_kw={"width_ratios": [1.2, 1]})
    ax = axes[0]
    ax.set_title("Reverse the order, change the endpoint", fontsize=12, pad=15)
    ax.set(xlim=(.6, 4.4), ylim=(-.55, 2.15), xlabel="Position on the real line")
    ax.set_xticks([1, 2, 3, 4])
    ax.set_yticks([])
    ax.spines[["top", "right", "left"]].set_visible(False)
    for y, end, color, title, first_label, second_label in [
            (1.25, 4., blue, r"Translate, then double: $S_{\log 2}U_1$",
             "+1", "×2"),
            (.1, 3., orange, r"Double, then translate: $U_1S_{\log 2}$",
             "×2", "+1")]:
        ax.axhline(y, color="#d4dce1", lw=1, zorder=0)
        ax.text(.72, y + .65, title, color=color, fontsize=11)
        for start, finish, label in [(1., 2., first_label), (2., end, second_label)]:
            ax.annotate("", xy=(finish - .07, y), xytext=(start + .07, y),
                        arrowprops=dict(arrowstyle="->", color=color, lw=2))
            ax.text((start + finish) / 2, y + .17, label, color=color,
                    fontsize=12, ha="center")
        ax.scatter([1, 2, end], [y] * 3, color=color, s=40, zorder=5)
        for value in [1, 2, end]:
            ax.text(value, y - .27, f"{value:g}", ha="center", color=color,
                    fontsize=12)

    ax = axes[1]
    eps = np.linspace(0., .4, 400)
    ax.plot(eps, eps * np.expm1(eps), color=blue, lw=2,
            label=r"Exact: $\varepsilon(e^\varepsilon-1)$")
    ax.plot(eps, eps**2, "--", color=orange, lw=2,
            label=r"Leading term: $\varepsilon^2$")
    ax.scatter([.1], [displacement], color=blue, s=35, zorder=4)
    ax.annotate("ε = 0.1\nshift = 0.01051709", xy=(.1, displacement),
                xytext=(.04, .085), fontsize=10, color=gray,
                arrowprops=dict(arrowstyle="->", color=gray))
    ax.set(xlim=(0, .4), ylim=(0, .21), xlabel=r"Equal parameters $a=b=\varepsilon$",
           ylabel="Residual translation")
    ax.set_title("Four moves leave a second-order shift", fontsize=12, pad=15)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=.18)
    ax.legend(loc="upper left", fontsize=10, frameon=False)
    fig.tight_layout(pad=1.5, w_pad=2)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"endpoints: {first:g}, {second:g}")
    print(f"commutator displacement at a=b=.1 = {displacement:.12f}")
    print(f"displacement/epsilon^2 for .1, .05, .01 = {ratios}")
    print(output.name)


if __name__ == "__main__":
    main()
