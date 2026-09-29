"""Original phase geometry; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes the opaque white PNG with this script's basename.
Arrows are (cos(theta), sin(theta)), NOT velocity or gradient arrows.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def phase(x, y):
    return np.arctan2(y, x + 1) - np.arctan2(y, x - 1)


def winding(cx, cy, radius):
    t = np.linspace(0, 2 * np.pi, 4097)
    values = np.exp(1j * phase(cx + radius * np.cos(t), cy + radius * np.sin(t)))
    return np.angle(values[1:] / values[:-1]).sum() / (2 * np.pi)


def main():
    charges = [winding(-1, 0, .42), winding(1, 0, .42), winding(0, 0, 2)]
    np.testing.assert_allclose(charges, [1, -1, 0], atol=1e-12)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (ax, ring) = plt.subplots(1, 2, figsize=(9.6, 4.7), width_ratios=[1.5, 1], layout="constrained")
    x, y = np.meshgrid(np.linspace(-2.6, 2.6, 24), np.linspace(-2, 2, 19))
    theta = phase(x, y)
    mask = ((x + 1) ** 2 + y ** 2 > .17 ** 2) & ((x - 1) ** 2 + y ** 2 > .17 ** 2)
    ax.quiver(x[mask], y[mask], np.cos(theta[mask]), np.sin(theta[mask]),
              color="#2c5873", pivot="mid", angles="xy", scale_units="xy", scale=6.5, width=.004)
    for cx, charge, color in [(-1, "+1", "#b23b36"), (1, "−1", "#276f99")]:
        ax.add_patch(Circle((cx, 0), .17, facecolor="white", edgecolor=color, lw=2))
        ax.text(cx, -.45, "$q=" + charge + "$", ha="center", color=color, bbox={"facecolor":"white", "edgecolor":"none", "pad":1})
        ax.add_patch(Circle((cx, 0), .66, fill=False, edgecolor=color, ls="--", lw=1.5))
    ax.add_patch(Circle((0, 0), 2.13, fill=False, edgecolor="#676767", ls=":", lw=1.7))
    ax.text(0, 2.25, "Loop around both cores: total winding 0", ha="center", fontsize=10)
    ax.set(xlim=(-2.8, 2.8), ylim=(-2.5, 2.65), aspect="equal", xlabel="$x$ (arbitrary length)", ylabel="$y$ (arbitrary length)", title="A neutral vortex–antivortex pair")
    t = np.linspace(0, 2 * np.pi, 400)
    ring.plot(np.cos(t), np.sin(t), color="#aaaaaa", lw=1.4)
    for i, color in [(1, "#b23b36"), (-1, "#276f99")]:
        ts = np.linspace(0, 2 * np.pi, 50)
        r = 1.04 if i == 1 else .77
        ring.plot(r * np.cos(i * ts), r * np.sin(i * ts), color=color, lw=2)
        k = 12
        ring.annotate("", xy=(r * np.cos(i * ts[k + 2]), r * np.sin(i * ts[k + 2])),
                      xytext=(r * np.cos(i * ts[k]), r * np.sin(i * ts[k])),
                      arrowprops={"arrowstyle":"->", "color":color, "lw":2})
    ring.text(0, .24, r"$q=+1$: phase gains $2\pi$", ha="center", color="#b23b36", fontsize=10)
    ring.text(0, -.18, r"$q=-1$: phase loses $2\pi$", ha="center", color="#276f99", fontsize=10)
    ring.text(0, -1.35, "Traverse a spatial loop counterclockwise;\nfollow its phase on the unit circle.", ha="center", fontsize=10)
    ring.set(xlim=(-1.5, 1.5), ylim=(-1.7, 1.6), aspect="equal", title=r"The phase is an angle modulo $2\pi$")
    ring.axis("off")
    fig.suptitle("Arrows show local phase orientation, not fluid velocity", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print({"loop_windings": charges})


if __name__ == "__main__":
    main()
