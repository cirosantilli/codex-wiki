"""Generate lie-bracket-rotation-order.png in the current working directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: python ../lie-bracket-rotation-order.py
Active rotations act on column vectors; the rightmost matrix acts first.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def rotation_x(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[1., 0., 0.], [0., c, -s], [0., s, c]])


def rotation_y(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, 0., s], [0., 1., 0.], [-s, 0., c]])


def commutator(angle):
    return (rotation_x(angle) @ rotation_y(angle)
            @ rotation_x(-angle) @ rotation_y(-angle))


def main():
    e1 = np.array([1., 0., 0.])
    x = np.array([[0., 0., 0.], [0., 0., -1.], [0., 1., 0.]])
    y = np.array([[0., 0., 1.], [0., 0., 0.], [-1., 0., 0.]])
    z = x @ y - y @ x
    assert np.array_equal(z, [[0, -1, 0], [1, 0, 0], [0, 0, 0]])
    identity = np.eye(3)
    for angle in (.1, .25, .4):
        product = commutator(angle)
        c, s = np.cos(angle), np.sin(angle)
        exact = np.array([c*c + c*s*s, s*s*(2*c-c*c),
                          s*(c*c*c-c*c+s*s)])
        assert np.allclose(product @ e1, exact, atol=2e-15, rtol=0)
        assert np.allclose(product.T @ product, identity, atol=2e-15)
        assert np.isclose(np.linalg.det(product), 1)
        swapped = (rotation_y(angle) @ rotation_x(angle)
                   @ rotation_y(-angle) @ rotation_x(-angle))
        assert np.allclose(swapped, product.T, atol=2e-15)
    small = 1e-3
    assert np.linalg.norm((commutator(small) - identity) / small**2 - z) < .002
    assert np.linalg.norm((commutator(small / 2) - identity)
                          / (small / 2)**2 - z) < .001

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12,
                         "axes.labelsize": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), dpi=120)
    fig.subplots_adjust(left=.08, right=.97, bottom=.25, top=.79, wspace=.34)
    fig.suptitle("Four rotations leave a second-order motion", fontsize=16, y=.97)
    fig.text(.5, .87,
             r"$C_\varepsilon=R_x(\varepsilon)R_y(\varepsilon)"
             r"R_x(-\varepsilon)R_y(-\varepsilon)"
             r"=I+\varepsilon^2Z+O(\varepsilon^3),\quad [X,Y]=Z$",
             ha="center", fontsize=13)

    angle = .25
    ax = axes[0]
    colors = ["#276ba3", "#c76a21", "#218466", "#8662aa"]
    steps = [(rotation_y, -angle), (rotation_x, -angle),
             (rotation_y, angle), (rotation_x, angle)]
    point = e1.copy()
    endpoints = [point.copy()]
    for number, ((rotate, signed_angle), color) in enumerate(zip(steps, colors), 1):
        arc = np.array([rotate(t) @ point
                        for t in np.linspace(0, signed_angle, 101)])
        ax.plot(arc[:, 1], arc[:, 2], color=color, lw=2.5)
        ax.annotate("", xy=arc[65, [1, 2]], xytext=arc[45, [1, 2]],
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
        point = arc[-1]
        endpoints.append(point.copy())
        ax.scatter(point[1], point[2], color=color, s=26, zorder=5)
    assert np.allclose(point, commutator(angle) @ e1, atol=2e-15)
    ax.scatter(0, 0, s=32, color="#29333d", zorder=6)
    labels = [("Start", (0, 0), (-.021, -.035)),
              ("1", endpoints[1][[1, 2]], (-.012, .268)),
              ("2", endpoints[2][[1, 2]], (.074, .245)),
              ("3", endpoints[3][[1, 2]], (.079, -.030)),
              ("4: endpoint", endpoints[4][[1, 2]], (.078, .043))]
    for label, xy, xytext in labels:
        ax.annotate(label, xy=xy, xytext=xytext, fontsize=10,
                    arrowprops={"arrowstyle": "-", "color": "#65717c"})
    ax.annotate("", xy=point[[1, 2]], xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "color": "#29333d", "lw": 1.7})
    ax.scatter(angle**2, 0, marker="x", s=55, color="#b92e3c", zorder=8)
    ax.annotate(r"$\varepsilon^2Ze_1$", xy=(angle**2, 0), xytext=(.017, .085),
                color="#b92e3c", fontsize=12,
                arrowprops={"arrowstyle": "-", "color": "#b92e3c"})
    ax.set(title=r"Actual arcs, projected onto $yz$ ($\varepsilon=0.25$)",
           xlabel=r"$y$", ylabel=r"$z$", xlim=(-.026, .13), ylim=(-.048, .29))
    ax.set_xticks([0, .05, .10])
    ax.set_yticks([0, .1, .2])
    ax.grid(alpha=.18)

    ax = axes[1]
    angles = np.linspace(.002, .4, 220)
    residuals = np.array([(commutator(t) @ e1 - e1) / t**2 for t in angles])
    ax.plot(angles, residuals[:, 1], color=colors[2], lw=2.5,
            label=r"$\Delta y/\varepsilon^2\ \longrightarrow\ 1$")
    ax.plot(angles, residuals[:, 2], color=colors[0], lw=2.5,
            label=r"$\Delta z/\varepsilon^2\ \longrightarrow\ 0$")
    ax.axhline(1, color="#a8b1ba", lw=1, ls="--")
    ax.axhline(0, color="#a8b1ba", lw=1, ls="--")
    ax.scatter([0, 0], [1, 0], facecolors="white", edgecolors="#29333d", zorder=5)
    ax.set(title="Divide by the square of the angle",
           xlabel=r"$\varepsilon$ (radians)", ylabel="Scaled residual",
           xlim=(-.012, .412), ylim=(-.07, 1.1))
    ax.set_xticks([0, .1, .2, .3, .4])
    ax.legend(loc="center right", frameon=False, fontsize=11)
    ax.grid(alpha=.18)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)

    fig.text(.5, .14, "Action order on a column vector (rightmost first):",
             ha="center", fontsize=11)
    fig.text(.5, .09,
             r"1: $R_y(-\varepsilon)$     2: $R_x(-\varepsilon)$"
             r"     3: $R_y(+\varepsilon)$     4: $R_x(+\varepsilon)$",
             ha="center", fontsize=12)
    fig.text(.5, .025,
             "The bracket predicts the leading +z-axis rotation; finite angles have smaller corrections.",
             ha="center", fontsize=10, color="#52616c")
    output = Path.cwd() / "lie-bracket-rotation-order.png"
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output}")
    print("C_0.1 e1 =", commutator(.1) @ e1)


if __name__ == "__main__":
    main()
