"""Draw two conformal geometries; output the same-basename PNG in cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 6.6), dpi=100, layout="constrained")
    ds, ads = axes
    eta = np.linspace(-np.pi / 2, np.pi / 2, 600)
    halfwidth = np.pi / 2 - np.abs(eta)
    ds.fill_betweenx(eta, -halfwidth, halfwidth, color="#e4eef8", label="Central static patch")
    for sign in (-1, 1):
        ds.plot(sign * (np.pi / 2 - eta), eta, color="#d55e00", linewidth=2, label="Future event horizon" if sign == 1 else None)
        ds.plot(sign * (np.pi / 2 + eta), eta, color="#999999", linestyle=":", linewidth=1.3)
        ds.axvline(sign * np.pi, color="#777777", linestyle="--", linewidth=1)
    ds.plot(np.zeros_like(eta), eta, color="#0072b2", linewidth=2)
    ds.axhline(np.pi / 2, color="black", linewidth=2)
    ds.axhline(-np.pi / 2, color="black", linewidth=2)
    ds.text(0, np.pi / 2 + 0.15, "Spacelike future infinity", ha="center", va="bottom")
    ds.text(0, -np.pi / 2 - 0.15, "Spacelike past infinity", ha="center", va="top")
    ds.text(0, 0.26, "Observer", color="#0072b2", ha="center", bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ds.set(xlim=(-np.pi - 0.13, np.pi + 0.13), ylim=(-np.pi / 2 - 0.45, np.pi / 2 + 0.45), xlabel=r"Spatial angle $\chi$ (dashed edges identified)", ylabel=r"Conformal time $\eta$")
    ds.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
    ds.set_yticks([-np.pi / 2, 0, np.pi / 2], [r"$-\pi/2$", "0", r"$\pi/2$"])
    ds.set_title("de Sitter: conformal cylinder")
    ds.legend(loc="lower center", bbox_to_anchor=(0.5, -0.39), fontsize=10, framealpha=1)
    ds.set_aspect("equal")

    tau = np.linspace(-np.pi, np.pi, 900)
    energy = 1.7
    amplitude = np.sqrt(energy**2 - 1)
    psi = np.arctan(amplitude * np.sin(tau))
    time = np.unwrap(np.arctan2(energy * np.sin(tau), np.cos(tau)))
    ads.plot(psi, time, color="#0072b2", linewidth=2, label="Timelike geodesic")
    ads.plot([0, np.pi / 2], [0, np.pi / 2], color="#d55e00", linewidth=2, label="Null geodesic")
    ads.plot([0, -np.pi / 2], [0, np.pi / 2], color="#d55e00", linewidth=2)
    for sign in (-1, 1):
        ads.axvline(sign * np.pi / 2, color="black", linewidth=2)
        ads.text(sign * (np.pi / 2 + 0.13), 0, "Timelike infinity", rotation=90, ha="center", va="center")
        ads.annotate("", xy=(0, sign * (np.pi + 0.32)), xytext=(0, sign * (np.pi - 0.1)), arrowprops={"arrowstyle": "->", "color": "#555555", "lw": 1.4})
    ads.text(0, np.pi / 2 + 0.13, "Finite coordinate time;\ninfinite affine parameter", ha="center", fontsize=10, bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ads.set(xlim=(-np.pi / 2 - 0.4, np.pi / 2 + 0.4), ylim=(-np.pi - 0.4, np.pi + 0.4), xlabel=r"Conformal radius $\psi$", ylabel=r"Global time $t$ (continues indefinitely)")
    ads.set_xticks([-np.pi / 2, 0, np.pi / 2], [r"$-\pi/2$", "0", r"$\pi/2$"])
    ads.set_yticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
    ads.set_title("Anti-de Sitter: universal-cover strip")
    ads.legend(loc="lower center", bbox_to_anchor=(0.5, -0.19), fontsize=10, framealpha=1)
    ads.set_aspect("equal")
    for axis in axes:
        axis.grid(alpha=0.15)
        for spine in axis.spines.values():
            spine.set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
