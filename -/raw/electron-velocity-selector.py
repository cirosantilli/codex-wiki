"""Draw an ideal electron velocity selector; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media: MPLBACKEND=Agg python ../electron-velocity-selector.py
The off-speed tracks solve the crossed-field equations exactly in scaled units.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def flight_time(x, u):
    """Invert x=t+(u-1)sin(t), with m=e=B=E=1 and u=v_initial/v_selected."""
    lo, hi = 0.0, 5.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if mid + (u - 1) * np.sin(mid) < x:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10, 5), dpi=120, facecolor="white")
    ax = fig.add_axes((.04, .22, .65, .63))
    forces = fig.add_axes((.73, .28, .25, .49))
    fig.suptitle("Ideal electron velocity selector", fontsize=18, y=.96)
    ax.add_patch(Rectangle((0, -.72), 2, 1.44, color="#eaf3fa", zorder=0))
    for y, sign in [(.76, "−"), (-.76, "+")]:
        ax.plot([0, 2], [y, y], lw=6, color="#536877", solid_capstyle="butt")
        for x in np.linspace(.15, 1.85, 7):
            ax.text(x, y + (.13 if y > 0 else -.15), sign, ha="center", va="center", fontsize=16)
    for x in np.linspace(.15, 1.85, 6):
        for y in [-.52, .52]:
            ax.plot(x, y, ".", color="#8498a7", ms=5)
    ax.text(.1, 1.11, r"$\mathbf{B}_s$ out of page (dots)", fontsize=12)
    ax.annotate("", xy=(1.48, .53), xytext=(1.48, .12), arrowprops={"arrowstyle": "->", "lw": 2, "color": "#495965"})
    ax.text(1.55, .4, r"$\mathbf{E}$", fontsize=15)
    tracks = [(.8, "#b45b1a", r"$0.8v_0$: bends down"), (1., "#087c73", r"$v_0=E/B_s$: straight"), (1.2, "#7d4ab0", r"$1.2v_0$: bends up")]
    for u, color, label in tracks:
        t = np.linspace(0, flight_time(2.15, u), 400)
        # The uniform fields end at x=2. Drift freely to the aperture.
        te = flight_time(2, u)
        tf = np.minimum(t, te)
        x = tf + (u - 1) * np.sin(tf)
        y = (u - 1) * (1 - np.cos(tf))
        after = np.maximum(t - te, 0)
        x += after * (1 + (u - 1) * np.cos(te))
        y += after * (u - 1) * np.sin(te)
        keep = x <= 2.15
        ax.plot(np.r_[-.55, x[keep]], np.r_[0, y[keep]], color=color, lw=2.6)
        label_y = -.14 if u == 1 else y[keep][-1]
        ax.text(2.27, label_y, label, color=color, fontsize=11, va="center")
    for low, high in [(-.72, -.055), (.055, .72)]:
        ax.plot([2.15, 2.15], [low, high], lw=4, color="#344450")
    ax.plot([2.15, 2.65], [0, 0], color="#087c73", lw=2.6)
    ax.text(2.15, -.96, "exit slit", ha="center", fontsize=11)
    ax.text(-.52, -.16, r"$e^-$", fontsize=15)
    ax.annotate("", xy=(-.03, .1), xytext=(-.5, .1), arrowprops={"arrowstyle": "->", "color": "#344450", "lw": 1.6})
    ax.text(-.53, .2, "beam", fontsize=11)
    ax.set(xlim=(-.6, 3.65), ylim=(-1.05, 1.3))
    ax.axis("off")
    forces.scatter([0], [0], s=130, color="#087c73")
    forces.text(.09, 0, r"$q=-e$", va="center")
    forces.annotate("", xy=(0, .83), xytext=(0, .08), arrowprops={"arrowstyle": "->", "lw": 2.5, "color": "#7d4ab0"})
    forces.annotate("", xy=(0, -.83), xytext=(0, -.08), arrowprops={"arrowstyle": "->", "lw": 2.5, "color": "#b45b1a"})
    forces.text(.1, .57, r"$F_B=ev_0B_s$", color="#7d4ab0", va="center")
    forces.text(.1, -.57, r"$F_E=eE$", color="#b45b1a", va="center")
    forces.set(xlim=(-.3, 1.4), ylim=(-1.25, 1.15))
    forces.text(-.2, 1.0, "Selected electron", fontsize=13)
    forces.text(-.2, -1.15, "Equal, opposite forces", fontsize=11)
    forces.axis("off")
    fig.text(.05, .12, r"$\mathbf{v}\perp\mathbf{E}\perp\mathbf{B}_s$; the slit accepts a finite band of speeds.", fontsize=12)
    fig.text(.05, .055, "Original teaching model; scaled geometry, not Thomson's 1897 tube.", fontsize=11, color="#495965")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
