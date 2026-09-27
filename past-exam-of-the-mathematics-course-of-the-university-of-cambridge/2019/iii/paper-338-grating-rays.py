"""Reflection-grating sign convention; save PNG in cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(7, 4), dpi=100, facecolor="white")
    alpha, beta = np.deg2rad([28, 61])
    ax.plot([-1.1, 4.1], [0, 0], color="0.25", lw=3)
    for groove in [0, 1.5]:
        ax.plot([groove, groove], [-.08, .08], color="0.15", lw=3)
        ax.plot([groove, groove], [0, 2.7], color="0.5", ls="--", lw=1)
        for angle, color, incoming in [(alpha, "#1766aa", True), (beta, "#c66b22", False)]:
            end = np.array([groove, 0.]) + 2.45*np.array([np.sin(angle), np.cos(angle)])
            origin = np.array([groove, 0.])
            start, finish = (end, origin) if incoming else (origin, end)
            ax.annotate("", xy=finish, xytext=start,
                        arrowprops=dict(arrowstyle="->", color=color, lw=2.1))
    ax.add_patch(Arc((0, 0), 1.25, 1.25, theta1=90-np.rad2deg(alpha), theta2=90,
                     color="#1766aa", lw=1.5))
    ax.add_patch(Arc((0, 0), 1.8, 1.8, theta1=90-np.rad2deg(beta), theta2=90,
                     color="#c66b22", lw=1.5))
    ax.text(.1, .69, r"$\alpha$", color="#1766aa", fontsize=13)
    ax.text(.57, .58, r"$\beta$", color="#c66b22", fontsize=13)
    ax.text(.95, 2.45, "Incident rays", color="#1766aa", fontsize=11)
    ax.text(2.8, 1.38, "Diffracted rays", color="#c66b22", fontsize=11)
    ax.text(-.55, 2.65, "Normal", color="0.4", fontsize=10)
    ax.annotate("", xy=(1.5, -.37), xytext=(0, -.37),
                arrowprops=dict(arrowstyle="<->", color="0.25", lw=1.3))
    ax.text(.75, -.61, r"Groove spacing $d$", ha="center", fontsize=11)
    ax.text(2.9, -.14, "Grating surface", va="top", color="0.3", fontsize=10)
    ax.set_title(r"Constructive interference: $d(\sin\alpha+\sin\beta)=m\lambda$", fontsize=12)
    ax.set(xlim=(-1.1, 4.1), ylim=(-.85, 2.95), aspect="equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
