"""Original QED tree diagrams; opaque PNG written to caller's CWD.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Arrows indicate fermion flow, not the momentum direction of a positron.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def fermion(ax, start, end):
    a, b = np.array(start), np.array(end)
    ax.plot([a[0], b[0]], [a[1], b[1]], color="#253c57", lw=2)
    ax.annotate("", xy=a + 0.6 * (b-a), xytext=a + 0.4 * (b-a),
                arrowprops={"arrowstyle": "-|>", "color": "#253c57", "lw": 1.6})


def photon(ax, start, end):
    a, b = np.array(start), np.array(end)
    vector = b-a
    normal = np.array([-vector[1], vector[0]]) / np.linalg.norm(vector)
    t = np.linspace(0, 1, 400)
    curve = a[:, None] + vector[:, None]*t + normal[:, None]*(0.05*np.sin(12*np.pi*t))
    ax.plot(*curve, color="#c46a22", lw=1.8)


def panel(ax, title, left_label, right_label, internal, annihilation=False):
    a, b = (-0.5, 0), (0.5, 0)
    fermion(ax, (-1.6, -0.8), a)
    fermion(ax, a, b)
    fermion(ax, b, (1.6, -0.8))
    photon(ax, a, (-1.6, 0.8))
    photon(ax, b, (1.6, 0.8))
    ax.scatter([-0.5, 0.5], [0, 0], color="black", s=20, zorder=5)
    ax.text(-1.6, -1.05, r"Incoming $e^-,p$", ha="center", fontsize=10)
    ax.text(1.6, -1.05, r"Incoming $e^+,q$" if annihilation else r"Outgoing $e^-,p'$",
            ha="center", fontsize=10)
    ax.text(-1.6, 0.97, left_label, ha="center", fontsize=10)
    ax.text(1.6, 0.97, right_label, ha="center", fontsize=10)
    ax.text(0, -0.27, internal, ha="center", fontsize=11)
    ax.set(xlim=(-2.3, 2.3), ylim=(-1.2, 1.28), title=title)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    fig, axes = plt.subplots(2, 2, figsize=(11.4, 8.0), dpi=100)
    panel(axes[0, 0], "Annihilation: first photon order",
          r"Outgoing $\gamma,k_1$", r"Outgoing $\gamma,k_2$", r"$p-k_1$", True)
    panel(axes[0, 1], "Annihilation: second photon order",
          r"Outgoing $\gamma,k_2$", r"Outgoing $\gamma,k_1$", r"$p-k_2$", True)
    panel(axes[1, 0], "Compton scattering: s channel",
          r"Incoming $\gamma,k$", r"Outgoing $\gamma,k'$", r"$p+k$")
    panel(axes[1, 1], "Compton scattering: u channel",
          r"Outgoing $\gamma,k'$", r"Incoming $\gamma,k$", r"$p-k'$")
    fig.suptitle("Two-photon QED tree diagrams", fontsize=15)
    fig.text(0.5, 0.025, "Solid arrows: fermion flow. Wavy lines: photons. Internal labels: electron four-momentum.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.06, 1, 0.95))
    fig.subplots_adjust(hspace=0.4)
    fig.savefig(Path.cwd() / "paper-44-two-photon-diagrams.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
