"""Original exact linear-drag basin streamlines; Python 3.14, numpy, matplotlib."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a, period, forcing = 1188e3, 6.4 * 86400, 1e-10
    drag, beta = 1 / period, 4 * np.pi / (period * a)
    b, length = a * np.pi / 3, a * np.deg2rad(50)
    m = np.pi / b
    lam = (beta + np.sqrt(beta**2 + 4 * drag**2 * m**2)) / (2 * drag)
    gamma = m**2 / lam
    cw = -np.expm1(-gamma * length) / -np.expm1(-(lam + gamma) * length)
    ce = -np.expm1(-lam * length) / -np.expm1(-(lam + gamma) * length)
    amplitude = -forcing / (drag * m**2)
    x, y = np.linspace(0, length, 500), np.linspace(-b / 2, b / 2, 350)
    xx, yy = np.meshgrid(x, y)
    profile = amplitude * (1 - cw * np.exp(-lam * xx) - ce * np.exp(gamma * (xx - length)))
    psi = profile * np.cos(m * yy)
    fig, ax = plt.subplots(figsize=(7.4, 6), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    scale = forcing * length / beta
    ax.contour(xx / 1000, yy / 1000, psi / scale, levels=np.linspace(psi.min() / scale * 0.97, psi.min() / scale * 0.08, 11), colors="#28639a", linewidths=1.4)
    for start, end in [((550, 480), (350, 480)), ((350, -480), (550, -480)), ((50, 130), (50, -100)), ((850, -100), (850, 130))]:
        ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "-|>", "color": "#b24632", "lw": 2, "mutation_scale": 16})
    ax.axvspan(0, drag / beta / 1000, color="#e4edf4", alpha=0.45, zorder=-2)
    ax.text(120, 0, "Fast southward\nreturn", fontsize=11, va="center")
    ax.text(600, 0, "Broad northward\ninterior flow", fontsize=11, va="center")
    ax.set(xlim=(0, length / 1000), ylim=(-b / 2000, b / 2000), aspect="equal", xlabel="Eastward distance $x$ (km)", ylabel="Northward distance $y$ (km)", title="Closed basin circulation: exact streamfunction contours")
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
