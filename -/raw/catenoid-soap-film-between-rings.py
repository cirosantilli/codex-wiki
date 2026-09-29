"""Generate an ideal catenoid and two profiles at L/R=0.60.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
Geometry is dimensionless and represents no measured film.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def bisect_root(left, right):
    def residual(u):
        return u / np.cosh(u) - 0.60

    for _ in range(80):
        midpoint = (left + right) / 2
        if residual(left) * residual(midpoint) <= 0:
            right = midpoint
        else:
            left = midpoint
    return (left + right) / 2


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    half_gap = 0.60
    wide_u, thin_u = bisect_root(0.01, 1.199), bisect_root(1.201, 6)
    wide_a, thin_a = half_gap / wide_u, half_gap / thin_u
    fig = plt.figure(figsize=(10.5, 5.3))
    surface = fig.add_subplot(121, projection="3d")
    z, phi = np.meshgrid(np.linspace(-half_gap, half_gap, 49), np.linspace(0, 2 * np.pi, 81))
    r = wide_a * np.cosh(z / wide_a)
    surface.plot_surface(r * np.cos(phi), r * np.sin(phi), z, color="#80c8d5", alpha=0.48, linewidth=0)
    angle = np.linspace(0, 2 * np.pi, 241)
    for height in [-half_gap, half_gap]:
        surface.plot(np.cos(angle), np.sin(angle), np.full_like(angle, height), color="#333333", lw=2.8)
    surface.plot(wide_a * np.cos(angle), wide_a * np.sin(angle), np.zeros_like(angle), color="#a35425", lw=2.2)
    surface.quiver(wide_a, 0, 0, 0.36, 0, 0, color="#a35425", arrow_length_ratio=0.22)
    surface.text(wide_a + 0.25, 0, 0.10, "$N$", color="#a35425")
    surface.set(xlabel="$x/R$", ylabel="$y/R$", zlabel="$z/R$", title="Wide-waist catenoid")
    surface.set_box_aspect((2, 2, 1.2))
    surface.set_zticks([-0.6, 0, 0.6])
    surface.view_init(elev=18, azim=-57)
    profile = fig.add_subplot(122)
    zz = np.linspace(-half_gap, half_gap, 301)
    for a, style, label, color in [(wide_a, "-", "Wide waist", "#227b94"), (thin_a, "--", "Thin waist", "#b65a27")]:
        profile.plot(zz, a * np.cosh(zz / a), style, color=color, lw=2.6, label=f"{label}: a/R={a:.3f}")
    profile.scatter([-half_gap, half_gap], [1, 1], c="#333333", s=55, zorder=5)
    profile.text(-0.57, 1.045, "Ring", ha="center")
    profile.text(0.57, 1.045, "Ring", ha="center")
    profile.axvline(0, lw=0.8, color="#aaaaaa")
    profile.set(xlabel="Axial position $z/R$", ylabel="Profile radius $r/R$", xlim=(-0.67, 0.67), ylim=(0, 1.13), title="Same boundary, two stationary profiles")
    profile.legend(loc="lower center", fontsize=11, frameon=False)
    profile.grid(alpha=0.2)
    profile.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"$r(z)=a\cosh(z/a)$    •    $L/R=0.60$    •    $H=0$ on both profiles", fontsize=15, y=0.98)
    fig.text(0.5, 0.035, "Ideal mid-surface geometry; equal rings of radius R at z = ±L", ha="center", fontsize=12)
    fig.subplots_adjust(left=0.02, right=0.97, top=0.84, bottom=0.18, wspace=0.28)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
