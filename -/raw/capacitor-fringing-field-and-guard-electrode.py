"""Bounded 2D Laplace field and a conceptual three-electrode guard layout.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
python3.14 ../capacitor-fringing-field-and-guard-electrode.py
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
No open-domain or three-dimensional capacitance is computed.
"""

from pathlib import Path
import json

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def solve_dirichlet(fixed, values, tolerance=2e-10, max_iterations=5000):
    """Solve the five-point Dirichlet system by matrix-free conjugate gradients.

    Return the potential and the maximum dimensionless stencil residual.
    Boundary nodes must be fixed. The system is positive definite on free nodes.
    """
    assert np.all(fixed[[0, -1], :]) and np.all(fixed[:, [0, -1]])
    free = ~fixed

    def stencil(u):
        out = 4 * u.copy()
        out[1:, :] -= u[:-1, :]
        out[:-1, :] -= u[1:, :]
        out[:, 1:] -= u[:, :-1]
        out[:, :-1] -= u[:, 1:]
        out[fixed] = 0
        return out

    prescribed = np.where(fixed, values, 0.0)
    rhs = -stencil(prescribed)
    u = np.zeros_like(values)
    residual = rhs.copy()
    direction = residual.copy()
    rr = np.sum(residual * residual)
    for iteration in range(max_iterations):
        if np.max(np.abs(residual[free])) < tolerance:
            break
        ad = stencil(direction)
        alpha = rr / np.sum(direction * ad)
        u += alpha * direction
        residual -= alpha * ad
        next_rr = np.sum(residual * residual)
        direction = residual + (next_rr / rr) * direction
        rr = next_rr
    else:
        raise RuntimeError("Dirichlet solver did not converge")
    potential = u + prescribed
    error = float(np.max(np.abs(stencil(potential)[free])))
    assert error < 2 * tolerance, error
    return potential, {"iterations": iteration, "stencil_residual": error}


