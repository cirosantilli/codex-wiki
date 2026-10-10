"""Compare gap/width ratios in the same explicitly bounded 2D Laplace model.

Run from _media with MPLBACKEND=Agg and MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Imports the neighbouring field generator; all curves are model predictions.
"""

import importlib.util
import json
from pathlib import Path

import matplotlib.pyplot as plt


def load_model():
    path = Path(__file__).with_name("capacitor-fringing-field-and-guard-electrode.py")
    spec = importlib.util.spec_from_file_location("capacitor_fringe_model", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    model = load_model()
    fig = plt.figure(figsize=(10.5, 6.2), layout="constrained", facecolor="white")
    grid = fig.add_gridspec(2, 3, height_ratios=[1, 1.1])
    profile = fig.add_subplot(grid[1, :])
    checks = []
    for i, (gap, color) in enumerate([(0.10, "#1b9e77"), (0.25, "#d95f02"), (0.50, "#7570b3")]):
        x, y, phi, ex, ey, fixed, check = model.capacitor_model(gap=gap)
        checks.append(check)
        ax = fig.add_subplot(grid[0, i])
        model.draw_field(ax, x, y, phi, ex, ey, fixed, gap,
                         view=(-0.85, 0.85, -0.55, 0.55))
        ax.set_title(f"d / W = {gap:.2f}", fontsize=11)
        profile.plot(x, -gap * ey[len(y)//2], lw=2, color=color, label=f"d / W = {gap:.2f}")
    profile.axhline(1, color="#555555", ls="--", lw=1, label="Infinite-plate gap field")
    profile.axvspan(-0.5, 0.5, color="#aaaaaa", alpha=0.10)
    for edge in (-0.5, 0.5):
        profile.axvline(edge, color="#777777", ls=":", lw=1)
    profile.text(0, 0.18, "Plate footprint", ha="center", color="#666666", fontsize=10)
    profile.set(xlim=(-1.0, 1.0), ylim=(0, 1.12), xlabel="x / W along the midplane y = 0",
                ylabel="Downward field  −Ey d / V")
    profile.legend(loc="upper right", fontsize=9)
    profile.grid(alpha=0.18)
    fig.suptitle("A smaller gap leaves a wider nearly uniform central region", fontsize=14)
    fig.supxlabel("Original bounded 2D predictions, not measurements or 3D capacitances.\nAll panels: W = V = 1; h = W/160; φ = 0 on x = ±2W and y = ±1.5W; zero-thickness ideal plates.", fontsize=9)
    output = Path(Path(__file__).stem + ".png")
    fig.savefig(output, dpi=130, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"output": str(output), "models": checks}))


if __name__ == "__main__":
    main()
