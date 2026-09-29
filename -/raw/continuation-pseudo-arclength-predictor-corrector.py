"""Draw one pseudo-arclength step across a cubic solution curve's fold.

The tangent is normalized in the displayed Euclidean coordinates.
Run from the output directory; dependency versions are in pyproject.toml.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def continuation_step(x0=0.45, h=0.18):
    seed = np.array([x0, x0 - x0**3])
    tangent = np.array([1.0, 1.0 - 3 * x0**2])
    tangent /= np.linalg.norm(tangent)
    predictor = seed + h * tangent
    corrected = predictor.copy()
    for _ in range(12):
        x, lam = corrected
        residual = np.array([x**3 - x + lam, tangent @ (corrected - predictor)])
        if np.linalg.norm(residual, ord=np.inf) < 2e-14:
            break
        jacobian = np.array([[3 * x**2 - 1, 1.0], tangent])
        corrected += np.linalg.solve(jacobian, -residual)
    x, lam = corrected
    assert abs(x**3 - x + lam) < 2e-14
    assert abs(tangent @ (corrected - seed) - h) < 2e-14
    assert x0 < 1 / np.sqrt(3) < x
    return seed, tangent, predictor, corrected


def main():
    seed, tangent, predictor, corrected = continuation_step()
    print({"seed": seed.tolist(), "tangent": tangent.tolist(),
           "predictor": predictor.tolist(), "corrected": corrected.tolist()})
    normal = np.array([-tangent[1], tangent[0]])
    line = predictor + np.linspace(-0.11, 0.055, 100)[:, None] * normal
    x = np.linspace(0.32, 0.80, 400)
    fold = np.array([1 / np.sqrt(3), 2 / (3 * np.sqrt(3))])
    fig, ax = plt.subplots(figsize=(8.2, 5.0), dpi=120, layout="constrained")
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.plot(x, x - x**3, color="#176b8e", lw=2.5, label=r"Solution curve $F=0$")
    ax.plot(line[:, 0], line[:, 1], color="#7c3aed", ls="--", lw=1.5,
            label="Transverse line through predictor")
    ax.annotate("", xy=predictor, xytext=seed,
                arrowprops={"arrowstyle": "->", "color": "#64748b", "lw": 2})
    ax.annotate("", xy=corrected, xytext=predictor,
                arrowprops={"arrowstyle": "->", "color": "#7c3aed", "lw": 2})
    ax.scatter(*fold, color="#b45309", s=55, zorder=5)
    ax.scatter(*seed, color="#176b8e", s=45, zorder=5)
    ax.scatter(*predictor, color="#64748b", marker="s", s=45, zorder=5)
    ax.scatter(*corrected, color="#7c3aed", s=45, zorder=5)
    for point, text, offset in (
        (seed, r"Seed $z_k$", (-40, -27)),
        (predictor, r"Predictor $z_{\mathrm{p}}$", (-4, 16)),
        (corrected, r"Corrected $z_{k+1}$", (14, -23)),
        (fold, "Fold", (-34, 20)),
    ):
        ax.annotate(text, xy=point, xytext=offset, textcoords="offset points", fontsize=11)
    # A small right-angle marker shows the two perpendicular directions.
    size = 0.012
    corner = np.array([predictor - size * tangent,
                       predictor - size * tangent - size * normal,
                       predictor - size * normal])
    ax.plot(corner[:, 0], corner[:, 1], color="#475569", lw=1)
    ax.set_aspect("equal", adjustable="box")
    ax.set(xlabel=r"State $x$", ylabel=r"Parameter $\lambda$",
           xlim=(0.32, 0.80), ylim=(0.285, 0.49),
           title=r"Predict along the tangent; correct on a transverse line ($h=0.18$)")
    ax.legend(loc="upper left", fontsize=9, framealpha=1)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
