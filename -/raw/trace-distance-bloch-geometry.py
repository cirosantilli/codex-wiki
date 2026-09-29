"""Original Bloch geometry for zero-versus-plus discrimination.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Run from _media; writes the matching opaque white PNG basename to cwd.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    r = np.array([0., 0., 1.])
    s = np.array([1., 0., 0.])
    difference = r - s
    n = difference / np.linalg.norm(difference)
    blue, green, red, gold = "#2367a0", "#188454", "#b33d4b", "#a36d08"
    fig = plt.figure(figsize=(10.4, 5.3), dpi=120)
    sphere = fig.add_subplot(121, projection="3d")
    azimuth, polar = np.meshgrid(np.linspace(0, 2 * np.pi, 25),
                                np.linspace(0, np.pi, 13))
    sphere.plot_wireframe(np.cos(azimuth) * np.sin(polar),
                          np.sin(azimuth) * np.sin(polar), np.cos(polar),
                          color="#bdc6ce", lw=0.5, alpha=0.55)
    for tip, color in [(r, blue), (s, green), (n, gold)]:
        sphere.quiver(0, 0, 0, *tip, color=color, linewidth=2.5,
                      arrow_length_ratio=0.12)
    sphere.quiver(*s, *difference, color=red, linewidth=2.5,
                  arrow_length_ratio=0.10)
    sphere.text(0.06, 0, 1.15, r"$\mathbf{r}$: $|0\rangle$", color=blue)
    sphere.text(1.10, 0, -0.06, r"$\mathbf{s}$: $|+\rangle$", color=green)
    sphere.text(-0.95, 0, 0.84, r"$\mathbf{n}$", color=gold)
    sphere.set(xlim=(-1.2, 1.25), ylim=(-1.2, 1.2), zlim=(-1.2, 1.3),
               xlabel="x", ylabel="y", zlabel="z",
               title="Pure states on the Bloch sphere")
    sphere.set_xticks([-1, 0, 1])
    sphere.set_yticks([-1, 0, 1])
    sphere.set_zticks([-1, 0, 1])
    sphere.set_box_aspect((1, 1, 1))
    sphere.view_init(elev=20, azim=55)
    sphere.grid(False)
    for axis in (sphere.xaxis, sphere.yaxis, sphere.zaxis):
        axis.pane.fill = False

    plane = fig.add_subplot(122)
    angle = np.linspace(0, 2 * np.pi, 401)
    plane.plot(np.cos(angle), np.sin(angle), color="#bdc6ce", lw=1.5)
    plane.axhline(0, color="#dddfe2", lw=0.8)
    plane.axvline(0, color="#dddfe2", lw=0.8)
    plane.plot([-1.16 * n[0], 1.16 * n[0]],
               [-1.16 * n[2], 1.16 * n[2]], "--", color=gold, lw=1.4)
    for tip, color in [(r, blue), (s, green), (n, gold)]:
        plane.annotate("", (tip[0], tip[2]), (0, 0),
                       arrowprops={"arrowstyle": "->", "color": color, "lw": 2.5})
    plane.annotate("", (r[0], r[2]), (s[0], s[2]),
                   arrowprops={"arrowstyle": "->", "color": red, "lw": 2.5})
    plane.scatter([r[0], s[0]], [r[2], s[2]], s=40,
                  color=[blue, green], zorder=4)
    plane.text(0.06, 1.08, r"$\mathbf{r}=(0,0,1)$", color=blue)
    plane.text(0.73, -0.19, r"$\mathbf{s}=(1,0,0)$", color=green)
    plane.text(-1.15, 0.87, r"$\mathbf{n}=(-1,0,1)/\sqrt{2}$", color=gold, fontsize=10)
    plane.text(0.45, 0.66, r"$\mathbf{r}-\mathbf{s}$", color=red)
    plane.text(0.36, 0.43, r"length $\sqrt{2}$", color=red)
    plane.text(-1.12, -1.05, "Dashed line: optimal measurement axis", color=gold,
               fontsize=10)
    plane.set(xlim=(-1.25, 1.38), ylim=(-1.2, 1.3), aspect="equal",
              xlabel="Bloch x coordinate", ylabel="Bloch z coordinate",
              title="The same geometry in the y = 0 plane")
    plane.set_xticks([-1, 0, 1])
    plane.set_yticks([-1, 0, 1])
    plane.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Trace distance: half the straight-line Bloch-vector separation",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.035,
             r"$D=|\mathbf{r}-\mathbf{s}|/2=1/\sqrt{2}$"
             "     |     "
             r"$P_{\mathrm{success}}^{\mathrm{opt}}=(1+D)/2\approx0.853553$",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.025, right=0.97, bottom=0.15, top=0.85, wspace=0.22)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
