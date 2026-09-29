"""Draw electromagnetic-plane-wave.png in cwd using NumPy and Matplotlib.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp.
The 3D plotting coordinates are (physical z, physical x, physical y),
a cyclic permutation that preserves the right-handed orientation.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    c = 299_792_458.0
    epsilon0 = 8.8541878e-12
    electric_peak = 100.0
    magnetic_peak = electric_peak / c
    flux_peak = epsilon0 * c * electric_peak**2
    position = np.linspace(0.0, 2.0, 801)
    profile = np.cos(2 * np.pi * position)
    blue, orange, green = "#1766a6", "#bd580b", "#217144"

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig = plt.figure(figsize=(11.5, 8.0), facecolor="white")
    fig.suptitle("A vacuum plane wave: transverse fields, forward energy flow", y=0.97, fontsize=16)
    fig.text(0.5, 0.919, r"$\mathbf{E}=E_0\cos(kz-\omega t)\,\hat{\mathbf{x}},\quad"
             r"\mathbf{B}=(E_0/c)\cos(kz-\omega t)\,\hat{\mathbf{y}},\quad\omega=ck$",
             ha="center", fontsize=13)

    spatial = fig.add_axes((0.02, 0.48, 0.61, 0.40), projection="3d", facecolor="white")
    spatial.plot(position, profile, np.zeros_like(profile), color=blue, lw=2.5)
    spatial.plot(position, np.zeros_like(profile), profile, color=orange, lw=2.5)
    sample = np.linspace(0.0, 2.0, 17)
    values = np.cos(2 * np.pi * sample)
    for z, value in zip(sample, values):
        spatial.plot([z, z], [0, value], [0, 0], color=blue, lw=0.7, alpha=0.7)
        spatial.plot([z, z], [0, 0], [0, value], color=orange, lw=0.7, alpha=0.7)
    spatial.quiver(0, 0, 0, 2.25, 0, 0, color=green, arrow_length_ratio=0.055, linewidth=2)
    spatial.set(xlim=(0, 2.3), ylim=(-1.1, 1.1), zlim=(-1.1, 1.1))
    spatial.set_xlabel(r"Position $z/\lambda$", labelpad=7)
    spatial.set_ylabel(r"$x$: $E_x/E_0$", labelpad=6, color=blue)
    spatial.set_zlabel(r"$y$: $cB_y/E_0$", labelpad=6, color=orange)
    spatial.set_xticks([0, 1, 2])
    spatial.set_yticks([-1, 0, 1])
    spatial.set_zticks([-1, 0, 1])
    spatial.view_init(elev=21, azim=-65)
    spatial.set_box_aspect((2.8, 1.3, 1.3))
    spatial.set_title(r"Snapshot at $t=0$: fields at positions along $z$", pad=2)
    for axis in (spatial.xaxis, spatial.yaxis, spatial.zaxis):
        axis.set_pane_color((1, 1, 1, 1))

    note = fig.add_axes((0.66, 0.50, 0.32, 0.35), facecolor="white")
    note.axis("off")
    note.text(0, 0.97, "Same phase; perpendicular directions", fontsize=12, weight="bold")
    note.text(0, 0.79, r"$\hat{\mathbf{x}}\times\hat{\mathbf{y}}=\hat{\mathbf{z}}$", fontsize=17, color=green)
    note.text(0, 0.63, "Both fields reverse together.\nEnergy still flows along +z.", linespacing=1.5)
    note.text(0, 0.39, r"$E_0=100\ \mathrm{V/m}$", color=blue, fontsize=13)
    note.text(0, 0.25, rf"$B_0={magnetic_peak * 1e9:.1f}\ \mathrm{{nT}}$", color=orange, fontsize=13)
    note.text(0, 0.10, "B is rescaled by c to compare amplitudes.", fontsize=10)

    fields = fig.add_axes((0.10, 0.30, 0.85, 0.155), facecolor="white")
    fields.plot(position, electric_peak * profile, color=blue, lw=3, label=r"$E_x$ (V/m)")
    fields.plot(position, c * magnetic_peak * profile, color=orange, lw=1.8, ls="--", label=r"$cB_y$ (V/m)")
    fields.set(xlim=(0, 2), ylim=(-118, 118), ylabel="Scaled fields (V/m)")
    fields.set_yticks([-100, 0, 100])
    fields.tick_params(labelbottom=False)
    fields.legend(loc="upper right", ncol=2, frameon=True, facecolor="white", framealpha=1)
    fields.axhline(0, color="#9ca5af", lw=0.8)
    fields.grid(alpha=0.18)

    flux = fig.add_axes((0.10, 0.095, 0.85, 0.155), facecolor="white")
    flux.plot(position, flux_peak * profile**2, color=green, lw=2.4, label=r"$S_z=\epsilon_0cE_0^2\cos^2(kz)$")
    flux.axhline(flux_peak / 2, color="#555555", ls="--", lw=1.5,
                 label=rf"Cycle average: {flux_peak / 2:.2f} W/m$^2$")
    flux.fill_between(position, 0, flux_peak * profile**2, color=green, alpha=0.10)
    flux.set(xlim=(0, 2), ylim=(0, flux_peak * 1.13), xlabel=r"Position $z/\lambda$ at $t=0$",
             ylabel=r"Flux $S_z$ (W/m$^2$)")
    flux.set_yticks([0, flux_peak / 2, flux_peak], labels=["0", "13.27", "26.54"])
    flux.legend(loc="upper center", ncol=2, frameon=True, facecolor="white", framealpha=1, fontsize=10)
    flux.grid(alpha=0.18)
    fig.text(0.5, 0.022, "Curves show local field values, not particle paths. Each snapshot translates along +z at speed c.",
             ha="center", fontsize=10)
    fig.savefig("electromagnetic-plane-wave.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
