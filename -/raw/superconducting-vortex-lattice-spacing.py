"""Original triangular vortex geometry, with a stipulated core amplitude profile."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

PLANCK = 6.62607015e-34
ELEMENTARY_CHARGE = 1.602176634e-19
FLUX_QUANTUM = PLANCK / (2 * ELEMENTARY_CHARGE)
XI_NM = 10.0
LAMBDA_NM = 100.0
BC2 = FLUX_QUANTUM / (2 * np.pi * (XI_NM * 1e-9) ** 2)


def spacing_nm(field):
    return 1e9 * np.sqrt(2 * FLUX_QUANTUM / (np.sqrt(3) * field))


def nearest_core_profile(field, extent=120.0):
    pitch = spacing_nm(field)
    grid = np.linspace(-extent, extent, 401)
    xx, yy = np.meshgrid(grid, grid)
    distance2 = np.full_like(xx, np.inf)
    bound = int(np.ceil(2 * extent / pitch)) + 3
    for row in range(-bound, bound + 1):
        for col in range(-bound, bound + 1):
            cx = pitch * (col + row / 2)
            cy = pitch * np.sqrt(3) * row / 2
            if abs(cx) > extent + pitch or abs(cy) > extent + pitch:
                continue
            distance2 = np.minimum(distance2, (xx - cx) ** 2 + (yy - cy) ** 2)
    return np.tanh(np.sqrt(distance2) / (np.sqrt(2) * XI_NM))


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axs = plt.subplots(1, 3, figsize=(13.8, 4.65), layout="constrained")
    for ax, field in zip(axs[:2], [0.2, 1.0]):
        a = spacing_nm(field)
        image = ax.imshow(nearest_core_profile(field), origin="lower", extent=(-120, 120, -120, 120),
                          vmin=0, vmax=1, cmap="YlGnBu_r", interpolation="nearest")
        origin = np.array([-a / 2, -np.sqrt(3) * a / 2])
        v1 = np.array([a, 0])
        v2 = np.array([a / 2, np.sqrt(3) * a / 2])
        ax.add_patch(Polygon([origin, origin + v1, origin + v1 + v2, origin + v2],
                             closed=True, fill=False, edgecolor="black", linestyle="--", linewidth=1.2))
        ax.set(title=fr"$\overline{{B}}={field:.2f}\,\mathrm{{T}}$: $a={a:.1f}\,\mathrm{{nm}}$",
               xlabel="x (nm)", ylabel="y (nm)")
        ax.set_aspect("equal")
    fig.colorbar(image, ax=list(axs[:2]), shrink=0.65, pad=0.015,
                 label=r"Stipulated $|\psi|/|\psi_0|$")
    field = np.linspace(0.08, BC2, 500)
    axs[2].plot(field, spacing_nm(field), color="#285c9e", linewidth=2.4)
    for b in [0.2, 1.0]:
        a = spacing_nm(b)
        axs[2].plot(b, a, "o", color="#a32d32")
        axs[2].annotate(f"{a:.1f} nm", (b, a), xytext=(12, 8), textcoords="offset points")
    axs[2].axvline(BC2, color="black", linestyle="--", linewidth=1.1)
    axs[2].axvspan(BC2, 3.6, color="#eeeeee")
    axs[2].text(BC2 - 0.06, 83, fr"$B_{{c2}}={BC2:.2f}$ T", rotation=90, ha="right", va="center")
    axs[2].set(title=r"One $\Phi_0$ per triangular cell", xlabel=r"Mean internal $\overline{B}$ (T)",
               ylabel="Nearest-neighbor spacing a (nm)", xlim=(0, 3.6), ylim=(0, 205))
    axs[2].grid(alpha=0.22)
    fig.suptitle("Chosen superconducting vortex arrays — geometry and core-profile illustration", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
