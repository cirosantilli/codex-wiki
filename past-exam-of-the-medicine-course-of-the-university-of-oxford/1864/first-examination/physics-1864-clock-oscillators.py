"""Ideal clock restoring mechanisms; write an opaque PNG to the current directory."""
from pathlib import Path
import os

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "ourbigbook.json").exists())
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "_out/matplotlib"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
import numpy as np


def draw():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, (pendulum, balance) = plt.subplots(1, 2, figsize=(12, 5), dpi=120, facecolor="white")
    blue, orange = "#0072B2", "#D55E00"
    length, theta = 2.05, .48
    bob = np.array([length * np.sin(theta), -length * np.cos(theta)])
    pendulum.plot([-.4, .4], [.06, .06], color="#555555", lw=4)
    pendulum.plot([0, 0], [0, -2.35], "--", color="#888888", lw=1)
    pendulum.plot([0, bob[0]], [0, bob[1]], color=blue, lw=3)
    pendulum.add_patch(Circle(bob, .16, facecolor=blue, zorder=4))
    pendulum.add_patch(Circle((0, 0), .045, facecolor="#222222", zorder=5))
    pendulum.add_patch(Arc((0, 0), 1.02, 1.02, theta1=270, theta2=270+np.degrees(theta),
                           color="#555555", lw=1.5))
    pendulum.text(.18, -.7, r"$\theta$", fontsize=16)
    pendulum.text(.65, -.8, r"$L$", fontsize=16, color=blue)
    pendulum.annotate("", xy=bob+[0, -.65], xytext=bob,
                      arrowprops={"arrowstyle": "->", "lw": 2.4, "color": orange})
    pendulum.text(bob[0]+.1, bob[1]-.49, r"$mg$", color=orange, fontsize=15)
    pendulum.text(-1.05, -.85, "Gravity supplies\nthe restoring torque", ha="center", fontsize=12)
    pendulum.text(0, -2.8, r"$\tau=-mgL\sin\theta$", ha="center", fontsize=16)
    pendulum.text(0, -3.25, r"$T\simeq2\pi\sqrt{L/g}$", ha="center", fontsize=16)
    pendulum.set_title("Pendulum: small-angle gravitational oscillator")
    pendulum.set_xlim(-1.75, 1.75)
    pendulum.set_ylim(-3.55, .35)

    radius, angle = 1.05, .35
    balance.add_patch(Circle((0, -.9), radius, fill=False, edgecolor=blue, lw=4))
    for offset in (0, np.pi/2):
        v = radius*np.array([np.cos(angle+offset), np.sin(angle+offset)])
        balance.plot([-v[0], v[0]], [-.9-v[1], -.9+v[1]], color=blue, lw=2)
    t = np.linspace(0, 6*np.pi, 600)
    r = .08+.68*t/t[-1]
    balance.plot(r*np.cos(t), -.9+r*np.sin(t), color=orange, lw=1.7)
    balance.plot([.76, 1.43], [-.9, -.9], color=orange, lw=1.8)
    balance.plot([1.43, 1.43], [-1.1, -.7], color="#555555", lw=4)
    balance.add_patch(Circle((0, -.9), .045, color="#222222", zorder=5))
    balance.annotate("Fixed outer end", xy=(1.43, -.9), xytext=(.7, .4),
                     arrowprops={"arrowstyle": "->", "color": "#555555"}, ha="center", fontsize=11)
    balance.annotate("Spiral spring", xy=(.33, -.6), xytext=(-1.03, .35),
                     arrowprops={"arrowstyle": "->", "color": orange}, ha="center", fontsize=11)
    balance.text(0, -2.25, "Elasticity supplies the restoring torque", ha="center", fontsize=12)
    balance.text(0, -2.8, r"$\tau\simeq-\kappa\phi$", ha="center", fontsize=16)
    balance.text(0, -3.25, r"$T\simeq2\pi\sqrt{I/\kappa}$", ha="center", fontsize=16)
    balance.set_title("Balance wheel: elastic angular oscillator")
    balance.set_xlim(-1.75, 1.75)
    balance.set_ylim(-3.55, .65)
    for ax in (pendulum, balance):
        ax.set_aspect("equal")
        ax.axis("off")
    fig.suptitle("Two clock regulators: restoring action plus inertia", fontsize=17)
    fig.tight_layout(rect=(0, 0, 1, .93))
    fig.savefig(Path.cwd() / "physics-1864-clock-oscillators.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    draw()
