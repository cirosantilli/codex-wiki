"""Compare local estimates, exact-local defects and accumulated errors.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Imports the matching trajectory generator without creating bytecode files.
"""

from pathlib import Path
import importlib.util
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.dont_write_bytecode = True
model_path = Path(__file__).with_name("adaptive-euler-decay-trajectory-and-steps.py")
spec = importlib.util.spec_from_file_location("adaptive_euler_decay", model_path)
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)


def main():
    _, _, trials = model.integrate()
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), constrained_layout=True)
    estimates = np.array([abs(r["estimate"]) for r in trials])
    local = np.array([abs(r["local"]) for r in trials])
    for accepted, marker, color, label in [(True, "o", "#0072B2", "Accepted"),
                                            (False, "x", "#D55E00", "Rejected")]:
        mask = np.array([r["accepted"] == accepted for r in trials])
        axes[0].loglog(estimates[mask], local[mask], marker, ms=5, color=color, label=label)
    bounds = [min(estimates.min(), local.min()) * 0.65,
              max(estimates.max(), local.max()) * 1.5]
    axes[0].loglog(bounds, bounds, "--", color="#555555", lw=1, label="Exact agreement")
    axes[0].set(xlabel="Estimated fine-step error |fine − coarse|",
                ylabel="Actual local error |y exp(−h) − fine|",
                title="Same numerical starting value", xlim=bounds, ylim=bounds)
    axes[0].legend(fontsize=9)
    for i, r in enumerate(trials):
        if not r["accepted"]:
            axes[1].semilogy(i + 1, r["scaled"], "x", color="#D55E00", ms=8, mew=2)
    indices = np.array([i + 1 for i, r in enumerate(trials) if r["accepted"]])
    good = [r for r in trials if r["accepted"]]
    axes[1].semilogy(indices, [r["scaled"] for r in good], ".-", color="#0072B2",
                     ms=3, label="Accepted local estimate / s")
    axes[1].semilogy(indices, [abs(r["local"]) / r["scale"] for r in good],
                     "--", color="#009E73", label="Accepted actual local error / s")
    axes[1].semilogy(indices, [abs(r["global_error"]) / r["scale"] for r in good],
                     color="#CC79A7", label="Actual global error / same s")
    axes[1].semilogy([], [], "x", color="#D55E00", ms=8, label="Rejected local estimate / s")
    axes[1].axhline(1, ls=":", color="#222222", label="Local acceptance threshold")
    axes[1].set(xlabel="Trial number (including rejections)", ylabel="Scaled absolute error",
                title="Local acceptance does not bound global error")
    axes[1].legend(fontsize=8.5, loc="lower left")
    for ax in axes:
        ax.grid(alpha=0.22)
    fig.suptitle("Two-half-step Euler decay: atol = 10⁻⁵, rtol = 10⁻³; no extrapolation", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
