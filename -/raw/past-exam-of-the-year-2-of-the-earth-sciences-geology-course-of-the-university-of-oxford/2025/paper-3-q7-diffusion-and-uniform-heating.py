"""Original periodic heat-equation calculation; write the PNG to the CWD."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def heat_profiles(n=128, time=10.0, diffusivity=0.01):
    length = 10.0
    x = np.arange(n) * length / n
    xx, yy = np.meshgrid(x, x)
    initial = np.exp(-((xx - 5) ** 2 + (yy - 5) ** 2) / 0.1)
    k = 2 * np.pi * np.fft.fftfreq(n, d=length / n)
    kx, ky = np.meshgrid(k, k)
    final = np.fft.ifft2(np.fft.fft2(initial) * np.exp(-diffusivity * time * (kx**2 + ky**2))).real
    forced = final + 1 - np.exp(-time / 10)
    return x, initial, final, forced


def main():
    x, initial, final, forced = heat_profiles()
    plt.rcParams.update({"font.size": 11})
    fig, axes = plt.subplots(1, 3, figsize=(12.5, 4.8), layout="constrained", gridspec_kw={"width_ratios": [1, 1, 1.35]})
    fig.patch.set_facecolor("white")
    for axis, field, title in zip(axes[:2], [initial, final], ["Initial hot spot: peak 1.00", "After 10 s: peak 0.20"]):
        picture = axis.pcolormesh(x, x, field, shading="nearest", cmap="magma", vmin=0, vmax=1, rasterized=True)
        axis.set(xlim=(3, 7), ylim=(3, 7), xlabel="x (cm)", ylabel="y (cm)", title=title, xticks=[3, 5, 7], yticks=[3, 5, 7])
        axis.set_aspect("equal")
    fig.colorbar(picture, ax=list(axes[:2]), shrink=0.72, label="Temperature (initial peak = 1)")
    centre = len(x) // 2
    axis = axes[2]
    axis.plot(x, initial[centre], "--", color="0.35", label="Initial")
    axis.plot(x, final[centre], color="#116da9", lw=2, label="Diffusion only")
    axis.plot(x, forced[centre], color="#b44b19", lw=2, label="With source")
    axis.axhline(1 - np.exp(-1), color="#b44b19", ls=":", alpha=0.8)
    axis.set(xlim=(3, 7), ylim=(0, 1.07), xlabel="x (cm), through y = 5 cm", ylabel="Temperature", title="A uniform source adds an offset")
    axis.grid(alpha=0.18)
    axis.legend(fontsize=9, loc="upper right")
    fig.suptitle("Periodic diffusion of a Gaussian hot spot; integrated uniform source at 10 s = 0.6321", fontsize=14)
    fig.savefig(Path.cwd() / "paper-3-q7-diffusion-and-uniform-heating.png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
