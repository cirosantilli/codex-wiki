"""Write albedo-planet-energy-balance.png in CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
An illustrative atmosphere-free planet has uniform temperature, prescribed
solar-band reflection, and thermal emissivity one; this is not an Earth forecast.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    solar, sigma = 1360.0, 5.670374419e-8
    albedos = np.array([0.3, 0.6])
    incoming = solar / 4
    reflected = incoming * albedos
    absorbed = incoming * (1 - albedos)
    temperatures = (absorbed / sigma) ** 0.25
    assert np.allclose(reflected + absorbed, incoming)
    assert np.allclose(temperatures, [254.531364159, 221.300193129], atol=1e-8)

    fig = plt.figure(figsize=(11.2, 5.2), dpi=100)
    grid = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.0, 1.5],
                           left=0.03, right=0.98, bottom=0.27,
                           top=0.77, wspace=0.25)
    sun_color, thermal_color = "#d58a00", "#a32638"
    disk = fig.add_subplot(grid[0, 0])
    disk.add_patch(Circle((0, 0), 1, facecolor="#fff1c7",
                          edgecolor=sun_color, lw=2, hatch="///"))
    for y in [-0.65, 0, 0.65]:
        end = -np.sqrt(1 - y*y)
        disk.annotate("", xy=(end - 0.04, y), xytext=(-2.4, y),
                      arrowprops={"arrowstyle": "->", "color": sun_color, "lw": 2})
    disk.plot([0, 0.70], [0, 0.70], color="0.3", lw=1.4)
    disk.text(0.20, 0.55, "R", color="0.25")
    disk.text(-1.65, 1.10, "sunlight S", ha="center", color=sun_color)
    disk.text(0, -1.35, r"Intercepting area: $\pi R^2$", ha="center")
    disk.set_title("Seen from the Sun", pad=20, fontsize=13)
    disk.set(xlim=(-2.6, 1.55), ylim=(-1.65, 1.45), aspect="equal")
    disk.axis("off")

    sphere = fig.add_subplot(grid[0, 1])
    sphere.add_patch(Circle((0, 0), 1, facecolor="#edf3f8",
                            edgecolor="#346a94", lw=2))
    for width in [0.55, 1.45]:
        sphere.add_patch(Ellipse((0, 0), width, 2, fill=False,
                                 edgecolor="#8ba9bf", lw=1))
    sphere.add_patch(Ellipse((0, 0), 2, 0.5, fill=False,
                             edgecolor="#8ba9bf", lw=1))
    for theta in np.linspace(0, 2*np.pi, 8, endpoint=False):
        v = np.array([np.cos(theta), np.sin(theta)])
        sphere.annotate("", xy=1.50*v, xytext=1.04*v,
                        arrowprops={"arrowstyle": "->", "color": thermal_color, "lw": 1.6})
    sphere.text(0, 0.17, "uniform T", ha="center", color="#254a66")
    sphere.text(0, -0.20, r"$\sigma T^4$ per area", ha="center", color=thermal_color)
    sphere.text(0, -1.85, r"Emitting area: $4\pi R^2$", ha="center")
    sphere.set_title("Whole emitting sphere", pad=20, fontsize=13)
    sphere.set(xlim=(-1.85, 1.85), ylim=(-2.10, 1.60), aspect="equal")
    sphere.axis("off")

    ax = fig.add_subplot(grid[0, 2])
    yy = np.array([1.0, 0.0])
    ax.barh(yy, reflected, color="#f4c767", label="reflected", height=0.52)
    ax.barh(yy, absorbed, left=reflected, color="#3a7ba4", label="absorbed", height=0.52)
    for y, a, r, q, t in zip(yy, albedos, reflected, absorbed, temperatures):
        ax.text(r/2, y, f"{r:.0f}", ha="center", va="center", color="#332511")
        ax.text(r+q/2, y, f"{q:.0f}", ha="center", va="center", color="white")
        ax.text(340, y-0.36, f"equilibrium T = {t:.3f} K", ha="right", fontsize=11)
    ax.set(yticks=yy, yticklabels=[r"$\alpha=0.30$", r"$\alpha=0.60$"],
           xlim=(0, 355), ylim=(-0.65, 1.50), xticks=[0, 102, 204, 340],
           xlabel=r"Global average power per area (W m$^{-2}$)")
    ax.set_title("Same illumination, different albedo", pad=20, fontsize=13)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.legend(loc="lower center", bbox_to_anchor=(0.52, -0.44),
              ncol=2, frameon=False, fontsize=11)
    fig.suptitle("Albedo controls absorbed sunlight; geometry supplies the factor four",
                 y=0.96, fontsize=15)
    fig.text(0.31, 0.18,
             r"$S\pi R^2\, /\,(4\pi R^2)=S/4=340\ \mathrm{W\,m^{-2}}$",
             ha="center", fontsize=14)
    fig.text(0.5, 0.035,
             "Illustrative model: S = 1360 W m⁻² • no atmosphere • uniform T • thermal emissivity = 1",
             ha="center", fontsize=11, color="0.3")
    fig.savefig("albedo-planet-energy-balance.png", facecolor="white", transparent=False)
    plt.close(fig)
    print("Fixed albedos:", list(zip(albedos.tolist(), temperatures.tolist())))


if __name__ == "__main__":
    main()
