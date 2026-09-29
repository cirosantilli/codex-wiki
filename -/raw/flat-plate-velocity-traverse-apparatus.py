"""Generate flat-plate-velocity-traverse-apparatus.png in the working directory.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
This is an illustrative pressure-averaging model, not measured laboratory data.
The assumed 0.50 mm sensing footprint is not a reported probe bore diameter.
"""
from pathlib import Path
import importlib.util
import json
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

sys.dont_write_bytecode = True

spec = importlib.util.spec_from_file_location(
    "laminar_profile", Path(__file__).with_name("flat-plate-laminar-velocity-profiles.py"))
profile = importlib.util.module_from_spec(spec)
spec.loader.exec_module(profile)


def sample_model(eta, states, centres, footprint, U, nu, x, rho):
    y = eta * np.sqrt(nu * x / U)
    offsets = np.linspace(-footprint / 2, footprint / 2, 301)
    locations = centres[:, None] + offsets[None, :]
    assert np.min(locations) >= 0
    speeds = U * np.interp(locations, y, states[:, 1])
    q_samples = np.trapezoid(0.5 * rho * speeds**2, offsets, axis=1) / footprint
    mean_speed = np.trapezoid(speeds, offsets, axis=1) / footprint
    inferred = np.sqrt(2 * q_samples / rho)
    return q_samples, inferred, mean_speed


def main():
    eta, states = profile.blasius_profile()
    U, nu, x, rho, footprint = 10.0, 1.5e-5, 0.3048, 1.2, 0.00050
    centres = np.array([0.25, 0.45, 0.7, 1.0, 1.35, 1.7, 2.1, 2.6, 3.3, 4.2]) * 1e-3
    q, inferred, mean = sample_model(eta, states, centres, footprint, U, nu, x, rho)
    assert np.all(inferred >= mean - 1e-12)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (sketch, readout) = plt.subplots(1, 2, figsize=(10.6, 5.3),
                    gridspec_kw={"width_ratios": [1.55, 1]}, layout="constrained")
    fig.suptitle("Sampling a flat-plate velocity profile with pressure", fontsize=15)
    sketch.set(xlim=(0, 10), ylim=(-1.1, 7.5))
    sketch.axis("off")
    sketch.plot([0.1, 9.7], [0.3, 0.3], color="gray", lw=1)
    sketch.plot([0.1, 9.7], [6.8, 6.8], color="gray", lw=1)
    sketch.add_patch(Rectangle((1, 1.1), 6.0, 0.13, color="#424b55"))
    sketch.text(1.1, 0.7, "Stationary smooth plate", fontsize=11)
    positions = np.linspace(1, 7, 150)
    edge = 1.23 + 0.9 * np.sqrt((positions - 1) / 6)
    sketch.fill_between(positions, 1.23, edge, color="#e0edf4")
    sketch.plot(positions, edge, ls="--", color="#1f6f9b")
    sketch.text(1.2, 2.35, "Thin velocity deficit\n(normal scale exaggerated)", fontsize=10)
    for yy in [3.6, 4.6]:
        sketch.annotate("", (2, yy), (0.25, yy), arrowprops={"arrowstyle": "->", "lw": 2,
                                                                      "color": "#1f6f9b"})
    sketch.text(0.25, 5.1, "Incoming U", fontsize=11, color="#1f6f9b")
    # Upstream-facing two-port probe, carried by a normal traverse.
    sketch.plot([5.0, 6.5, 6.5], [1.78, 1.78, 5.4], lw=3, color="#313d48")
    sketch.scatter([5.0], [1.78], s=30, color="#b84145", zorder=4)
    sketch.scatter([5.55], [1.78], s=22, color="#437741", zorder=4)
    sketch.annotate("", (6.15, 4.6), (6.15, 2.5), arrowprops={"arrowstyle": "<->", "lw": 1.5})
    sketch.text(4.5, 6.15, "Micrometer traverse\nrecords inlet-centre y", fontsize=11)
    sketch.annotate("Upstream opening: p₀(y)", (5, 1.78), (3.8, 3.45), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": "#b84145"})
    sketch.text(6.75, 2.6, "Static port: p(y)", fontsize=10, color="#437741")
    sketch.plot([6.5, 7.45, 7.45], [5.3, 5.3, 4.1], color="#b84145", lw=1.5)
    sketch.plot([6.6, 8.75, 8.75], [4.8, 4.8, 4.1], color="#437741", lw=1.5)
    sketch.add_patch(Rectangle((7.15, 3.2), 2.2, 0.85, facecolor="white", edgecolor="#424b55"))
    sketch.text(8.25, 3.63, "Manometer\nq = p₀ − p", ha="center", va="center", fontsize=10)
    sketch.text(7.45, 5.5, "Pressure lines", fontsize=10)
    sketch.text(0.4, -0.25, "Model x = 0.3048 m  •  U = 10 m/s\nρ = 1.2 kg/m³  •  ν = 1.5 × 10⁻⁵ m²/s", fontsize=10, va="top")
    yy = eta * np.sqrt(nu * x / U) * 1000
    readout.plot(states[:, 1], yy, lw=2, color="#1f6f9b", label="Ideal point profile")
    readout.scatter(inferred / U, centres * 1000, s=45, edgecolor="#b84145", facecolor="white",
                    linewidth=1.5, label="Pressure-averaged model", zorder=4)
    readout.axhline(0, color="#424b55", lw=2)
    readout.set(xlim=(0, 1.1), ylim=(0, 4.8), xlabel=r"Inferred speed $\sqrt{2q/\rho}/U$",
                ylabel="Inlet-centre y (mm)")
    readout.spines[["top", "right"]].set_visible(False)
    readout.grid(alpha=0.17)
    readout.legend(loc="upper left", fontsize=9)
    readout.text(0.06, 3.5, "Synthetic readings only\nAssumed footprint: 0.50 mm\nProbe bore is unspecified", fontsize=9,
                 bbox={"facecolor": "white", "alpha": 0.9, "edgecolor": "none"})
    readout.text(0.45, 0.3, "Wall is unsampled", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"sample_count": len(centres), "min_centre_mm": float(centres.min() * 1000),
                      "footprint_mm": footprint * 1000, "pressure_range_pa": [float(q.min()), float(q.max())],
                      "max_rms_minus_mean_ms": float((inferred - mean).max())}, sort_keys=True))


if __name__ == "__main__":
    main()
