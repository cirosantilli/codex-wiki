"""Original scalar Fourier-optics toy; output opaque PNG to CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Ideal coherent monochromatic on-axis point source; circular unobstructed
pupil, no aberrations, scatter, atmosphere, bandwidth, or detector noise.
Coordinates x are in pupil diameters; u = theta*D/lambda. Centered unitary
DFTs propagate field amplitudes, never intensities. The finite periodic
grid has 1024 samples, 128 across D, and 0.125 lambda/D image sampling.
An unlimited relay (L=1) is contrasted with L=P and a 0.8D Lyot stop.
All image curves share the unmasked full-pupil peak normalization.
"""
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.patches import Circle
import numpy as np


def forward(field):
    return np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(field), norm="ortho"))


def inverse(field):
    return np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(field), norm="ortho"))


def calculate(n=1024, diameter_samples=128):
    x = (np.arange(n) - n // 2) / diameter_samples
    xx, yy = np.meshgrid(x, x)
    pupil_radius = np.hypot(xx, yy)
    pupil = (pupil_radius <= .5).astype(float)
    u = np.fft.fftshift(np.fft.fftfreq(n, 1 / diameter_samples))
    ux, uy = np.meshgrid(u, u)
    image_radius = np.hypot(ux, uy)
    mask = (image_radius > 3).astype(float)
    stop = (pupil_radius <= .4).astype(float)
    direct = forward(pupil)
    masked = direct * mask
    lyot_field = inverse(masked)
    fields = [direct, masked, forward(lyot_field * pupil), forward(lyot_field * stop)]
    intensities = [np.abs(field) ** 2 for field in fields]
    peak = intensities[0][n // 2, n // 2]
    annulus = (image_radius >= 4) & (image_radius <= 10)
    metrics = {
        "n": n, "diameter_samples": diameter_samples,
        "mask_radius_lambda_over_D": 3, "stop_diameter_over_D": .8,
        "image_sampling_lambda_over_D": diameter_samples / n,
        "power_fraction": [float(v.sum() / pupil.sum()) for v in intensities],
        "annular_mean_4_to_10_over_direct_peak": [float(v[annulus].mean() / peak) for v in intensities],
        "rim_fraction_of_full_pupil_residual_power": float((np.abs(lyot_field) ** 2)[(pupil > 0) & (stop == 0)].sum()
            / (np.abs(lyot_field) ** 2)[pupil > 0].sum()),
        "far_off_axis_geometric_throughput": float(stop.sum() / pupil.sum()),
    }
    return x, image_radius, lyot_field, intensities, peak, metrics


def main():
    x, radius, field, intensities, peak, metrics = calculate()
    print(json.dumps(metrics, indent=2))
    plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(10.5, 4.65), gridspec_kw={"width_ratios": [1, 1.35]}, facecolor="white")
    selected = np.flatnonzero(np.abs(x) <= .65)
    cropped = (np.abs(field) ** 2)[np.ix_(selected, selected)]
    step = x[1] - x[0]
    bounds = [x[selected[0]] - step / 2, x[selected[-1]] + step / 2] * 2
    picture = ax0.imshow(cropped, origin="lower", extent=bounds, cmap="YlOrBr", norm=LogNorm(vmin=1e-5, vmax=.5))
    ax0.add_patch(Circle((0, 0), .5, fill=False, edgecolor="#252525", lw=1.2, ls="--"))
    ax0.add_patch(Circle((0, 0), .4, fill=False, edgecolor="#1466a1", lw=2))
    ax0.set(title="Pupil field after focal mask, before stop", xlabel="x / D", ylabel="y / D")
    ax0.text(.03, .03, "Dashed: original pupil\nBlue: Lyot opening", transform=ax0.transAxes,
             fontsize=9, bbox={"facecolor": "white", "edgecolor": "none", "alpha": .92})
    cb = fig.colorbar(picture, ax=ax0, fraction=.045, pad=.035)
    cb.set_label(r"$|E|^2$ / incident pupil intensity", fontsize=9)
    edges = np.arange(0, 12.2501, .25)
    bins = np.digitize(radius.ravel(), edges) - 1
    valid = (bins >= 0) & (bins < len(edges) - 1)
    counts = np.bincount(bins[valid], minlength=len(edges) - 1)
    labels = ["Direct image", "Focal mask only (unlimited relay)", "Mask + full pupil (D)", "Mask + Lyot stop (0.8D)"]
    colors = ["#333333", "#d18419", "#9370ad", "#1466a1"]
    for intensity, label, color, style in zip(intensities, labels, colors, ["-", "--", "-", "-"]):
        sums = np.bincount(bins[valid], weights=intensity.ravel()[valid] / peak, minlength=len(counts))
        means = sums / counts
        ax1.semilogy((edges[:-1] + edges[1:]) / 2, np.maximum(means, 1e-12), label=label, color=color, ls=style, lw=1.7)
    ax1.axvspan(0, 3, color="#eeeeee", zorder=-2)
    ax1.axvline(3, color="#777777", lw=.8)
    ax1.text(1.5, 2e-8, "Mask radius", ha="center", color="#555555", fontsize=9)
    ax1.set(xlim=(0, 12), ylim=(1e-8, 1.2), xlabel=r"Angular radius $\theta D / \lambda$", ylabel="Annular mean / direct-image peak",
            title="Same input star, same intensity normalization")
    ax1.grid(alpha=.18, which="major")
    ax1.legend(loc="upper right", fontsize=8.5, framealpha=1)
    fig.suptitle("Computed toy: blocking the core leaves rings; clipping the pupil rim helps", fontsize=13, y=.97)
    fig.text(.5, .035, "Ideal circular pupil • monochromatic point source • mask radius 3λ/D • not measured data", ha="center", fontsize=10)
    fig.subplots_adjust(left=.07, right=.98, bottom=.20, top=.80, wspace=.36)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=115, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
