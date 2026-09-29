"""Generate 2017-eisenstein-division.png in the current working directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import numpy as np


def main():
    omega = complex(-0.5, np.sqrt(3) / 2)
    fig, ax = plt.subplots(figsize=(8, 5.6), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    lattice = np.array([a + b * omega for a in range(-4, 5) for b in range(-4, 5)])
    ax.scatter(lattice.real, lattice.imag, color="#64748b", s=20, zorder=2,
               label=r"Lattice points $a+b\omega$")
    corners = [s + t * omega for s, t in [(0.5, 0.5), (-0.5, 0.5),
                                          (-0.5, -0.5), (0.5, -0.5)]]
    ax.add_patch(Polygon([(z.real, z.imag) for z in corners], facecolor="#bfdbfe",
                         edgecolor="#2563eb", linewidth=2, alpha=0.85,
                         label=r"Rounding cell: $|s|,|t|\leq 1/2$"))
    ax.add_patch(Circle((0, 0), np.sqrt(3) / 2, fill=False, edgecolor="#c2410c",
                        linewidth=1.8, label=r"Error bound: $|e|\leq\sqrt{3}/2$"))
    ax.add_patch(Circle((0, 0), 1, fill=False, edgecolor="#b91c1c", linestyle="--",
                        linewidth=1.5, label=r"Unit circle: $|e|=1$"))
    ax.scatter([0], [0], color="#111827", s=45, zorder=5)
    ax.annotate("chosen point", (0, 0), xytext=(13, 12), textcoords="offset points",
                fontsize=10, bbox=dict(facecolor="white", edgecolor="none", alpha=0.9))
    for z, label, offset in [(1 + 0j, r"$1$", (10, 6)),
                              (omega, r"$\omega$", (-20, 5))]:
        ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", color="#334155", lw=1.6))
        ax.annotate(label, (z.real, z.imag), xytext=offset, textcoords="offset points",
                    fontsize=13)
    error = 0.4 - 0.4 * omega
    ax.scatter([error.real], [error.imag], color="#1d4ed8", s=40, zorder=6)
    ax.annotate(r"$e=s+t\omega$", (error.real, error.imag), xytext=(12, -8),
                textcoords="offset points", color="#1d4ed8", fontsize=11,
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.9))
    ax.axhline(0, color="#cbd5e1", linewidth=0.8, zorder=0)
    ax.axvline(0, color="#cbd5e1", linewidth=0.8, zorder=0)
    ax.set(xlim=(-2.05, 2.05), ylim=(-1.55, 1.55), xlabel="Real part", ylabel="Imaginary part")
    ax.set_aspect("equal")
    ax.set_title("Eisenstein division by coordinate rounding", fontsize=15, pad=12)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2,
              frameon=False, fontsize=10)
    fig.subplots_adjust(left=0.09, right=0.97, top=0.89, bottom=0.23)
    fig.savefig("2017-eisenstein-division.png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