def capacitor_model(gap=0.25, resolution=160, box=(2.0, 1.5)):
    """W=1, V=1; plates y=+-gap/2, |x|<=1/2; outer potential=0."""
    bx, by = box
    h = 1 / resolution
    x = np.linspace(-bx, bx, round(2 * bx * resolution) + 1)
    y = np.linspace(-by, by, round(2 * by * resolution) + 1)
    assert np.isclose(x[1] - x[0], h) and np.isclose(y[1] - y[0], h)
    fixed = np.zeros((len(y), len(x)), dtype=bool)
    fixed[[0, -1], :] = True
    fixed[:, [0, -1]] = True
    values = np.zeros(fixed.shape)
    width = np.abs(x) <= 0.5 + h / 10
    for sign in (-1, 1):
        row = int(np.argmin(np.abs(y - sign * gap / 2)))
        assert np.isclose(y[row], sign * gap / 2)
        fixed[row, width] = True
        values[row, width] = sign / 2
    phi, checks = solve_dirichlet(fixed, values)
    gy, gx = np.gradient(phi, h, h, edge_order=2)
    ex, ey = -gx, -gy
    center = len(y) // 2
    checks.update({"gap": gap, "width": 1, "h": h, "shape": list(phi.shape),
                   "outer_box": [-bx, bx, -by, by], "outer_potential": 0,
                   "center_normalized_field": float(-gap * ey[center, len(x)//2]),
                   "even_x_error": float(np.max(np.abs(phi - phi[:, ::-1]))),
                   "odd_y_error": float(np.max(np.abs(phi + phi[::-1, :]))),
                   "potential_min": float(phi.min()), "potential_max": float(phi.max())})
    return x, y, phi, ex, ey, fixed, checks


def draw_field(ax, x, y, phi, ex, ey, fixed, gap, view=(-1.1, 1.1, -0.75, 0.75)):
    ax.contour(x, y, phi, levels=np.linspace(-0.45, 0.45, 13),
               colors="#999999", linewidths=0.7)
    # The conductor nodes are excluded from stream interpolation.
    ax.streamplot(x, y, np.ma.array(ex, mask=fixed), np.ma.array(ey, mask=fixed),
                  density=1.4, color="#2166ac", linewidth=0.95, arrowsize=1.0)
    # Explicit midplane arrows remain readable even for gaps too short for
    # Matplotlib's automatic streamline seeding. Their direction is computed.
    tips = np.linspace(-0.43, 0.43, 9)
    row = len(y) // 2
    ux = np.interp(tips, x, ex[row])
    uy = np.interp(tips, x, ey[row])
    norm = np.hypot(ux, uy)
    ax.quiver(tips, np.zeros_like(tips), ux/norm*gap*0.6, uy/norm*gap*0.6,
              angles="xy", scale_units="xy", scale=1, pivot="mid", width=0.003,
              color="#2166ac", headwidth=3.5)
    ax.plot([-0.5, 0.5], [gap/2]*2, color="#b2182b", lw=4)
    ax.plot([-0.5, 0.5], [-gap/2]*2, color="#2166ac", lw=4)
    ax.set(xlim=view[:2], ylim=view[2:], xlabel="x / W", ylabel="y / W", aspect="equal")


def main():
    x, y, phi, ex, ey, fixed, checks = capacitor_model()
    fig, (field, guard) = plt.subplots(1, 2, figsize=(10.5, 4.5),
                                       gridspec_kw={"width_ratios": [1.2, 1]}, layout="constrained")
    fig.patch.set_facecolor("white")
    draw_field(field, x, y, phi, ex, ey, fixed, gap=0.25)
    field.set_title("Computed finite-plate field: d / W = 0.25", fontsize=11)
    field.text(0, 0.19, "+V / 2", color="#b2182b", ha="center", fontsize=10,
               bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    field.text(0, -0.23, "−V / 2", color="#2166ac", ha="center", fontsize=10,
               bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    field.legend(handles=[Line2D([], [], color="#2166ac", label="E direction"),
                          Line2D([], [], color="#999999", label="Equipotentials")],
                 loc="lower right", fontsize=8)
    guard.set_title("Separate sensing electrode and guard", fontsize=11)
    guard.plot([-1, 1], [0.4, 0.4], lw=6, color="#b2182b")
    guard.plot([-0.4, 0.4], [-0.25, -0.25], lw=6, color="#2166ac")
    for a, b in [(-1, -0.45), (0.45, 1)]:
        guard.plot([a, b], [-0.25]*2, lw=6, color="#35978f")
    for xx in np.linspace(-0.32, 0.32, 5):
        guard.annotate("", (xx, -0.21), (xx, 0.37),
                       arrowprops={"arrowstyle": "->", "color": "#2166ac", "lw": 1.2})
    for sign in (-1, 1):
        guard.annotate("", (sign*0.89, -0.21), (sign*0.86, 0.38),
                       arrowprops={"arrowstyle": "->", "color": "#35978f",
                                   "connectionstyle": f"arc3,rad={sign*0.7}"})
    guard.text(0, 0.52, "Excitation electrode", ha="center", fontsize=10)
    guard.text(0, -0.40, "Sensing electrode", ha="center", color="#2166ac", fontsize=10)
    guard.text(0, -0.56, "Sense and guard held at the same potential", ha="center", fontsize=9)
    guard.annotate("Insulating slot", (-0.425, -0.25), (-0.95, 0.05), fontsize=9,
                   arrowprops={"arrowstyle": "->", "lw": 0.8})
    guard.annotate("Guard current\nbypasses readout", (0.72, -0.25), (0.62, -0.75),
                   ha="center", fontsize=9, color="#35978f",
                   arrowprops={"arrowstyle": "->", "color": "#35978f"})
    guard.set(xlim=(-1.2, 1.2), ylim=(-0.95, 0.8), aspect="equal")
    guard.axis("off")
    fig.suptitle("Fringing bends the field; a guard moves the measured edge outward", fontsize=13)
    fig.supxlabel("Left: bounded 2D Laplace model, W = V = 1, h = W/160; outer box ±2W × ±1.5W at φ = 0.\nRight: conceptual cross-section through a guard ring; arrows are schematic, not a computed guarded field.", fontsize=9)
    output = Path(Path(__file__).stem + ".png")
    fig.savefig(output, dpi=130, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"output": str(output), "model": checks}))


if __name__ == "__main__":
    main()
