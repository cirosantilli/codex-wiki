"""Plot normalized primary coma: pupil rings mapped by grad(w).

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; writes an opaque white PNG to the working directory.
No physical lens prescription, diffraction calculation, or measured data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def ray_map(u, v, h=1.0):
    """w = h*u*(u*u+v*v); normalized transverse error = grad(w)."""
    return h * (3 * u * u + v * v), 2 * h * u * v


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (pupil, image) = plt.subplots(1, 2, figsize=(10.4, 5.2))
    fig.subplots_adjust(left=.075, right=.98, bottom=.26, top=.80, wspace=.35)
    fig.suptitle("Primary coma: one pupil ring becomes one displaced circle", y=.98)
    fig.text(.5, .87, r"$w=h\,u(u^2+v^2)$,  $h=1$;   $(X,Y)=(3u^2+v^2,\,2uv)$",
             ha="center")
    theta = np.linspace(0, 2*np.pi, 721)
    radii = [.25, .5, .75, 1.0]
    colors = ["#007f86", "#d98a00", "#7c51a1", "#2458a4"]
    for rho, color in zip(radii, colors):
        u, v = rho*np.cos(theta), rho*np.sin(theta)
        x, y = ray_map(u, v)
        pupil.plot(u, v, color=color, lw=1.7, label=fr"$\rho={rho:g}$")
        image.plot(x, y, color=color, lw=1.7)
        image.plot(2*rho*rho, 0, "+", color=color, ms=7)
    u, v = np.sqrt(.5), np.sqrt(.5)
    x, y = ray_map(u, v)
    pupil.plot([u, -u], [v, -v], "o", color="#222222", ms=6)
    pupil.text(u+.05, v, "A", fontsize=11)
    pupil.text(-u-.18, -v, "B", fontsize=11)
    image.plot(x, y, "o", color="#222222", ms=6)
    image.annotate("A and B land together", (x, y), xytext=(1.15, 1.26),
                   arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    fig.text(.485, .56, "gradient\nmapping →", ha="center", fontsize=10)
    image.plot(0, 0, "o", color="#222222", ms=4)
    image.annotate("central ray", (0, 0), xytext=(.12, -.55), fontsize=10,
                   arrowprops={"arrowstyle": "->", "color": "#555555"})
    pupil.set(xlim=(-1.15, 1.15), ylim=(-1.15, 1.15), xlabel="u = pupil x / radius",
              ylabel="v = pupil y / radius", title="Circular pupil")
    image.set(xlim=(-.12, 3.18), ylim=(-1.25, 1.45), xlabel="X: normalized image error",
              ylabel="Y: normalized image error", title="Ray intersections in the image plane")
    handles, labels = pupil.get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=4,
               bbox_to_anchor=(.5, .10), frameon=False)
    for ax in (pupil, image):
        ax.set_aspect("equal")
        ax.axhline(0, color="#dddddd", lw=.8, zorder=0)
        ax.axvline(0, color="#dddddd", lw=.8, zorder=0)
    fig.text(.5, .025, "Ring radius and centre shift grow as pupil radius squared.\n"
             "Normalized geometrical model; no instrument dimensions or diffraction.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
